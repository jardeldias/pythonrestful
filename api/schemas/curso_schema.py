from marshmallow_sqlalchemy import auto_field

from api import ma
from api.models import curso_model
from marshmallow import fields

from api.schemas.disciplina_schema import DisciplinaSchema


class CursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = curso_model.CursoModel
        load_instance = True
    #     fields = ('id', 'nome', 'descricao', 'disciplinas')
    #
    # nome = fields.String(required=True)
    # descricao = fields.String(required=True)
    # disciplinas = auto_field()
    disciplinas_ids = fields.List(fields.Int(), load_only=True, data_key="disciplinas")
    disciplinas = ma.Nested(DisciplinaSchema, many=True, dump_only=True)

curso_schema = CursoSchema()
cursos_schema = CursoSchema(many=True)
