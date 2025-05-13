from datetime import datetime

date_string = "2024-12-30 15:30"
format = "%Y-%m-%d %H:%M"

parsed_datetime = datetime.strptime(date_string, format)
print(parsed_datetime)
