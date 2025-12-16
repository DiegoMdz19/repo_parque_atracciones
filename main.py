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
        #VISITANTES -- FUNCIONA BIEN TODO - FALTA TEST
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
                        fecha_registro = datetime.now()
                        while True:
                            tipo_favorito = input("Tipo favorito (extrema/familiar/infantil/acuatica): ")
                            if tipo_favorito in ['extrema','familiar','infantil','acuatica']:
                                break
                            else:
                                print("Tipo no válido. Prueba otra vez")

                        restricciones_input = input("Restricciones (separa por comas si hay varias, o deja vacio): ")
                        if restricciones_input.strip() == "":
                            restricciones = []
                        else:
                            restricciones = [r.strip() for r in restricciones_input.split(",")]

                        historial_visitas = []
                        agregar_historial = input("¿Desea agregar historial de visitas? (s/n): ").lower().strip()
                        while agregar_historial == "s":
                            fecha_visita_input = input("Fecha visita (YYYY-MM-DD): ")
                            try:
                                fecha_visita = datetime.strptime(fecha_visita_input, "%Y-%m-%d").strftime("%Y-%m-%d")
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
                        while True:
                            try:
                                id_visitante = int(input("ID del visitante a eliminar: "))
                                break
                            except ValueError:
                                print("El ID debe ser numérico. Intenta de nuevo.")

                        filas = RepoVisitante.delete_visitante(id_visitante)
                        if filas != 0:
                            print(f"Visitante con id {id_visitante} eliminado correctamente (tickets incluidos)")
                        else:
                            print(f"No existe ningún visitante con id {id_visitante}")
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
        #ATRACCIONES -- FUNCIONA TODO BIEN- FALTA TEST
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
                        nombre = input("\nNombre de la nueva atracción: \n")
                        while True:
                                tipo = input("\nTipo (extrema/familiar/infantil/acuatica): \n")
                                if tipo in ['extrema','familiar','infantil','acuatica']:
                                    break
                                else:
                                    print("Tipo no válido. Prueba otra vez")
                        while True:
                            try:
                                altura_minima = int(input("Altura minima (cm): "))
                                break
                            except ValueError:
                                print("Altura no válida. Ingresa un número.")

                        while True:
                            try:
                                duracion_segundos = int(input("Duración de la atracción (segundos): "))
                                break
                            except ValueError:
                                print("Duración no válida. Debe ser un número")
                        
                        while True:
                            try:
                                capacidad_por_turno = int(input("Capacidad de la atracción: "))
                                break
                            except ValueError:
                                print("Capacidad no válida. Debe ser un número entero")

                        while True:
                            try:
                                intensidad = int(input("Intensidad de la atracción (0-10): "))
                                if intensidad >= 0 and intensidad <= 10:
                                    break
                                else:
                                    print("La intensidad debe ser entre 0 y 10")
                            except ValueError:
                                print("Intensidad no válida. Debe ser un número entero del 0 al 10")

                        caracteristicas = input("Caracteristicas (separadas por coma): ").split(",")
                        apertura = input("Hora de apertura (hh:mm): ")
                        cierre = input("Hora de cierre (hh:mm): ")
                        mantenimiento = input("Horarios de mantenimiento(hh:mm-hh:mm)(para insertar varios separar por comas): ").split(",")


                        detalles = {
                            "duracion_segundos": duracion_segundos,
                            "capacidad_por_turno": capacidad_por_turno,
                            "intensidad": intensidad,
                            "caracteristicas": [c.strip() for c in caracteristicas],
                            "horarios": {
                                "apertura" : apertura,
                                "cierre" : cierre,
                                "mantenimiento" : [m.strip() for m in mantenimiento]
                            }
                        }
                        
                        try:
                            atraccion = RepoAtraccion.create_atraccion(
                                nombre=nombre,
                                tipo=tipo,
                                altura_minima=altura_minima,
                                detalles=detalles
                            )

                            if atraccion:
                                print(f"Atraccion '{atraccion.nombre}' creada correctamente con ID {atraccion.id}")
                        except Exception as e:
                            print(f"Error al crear la atracción  : {e}")
                    case "2":
                        print("\n----BUSCAR ATRACCIÓN (ID)----\n")
                        while True:
                            try:
                                atraccion_id = int(input("Id de la atracción: "))
                                break
                            except Exception as e:
                                print("El id debe ser numérico")
                        
                        atraccion = RepoAtraccion.search_by_id_atraccion(atraccion_id)
                        if atraccion is None:
                            print(f"No existe una atracción con el id: {atraccion_id}")
                        else:
                            print(atraccion)
                    case "3":
                        print("\n----OBTENER TODAS LAS ATRACCIONES----\n")
                        for atraccion in RepoAtraccion.search_all_atraccion():
                            print(atraccion)
                    case "4":
                        print("\n----ATRACCIONES DISPONIBLES (ACTIVAS)----\n")
                        for atraccion in RepoAtraccion.search_disp():
                            print(atraccion)
                    case "5":
                        print("\n----ELIMINAR UNA ATRACCIÓN (ID)----\n")
                        id_atraccion = int(input("ID de la atracción a eliminar: "))
                        RepoAtraccion.delete_atraccion(id_atraccion)
                        print(f"Atracción con id: {id_atraccion} eliminada correctamente.")
                    case "6":
                        print("\n----CAMBIAR ESTADO DE UNA ATRACCIÓN (ACTIVO/INACTIVO)----\n")
                        while True:
                            try:
                                id_atraccion = int(input("Id de atracción a cambiar estado: "))
                                break
                            except ValueError:
                                print("El ID debe ser un número. Intenta de nuevo.")
                        atraccion = RepoAtraccion.modificar_activa(id_atraccion)
                        if atraccion is None:
                            print(f"No existe ninguna atracción con el id : {id_atraccion}")
                        else:
                            estado = ""
                            if atraccion.activa:
                                estado = "Activa"
                            else:
                                estado = "Inactiva"
                            print(f"El estado de la atracción '{atraccion.nombre}' ha sido cambiado a : {estado}")

                    case "7":
                        print("Volviendo al menú principal...")
                        break
                    case _:
                        print("Opción no válida")
        #TICKETS
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
        #CONSULTAS
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
                        visitantes = RepoVisitante.visit_extremas()
                        if not visitantes:
                            print("No existen visitantes con preferencia de atracciones extremas") 
                        else:
                            for visitante in visitantes:
                                print(visitante)

                    case "2":
                        print("\n----ATRACCIONES CON INTENSIDAD MAYOR A 7----\n")
                        atracciones = RepoAtraccion.mayor_siete()
                        for atraccion in atracciones:
                            print(atraccion)
                    case "3":
                        print("\n----TICKETS TIPO 'COLEGIO' CON PRECIO MENOR A 30€----\n")
                        tickets = RepoTicket.tickets_colegio_menor_30()
                        for ticket in tickets:
                            print(ticket)
                    case "4":
                        print("\n----ATRACCIONES CON DURACIÓN MAYOR A 120 SEGUNDOS----\n")
                        atracciones = RepoAtraccion.mayor_cientoveinte()
                        for atraccion in atracciones:
                            duracion = int(atraccion.detalles.get("duracion_segundos",))
                            print(f"{atraccion.nombre}, Duracion: {duracion}")
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
        #JSONB falta testing
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
                        print("\n----CAMBIAR PRECIO A UN TICKET----\n")
                        while True:
                            try:
                                id_ticket = int(input("Id del ticket a cambiar precio: "))
                                break
                            except ValueError:
                                print("El id debe ser numérico")
                        while True:
                            try:
                                precio_nuevo = float(input("Nuevo precio: "))
                                break
                            except ValueError:
                                print("El precio debe ser un número (se aceptan decimales)")
                        RepoTicket.cambiar_precio_ticket(id_ticket,precio_nuevo)
                        print(f"Precio del ticket #{id_ticket} se ha cambiado a {precio_nuevo} €")
                    case "2":
                        print("\n----ELIMINAR UNA RESTRICCIÓN A UN VISITANTE----\n")                  
                        while True:
                            try:
                                id_visitante = int(input("Id del visitante: "))
                                visitante = Visitante.get(Visitante.id == id_visitante)
                                break 
                            except ValueError:
                                print("El id debe ser numérico")
                            except Visitante.DoesNotExist:
                                print(f"No se encuentra ningún visitante con el id {id_visitante}")

                        restriccion = input("Restricción a eliminar: ").strip().lower()

                        resultado = RepoVisitante.eliminar_restriccion(id_visitante, restriccion)

                        if resultado is False:
                            print(f"La restricción '{restriccion}' no se encuentra en el visitante con id {id_visitante}")
                        else:
                            print(f"La restricción '{restriccion}' ha sido eliminada del visitante con id {id_visitante} correctamente")
                    case "3":
                        print("\n----AÑADIR UNA NUEVA CARACTERISTICA A UNA ATRACCIÓN----\n")
                        while True:
                            try:
                                id_atraccion = int(input("Id de la atracción: "))
                                atraccion = Atraccion.get(Atraccion.id == id_atraccion)
                                break 
                            except ValueError:
                                print("El id debe ser numérico")
                            except Atraccion.DoesNotExist:
                                print(f"No se encuentra ninguna atracción con el id {id_atraccion}")

                        caracteristica = input("Característica a añadir: ").strip().lower()
                        RepoAtraccion.nueva_caracteristica_atraccion(id_atraccion, caracteristica)
                        print(f"La característica ha sido añadida con éxito")
                    case "4":
                        print("\n----AÑADIR UNA NUEVA VISITAL AL HISTORIAL DE UN VISITANTE----\n")
                        while True:
                            try:
                                id_visitante = int(input("Id del visitante: "))
                                visitante = Visitante.get(Visitante.id == id_visitante)
                                break 
                            except ValueError:
                                print("El id debe ser numérico")
                            except Atraccion.DoesNotExist:
                                print(f"No se encuentra ningun visitante con el id {id_visitante}")
                        while True:
                            fecha_visita = input("Fecha visita (YYYY-MM-DD): ").strip()
                            try:
                                datetime.strptime(fecha_visita, "%Y-%m-%d")
                                break
                            except ValueError:
                                print("Fecha no válida, recuerda el formato YYYY-MM-DD")
                        while True:
                            try:
                                cantidad = int(input("Atracciones visitadas: "))
                                break
                            except ValueError:
                                print("Debe ser un número")
                        
                        resultado = RepoVisitante.anyadir_visita(id_visitante, fecha_visita, cantidad)

                        if resultado is not None:
                            print(f"Visita añadida correctamente al historial del visitante {visitante.nombre}")
                    case "5":
                        print("Volviendo al menú principal...")
                        break
                    case _:
                        print("Opción no válida")
        #CONSULTAS ÚTILES
        case "6":
            while True:
                print("\n----CONSULTAS ÚTILES----\n" \
                    "\n1. Listar visitantes ordenados por cantidad total de tickets comprados (Descendente)\n" \
                    "\n2. 5 Atracciones más vendidas\n"
                    "\n3. Obtener visitantes con más de 100€ de gasto en tickets\n" \
                    "\n4. Atracciones compatibles para un visitante\n" \
                    "\n5. Salir\n")
                opcion = input("Selecciona una opción: ")
                match opcion:
                    case "1":
                        print("\n----LISTAR VISITANTES POR CANTIDAD DE TICKETS (DESCENDENTE)----\n")
                        visitantes = RepoTicket.tickets_total_visitante()
                        for visitante in visitantes:
                            print(visitante, f"Total de tickets: {visitante.total_tickets}")
                    case "2":
                        print("\n----5 ATRACCIONES MÁS VENDIDAS----\n")
                        atracciones = RepoTicket.top_5_atracciones_mas_vendidas()
                        i = 0
                        for atraccion in atracciones:
                            i += 1
                            print(f"{i} . {atraccion.nombre}")
                            
                    case "3":
                        print("\n----OBTENER VISITANTES CON MÁS DE 100€ DE GASTO EN TICKETS----\n")
                        visitantes = RepoTicket.visitantes_mas_100_euros()
                        for visitante in visitantes:
                            total = sum(float(ticket.detalles_compra["precio"]) for ticket in visitante.tickets)
                            print(f" {visitante.nombre}(ID:{visitante.id})--> Gasto total: {total} €")
                    case "4":
                        print("\n----ATRACCIONES COMPATIBLES PARA UN VISITANTE----\n")
                        try:
                            id_visitante = input("Id del visitante: ")
                        except ValueError:
                            print("El id debe ser un número")
                        atracciones = RepoAtraccion.atracciones_compatibles(id_visitante)
                        for atraccion in atracciones:
                            print(atraccion.nombre)
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