from peewee import *
from playhouse import postgres_ext
from models.model_ticket import Ticket
from models.model_visitante import Visitante
from models.model_atraccion import Atraccion

class RepoTicket:
    @staticmethod
    def cambiar_precio_ticket(id_ticket, precio_nuevo):
        ticket = Ticket.get(Ticket.id == id_ticket)
        if ticket:
            if precio_nuevo > 0:
                ticket.detalles_compras["precio"] = precio_nuevo
                ticket.save()
                return ticket
            else:
                return "Error, el nuevo precio no es válido"
        else:
            return "Error, el ticket no existe"
        
    @staticmethod
    def tickets_total_visitante():
        query=(
            Visitante.select()
            .join(Ticket)
            .group_by(Visitante.id)
            .order_by()
        )

        


    