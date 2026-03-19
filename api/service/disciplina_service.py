from api import db
from api.models import disciplina_model


def cadastrar_disciplina(disciplina):
    disciplina_db = disciplina_model.DisciplinaModel(nome=disciplina.nome)
    db.session.add(disciplina_db)
    db.session.commit()
    return disciplina_db

def listar_disciplina():
    disciplinas = disciplina_model.DisciplinaModel.query.all()
    return disciplinas

def listar_disciplinas_by_id(parm_id):
    disciplina = disciplina_model.DisciplinaModel.query.filter_by(id=parm_id).first()
    return disciplina

def atualizar_disciplina(disciplina_db, disciplina_atualizada):
    disciplina_db.nome = disciplina_atualizada.nome

def excluir_disciplina(disciplina):
    db.session.delete(disciplina)
    db.session.commit()