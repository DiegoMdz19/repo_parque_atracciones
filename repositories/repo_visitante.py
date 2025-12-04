from peewee import *
from playhouse import postgres_ext
from models.model_visitante import Visitante
from models.model_atraccion import Atraccion
from models.model_ticket import Ticket


class RepoVisitante:

    @staticmethod
    def create(nombre,email,preferencias=None):
        try:
            if preferencias:
                return Visitante.create(nombre=nombre,email=email,preferencias=preferencias)
            else:
                return Visitante.create(nombre=nombre,email=email)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def search_all():
        return list(Visitante.select())
    
    @staticmethod
    def delete(id):
        return Visitante.delete().where(Visitante.id == id)
    
    def visit_extremas():
        json_struct = {"tipo_favorito": ["extrema"]}
        
        visit = (
            Visitante.select()
            .where(Visitante.preferencias.contains(json_struct))
        )

        return list(visit)
    
    def visit_tickets():
        return list(Visitante.select().where(Ticket.visiante_id == Visitante.id))