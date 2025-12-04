from datetime import datetime
import random

from models.model_atraccion import Atraccion
from models.model_visitante import Visitante
from models.model_ticket import Ticket
def ingesta_datos():
    # LIMPIAR TABLAS
    Ticket.delete().execute()
    Visitante.delete().execute()
    Atraccion.delete().execute()

    print("Iniciando ingesta de datos...\n")

    # ATRACCIONES (10) 
    nombres_atracciones = [
        "Vórtice Carmesí","Titán del Acero","Raptor 360",
        "Selva Mística","Neblina Azul",
        "Caverna de Eco","Laberinto Solar",
        "AquaTornado","Furia Marina","Cumbre Estelar"
    ]

    tipos_atraccion = [
        "extrema","extrema","extrema",
        "familiar","familiar",
        "infantil","infantil",
        "acuatica","acuatica","acuatica"
    ]

    detalles_base = [
        {"duracion_segundos": 80,"capacidad_por_turno": 20,"intensidad": 9,
        "caracteristicas":["giros","caída_lateral"],
        "horarios":{"apertura":"09:00","cierre":"21:00","mantenimiento":["13:00-14:00"]}},
        {"duracion_segundos": 60,"capacidad_por_turno": 18,"intensidad": 5,
        "caracteristicas":["bosque","tobogán"],
        "horarios":{"apertura":"10:00","cierre":"20:00","mantenimiento":[]}},
        {"duracion_segundos": 120,"capacidad_por_turno": 30,"intensidad": 8,
        "caracteristicas":["looping","subidas"],
        "horarios":{"apertura":"11:00","cierre":"22:00","mantenimiento":["16:00-17:00"]}},
        {"duracion_segundos": 45,"capacidad_por_turno": 16,"intensidad": 6,
        "caracteristicas":["agua","rápidos"],
        "horarios":{"apertura":"10:00","cierre":"21:00","mantenimiento":[]}}
    ]

    atracciones = []
    for i in range(10):
        a = Atraccion.create(
            nombre=nombres_atracciones[i],
            tipo=tipos_atraccion[i],
            altura_minima=random.randint(150,200),
            detalles=random.choice(detalles_base),
            activa=True,
            fecha_inauguracion=datetime(2018 + (i % 3), random.randint(1,12), random.randint(1,28))
        )
        atracciones.append(a)

    print("10 atracciones creadas con éxito")

    # VISITANTES (50)
    nombres_visitantes = [
        "Andrea Molina","Carlos Britez","Lucía Naranjo","Mateo Guajardo","Elena Prado",
        "Sebastián Lamas","Agustina Tellez","Federico Rivas","Aldana Duarte","Hugo Varela",
        "Cintia Romero","Javier Luján","Tamara Escalante","Fernando Paz","Ariana Quiroga",
        "Tomás Barreto","Carolina Viera","Bruno Altamirano","Valeria Rosas","Ignacio Fuentes",
        "Lorena Cabral","Mauro Ponce","Paula Espinoza","Diego Montiel","Karen Robledo",
        "Gonzalo Silva","Mariela Burgos","Dante Segovia","Rocío Gaitán","Emanuel Villalba",
        "Zaira Alarcón","Ramiro Cáceres","Miranda Olmos","Lucas Segura","Milena Bazán",
        "Nicolás Pereyra","Julieta Toledo","Ian Duarte","Sofía Menéndez","Leandro Chávez",
        "Gisela Lugo","Adrián Cordero","Florencia Peña","Gabriel Soria","Pilar Nuñez",
        "Joaquín Campos","Abril Franco","Mauricio Roldán","Emma Vallejos","Renzo Maidana"
    ]

    tipos_favoritos = ["extrema","familiar","infantil","acuatica"]
    restricciones_posibles = [[],["mareos"],["vertigo"],["cardiaco"]]

    dominios = ["mail.com","correo.com","example.com"]
    visitantes = []

    for i in range(50):
        registro = datetime(
            2022 + random.randint(0,2),
            random.randint(1,12),
            random.randint(1,28),
            random.randint(8,20),
            random.randint(0,59) 
        )
        historial = []
        for j in range(random.randint(1,3)):
            fecha_visita = datetime(2023 + random.randint(0,1), random.randint(1,12), random.randint(1,28))
            historial.append({
                "fecha": fecha_visita.strftime("%Y-%m-%d"),
                "atracciones_visitadas": random.randint(1,10)
            })
        nombre = nombres_visitantes[i].split()[0].lower()
        apellido = nombres_visitantes[i].split()[1].lower()
        email = f"{nombre}.{apellido}{random.randint(1,99)}@{random.choice(dominios)}"

        v = Visitante.create(
            nombre=nombres_visitantes[i],
            email=email,
            altura=random.randint(150,200),
            fecha_registro=registro,
            preferencias={
                "tipo_favorito": random.choice(tipos_favoritos),
                "restricciones": random.choice(restricciones_posibles),
                "historial_visitas": historial
            }
        )
        visitantes.append(v)

    print("50 visitantes creados con éxito")

    # TICKETS (100)
    tipos_ticket = ["general","colegio","empleado"]
    detalles_tickets = [
        {"precio":"35.50","descuentos_aplicados":[],"servicios_extra":[],"metodo_pago":"efectivo"},
        {"precio":"49.99","descuentos_aplicados":["promo_verano"],"servicios_extra":["fast_pass"],"metodo_pago":"tarjeta"},
        {"precio":"29.00","descuentos_aplicados":["colegio"],"servicios_extra":[],"metodo_pago":"transferencia"},
        {"precio":"65.00","descuentos_aplicados":[],"servicios_extra":["vip_zone","foto_recuerdo"],"metodo_pago":"tarjeta"}
    ]

    for i in range(100):
        visitante = visitantes[i % 50]
        atraccion = atracciones[i % 10]
        
        fecha_compra = datetime(
            2024,
            random.randint(1,12),
            random.randint(1,28),
            random.randint(9,21),
            random.randint(0,59)
        )
        
        fecha_visita = datetime(2024, random.randint(1,12), random.randint(1,28))
        fecha_uso = datetime(
            fecha_visita.year,
            fecha_visita.month,
            fecha_visita.day,
            random.randint(9,21),
            random.randint(0,59)
        )
        
        usado = i % 2 == 0 
        
        Ticket.create(
            visitante_id=visitante,
            atraccion_id=atraccion,
            fecha_compra=fecha_compra,
            fecha_visita=fecha_visita.date(),
            tipo_ticket=tipos_ticket[i % 3],
            usado=usado,
            fecha_uso=fecha_uso,
            detalles_compra=random.choice(detalles_tickets)
        )

    print("100 tickets creados con éxito\n")
    print("Ingesta de datos completada correctamente\n")




