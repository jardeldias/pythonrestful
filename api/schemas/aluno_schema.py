# Schemas são responsáveis pelas validações do que chegar do controller
# Schemas é usa para fazer validação
from api import ma
from api.models import aluno_model
from marshmallow import fields

class AlunoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = aluno_model.AlunoModel
        load_instance = True
        fields = ("id","nome","data_nascimento")

    nome = fields.String(required=True)
    data_nascimento = fields.Date(required=True)
