from api.models import curso_model
from api.service.disciplina_service import listar_disciplinas_by_id
from api import db

def cadastrar_curso(curso):
    curso_db = curso_model.CursoModel(nome=curso.nome, descricao=curso.descricao)
    for i in curso.disciplinas:
        disciplina = listar_disciplinas_by_id(i)
        curso_db.disciplinas.append(disciplina)
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
    curso_db.disciplinas = []
    for i in curso_atualizado.disciplinas:
        disciplina = listar_disciplinas_by_id(i)
        curso_db.disciplinas.append(disciplina)
    db.session.commit()

def excluir_curso(curso):
    db.session.delete(curso)
    db.session.commit()
