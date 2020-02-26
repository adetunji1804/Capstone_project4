from visitor import *

def get_visitor_personal_info(first_name, last_name):
    first_name = input('Please provide your first name: ')
    last_name = input('and your last name: ')
    obj = Visitor('', '', first_name)
   # email = last_name + first_name
    email = obj.get_email()
    obj_visitor = Visitor.create(first_name = first_name, last_name = last_name, email= email)
    return obj_visitor
    #new_record = Visitor.insert(first_name = first_name, last_name = last_name).execute()


db.connect() # established connection to datavase
db.create_tables([Visitor, Visit_record]) #peewee auto generate tables

#visitor_obj=get_visitor_personal_info('fname', 'lname')

#check the all records on visitor table
for item in Visitor.select():
    print(item)

