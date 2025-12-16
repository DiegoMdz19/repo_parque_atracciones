from models.base_model import BaseModel
from peewee import *
from playhouse import postgres_ext
from datetime import datetime
from models.model_visitante import Visitante
from models.model_atraccion import Atraccion
import json

class Ticket(BaseModel):
    visitante_id = ForeignKeyField(Visitante, backref='tickets', on_delete= "CASCADE", on_update="CASCADE")
    atraccion_id = ForeignKeyField(Atraccion, backref='tickets', null = True) # null si vale para cualquier atraccion
    fecha_compra = DateTimeField()
    fecha_visita = DateField()
    tipo_ticket = TextField(constraints= [Check("tipo_ticket IN ('general','colegio','empleado')")])
    detalles_compra = postgres_ext.BinaryJSONField(default = {
        "precio": "45.99",
        "descuentos_aplicados": ["estudiante","early_bird"],
        "servicios_extra": ["fast_pass","comida_incluida"],
        "metodo_pago": "tarjeta"
    })
    usado = BooleanField(default=False)
    fecha_uso = DateTimeField(null = True)

    class Meta:
        table_name = 'tickets'


    def __str__(self):
        fecha_usado = ""
        gastado = ""
        atraccion = ""
        if self.atraccion_id:
            atraccion = self.atraccion_id.nombre
        else:
            atraccion = "Válido para cualquier atracción"
        if self.usado == True:
            gastado = "Si"
        else:
            gastado = "No"
        if self.fecha_uso is None:
            fecha_usado = "No se ha usado el ticket"
        else:
            fecha_usado = self.fecha_uso
        return (f"\TICKET #{self.id}\n"
        f"Visitante: {self.visitante_id.nombre} Id:{self.visitante_id.id}\n"
        f"ID Atraccion: {atraccion}\n"
        f"Fecha compra: {self.fecha_compra}\n"
        f"Fecha visita: {self.fecha_visita}\n"
        f"tipo: {self.tipo_ticket}\n"
        f"Detalles compra:\n{json.dumps(self.detalles_compra, indent = 4)}\n"
        f"Usado: {gastado}\n"
        f"Fecha de uso: {fecha_usado}\n")
    