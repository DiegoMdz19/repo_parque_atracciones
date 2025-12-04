from peewee import *
import envyte # type: ignore

db = PostgresqlDatabase(
    envyte.get("SUPABASE_DB"),
    host=envyte.get("SUPABASE_DB_HOST"),
    port=int(envyte.get("SUPABASE_DB_PORT")),
    user=envyte.get("SUPABASE_DB_USER"),
    password=envyte.get("SUPABASE_DB_PASSWORD")
)

def inicializar_base(tablas, reiniciar=True):
    if reiniciar:
        db.drop_tables(tablas[::-1], safe=True)
        db.create_tables(tablas, safe=True)
    else:
        db.create_tables(tablas, safe=True)