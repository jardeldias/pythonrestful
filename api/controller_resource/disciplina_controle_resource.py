from flask_restful import Resource
from api import api
from api.schemas import disciplina_schema
from api.service import disciplina_service
from api.dto import disciplina_dto
from flask import request, make_response, jsonify

class DisciplinaControllerResource(Resource):
    def get(self):
        disciplinas = disciplina_service.listar_disciplina()
        validate = disciplina_schema.DisciplinaSchema(many=True)
        return make_response(validate.jsonify(disciplinas), 200)
    def post(self):
        disciplina_schema_var = disciplina_schema.DisciplinaSchema()
        validate = disciplina_schema_var.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            nova_disciplina = disciplina_dto.DisciplinaDTO(nome=nome)
            retorno = disciplina_service.cadastrar_disciplina(nova_disciplina)
            disciplina_json = disciplina_schema_var.jsonify(retorno)
            return make_response(disciplina_json, 201)

    def put(self, id):
        disciplina = disciplina_service.listar_disciplinas_by_id(id)
        if disciplina is None:
            return make_response(jsonify("Disciplina não encontrada"), 404)
        disciplina_schema_var = disciplina_schema.DisciplinaSchema()
        validate = disciplina_schema_var.validate(request.json)
        if validate:
            make_response(jsonify(validate), 400)
            return None
        else:
            nome = request.json['nome']
            nova_disciplina_alterada = disciplina_dto.DisciplinaDTO(nome=nome)
            disciplina_service.atualizar_disciplina(disciplina, nova_disciplina_alterada)
            disciplina_atualizada = disciplina_service.listar_disciplinas_by_id(id)
            return make_response(disciplina_schema_var.jsonify(disciplina_atualizada), 200)

    def delete(self, id):
        disciplinadb = disciplina_service.listar_disciplinas_by_id(id)
        if disciplinadb is None:
            return make_response(jsonify("Disciplina não encontrada"), 400)
        disciplina_service.excluir_disciplina(disciplinadb)
        return make_response("Disciplina Excluida com sucesso")

class DisciplinaDetailControllerResource(Resource):
    def get(self, id_detail_get):
        disciplina = disciplina_service.listar_disciplinas_by_id(id_detail_get)
        if disciplina is None:
            return make_response(jsonify("Disciplina não encontrada"), 404)
        validate = disciplina_schema.DisciplinaSchema()
        return make_response(validate.jsonify(disciplina), 200)

api.add_resource(DisciplinaControllerResource,'/disciplina', endpoint='getDisciplinas')
api.add_resource(DisciplinaControllerResource, '/disciplina/<int:id>', endpoint='IdPutDelete', methods=['PUT', 'DELETE'])
api.add_resource(DisciplinaDetailControllerResource,'/disciplina/<int:id_detail_get>', endpoint='getId')
