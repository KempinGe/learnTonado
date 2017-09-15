from peewee import *
from peewee import BaseModel
database = MySQLDatabase('TORNADO', **{'user': 'root', 'password': 'g123567G'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class TbUserInfo(BaseModel):
    ui_age = IntegerField(null=True)
    ui_avatar = CharField(null=True)
    ui_craete_time = DateTimeField()
    ui_gender = IntegerField(null=True)
    ui_isdel = IntegerField()
    ui_password = CharField()
    ui_phone = CharField(unique=True)
    ui_update_time = DateTimeField()
    ui_user = BigIntegerField(db_column='ui_user_id', primary_key=True)
    ui_user_name = CharField()

    class Meta:
        db_table = 'tb_user_info'

class TbHouseInfo(BaseModel):
    hi_create_time = DateTimeField()
    hi_house_address = CharField()
    hi_house = BigIntegerField(db_column='hi_house_id', primary_key=True)
    hi_house_name = CharField()
    hi_house_price = IntegerField()
    hi_house_use = ForeignKeyField(db_column='hi_house_use_id', rel_model=TbUserInfo, to_field='ui_user')
    hi_update_time = DateTimeField()

    class Meta:
        db_table = 'tb_house_info'

class TbHouseImage(BaseModel):
    hi_create_time = DateTimeField()
    hi_house = ForeignKeyField(db_column='hi_house_id', rel_model=TbHouseInfo, to_field='hi_house')
    hi_imag_url = CharField()
    hi_img = BigIntegerField(db_column='hi_img_id', primary_key=True)
    hi_update_time = DateTimeField()

    class Meta:
        db_table = 'tb_house_image'

