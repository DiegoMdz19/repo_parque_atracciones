from database import db
from peewee import *

class BaseModel(Model):
    class Meta:
        database = db 