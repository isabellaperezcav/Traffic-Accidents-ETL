
print("✅ conexion_db.py se está ejecutando correctamente")

# conexion_db.py
import psycopg2

def conectar_db():
    try:
        conn = psycopg2.connect(
            dbname="CrashTraffic",
            user="postgres",
            password="root",
            host="localhost",
            port="5432",
            options="-c client_encoding=UTF8"
        )
        conn.set_client_encoding('UTF8')  # Asegurar que la codificación sea UTF-8
        print("✅ Conexión exitosa con psycopg2")
        return conn
    except Exception as e:
        print("❌ Error en conexión con psycopg2:", e)
        return None