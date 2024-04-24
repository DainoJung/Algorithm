from datetime import datetime, timedelta

x = datetime.now() + timedelta(hours=9)

x = x.strftime("%Y-%m-%d")

print(x)