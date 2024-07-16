from sqlmodel import create_engine, SQLModel

sql_file_name = 'Archive.db'
sql_url = f'sqlite:///{sql_file_name}'

engine = create_engine(sql_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)