from datetime import date, datetime,timedelta
from time import time
today = date.today()
lastweek = today - timedelta(days=7)
print(today,'\n',lastweek)
# today = str(today)
print(today)
oneweek = today - timedelta(days=7)
print(oneweek)