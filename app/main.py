from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal, engine, create_db_and_tables
from typing import List

create_db_and_tables()

app = FastAPI(title="Task Manager API")

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para CREAR una nueva tarea
@app.post("/tasks/", response_model=schemas.Task)
def create_new_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

# Endpoint para LEER todas las tareas
@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks

# (Añade esto al final del archivo crud.py)

# Función para OBTENER una sola tarea por su ID
def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

# Función para BORRAR una tarea
def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return db_task
    return None

# (Añade esto al final del archivo main.py)
from fastapi import HTTPException

# ... (tus otros endpoints aquí)

# Endpoint para OBTENER una sola tarea
@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# Endpoint para BORRAR una tarea
@app.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task