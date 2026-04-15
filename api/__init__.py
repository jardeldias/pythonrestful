from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)
app.json.ensure_ascii = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from api.controller_resource import aluno_controler_resource
from api.models import aluno_model
from api.service import aluno_service

from api.controller_resource import professor_controller_resource
from api.models import professor_model
from api.service import professor_service

from api.controller_resource import turma_controller_resource
from api.models import turma_model
from api.service import turma_service

from api.controller_resource import disciplina_controle_resource
from api.models import disciplina_model
from api.service import disciplina_service

from api.controller_resource import curso_controller_resource
from api.models import curso_model
from api.service import curso_service
