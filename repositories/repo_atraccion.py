from peewee import *
from playhouse import postgres_ext
from models.model_atraccion import Atraccion

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
        return list(
            Atraccion.select()
            .where(Atraccion.detalles["duracion_segundos"] > "120")
        )


    @staticmethod
    def mayor_ocho():
        return list(
            Atraccion.select()
            .where(Atraccion.detalles["intensidad"] > "7")
        )


    @staticmethod
    def nueva_caracteristica_atraccion(id_atraccion, caracteristica):
        atraccion = Atraccion.get(Atraccion.id == id_atraccion)

        if not atraccion:
            return f"Error, la atracción [{id_atraccion}] no existe"
        if not caracteristica:
            return f"Error, introduce una caracteristica [{caracteristica}] válida"
        
        caracteristicas = atraccion.detalles["caracteristicas"]

        if caracteristica not in caracteristicas:
            caracteristicas.append(caracteristica)
            atraccion.detalles["caracteristicas"] = caracteristicas
            atraccion.save()

        else:
            return f"Error, la caracteristica ya existe"
        
        return atraccion

