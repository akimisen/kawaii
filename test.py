from sqlalchemy import Column, String, create_engine, Table, MetaData, Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

dbuser = 'sa'
dbpwd = 'test@local'
dbhost = 'localhost'
dbname = 'test'
db_uri = "mssql+pymssql://{}:{}@{}/{}".format(dbuser,quote_plus(dbpwd),dbhost,dbname) 
engine = create_engine(db_uri, echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()
connection = engine.connect()
m = MetaData()
t = Table('test', m, Column('id', Integer, primary_key=True),Column('num', Integer))
m.create_all(engine)
engine.execute(t.insert(), {'id': 1, 'num':1}, {'id':2, 'num':2})
connection.close()
engine.dispose()