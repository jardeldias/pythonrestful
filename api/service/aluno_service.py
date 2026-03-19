# O service é responsável por lidar com as regras de negócio da nossa aplicação.
# É uma parte fundamental da arquitetura em camadas.
# ORM é uma forma de se operar com banco de dados relacional usando orientação a objeto
from api.models import aluno_model
from api import db

def cadastrar_aluno(aluno):
    aluno_db = aluno_model.AlunoModel(nome=aluno.nome, data_nascimento=aluno.data_nascimento)
    db.session.add(aluno_db) # inset into aluno(nome, data_nascimento)
    db.session.commit()
    return aluno_db

def listar_aluno():
    alunos = aluno_model.AlunoModel.query.all()
    return alunos

def listar_alunos_by_id(parm_id):
    aluno = aluno_model.AlunoModel.query.filter_by(id=parm_id).first()
    return aluno

def atualizar_aluno(aluno_db, aluno_atualizado):
    aluno_db.nome = aluno_atualizado.nome
    aluno_db.data_nascimento = aluno_atualizado.data_nascimento
    db.session.commit()

def excluir_aluno(aluno):
    db.session.delete(aluno)
    db.session.commit()
