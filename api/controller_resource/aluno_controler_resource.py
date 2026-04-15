# A principal peça de nossa API é o controler/resource,
# ele será responsável por receber e tratar as requisições HTTP

from flask_restful import Resource

from api import api
from api.schemas import aluno_schema
from api.service import aluno_service
from api.dto import aluno_dto
from flask import request, make_response, jsonify

class AlunoController(Resource):
    def get(self, id=None):
        if id is None:
            alunos = aluno_service.listar_aluno()
            validate = aluno_schema.AlunoSchema(many=True)
            return make_response(validate.jsonify(alunos), 200)
        else:
            aluno = aluno_service.listar_alunos_by_id(id)
            if aluno is None:
                return make_response(jsonify("Aluno não encontrado"), 404)
            validate = aluno_schema.AlunoSchema()
            return make_response(validate.jsonify(aluno), 200)

    def post(self):
        aluno_schema_var = aluno_schema.AlunoSchema()
        validate = aluno_schema_var.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            data_nascimento = request.json["data_nascimento"]
            novo_aluno = aluno_dto.AlunoDTO(nome=nome, data_nascimento=data_nascimento)
            retorno = aluno_service.cadastrar_aluno(novo_aluno)
            aluno_json = aluno_schema_var.jsonify(retorno)
            return make_response(aluno_json, 201)

    def put(self, id):
        aluno = aluno_service.listar_alunos_by_id(id)
        if aluno is None:
            return make_response(jsonify("Aluno não encontrado!"), 404)
        aluno_schema_var = aluno_schema.AlunoSchema()
        validate = aluno_schema_var.validate(request.json)
        if validate:
            make_response(jsonify(validate), 400)
            return None
        else:
            nome = request.json["nome"]
            data_nascimento = request.json["data_nascimento"]
            novo_aluno_alterado = aluno_dto.AlunoDTO(nome, data_nascimento)
            aluno_service.atualizar_aluno(aluno, novo_aluno_alterado)
            aluno_atualizado = aluno_service.listar_alunos_by_id(id)
            return make_response(aluno_schema_var.jsonify(aluno_atualizado), 200)

    def delete(self, id):
        alunodb = aluno_service.listar_alunos_by_id(id)
        if alunodb is None:
            return make_response(jsonify("Aluno não encontrado)"), 404)
        aluno_service.excluir_aluno(alunodb)
        return make_response("Aluno excluido com sucesso", 204)

api.add_resource(AlunoController,'/aluno','/aluno/<int:id>')
