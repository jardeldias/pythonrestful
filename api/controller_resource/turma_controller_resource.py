from asttokens.util import NodeMethods
from flask_restful import Resource
from api import api
from api.schemas import turma_schema
from api.dto import turma_dto
from api.service import turma_service
from flask import request, make_response, jsonify

class TurmaController(Resource):
    def get(self):
        turmas = turma_service.listar_turmas()
        validate = turma_schema.TurmaSchema(many=True)
        return make_response(validate.jsonify(turmas), 200)

    def post(self):
        turma_schema_var = turma_schema.TurmaSchema()
        validate = turma_schema_var.validate(request.json)
        if validate:
            return make_response((jsonify(validate)), 400)
        else:
            nome = request.json["nome"]
            data_incio  = request.json["data_inicio"]
            data_fim  = request.json["data_fim"]
            descricao = request.json["descricao"]
            curso_id = request.json["curso_id"]
            nova_turma = turma_dto.TurmaDTO(nome=nome, data_inicio=data_incio, data_fim=data_fim,descricao=descricao, curso_id=curso_id)
            retorno = turma_service.cadastrar_turma(nova_turma)
            turma_json = turma_schema_var.jsonify(retorno)
            return make_response(turma_json, 201)

    def put(self, id):
        turma = turma_service.listar_turmas_by_id(id)
        if turma is None:
            return make_response(jsonify("Turma não encontrada"))
        turma_schema_var = turma_schema.TurmaSchema()
        validate = turma_schema_var.validate(request.json)
        if validate:
            make_response(jsonify(validate), 400)
            return None
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            data_inicio = request.json['data_inicio']
            data_fim = request.json['data_fim']
            curso_id = request.json['curso_id']
            nova_turma_alterado = turma_dto.TurmaDTO(nome=nome,
                                                     descricao=descricao,
                                                     data_inicio=data_inicio,
                                                     data_fim=data_fim,
                                                     curso_id=curso_id)
            turma_service.atualizar_turma(turma, nova_turma_alterado)
            turma_atualizada = turma_service.listar_turmas_by_id(id)
            return make_response(turma_schema_var.jsonify(turma_atualizada), 200)

    def delete(self, id):
        turmadb = turma_service.listar_turmas_by_id(id)
        if turmadb is None:
            return make_response(jsonify("Turma não encontrada"), 404)
        turma_service.excluir_turma(turmadb)
        return make_response("Turma excluida com sucesso", 204)

class TurmaDetailController(Resource):
    def get(self, id):
        turma = turma_service.listar_turmas_by_id(id)
        if turma is None:
            return make_response(jsonify("Turma não encontrada"), 404)
        validate = turma_schema.TurmaSchema()
        return make_response(validate.jsonify(turma), 200)

api.add_resource(TurmaController, '/turma', endpoint='turmaGET')
api.add_resource(TurmaController, '/turma/<int:id>', endpoint='turmaPUT_DELETE', methods=['PUT', 'DELETE'])
api.add_resource(TurmaDetailController, '/turma/<int:id>', endpoint='getID')
