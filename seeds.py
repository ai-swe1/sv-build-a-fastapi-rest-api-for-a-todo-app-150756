from models import Todo, session

todo1 = Todo(title='Todo 1', description='This is the first todo')
session.add(todo1)
session.commit()
