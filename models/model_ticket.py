from models.base_model import BaseModel
from peewee import *
from playhouse import postgres_ext
from datetime import datetime
from models.model_visitante import Visitante
from models.model_atraccion import Atraccion

class Ticket(BaseModel):
    visitante_id = ForeignKeyField(Visitante, backref='tickets', on_delete= "CASCADE", on_update="CASCADE")
    atraccion_id = ForeignKeyField(Atraccion, backref='tickets', null = True) # null si vale para cualquier atraccion
    fecha_compra = DateTimeField()
    fecha_visita = DateField()
    tipo_ticket = TextField(constraints= Check("tipo_ticket IN ('general','colegio','empleado')"))
    detalles_compra = postgres_ext.BinaryJSONField(default = {
        "tipo_favorito": "extrema",
        "restricciones": ["problemas_cardiacos"],
        "historial_visitas": [
            {"fecha": "2024-06-15", "atracciones_visitadas": 8},
            {"fecha": "2024-08-20", "atracciones_visitadas": 12}
        ]
    })
    usado = BooleanField(default=False)
    fecha_uso = DateTimeField(null = True)

    class Meta:
        table_name = 'tickets'