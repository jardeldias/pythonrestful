from flask_restful import Resource
from api import api
from api.schemas import professor_schema
from api.service import professor_service
from api.dto import professor_dto
from flask import request, make_response, jsonify

class ProfessorController(Resource):
    def get(self, id=None):
        if id is None:
            professores = professor_service.listar_professor()
            validate = professor_schema.ProfessorSchema(many=True)
            return make_response(validate.jsonify(professores), 200)
        else:
            professor = professor_service.listar_professor_by_id(id)
            if professor is None:
                return make_response(jsonify('Professor não encontrado.'))
            validate = professor_schema.ProfessorSchema()
            return make_response(validate.jsonify(professor), 200)

    def post(self):
        professor_schema_var = professor_schema.ProfessorSchema()
        validate = professor_schema_var.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            data_nascimento = request.json["data_nascimento"]

            novo_professor = professor_dto.ProfessorDTO(nome=nome, data_nascimento=data_nascimento)
            retorno = professor_service.cadastrar_professor(novo_professor)
            professor_json = professor_schema_var.jsonify(retorno)

            return make_response(professor_json, 201)

    def put(self, id):
        professor = professor_service.listar_professor_by_id(id)
        if professor is None:
            return make_response(jsonify("Professor não encontrado"))
        professor_schema_var = professor_schema.ProfessorSchema()
        validate = professor_schema_var.validate(request.json)
        if validate:
            make_response(jsonify(validate), 400)
            return None
        else:
            nome = request.json["nome"]
            data_nascimento = request.json["data_nascimento"]
            novo_professor_alterado = professor_dto.ProfessorDTO(nome=nome, data_nascimento=data_nascimento)
            professor_service.atualizar_professor(professor, novo_professor_alterado)
            professor_atualizado = professor_service.listar_professor_by_id(id)
            return make_response(professor_schema_var.jsonify(professor_atualizado), 200)

    def delete(self, id):
        professordb = professor_service.listar_professor_by_id(id)
        if professordb is None:
            return make_response(jsonify("Professor não encontrado"), 404)
        professor_service.excluir_professor(professordb)
        return make_response("Professor excluido com sucesso", 204)

api.add_resource(ProfessorController,'/professor', '/professor/<int:id>')
