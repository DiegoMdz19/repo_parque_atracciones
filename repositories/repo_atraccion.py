from peewee import *
from playhouse import postgres_ext
from models.model_atraccion import Atraccion
from models.model_visitante import Visitante

class RepoAtraccion:
    @staticmethod
    def create_atraccion(nombre,tipo,altura_minima,detalles=None):
        try:
            if detalles:
                return Atraccion.create(nombre=nombre,tipo=tipo,altura_minima=altura_minima,detalles=detalles)
            else:
                return Atraccion.create(nombre=nombre,tipo=tipo,altura_minima=altura_minima)
        except Exception as e:
            print(e)

    @staticmethod
    def search_all_atraccion():
        return list(Atraccion.select())
    
    @staticmethod
    def search_disp():
        return list(Atraccion.select().where(Atraccion.activa == True))

    @staticmethod
    def search_by_id_atraccion(id):
        try:
            return Atraccion.get(Atraccion.id == id)
        except DoesNotExist:
            return None

    @staticmethod
    def modificar_activa(id):
        atrac = RepoAtraccion.search_by_id_atraccion(id)
        if not atrac:
            return None

        atrac.activa = not atrac.activa
        atrac.save()
        return atrac

    @staticmethod
    def delete_atraccion(id):
        return Atraccion.delete().where(Atraccion.id == id).execute()

    @staticmethod
    def mayor_cientoveinte():
        atracciones = list(Atraccion.select())
        resultado = []
        for atraccion in atracciones:
            duracion = atraccion.detalles.get("duracion_segundos",)
            if duracion > 120:
                resultado.append(atraccion)
        return resultado
        


    @staticmethod
    def mayor_siete():
        return list(
            Atraccion.select()
            .where(Atraccion.detalles["intensidad"] > "7")
        )




    #corregido ya
    @staticmethod
    def nueva_caracteristica_atraccion(id_atraccion, caracteristica):
        atraccion = Atraccion.get(Atraccion.id == id_atraccion)

        if not atraccion:
            print(f"Error, la atracción [{id_atraccion}] no existe")
            return None
        if not caracteristica:
            print(f"Error, introduce una caracteristica [{caracteristica}] válida")
            return None
        
        caracteristicas = atraccion.detalles["caracteristicas"]

        if caracteristica not in caracteristicas:
            caracteristicas.append(caracteristica)
            atraccion.detalles["caracteristicas"] = caracteristicas
            atraccion.save()
        else:
            print(f"Error, la caracteristica ya existe")
            return None
        
        print("Caracteristica añadida correctamente")
        return atraccion

    @staticmethod
    def atracciones_compatibles(id_visitante):
        try:
            visitante = Visitante.get(Visitante.id == id_visitante)
        except Exception as e:
            print(f"Error: el visitante con id [{id_visitante}] no existe: {e}")
            return None
        
        tipo_favorito = ""
        if visitante.preferencias and 'tipo_favorito' in visitante.preferencias:
            tipo_favorito = visitante.preferencias['tipo_favorito']

        altura_visitante = visitante.altura

        query = (
            Atraccion.select()
            .where(
                (Atraccion.activa == True) &
                (Atraccion.altura_minima <= altura_visitante)
            )
        )

        if tipo_favorito:
            query = query.where(Atraccion.tipo == tipo_favorito)
        
        return list(query)
    
    @staticmethod
    def looping_y_caida():
        atracciones = list(Atraccion.select())
        resultado = []

        for atraccion in atracciones:
            caracteristicas = atraccion.detalles.get("caracteristicas", [])
            if "looping" in caracteristicas and "caida_libre" in caracteristicas:
                resultado.append(atraccion)

        return resultado

