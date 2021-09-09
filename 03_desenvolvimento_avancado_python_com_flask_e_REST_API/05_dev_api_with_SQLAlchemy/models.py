# Aqui onde vão ficar as classes da tabela do banco de dados SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite://atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         binds=engine))

Base = declarative_base()
Base.query = db_session.query_property()