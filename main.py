from pprint import pprint
from models.user_model import UserModel
from models.post_model import PostModel
from models.like_model import LikeModel
from repositories.user_repo import UserRepo
from database import db, inicializar_base
from repositories.like_repo import *

inicializar_base([UserModel,PostModel,LikeModel])
print("Base de datos inicializada correctamente, tablas reseteadas")
while True:
    print("----MENU X----\n" \
        "\n1. Usuarios\n" \
        "\n2. Posts\n" \
        "\n3. Likes\n" \
        "\n4. Salir\n")
    opcion = input("Selecciona una opción: ")
    match opcion:
        case "1":
            while True:
                print("\n----USUARIOS----\n" \
                    "\n1. Crear usuario\n" \
                    "\n2. Eliminar usuario\n" \
                    "\n3. Buscar usuario (ID)\n" \
                    "\n4. Mostrar todos los usuarios\n" \
                    "\n5.\n" \
                    "\n6.\n" \
                    "\n7.\n" \
                    "\n8.\n" \
                    "\n9.\n" \
                    "\n10.\n" \
                    "\n11.\n" \
                    "\n12. Salir\n\n")
                opcion = input("Selecciona una opción: ")
                match opcion:
                    case "1":
                        pass
                    case "2":
                        pass
                    case "3":
                        pass
                    case "4":
                        pass
                    case "5":
                        pass
                    case "6":
                        pass
                    case "7":
                        pass
                    case "8":
                        pass
                    case "9":
                        pass
                    case "10":
                        pass
                    case "11":
                        pass
                    case "12":
                        pass
                        print("Volviendo al menú principal...")
                        break
                    case _:
                        print("Opción no válida")
        case "2":
            print("\n----POSTS----\n" \
                "\n1.\n" \
                "\n2.\n" \
                "\n3.\n" \
                "\n4.\n" \
                "\n5.\n" \
                "\n6.\n" \
                "\n7.\n" \
                "\n8.\n")
            pass
        case "3":
            print("\n----LIKES----\n" \
                "\n1.\n" \
                "\n2.\n" \
                "\n3.\n" \
                "\n4.\n" \
                "\n5.\n" \
                "\n6.\n" \
                "\n7.\n" \
                "\n8.\n")
            pass
        case "4":
            print("\nSaliendo de X...")
            break
        case _:
            print("\nOpción no válida\n")