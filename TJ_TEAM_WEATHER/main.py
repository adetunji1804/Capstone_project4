#from vs import *
from db_query import *
from api import *


with db_connection() as con:
    cursor= con.cursor()
    con.execute(visitor_table)
    con.execute(visit_record_table)
    con.execute(weather_table)
    
    #con.commit()
dat, tem = weather_details()
#result = zip(dat, tem)
for i in range(len(dat)):
    cursor.execute('insert into weather values(?, ?, ?)', (dat[i], tem[i], 2))
con.commit()

#for i in range (len(dat)):
    #print(f'{dat[i]}, {tem[i]}')