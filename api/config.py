from api import app

DEBUG = True

# USERNAME = 'root'
# PASSWORD = '123456'
# SERVER = 'localhost'
# DB = 'projetoapiflask'

# CORRETO:
DB_USER='root'
DB_PASSWORD='123456'
DB_HOST='localhost'
DB_PORT=3306
DB_NAME='projetoapiflask'

SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
# DATABASE_URL=f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'

