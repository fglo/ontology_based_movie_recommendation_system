from fastapi import APIRouter
from .. import onto

router = APIRouter()

@router.get("/owl/series", tags=["series"])
async def get_all_series():
    global onto
    return [ind.name for ind in onto.get_series()]

@router.get("/owl/series/movies/{moviename}", tags=["series"])
async def get_series_of_movie(moviename : str):
    global onto
    series = []
    for movie in onto.get_movies():
        if movie.name == moviename:
            series = [ind.name for ind in list(movie.Film_jest_z_Seria)]
            break
    return series

@router.get("/owl/series/categories/{categoryname}", tags=["series"])
async def get_series_of_category(categoryname : str):
    global onto
    movies = []
    for category in onto.get_categories():
        if category.name == categoryname:
            movies = [ind for ind in list(category.Kategoria_przypisana_do_Film)]
            break
    series = []
    for movie in movies:
        for ind in list(movie.Film_jest_z_Seria):
            if ind.name not in series:
                series.append(ind.name)
    return series