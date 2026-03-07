import re 
import json 

with open("raw") as f:
    data = f.read()

price_pattern = re.compile(r"\d+,\d+ x \d+,\d+\s(.+)")
price_result = price_pattern.findall(data)

name_pattern = re.compile(r"\d+\.\s(.+)")
name_result = name_pattern.findall(data)

price_get = re.findall(r"ИТОГО:\s(.+)", data)

date_get = re.findall(r"Время:(.+)", data)

sposob_get = re.findall(r"Банковская карта", data)

datas = {
    "prices": price_result,
    "names": name_result,
    "total": price_get,
    "time": date_get,
    "payment method": sposob_get,  
}

json_data = json.dumps(datas, ensure_ascii=False, indent=4)

print(json_data)






