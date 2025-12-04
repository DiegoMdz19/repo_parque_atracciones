from models.base_model import BaseModel
from peewee import *
from playhouse import postgres_ext
from datetime import datetime

class Visitante(BaseModel):
    nombre = TextField()
    email = CharField(unique = True)
    altura = IntegerField()# se guarda en cm
    fecha_registro = DateTimeField()
    preferencias = postgres_ext.BinaryJSONField(default = {
        "tipo_favorito": "extrema",
        "restricciones": ["problemas_cardiacos"],
        "historial_visitas": [
            {"fecha": "2024-06-15", "atracciones_visitadas": 8},
            {"fecha": "2024-08-20", "atracciones_visitadas": 12}
        ]
    })

    class Meta:
        table_name = 'visitantes'