from sqlalchemy import Column, String, Integer

from database import Base

class Estabelecimento(Base):
    __tablename__ = 'estabelecimento'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50),nullable=False)
    cnpj = Column(Numeric(18),nullable=False)
    dono = Column(String(50),nullable=False)
    telefone = Column(String(11),nullable=False)


class recebimentos(Base):
    id = Column(Integer, primary_key=True)
    cliente = Column(Numeric,nullable=False)
    cnpj_estabelecimento = Column(Numeric,nullable=False)
