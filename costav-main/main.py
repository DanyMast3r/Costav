from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from pydantic import BaseModel

# Conexión a la base de datos MySQL con SQLAlchemy
SQLALCHEMY_DATABASE_URL = "mysql://root:@localhost/api"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definición de la clase base para las tablas
Base = declarative_base()

# Definición del modelo de datos para el telefono utilizando SQLAlchemy
class telefono(Base):
    __tablename__ = "telefonos"

    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String, index=True)
    marca = Column(String, index=True)
    precio = Column(String, index=True)
    cantidad = Column(String, index=True)

# Definición del modelo Pydantic para el telefono
class telefonoPydantic(BaseModel):
    id: int
    modelo: str
    marca: str
    precio: str
    cantidad: str


# Inicialización de la aplicación FastAPI
app = FastAPI()

# Funciones de acceso a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_telefono(db, telefono_id: int):
    telefono = db.query(telefono).filter(telefono.id == telefono_id).first()
    if not telefono:
        raise HTTPException(status_code=404, detail="telefono no encontrado")
    return telefono

def create_telefono(db, telefono: telefonoPydantic):
    db_telefono = telefono(**telefono.dict())
    db.add(db_telefono)
    db.commit()
    db.refresh(db_telefono)
    return db_telefono

def update_telefono(db, telefono_id: int, telefono: telefonoPydantic):
    db_telefono = get_telefono(db, telefono_id)
    for key, value in telefono.dict().items():
        setattr(db_telefono, key, value)
    db.commit()
    db.refresh(db_telefono)
    return db_telefono

def delete_telefono(db, telefono_id: int):
    db_telefono = get_telefono(db, telefono_id)
    db.delete(db_telefono)
    db.commit()
    return {"mensaje": "telefono eliminado exitosamente"}

# Rutas
@app.post("/telefonos/", response_model=telefonoPydantic)
def crear_telefono(telefono: telefonoPydantic, db: Session = Depends(get_db)):
    return create_telefono(db, telefono)

@app.get("/telefonos/{telefono_id}", response_model=telefonoPydantic)
def obtener_telefono(telefono_id: int, db: Session = Depends(get_db)):
    return get_telefono(db, telefono_id)

@app.put("/telefonos/{telefono_id}", response_model=telefonoPydantic)
def actualizar_telefono(telefono_id: int, telefono: telefonoPydantic, db: Session = Depends(get_db)):
    return update_telefono(db, telefono_id, telefono)

@app.delete("/telefonos/{telefono_id}")
def eliminar_telefono(telefono_id: int, db: Session = Depends(get_db)):
    return delete_telefono(db, telefono_id)