from sqlalchemy import Column, String, Integer,ForeignKey
from database import Base

#criando tabela de Estabelecimentos
class Estabelecimento(Base):
    __tablename__ = 'estabelecimento'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50),nullable=False)
    cnpj = Column(Numeric(18),nullable=False)
    dono = Column(String(50),nullable=False)
    telefone = Column(String(11),nullable=False)
