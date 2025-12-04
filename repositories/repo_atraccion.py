from peewee import *
from playhouse import postgres_ext
from models.model_atraccion import Atraccion

class RepoAtraccion:
    @staticmethod
    def create(nombre,tipo,altura_minima,detalles=None):
        try:
            if detalles:
                return Atraccion.create(nombre=nombre,tipo=tipo,altura_minima=altura_minima,detalles=detalles)
            else:
                return Atraccion.create(nombre=nombre,tipo=tipo,altura_minima=altura_minima)
        except Exception as e:
            print(e)

    @staticmethod
    def search_all():
        return list(Atraccion.select())
    
    @staticmethod
    def search_by_id(id):
        return Atraccion.get(Atraccion.id ==  id)
    
    @staticmethod
    def search_disp():
        
        atrac = (
            Atraccion.select()
            .where(Atraccion.activa == True)
        )

        return list(atrac)
    
    @staticmethod
    def modificar_activa(id):
        atrac = Atraccion.get(Atraccion.id == id)
        if not atrac:
            return
        if Atraccion.activa == True:
            Atraccion.activa = False
        else:
            Atraccion.activa = True
        atrac.save()
        return atrac

    @staticmethod
    def delete(id):
        return Atraccion.delete().where(Atraccion.id == id)

    @staticmethod
    def mayor_cientoveinte():
        visit = (
            Atraccion.select()
            .where(Atraccion.detalles["duracion_segundos"] > 120)
        )

        return list(visit)
    
    @staticmethod
    def mayor_ocho():
        visit = (
            Atraccion.select()
            .where(Atraccion.detalles["intensidad"] > 7)
        )

        return list(visit)




    @staticmethod
    def nueva_caracteristica_atraccion(id_atraccion, caracteristica):
        atraccion = Atraccion.get(Atraccion.id == id_atraccion)
        if not atraccion:
            return f"Error, la atracción [{id_atraccion}] no existe"
        if not caracteristica:
            return f"Error, introduce una caracteristica [{caracteristica}] válida"
        caracteristicas = atraccion.detalles["caracteristicas"]
        if caracteristica in caracteristicas:
            return f"Error, la caracteristica ya existe"
        json_struct = {"caracteristicas":{}}

