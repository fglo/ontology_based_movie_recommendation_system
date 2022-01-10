from fastapi import APIRouter
from owlready2 import *

onto = get_ontology("data/system_rekomendacji_extra.owl").load()

router = APIRouter()

@router.get("/owl/categories", tags=["categories"])
async def get_categories():
    global onto
    return [ind.name for ind in list(onto.get_instances_of(onto["Kategoria"]))]
    
@router.get("/owl/categories/movies/{moviename}", tags=["categories"])
async def get_categories_of_movie(moviename : str):
    global onto
    categories = []
    for movie in list(onto.get_instances_of(onto["Film"])):
        if movie.name == moviename:
            categories = [ind.name for ind in list(movie.Film_jest_Kategoria)]
            break
    return categories

@router.get("/owl/categories/series/{seriesname}", tags=["categories"])
async def get_categories_of_series(seriesname : str):
    global onto
    movies = []
    for series in list(onto.get_instances_of(onto["Seria"])):
        if series.name == seriesname:
            movies = [movie for movie in list(series.Seria_zawiera_Film)]
            break
    categories = []
    for movie in movies:
        for category in list(movie.Film_jest_Kategoria):
            if category.name not in categories:
                categories.append(category.name)
    return categories

@router.get("/owl/categories/liked/{username}", tags=["categories"])
async def get_users_liked_categories(username : str):
    global onto
    for user in list(onto.get_instances_of(onto["Uzytkownik"])):
        if user.name == username:
            break
    categories = []
    for movie in list(user.Uzytkownik_lubi_Film):
        for category in list(movie.Film_jest_Kategoria):
            if category.name not in categories:
                categories.append(category.name)
    return categories

@router.get("/owl/categories/watched/{username}", tags=["categories"])
async def get_users_watched_categories(username : str):
    global onto
    for user in list(onto.get_instances_of(onto["Uzytkownik"])):
        if user.name == username:
            break
    categories = []
    for movie in list(user.Uzytkownik_ogladal_Film):
        for category in list(movie.Film_jest_Kategoria):
            if category.name not in categories:
                categories.append(category.name)
    return categories