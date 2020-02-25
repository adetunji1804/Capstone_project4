from peewee import *

# create an instance of a database, establish connection and enforce foreignkey constraints
db = SqliteDatabase('visitor_db.sqlite', pragmas={'foreign_keys': 1})

class Visitor(Model):
    # visitor class attributes
    first_name = CharField()
    last_name = CharField()
    email = CharField()
        

    def __str__(self):
        return f'Fullname: {self.first_name} {self.last_name}, email: {self.email} '

    class Meta:
        database = db #model use the art_db.sqlite database



class Visit_record(Model):
    #visitor_record class attributes
    info_requested = CharField() # accept visitor's country and city of choice
    date_requested = DateTimeField()
    remark = CharField() 
    visitor_id = ForeignKeyField(Visitor, backref='vrecord')

    def __str__(self):
        return f'Requested Info: {self.info_requested} \nDate: {self.date_requested}\nRemark: {self.remark}'

    class Meta:
        database = db #model use the art_db.sqlite database
