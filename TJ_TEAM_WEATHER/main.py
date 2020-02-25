from visitor import *

def get_visitor_personal_info(first_name, last_name, email):
    first_name = input('Please provide your first name: ')
    last_name = input('and your last name: ')
    email = last_name + first_name+'@email.com'
    
    visitor_obj = Visitor.create(first_name=first_name, last_name=last_name, email=email)
    return visitor_obj
    #new_record = Visitor.insert(first_name = first_name, last_name = last_name).execute()



db.connect() # established connection to datavase
db.create_tables([Visitor, Visit_record]) #peewee auto generate tables

#visitor_obj=get_visitor_personal_info('fname', 'lname', 'email')
#for item in Visitor.select():
    #print(item)

