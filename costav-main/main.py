from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from fastapi import APIRouter, Response, status
from ..config.db import conn
from ..models.user import users
from ..schemas.user import Data
from starlette.status import HTTP_204_NO_CONTENT

app=FastAPI()
data = APIRouter()


@app.post("/telefonos/")
async def crear_telefono(telefono: telefono):
    query = "INSERT INTO telefonos (id,marca, modelo, codigo, cantidad, precio) VALUES (%s,%s, %s, %s, %s, %s)"
    valores = (telefono.id,telefono.marca, telefono.modelo, telefono.codigo, telefono.cantidad, telefono.precio)
    cursor.execute(query, valores)
    mysql_conn.commit()
    return {"mensaje": "Telefono creado exitosamente"}

@app.get("/telefonos/{id_telefono}")
async def obtener_telefono(id_telefono: int):
    query = "SELECT * FROM telefonos WHERE id = %s"
    cursor.execute(query, (id_telefono,))
    empleado = cursor.fetchone()
    if empleado:
        return {"id": telefono[0], "marca": telefono[1], "modelo": telefono[2], "codigo": telefono[3], "cantidad": empleado[4], "precio": empleado[5]}
    else:
        raise HTTPException(status_code=404, detail="telefono no encontrado")

@app.put("/telefonos/{id_empleado}")
async def actualizar_empleado(id_telefono: int, telefono : telefono):
    query = "UPDATE empleados SET id = %s,marca = %s, modelo = %s, codigo = %s, cantidad = %s, precio = %s WHERE id = %s"
    valores = (telefono.id,telefono.marca, telefono.modelo, telefono.codigo, telefono.cantidad, telefono.precio, id_telefono)
    cursor.execute(query, valores)
    mysql_conn.commit()
    return {"mensaje": "Detalles del telefono actualizados exitosamente"}

# Ruta para eliminar un empleado por su ID
@app.delete("/telefonos/{id_telefono}")
async def eliminar_telefono(id_telefono: int):
    query = "DELETE FROM telefonos WHERE id = %s"
    cursor.execute(query, (id_telefono,))
    mysql_conn.commit()
    return {"mensaje": "telefono eliminado exitosamente"}
