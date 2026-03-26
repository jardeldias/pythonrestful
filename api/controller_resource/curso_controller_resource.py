from flask_restful import Resource
from api import api
from api.dto import curso_dto
from api.schemas import curso_schema
from api.service import curso_service
from flask import request, make_response, jsonify

class CursoControllerResource(Resource):
    def get(self):
        cursos = curso_service.listar_curso()
        validate = curso_schema.CursoSchema(many=True)
        return make_response(validate.jsonify(cursos), 200)

    def post(self):
        curso_schema_var  = curso_schema.CursoSchema()
        validate = curso_schema_var.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            disciplinas = request.json['disciplinas']

            novo_curso = curso_dto.CursoDTO(nome=nome, descricao=descricao, disciplinas=disciplinas)
            retorno = curso_service.cadastrar_curso(novo_curso)
            curso_json = curso_schema_var.jsonify(retorno)
            return make_response(curso_json, 201)

    def put(self, id):
        curso = curso_service.listar_curso_by_id(id)
        if curso is None:
            return make_response(jsonify("Curso não encontrado"), 404)
        curso_schema_var = curso_schema.CursoSchema()
        validate = curso_schema_var.validate(request.json)
        if validate:
            make_response(jsonify(validate), 400)
            return None
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            disciplinas = request.json['disciplinas']

            novo_curso_alterado = curso_dto.CursoDTO(nome=nome,
                                                     descricao=descricao,
                                                     disciplinas=disciplinas)
            curso_service.atualizar_curso(curso, novo_curso_alterado)
            curso_atualizado = curso_service.listar_curso_by_id(id)
            return make_response(jsonify(validate), 400)

    def delete(self, id):
        cursodb = curso_service.listar_curso_by_id(id)
        if cursodb is None:
            return make_response(jsonify("Curso não encontrado"), 404)
        curso_service.excluir_curso(cursodb)
        # 204 é um response que não retorna corpo na página
        return make_response('Curso expluido com sucesso',200)

class CursoDetailControllerResource(Resource):
    def get(self, id):
        curso = curso_service.listar_curso_by_id(id)
        if curso is None:
            return make_response(jsonify('Curso não encontrado'), 404)
        validate = curso_schema.CursoSchema()
        return make_response(validate.jsonify(curso), 200)

api.add_resource(CursoControllerResource,'/curso', endpoint='cursoGetPost', methods=['GET','POST'])
api.add_resource(CursoControllerResource,'/curso/<int:id>', endpoint='cursoPutDelte', methods=['PUT', 'DELETE'])
api.add_resource(CursoDetailControllerResource,'/curso/<int:id>', endpoint='cursoGetId', methods=['GET'])
