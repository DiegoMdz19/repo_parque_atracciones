from peewee import *
from peewee import fn
from playhouse import postgres_ext
from datetime import datetime
from models.model_ticket import Ticket
from models.model_visitante import Visitante
from models.model_atraccion import Atraccion

class RepoTicket:
    
    @staticmethod
    def create_ticket(visitante_id, fecha_visita, tipo_ticket, detalles_compra_json, atraccion_id):
        try:
            if detalles_compra_json:
                return Ticket.create(visitante_id=visitante_id, fecha_visita = fecha_visita, tipo_ticket = tipo_ticket, detalles_compra_json = detalles_compra_json, atraccion_id = atraccion_id )
            else:
                return Ticket.create(visitante_id=visitante_id, fecha_visita = fecha_visita, tipo_ticket = tipo_ticket,atraccion_id = atraccion_id)
        except Exception as e:
            print(e)
            
            
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
                print("Error, el nuevo precio no es válido")
                return None
        else:
            print("Error, el ticket no existe")
            return None
        
    #Falta por poner desc
    @staticmethod
    def tickets_total_visitante():
        query = (
        Visitante.select(
            Visitante,
            fn.COUNT(Ticket.id).alias('total_tickets')
        )
        .join(Ticket)  
        .group_by(Visitante.id)
        .order_by(fn.COUNT(Ticket.id).desc())
        )
        return list(query)

    @staticmethod
    def top_5_atracciones_mas_vendidas():
        query = (
            Atraccion.select(
                Atraccion,
                fn.COUNT(Ticket.id).alias('tickets_vendidos')                
            )
            .join(Ticket)
            .group_by(Atraccion.id)
            .order_by(fn.COUNT(Ticket.id).desc())
            .limit(5)
        )
        return list(query)
        
    @staticmethod
    def visitantes_mas_100_euros():
        query = (
            Visitante.select(
                Visitante,
                fn.SUM(Ticket.detalles_compra['precio']).alias('gasto_total')
            )
            .join(Ticket)
            .group_by(Visitante.id)
            .having(fn.SUM(Ticket.detalles_compra['precio']) > 100)
        )
        return list(query)

    