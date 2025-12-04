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
    
    