from datetime import date, datetime,timedelta
from time import time
today = datetime.today()
lastweek = today - timedelta(days=7)
print(today,'\n',lastweek)