import uuid
import json
import pandas as pd
from datetime import datetime
import requests


# FDO oluşturma fonksiyonu
def create_fdo(data, metadata):
    fdo_id = str(uuid.uuid4())
    metadata['id'] = fdo_id
    metadata['date_created'] = str(datetime.now())
    metadata['pid'] = fdo_id
    fdo = {
        "id": fdo_id,
        "metadata": metadata,
        "data": data
    }
    return fdo


# Statik ve dinamik parametrelerle matematik işlemi yapan fonksiyon
def math_operations(high_temp, low_temp, operation, *args):
    result = 0
    if operation == "add":
        result = high_temp + low_temp
    elif operation == "subtract":
        result = high_temp - low_temp
    elif operation == "multiply":
        result = high_temp * low_temp
    elif operation == "divide":
        result = high_temp / low_temp if low_temp != 0 else None

    # Dinamik parametreler ile ek işlemler
    for arg in args:
        if arg == "square":
            result = result ** 2
        elif arg == "sqrt":
            result = result ** 0.5

    return result


# CSV dosyasını yükleme
csv_file = "temperatures.csv"  # CSV dosyanızın adı
df = pd.read_csv(csv_file)

# Kullanıcıdan tarih alma
user_date = input("Lütfen bir tarih girin (YYYY-MM-DD formatında): ")

# Girilen tarihteki verileri bulma
row = df[df['Date'] == user_date]

if row.empty:
    print(f"{user_date} için veri bulunamadı.")
else:
    # Verilerden FDO'ları oluşturma
    row_data = row.iloc[0]  # Girilen tarihin ilk satırını alıyoruz

    # Metadata örneği
    metadata_template = {
        "creator": "Your Name",
        "date_created": str(datetime.now()),
        "keywords": ["Temperature", "FDO", "Data"],
        "license": "CC BY 4.0",
        "format": "application/json"
    }

    # High Temperature FDO'su oluşturma
    high_temp_metadata = metadata_template.copy()
    high_temp_metadata["title"] = f"High Temperature on {row_data['Date']}"
    high_temp_metadata["description"] = f"High temperature on {row_data['Date']}"
    high_temp_fdo = create_fdo({"high_temperature": row_data['High_Temperature_C']}, high_temp_metadata)

    # Low Temperature FDO'su oluşturma
    low_temp_metadata = metadata_template.copy()
    low_temp_metadata["title"] = f"Low Temperature on {row_data['Date']}"
    low_temp_metadata["description"] = f"Low temperature on {row_data['Date']}"
    low_temp_fdo = create_fdo({"low_temperature": row_data['Low_Temperature_C']}, low_temp_metadata)

    # FDO'lar arasında matematik işlemler ve sonuçları URL'ye ekleme
    results = []
    operations = ["add", "subtract", "multiply", "divide"]
    for operation in operations:
        result = math_operations(row_data['High_Temperature_C'], row_data['Low_Temperature_C'], operation, "square")
        if result is not None:
            result_entry = {
                "operation": operation,
                "high_temp_fdo_id": high_temp_fdo["id"],
                "low_temp_fdo_id": low_temp_fdo["id"],
                "result": result,
                "url": f"https://example.org/fdo_result/{user_date}/{operation}/{result}"
            }
            results.append(result_entry)

    # sonuçları JSON formatında kaydetme = save results JSON records
    with open("temperature_fdo_results.json", "w") as f:
        json.dump(results, f, indent=4)

    # Sonuçları konsolda gösterme
    print(json.dumps(results, indent=4))

    # Sonuçları bir API'ye gönderme (örnek URL, uygun bir endpoint ile değiştirin)
    url = "https://example.org/api/submit_results"  # Gerçek bir URL ile değiştirin
    response = requests.post(url, json=results)

    print(f"Response Status Code: {response.status_code}")




