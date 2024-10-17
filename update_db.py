from app import db, app
from sqlalchemy import text

# Crear el contexto de la aplicación
with app.app_context():
    # Conectar a la base de datos y verificar si la columna existe
    try:
        # Verificar si la columna 'rol' ya existe
        result = db.session.execute(text("PRAGMA table_info(usuarios)"))
        columns = [row[1] for row in result.fetchall()]
        
        if 'rol' not in columns:
            # Agregar la columna si no existe
            db.session.execute(text("ALTER TABLE usuarios ADD COLUMN rol TEXT DEFAULT 'cliente'"))
            db.session.commit()  # Confirmar la transacción
            print("Columna 'rol' agregada con éxito")
        else:
            print("La columna 'rol' ya existe en la tabla 'usuarios'.")
    except Exception as e:
        print(f"Error al agregar la columna: {e}")
