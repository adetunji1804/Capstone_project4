# from vs import *
from db_query import *
from api import *


conn = db_connection('visitor_db.sqlite')

a = create_tables() # create tables
#print(a) check if tables created else rollback
foreign_key = create_visitor(obj_visitor) #returned the foreign key after insert

dat, tem = weather_details() # weather API returned data
if dat == None or tem == None:
    print('Invalid input request')
else:

    #each data stored on database table
    for i in range(len(dat)):
        conn.execute('insert into weather values(?, ?, ?)', (dat[i], tem[i], foreign_key))
    conn.commit()

