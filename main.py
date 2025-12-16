from pprint import pprint
from models.model_visitante import Visitante
from models.model_atraccion import Atraccion
from models.model_ticket import Ticket
from repositories.repo_visitante import RepoVisitante
from repositories.repo_atraccion import RepoAtraccion
from repositories.repo_ticket import RepoTicket
from database import db, inicializar_base
from ingesta import ingesta_datos
import time
from datetime import datetime

#inicializar_base([Visitante,Atraccion,Ticket])
#print("Base de datos inicializada correctamente, tablas reseteadas")
#ingesta_datos()
print("Iniciando menú Pichalandia...")
time.sleep(1)
while True:
    print("----MENU PICHALANDIA----\n" \
        "\n1. Visitantes\n" \
        "\n2. Atracciones\n" \
        "\n3. Tickets\n" \
        "\n4. Consultas\n" \
        "\n5. Modificaciones en JSONB\n" \
        "\n6. Consultas útiles\n" \
        "\n7. Salir\n")
    opcion = input("Selecciona una opción: ")
    match opcion:
        case "1":
            while True:
                print("\n----VISITANTES----\n" \
                    "\n1. Crear visitante\n" \
                    "\n2. Buscar visitante por id\n" \
                    "\n3. Obtener todos los visitantes\n" \
                    "\n4. Eliminar visitante y sus tickets (ID)\n" \
                    "\n5. Obtener visitantes con ticket para una atracción (ID)\n" \
                    "\n6. Salir\n")
                opcion = input("Selecciona una opción: ")
                match opcion:
                    case "1":
                        print("\n----CREAR VISITANTE----\n")
                        
                        nombre = input("Nombre completo: ")
                        email = input("Email: ")

                        while True:
                            try:
                                altura = int(input("Altura (cm): "))
                                break
                            except ValueError:
                                print("Altura no válida. Ingresa un número.")

                        while True:
                            try:
                                fecha_registro = datetime.strptime(input("Fecha registro (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Formato de fecha incorrecto. Usa 'YYYY-MM-DD HH:MM'.")

                        tipo_favorito = input("Tipo favorito (extrema/familiar/infantil/acuatica): ")
                        restricciones_input = input("Restricciones (separa por comas si hay varias, o deja vacio): ")
                        if restricciones_input.strip() == "":
                            restricciones = []
                        else:
                            restricciones = [r.strip() for r in restricciones_input.split(",")]

                        historial_visitas = []
                        agregar_historial = input("¿Desea agregar historial de visitas? (s/n): ").lower().strip()
                        while agregar_historial == "s":
                            fecha_visita_str = input("Fecha visita (YYYY-MM-DD): ")
                            try:
                                fecha_visita = datetime.strptime(fecha_visita_str, "%Y-%m-%d").strftime("%Y-%m-%d")
                                atracciones_visitadas = int(input("Cantidad de atracciones visitadas: "))
                                historial_visitas.append({
                                    "fecha": fecha_visita,
                                    "atracciones_visitadas": atracciones_visitadas
                                })
                            except ValueError:
                                print("Datos incorrectos, intenta de nuevo.")
                            agregar_historial = input("¿Agregar otra visita? (s/n): ").lower().strip()

                        preferencias = {
                            "tipo_favorito": tipo_favorito,
                            "restricciones": restricciones,
                            "historial_visitas": historial_visitas
                        }

                        visitante = RepoVisitante.create(
                            nombre=nombre,
                            email=email,
                            altura=altura,
                            fecha_registro=fecha_registro,
                            preferencias=preferencias
                        )

                        if visitante:
                            print(f"Visitante '{visitante.nombre}' creado correctamente con ID {visitante.id}")
                    case "2":
                        print("\n----BUSCAR VISITANTE (ID)----\n")
                        while True:
                            id_visitante = input("Id de visitante a buscar: ")
                            try:
                                id = int(id_visitante)
                                break
                            except ValueError:
                                print("El ID debe ser un número. Intenta de nuevo.")
                        try:
                            visitante = RepoVisitante.search_by_id(id)
                            print(visitante)
                        except Exception as e:
                            print(f"No se encontró visitante con ID {id}")
                    case "3":
                        print("\n----OBTENER TODOS LOS VISITANTES----\n")
                        for visitante in RepoVisitante.search_all():
                            print(visitante)

                    case "4":
                        print("\n----ELIMINAR VISITANTE----\n")
                        id_visitante = int(input("ID del visitante a eliminar: "))
                        RepoVisitante.delete_visitante(id_visitante)
                        print(f"Visitante con id: {id_visitante} eliminado correctamente (tickets incluidos)")
                    case "5":
                        print("\n----OBTENER VISITANTES CON TICKET POR ATRACCIÓN (ID)----\n")
                        id_atraccion = int(input("ID de la atracción: "))
                        visitantes = RepoVisitante.visit_tickets(id_atraccion)
                        for visitante in visitantes:
                            print(visitante)
                    case "6":
                        print("Volviendo al menú principal...")
                        break
                    case _:
                        print("Opción no válida")
        case "2":
            while True:
                print("\n----ATRACCIONES----\n" \
                    "\n1. Crear atracción\n" \
                    "\n2. Buscar atracción por id\n" \
                    "\n3. Obtener todas las atracciones\n" \
                    "\n4. Atracciones disponibles (activas)\n" \
                    "\n5. Eliminar una atracción\n" \
                    "\n6. Cambiar el estado de una atracción (activo/inactivo)\n" \
                    "\n7. Salir\n")
                opcion = input("Selecciona una opción: ")
                match opcion:
                    case "1":
                        print("\n----CREAR ATRACCIÓN----\n")
                    case "2":
                        print("\n----BUSCAR ATRACCIÓN (ID)----\n")
                    case "3":
                        print("\n----OBTENER TODAS LAS ATRACCIONES----\n")
                    case "4":
                        print("\n----ATRACCIONES DISPONIBLES (ACTIVAS)----\n")
                    case "5":
                        print("\n----ELIMINAR UNA ATRACCIÓN (ID)----\n")
                    case "6":
                        print("\n----CAMBIAR ESTADO DE UNA ATRACCIÓN (ACTIVO/INACTIVO)----\n")
                    case "7":
                        print("Volviendo al menú principal...")
                        break
                    case _:
                        print("Opción no válida")
        case "3":
            while True:
                print("\n----TICKETS----\n" \
                    "\n1. Crear ticket\n" \
                    "\n2. Buscar ticket por id\n"
                    "\n3. Obtener todos los tickets\n" \
                    "\n4. Marcar un ticket como usado (ID)\n" \
                    "\n5. Obtener tickets por visitante (ID)\n" \
                    "\n6. Obtener tickets por atraccion (ID)\n" \
                    "\n7. Salir\n")
                opcion = input("Selecciona una opción: ")
                match opcion:
                    case "1":
                        print("\n----CREAR TICKET----\n")
                    case "2":
                        print("\n----BUSCAR TICKET (ID)----\n")
                    case "3":
                        print("\n----OBTENER TODOS LOS TICKETS----\n")
                    case "4":
                        print("\n----MARCAR TICKET COMO USADO----\n")
                    case "5":
                        print("\n----OBTENER TICKETS POR VISITANTE (ID)----\n")
                    case "6":
                        print("\n----OBTENER TICKETS POR ATRACCIÓN (ID)----\n")
                    case "7":
                        print("Volviendo al menú principal...")
                        break
                    case _:
                        print("Opción no válida")
        case "4":
            while True:
                print("\n----CONSULTAS----\n" \
                    "\n1. Visitantes con preferencia por atracciones 'extremas'\n" \
                    "\n2. Atracciones con instensidad mayor a 7\n"
                    "\n3. Tickets tipo 'colegio' con precio menor a 30€\n" \
                    "\n4. Atracciones con mayor duración a 120 segundos\n" \
                    "\n5. Visitantes con problemas cardiacos\n" \
                    "\n6. Atracciones que tengan 'looping' y 'caida libre'\n" \
                    "\n7. Tickets con descuento 'estudiante'\n" \
                    "\n8. Atracciones con al menos un horario de mantenimiento programado\n" \
                    "\n9. Salir\n")
                opcion = input("Selecciona una opción: ")
                match opcion:
                    case "1":
                        print("\n----VISITANTES CON PREFERENCIA POR ATRACCIONES 'EXTREMAS'----\n")
                    case "2":
                        print("\n----ATRACCIONES CON INTENSIDAD MAYOR A 7----\n")
                    case "3":
                        print("\n----TICKETS TIPO 'COLEGIO' CON PRECIO MENOR A 30€----\n")
                    case "4":
                        print("\n----ATRACCIONES CON DURACIÓN MAYOR A 120 SEGUNDOS----\n")
                    case "5":
                        print("\n----VISITANTES CON PROBLEMAS CARDIACOS----\n")
                    case "6":
                        print("\n----ATRACCIONES CON LOOPING Y CAIDA LIBRE----\n")
                    case "7":
                        print("\n----TICKETS CON DESCUENTO 'ESTUDIANTE'----\n")
                    case "8":
                        print("\n----ATRACCIONES CON HORARIO PROGRAMADO----\n")
                    case "9":
                        print("Volviendo al menú principal...")
                        break
                    case _:
                        print("Opción no válida")
        case "5":
            while True:
                print("\n----MODIFICACIONES EN JSONB----\n" \
                    "\n1. Cambiar el precio de un ticket\n" \
                    "\n2. Eliminar una restricción a un visitante\n"
                    "\n3. Añadir una nueva característica a una atracción\n" \
                    "\n4. Añadir una nueva visita al historial de un visitante\n" \
                    "\n5. Salir\n")
                opcion = input("Selecciona una opción: ")
                match opcion:
                    case "1":
                        print("\n----CAMBIAR PRECIO A UN TICKET----\n") # PONER BONITO porfa
                        id = input("id ticket")
                        precio_nuevo = int(input("precio: "))
                        RepoTicket.cambiar_precio_ticket(id,precio_nuevo)
                    case "2":
                        print("\n----ELIMINAR UNA RESTRICCIÓN A UN VISITANTE----\n") # COORREGIR NO FUNCIONA 
                        id = input("id")
                        restriccion = input("restriccion")
                        RepoVisitante.eliminar_restriccion(id,restriccion)
                    case "3":
                        print("\n----AÑADIR UNA NUEVA CARACTERISTICA A UNA ATRACCIÓN----\n")
                    case "4":
                        print("\n----AÑADIR UNA NUEVA VISITAL AL HISTORIAL DE UN VISITANTE----\n")
                    case "5":
                        print("Volviendo al menú principal...")
                        break
                    case _:
                        print("Opción no válida")
        case "6":
            while True:
                print("\n----CONSULTAS ÚTILES----\n" \
                    "\n1. Listar visitantes ordenados por cantidad total de tickets comprados (Descendiente)\n" \
                    "\n2. 5 Atracciones más vendidas\n"
                    "\n3. Obtener visitantes con más de 100€ de gasto en tickets\n" \
                    "\n4. Atracciones compatibles para un visitante\n" \
                    "\n5. Salir\n")
                opcion = input("Selecciona una opción: ")
                match opcion:
                    case "1":
                        print("\n----LISTAR VISITANTES POR CANTIDAD DE TICKETS (DESCENDIENTE)----\n")
                    case "2":
                        print("\n----5 ATRACCIONES MÁS VENDIDAS----\n")
                    case "3":
                        print("\n----OBTENER VISITANTES CON MÁS DE 100€ DE GASTO EN TICKETS----\n")
                    case "4":
                        print("\n----ATRACCIONES COMPATIBLES PARA UN VISITANTE----\n")
                    case "5":
                        print("Volviendo al menú principal...")
                        break
                    case _:
                        print("Opción no válida")
        case "7":
            print("\nSaliendo de PICHALANDIA...")
            break
        case _:
            print("\nOpción no válida\n")