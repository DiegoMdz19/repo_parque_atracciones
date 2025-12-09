from peewee import *
from playhouse import postgres_ext
from models.model_visitante import Visitante
from models.model_atraccion import Atraccion
from models.model_ticket import Ticket


class RepoVisitante:

    @staticmethod
    def create(nombre,email,altura,fecha_registro,preferencias=None):
        try:
            if preferencias:
                return Visitante.create(nombre=nombre,email=email,altura=altura,fecha_registro=fecha_registro,preferencias=preferencias)
            else:
                return Visitante.create(nombre=nombre,email=email,altura=altura,fecha_registro=fecha_registro)
        except Exception as e:
            print(f"Error al crear el visitante: {e}")
            return None

    @staticmethod
    def search_all():
        return list(Visitante.select())
    
    @staticmethod
    def search_by_id(id):
        return Visitante.get(Visitante.id ==  id)
    
    @staticmethod
    def delete(id):
        return Visitante.delete().where(Visitante.id == id)
    
    @staticmethod
    def visit_extremas():
        json_struct = {"tipo_favorito": ["extrema"]}
        
        visit = (
            Visitante.select()
            .where(Visitante.preferencias.contains(json_struct))
        )

        return list(visit)
    
    @staticmethod
    def visit_tickets():
        return list(Visitante.select().where(Ticket.visiante_id == Visitante.id))
    
    #Corregir
    @staticmethod
    def eliminar_restriccion(id_visitante, restriccion):
        visitante = Visitante.get(Visitante.id == id_visitante)
        if not visitante:
            return f"Error, el visitante con id [{id_visitante}] no existe"
        
        restricciones_actuales = visitante.preferencias
        if not restricciones_actuales:
            return f"Error, la restriccion [{restriccion}] no existe"
        
        del restricciones_actuales["restricciones"][restriccion]

        restricciones_actuales.save()
        print("Borrado con éxito")


    # Falta por comprobar que tenga una estructura valida, fecha  y numero de atracciones
    @staticmethod
    def anyadir_visita(id_visitante, visita):
        visitante = Visitante.get(Visitante.id == id_visitante)

        if not visitante:
            return f"Error, el visitante [{id_visitante}] no existe"
        if not visita:
            return f"Error, introduce una visita [{visita}] válida"
        
        historial = visitante.preferencias["historial_visitas"]

        if visita not in historial:
            historial.append(visita)
            visitante.preferencias["historial_visitas"] = historial
            visitante.save()
        else:
            return f"Error, la visita ya existe"
        
        return visitante
