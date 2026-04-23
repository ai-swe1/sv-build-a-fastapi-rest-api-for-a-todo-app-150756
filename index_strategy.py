from sqlalchemy import create_engine, Index
from models import Todo
engine = create_engine('postgresql://user:password@host:port/dbname')
Index('idx_todo_title', Todo.title).create(engine)
Index('idx_todo_created_at', Todo.created_at).create(engine)
