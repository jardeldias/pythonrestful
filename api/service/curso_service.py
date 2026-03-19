from api.models import curso_model
from api import db

def cadastrar_curso(curso):
    curso_db = curso_model.CursoModel(nome=curso.nome, descricao=curso.descricao)
    db.session.add(curso_db)
    db.session.commit()
    return curso_db

def listar_curso():
    cursos = curso_model.CursoModel.query.all()
    return cursos

def listar_curso_by_id(parm_id):
    curso = curso_model.CursoModel.query.filter_by(id=parm_id).first()
    return curso

def atualizar_curso(curso_db, curso_atualizado):
    curso_db.nome = curso_atualizado.nome
    curso_db.descricao = curso_atualizado.descricao
    db.session.commit()

def excluir_curso(curso):
    db.session.delete(curso)
    db.session.commit()
