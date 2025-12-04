from models.base_model import BaseModel
from peewee import *
from playhouse import postgres_ext
from datetime import datetime

class Atraccion(BaseModel):
    nombre = TextField(unique = True)
    tipo = TextField(constraints=[Check("tipo IN ('extrema','familiar','infantil','acuatica')")])
    altura_minima = IntegerField()# se guarda en cm
    detalles = postgres_ext.BinaryJSONField(default = {
        "duracion_segundos": 60,
        "capacidad_por_turno": 24,
        "intensidad": 8,
        "caracteristicas" : ["looping","caida_libre","giro_360"],
        "horarios": {
            "apertura" : "10:00",
            "cierre" : "22:00",
            "mantenimiento" : ["14:00-15:00"]
        }
    })
    activa = BooleanField(default = True)
    fecha_inauguracion = DateField(default = datetime.now)

    class Meta:
        table_name = 'atracciones'