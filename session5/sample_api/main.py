import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from mongo_mediator import MongoMediator

mongo_mediator = MongoMediator(os.environ['MONGO_CONN_STRING'])

app = FastAPI()


@app.get("/")
def all_routes_explained():
    return JSONResponse(content={
        "routes": {
            "/": "Current page",
            "GET /get-all": "GET all the elements in the database",
            "POST /city-info": "POST a city along with its information",
            "GET /city-info/{id}": "GET a city by its ID",
            "DELETE /city-info/{id}": "DELETE a city by its ID",
            "PUT /city-info/{id}": "PUT (update) an entry by its id"
        }
    })


@app.get("/get-all")
def get_all_cities():
    return JSONResponse(content=mongo_mediator.get_all())


@app.get("/city-info/{city_id}")
def get_city_by_id(city_id: int):
    return JSONResponse(content=mongo_mediator.get_by_id(city_id))


@app.post("/city-info")
def add_city(city_id: int, city: str, population: int):
    exists = mongo_mediator.get_by_id(city_id)
    if exists['result']:
        return {f"Error": f"City ID already exists "}, exists

    mongo_mediator.insert_one({
        'city_id': city_id,
        'city': city,
        'population': population
    })
    return {"Success": "City added to the database."}


@app.delete("/city-info/{city_id}")
def delete_city(city_id: int):
    try:
        mongo_mediator.delete_by_id(city_id)
        return {"Success"}
    except:
        return {"Error deleting city."}


@app.put("/city-info/{city_id}")
def delete_city(city_id: int, population: int, city: str):
    try:
        mongo_mediator.update_by_id(city_id, city, population)
        return {"Success"}
    except:
        return {"Error updating city."}
