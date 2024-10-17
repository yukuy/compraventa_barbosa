import secrets
from datetime import timedelta
import cloudinary

class config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # Cambia a SQLite con un archivo local llamado database.db
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex(16)  # Genera una clave secreta aleatoria
    SECRET_KEY = 'tu_clave_secreta_fija_aqui'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # Configuración del sistema para recuperar contraseña
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'compraventaoficial@gmail.com'
    MAIL_PASSWORD = 'krhh vsi h emey nulx'
    MAIL_DEFAULT_SENDER = 'compraventaoficial@gmail.com'
    
    # Configuración de Cloudinary
    CLOUD_NAME = 'dcg9njwmk'
    API_KEY = '173894522551611'
    API_SECRET = 'QpgpM1sFU6F7KDFFa47Jn-jvx5E'  # Asegúrate de que esta sea tu API Secret real

    @staticmethod
    def init_cloudinary():
        cloudinary.config(
            cloud_name=config.CLOUD_NAME,
            api_key=config.API_KEY,
            api_secret=config.API_SECRET
        )
