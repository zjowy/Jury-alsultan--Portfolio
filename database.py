from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string)


def load_projects_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from myprojects"))
    myprojects = []
    for row in result.all():
      myprojects.append(dict(row._mapping))
    return myprojects


def load_project_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"select * from myprojects where id = {id}"))
    rows = result.all()
    return dict(rows[0]._mapping)

def add_massage_to_db(data):
  with engine.connect() as conn:
    sql=text( f"INSERT INTO massages (Full_Name,email,massage) VALUES (\'{data['Full Name']}\',\'{data['email']}\',\'{data['massage']}\')"
    )


    conn.execute(sql)
    conn.commit()
