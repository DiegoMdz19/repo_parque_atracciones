from peewee import *
from peewee import fn
from playhouse import postgres_ext
from datetime import datetime
from models.model_ticket import Ticket
from models.model_visitante import Visitante
from models.model_atraccion import Atraccion

class RepoTicket:
    
    @staticmethod
    def get_all():
        return list(Ticket.select())

    @staticmethod
    def get_by_visitante(visitante_id):
        return list(Ticket.select().where(Ticket.visitante == visitante_id))

    @staticmethod
    def get_by_atraccion(atraccion_id):
        return list(Ticket.select().where(Ticket.atraccion == atraccion_id))

    @staticmethod
    def marcar_usado(ticket_id):
        return Ticket.update(
            usado=True,
            fecha_uso=datetime.now()
        ).where(Ticket.id == ticket_id).execute()

    @staticmethod
    def tickets_colegio_menor_30():
        return (Ticket
                .select()
                .where(
                    (Ticket.tipo_ticket == 'colegio') &
                    (Ticket.detalles_compra['precio'] < '30')
                ))

    @staticmethod
    def cambiar_precio_ticket(id_ticket, precio_nuevo):
        ticket = Ticket.get(Ticket.id == id_ticket)
        if ticket:
            if precio_nuevo > 0:
                ticket.detalles_compra["precio"] = precio_nuevo
                ticket.save()
                return ticket
            else:
                return "Error, el nuevo precio no es válido"
        else:
            return "Error, el ticket no existe"
        
    #Falta por poner desc
    @staticmethod
    def tickets_total_visitante():
        query=  (
            Visitante.select(Ticket.fn.COUNT(Ticket.visitante_id))
            .join(Ticket)
            .group_by(Visitante.id)
            .order_by(Ticket.fn.COUNT(Ticket.visitante_id) )
        )
        return list(query)

        


    