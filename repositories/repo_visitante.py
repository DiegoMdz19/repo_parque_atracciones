from peewee import *
from playhouse import postgres_ext
from models.model_visitante import Visitante
from models.model_atraccion import Atraccion
from models.model_ticket import Ticket
from datetime import datetime


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
    def delete_visitante(id):
        return Visitante.delete().where(Visitante.id == id).execute()
    
    @staticmethod
    def visit_extremas():
        visit = Visitante.select().where(Visitante.preferencias["tipo_favorito"].contains('extrema'))
        return list(visit)
    
    @staticmethod
    def visit_tickets(id_atraccion):
        return (Visitante.select().join(Ticket).where(Ticket.atraccion_id == id_atraccion).distinct())
        


    
    @staticmethod
    def eliminar_restriccion(id_visitante, restriccion):
        try:
            visitante = Visitante.get(Visitante.id == id_visitante)
        except Visitante.DoesNotExist:
            return None
        
        preferencias = visitante.preferencias

        if "restricciones" not in preferencias:
            return False         
        
        restricciones_lista = preferencias["restricciones"]
        
        if restriccion not in restricciones_lista:
            return False
           
        restricciones_lista.remove(restriccion)

        preferencias["restricciones"] = restricciones_lista

        visitante.preferencias = preferencias
        visitante.save()
        
        return True

    @staticmethod
    def anyadir_visita(id_visitante, fecha_string, cantidad):
        try:
            visitante = RepoVisitante.search_by_id(id_visitante)
        except Visitante.DoesNotExist:
            print(f"Error, el visitante [{id_visitante}] no existe")
            return None

        if cantidad <= 0:
            print(f"Error, cantidad {cantidad} no válida")
            return None

        try:
            fecha_datetime = datetime.strptime(fecha_string, "%Y-%m-%d")
        except ValueError:
            print(f"Error, la fecha {fecha_string} no tiene un formato válido")
            return None

        if fecha_datetime > datetime.now():
            print(f"Error, fecha introducida no puede ser futura")
            return None

        historial = visitante.preferencias.get("historial_visitas", [])

        if fecha_string in historial:
            print(f"Error, la visita ya existe")
            return None

        historial.append(fecha_string)
        visitante.preferencias["historial_visitas"] = historial
        visitante.preferencias["atracciones_visitadas"] = cantidad

        visitante.save()
        return visitante
    

    @staticmethod
    def problemas_cardiacos():
        visitantes = list(Visitante.select())
        lista_visitantes = []
        for visitante in visitantes:
            restricciones = visitante.preferencias.get("restricciones", [])
            if "problemas_cardiacos" in restricciones:
                lista_visitantes.append(visitante)
        return lista_visitantes



