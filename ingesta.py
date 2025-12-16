from datetime import datetime

from models.model_atraccion import Atraccion
from models.model_visitante import Visitante
from models.model_ticket import Ticket


def ingesta_datos():

    # ===============================
    # LIMPIAR TABLAS
    # ===============================
    Ticket.delete().execute()
    Visitante.delete().execute()
    Atraccion.delete().execute()

    print("Iniciando ingesta...\n")

    # =====================================================================
    # ATRACCIONES (10)
    # =====================================================================

    atracciones_data = [
        {
            "nombre": "Vórtice Carmesí",
            "tipo": "extrema",
            "altura_minima": 140,
            "detalles": {
                "duracion_segundos": 120,
                "capacidad_por_turno": 24,
                "intensidad": 9,
                "caracteristicas": ["giros", "looping"],
                "horarios": {"apertura": "10:00", "cierre": "22:00", "mantenimiento": ["15:00-16:00"]},
            },
            "activa": True,
            "fecha_inauguracion": datetime(2019, 5, 10)
        },
        {
            "nombre": "Titán del Acero",
            "tipo": "extrema",
            "altura_minima": 145,
            "detalles": {
                "duracion_segundos": 110,
                "capacidad_por_turno": 26,
                "intensidad": 8,
                "caracteristicas": ["caídas", "alta_velocidad"],
                "horarios": {"apertura": "10:00", "cierre": "22:00", "mantenimiento": ["15:00-16:00"]},
            },
            "activa": True,
            "fecha_inauguracion": datetime(2020, 7, 21)
        },
        {
            "nombre": "Raptor 360",
            "tipo": "extrema",
            "altura_minima": 135,
            "detalles": {
                "duracion_segundos": 90,
                "capacidad_por_turno": 22,
                "intensidad": 7,
                "caracteristicas": ["inversiones", "giros"],
                "horarios": {"apertura": "10:00", "cierre": "22:00", "mantenimiento": ["15:00-16:00"]},
            },
            "activa": True,
            "fecha_inauguracion": datetime(2018, 3, 14)
        },
        {
            "nombre": "Selva Mística",
            "tipo": "familiar",
            "altura_minima": 110,
            "detalles": {
                "duracion_segundos": 70,
                "capacidad_por_turno": 30,
                "intensidad": 4,
                "caracteristicas": ["temática", "suave"],
                "horarios": {"apertura": "09:30", "cierre": "21:00", "mantenimiento": []},
            },
            "activa": True,
            "fecha_inauguracion": datetime(2021, 9, 2)
        },
        {
            "nombre": "Neblina Azul",
            "tipo": "familiar",
            "altura_minima": 105,
            "detalles": {
                "duracion_segundos": 60,
                "capacidad_por_turno": 28,
                "intensidad": 5,
                "caracteristicas": ["tobogán", "suave"],
                "horarios": {"apertura": "09:30", "cierre": "21:00", "mantenimiento": []},
            },
            "activa": True,
            "fecha_inauguracion": datetime(2022, 1, 18)
        },
        {
            "nombre": "Caverna de Eco",
            "tipo": "infantil",
            "altura_minima": 90,
            "detalles": {
                "duracion_segundos": 45,
                "capacidad_por_turno": 15,
                "intensidad": 2,
                "caracteristicas": ["decorado", "movimiento_suave"],
                "horarios": {"apertura": "09:00", "cierre": "20:00", "mantenimiento": []},
            },
            "activa": True,
            "fecha_inauguracion": datetime(2020, 4, 5)
        },
        {
            "nombre": "Laberinto Solar",
            "tipo": "infantil",
            "altura_minima": 95,
            "detalles": {
                "duracion_segundos": 50,
                "capacidad_por_turno": 18,
                "intensidad": 3,
                "caracteristicas": ["colores", "sonidos"],
                "horarios": {"apertura": "09:00", "cierre": "20:00", "mantenimiento": []},
            },
            "activa": True,
            "fecha_inauguracion": datetime(2021, 10, 1)
        },
        {
            "nombre": "AquaTornado",
            "tipo": "acuatica",
            "altura_minima": 120,
            "detalles": {
                "duracion_segundos": 80,
                "capacidad_por_turno": 20,
                "intensidad": 6,
                "caracteristicas": ["agua", "rápidos"],
                "horarios": {"apertura": "10:00", "cierre": "21:00", "mantenimiento": ["14:00-14:30"]},
            },
            "activa": False,
            "fecha_inauguracion": datetime(2019, 6, 30)
        },
        {
            "nombre": "Furia Marina",
            "tipo": "acuatica",
            "altura_minima": 130,
            "detalles": {
                "duracion_segundos": 140,
                "capacidad_por_turno": 18,
                "intensidad": 7,
                "caracteristicas": ["tobogán", "salpicaduras"],
                "horarios": {"apertura": "10:00", "cierre": "21:00", "mantenimiento": ["14:00-14:30"]},
            },
            "activa": True,
            "fecha_inauguracion": datetime(2018, 9, 11)
        },
        {
            "nombre": "Cumbre Estelar",
            "tipo": "acuatica",
            "altura_minima": 125,
            "detalles": {
                "duracion_segundos": 200,
                "capacidad_por_turno": 22,
                "intensidad": 5,
                "caracteristicas": ["agua", "subidas"],
                "horarios": {"apertura": "10:00", "cierre": "21:00", "mantenimiento": ["14:00-14:30"]},
            },
            "activa": False,
            "fecha_inauguracion": datetime(2020, 12, 15)
        }
    ]

    Atraccion.insert_many(atracciones_data).execute()
    atracciones = list(Atraccion.select())
    print("10 atracciones insertadas")

    # =====================================================================
    # VISITANTES (50)
    # =====================================================================

    nombres = [
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

    fechas_registro = [
        datetime(2022,1,1,10,0), datetime(2022,1,2,10,0), datetime(2022,1,3,10,0),
        datetime(2022,1,4,10,0), datetime(2022,1,5,10,0), datetime(2022,1,6,10,0),
        datetime(2022,1,7,10,0), datetime(2022,1,8,10,0), datetime(2022,1,9,10,0),
        datetime(2022,1,10,10,0), datetime(2022,1,11,10,0), datetime(2022,1,12,10,0),
        datetime(2022,1,13,10,0), datetime(2022,1,14,10,0), datetime(2022,1,15,10,0),
        datetime(2022,1,16,10,0), datetime(2022,1,17,10,0), datetime(2022,1,18,10,0),
        datetime(2022,1,19,10,0), datetime(2022,1,20,10,0), datetime(2022,1,21,10,0),
        datetime(2022,1,22,10,0), datetime(2022,1,23,10,0), datetime(2022,1,24,10,0),
        datetime(2022,1,25,10,0), datetime(2022,1,26,10,0), datetime(2022,1,27,10,0),
        datetime(2022,1,28,10,0), datetime(2022,1,29,10,0), datetime(2022,1,30,10,0),
        datetime(2022,1,31,10,0), datetime(2022,2,1,10,0), datetime(2022,2,2,10,0),
        datetime(2022,2,3,10,0), datetime(2022,2,4,10,0), datetime(2022,2,5,10,0),
        datetime(2022,2,6,10,0), datetime(2022,2,7,10,0), datetime(2022,2,8,10,0),
        datetime(2022,2,9,10,0), datetime(2022,2,10,10,0), datetime(2022,2,11,10,0),
        datetime(2022,2,12,10,0), datetime(2022,2,13,10,0), datetime(2022,2,14,10,0),
        datetime(2022,2,15,10,0), datetime(2022,2,16,10,0), datetime(2022,2,17,10,0),
        datetime(2021,3,5,5,0), datetime(2022,6,5,15,0)
    ]

    tipos_favoritos = [
        "extrema","familiar","infantil","acuatica","extrema",
        "familiar","infantil","acuatica","extrema","familiar",
        "infantil","acuatica","extrema","familiar","infantil",
        "acuatica","extrema","familiar","infantil","acuatica",
        "extrema","familiar","infantil","acuatica","extrema",
        "familiar","infantil","acuatica","extrema","familiar",
        "infantil","acuatica","extrema","familiar","infantil",
        "acuatica","extrema","familiar","infantil","acuatica",
        "extrema","familiar","infantil","acuatica","extrema",
        "familiar","infantil","acuatica","extrema","familiar"
    ]

    restricciones_lista = [
        ["mareos"], [], ["dolor_de_espalda"], ["problemas_cardiacos"], [],
        ["mareos"], [], ["asma"], ["dolor_de_espalda"], [],
        ["mareos"], ["hipertensión"], [], ["mareos"], [],
        ["lesiones_previas"], [], ["asma"], [], ["mareos"],
        ["dolor_de_espalda"], [], ["problemas_cardiacos"], [], ["mareos"],
        [], ["asma"], [], ["dolor_de_espalda"], [],
        ["hipertensión"], [], ["mareos"], [], ["lesiones_previas"],
        [], ["asma"], [], ["dolor_de_espalda"], [],
        ["mareos"], [], ["problemas_cardiacos"], [], ["asma"],
        [], ["mareos"], [], ["hipertensión"], []
    ]

    alturas = [
        160,161,162,163,164,
        165,166,167,168,169,
        170,171,172,173,174,
        175,176,177,178,179,
        130,131,132,133,134,
        135,136,137,138,139,
        140,141,142,143,144,
        145,146,147,148,149,
        150,151,152,153,154,
        193,181,167,191,190
    ]

    visitantes_data = []

    for i in range(50):
        visitantes_data.append({
            "nombre": nombres[i],
            "email": nombres[i].lower().replace(" ", ".") + "@mail.com",
            "altura": alturas[i],
            "fecha_registro": fechas_registro[i],
            "preferencias": {
                "tipo_favorito": tipos_favoritos[i],
                "restricciones": restricciones_lista[i],
                "historial_visitas": [
                    {"fecha": "2023-01-10", "atracciones_visitadas": 3},
                    {"fecha": "2023-03-15", "atracciones_visitadas": 5}
                ]
            }
        })

    Visitante.insert_many(visitantes_data).execute()
    visitantes = list(Visitante.select())
    print("50 visitantes insertados")

    # =====================================================================
    # TICKETS (100)
    # =====================================================================


    tipos_ticket = [
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "general","colegio","empleado","general","colegio","empleado",
        "empleado","general","colegio","empleado"
    ]

    precios = [
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "35.50","29.00","32.00","35.50","29.00","32.00",
        "32.00","35.50","29.00","32.00"
    ]

    metodos_pago = [
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo","tarjeta","transferencia",
        "efectivo","tarjeta","transferencia","efectivo"
    ]




    descuentos = []
    for i in range(100):
        if i <= 25:
            descuentos.append(["promo_verano"])
        elif 25 < i <= 50:
            descuentos.append(["estudiante"])
        elif 50 < i <= 75:
            descuentos.append(["jubilado"])
        else: 
            descuentos.append([])

    servicios_extra = []
    for i in range(100):
        if i < 25:
            servicios_extra.append(["fast_pass"])
        else:
            servicios_extra.append([])

    usados = []
    for i in range(100):
        usados.append(True if i < 60 else False)

    fechas_compra = [
        datetime(2024,1,1,12,0), datetime(2024,1,2,12,0), datetime(2024,1,3,12,0),
        datetime(2024,1,4,12,0), datetime(2024,1,5,12,0), datetime(2024,1,6,12,0),
        datetime(2024,1,7,12,0), datetime(2024,1,8,12,0), datetime(2024,1,9,12,0),
        datetime(2024,1,10,12,0), datetime(2024,1,11,12,0), datetime(2024,1,12,12,0),
        datetime(2024,1,13,12,0), datetime(2024,1,14,12,0), datetime(2024,1,15,12,0),
        datetime(2024,1,16,12,0), datetime(2024,1,17,12,0), datetime(2024,1,18,12,0),
        datetime(2024,1,19,12,0), datetime(2024,1,20,12,0), datetime(2024,1,21,12,0),
        datetime(2024,1,22,12,0), datetime(2024,1,23,12,0), datetime(2024,1,24,12,0),
        datetime(2024,1,25,12,0), datetime(2024,1,26,12,0), datetime(2024,1,27,12,0),
        datetime(2024,1,28,12,0), datetime(2024,1,29,12,0), datetime(2024,1,30,12,0),
        datetime(2024,1,31,12,0), datetime(2024,2,1,12,0), datetime(2024,2,2,12,0),
        datetime(2024,2,3,12,0), datetime(2024,2,4,12,0), datetime(2024,2,5,12,0),
        datetime(2024,2,6,12,0), datetime(2024,2,7,12,0), datetime(2024,2,8,12,0),
        datetime(2024,2,9,12,0), datetime(2024,2,10,12,0), datetime(2024,2,11,12,0),
        datetime(2024,2,12,12,0), datetime(2024,2,13,12,0), datetime(2024,2,14,12,0),
        datetime(2024,2,15,12,0), datetime(2024,2,16,12,0), datetime(2024,2,17,12,0),
        datetime(2024,2,18,12,0), datetime(2024,2,19,12,0), datetime(2024,2,20,12,0),
        datetime(2024,2,21,12,0), datetime(2024,2,22,12,0), datetime(2024,2,23,12,0),
        datetime(2024,2,24,12,0), datetime(2024,2,25,12,0), datetime(2024,2,26,12,0),
        datetime(2024,2,27,12,0), datetime(2024,2,28,12,0), datetime(2024,2,29,12,0),
        datetime(2024,3,1,12,0), datetime(2024,3,2,12,0), datetime(2024,3,3,12,0),
        datetime(2024,3,4,12,0), datetime(2024,3,5,12,0), datetime(2024,3,6,12,0),
        datetime(2024,3,7,12,0), datetime(2024,3,8,12,0), datetime(2024,3,9,12,0),
        datetime(2024,3,10,12,0), datetime(2024,3,11,12,0), datetime(2024,3,12,12,0),
        datetime(2024,3,13,12,0), datetime(2024,3,14,12,0), datetime(2024,3,15,12,0),
        datetime(2024,3,16,12,0), datetime(2024,3,17,12,0), datetime(2024,3,18,12,0),
        datetime(2024,3,19,12,0), datetime(2024,3,20,12,0), datetime(2024,3,21,12,0),
        datetime(2024,3,22,12,0), datetime(2024,3,23,12,0), datetime(2024,3,24,12,0),
        datetime(2024,3,25,12,0), datetime(2024,3,26,12,0), datetime(2024,3,27,12,0),
        datetime(2024,3,28,12,0), datetime(2024,3,29,12,0), datetime(2024,3,30,12,0),
        datetime(2024,3,31,12,0), datetime(2024,4,1,12,0), datetime(2024,4,2,12,0),
        datetime(2024,4,3,12,0), datetime(2024,4,4,12,0), datetime(2024,4,5,12,0),
        datetime(2024,4,6,12,0), datetime(2024,4,7,12,0), datetime(2024,4,8,12,0),
        datetime(2024,4,9,12,0), datetime(2024,4,10,12,0)
    ]

    fechas_visita = [
        datetime(2024,1,3).date(), datetime(2024,1,4).date(), datetime(2024,1,5).date(),
        datetime(2024,1,6).date(), datetime(2024,1,7).date(), datetime(2024,1,8).date(),
        datetime(2024,1,9).date(), datetime(2024,1,10).date(), datetime(2024,1,11).date(),
        datetime(2024,1,12).date(), datetime(2024,1,13).date(), datetime(2024,1,14).date(),
        datetime(2024,1,15).date(), datetime(2024,1,16).date(), datetime(2024,1,17).date(),
        datetime(2024,1,18).date(), datetime(2024,1,19).date(), datetime(2024,1,20).date(),
        datetime(2024,1,21).date(), datetime(2024,1,22).date(), datetime(2024,1,23).date(),
        datetime(2024,1,24).date(), datetime(2024,1,25).date(), datetime(2024,1,26).date(),
        datetime(2024,1,27).date(), datetime(2024,1,28).date(), datetime(2024,1,29).date(),
        datetime(2024,1,30).date(), datetime(2024,1,31).date(), datetime(2024,2,1).date(),
        datetime(2024,2,2).date(), datetime(2024,2,3).date(), datetime(2024,2,4).date(),
        datetime(2024,2,5).date(), datetime(2024,2,6).date(), datetime(2024,2,7).date(),
        datetime(2024,2,8).date(), datetime(2024,2,9).date(), datetime(2024,2,10).date(),
        datetime(2024,2,11).date(), datetime(2024,2,12).date(), datetime(2024,2,13).date(),
        datetime(2024,2,14).date(), datetime(2024,2,15).date(), datetime(2024,2,16).date(),
        datetime(2024,2,17).date(), datetime(2024,2,18).date(), datetime(2024,2,19).date(),
        datetime(2024,2,20).date(), datetime(2024,2,21).date(), datetime(2024,2,22).date(),
        datetime(2024,2,23).date(), datetime(2024,2,24).date(), datetime(2024,2,25).date(),
        datetime(2024,2,26).date(), datetime(2024,2,27).date(), datetime(2024,2,28).date(),
        datetime(2024,2,29).date(), datetime(2024,3,1).date(), datetime(2024,3,2).date(),
        datetime(2024,3,3).date(), datetime(2024,3,4).date(), datetime(2024,3,5).date(),
        datetime(2024,3,6).date(), datetime(2024,3,7).date(), datetime(2024,3,8).date(),
        datetime(2024,3,9).date(), datetime(2024,3,10).date(), datetime(2024,3,11).date(),
        datetime(2024,3,12).date(), datetime(2024,3,13).date(), datetime(2024,3,14).date(),
        datetime(2024,3,15).date(), datetime(2024,3,16).date(), datetime(2024,3,17).date(),
        datetime(2024,3,18).date(), datetime(2024,3,19).date(), datetime(2024,3,20).date(),
        datetime(2024,3,21).date(), datetime(2024,3,22).date(), datetime(2024,3,23).date(),
        datetime(2024,3,24).date(), datetime(2024,3,25).date(), datetime(2024,3,26).date(),
        datetime(2024,3,27).date(), datetime(2024,3,28).date(), datetime(2024,3,29).date(),
        datetime(2024,3,30).date(), datetime(2024,3,31).date(), datetime(2024,4,1).date(),
        datetime(2024,4,2).date(), datetime(2024,4,3).date(), datetime(2024,4,4).date(),
        datetime(2024,4,5).date(), datetime(2024,4,6).date(), datetime(2024,4,7).date(),
        datetime(2024,4,8).date(), datetime(2024,4,9).date(), datetime(2024,4,10).date(),
        datetime(2024,4,10).date()
    ]

    fechas_uso = []
    for i in range(100):
        if usados[i]:
            fechas_uso.append(datetime(fechas_visita[i].year, fechas_visita[i].month, fechas_visita[i].day, 15, 0))
        else:
            fechas_uso.append(None)

    tickets_data = []
    for i in range(100):
        tickets_data.append({
            "visitante_id": visitantes[i % 50].id,
            "atraccion_id": atracciones[i % 10].id,
            "fecha_compra": fechas_compra[i],
            "fecha_visita": fechas_visita[i],
            "tipo_ticket": tipos_ticket[i],
            "usado": usados[i],
            "fecha_uso": fechas_uso[i],
            "detalles_compra": {
                "precio": precios[i],
                "descuentos_aplicados": descuentos[i],
                "servicios_extra": servicios_extra[i],
                "metodo_pago": metodos_pago[i]
            }
        })

    Ticket.insert_many(tickets_data).execute()
    print("100 tickets insertados")

    print("\nIngesta finalizada correctamente.\n")




