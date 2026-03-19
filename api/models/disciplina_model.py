from api import db

class DisciplinaModel(db.Model):
    __tablename__ = 'disciplina'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
