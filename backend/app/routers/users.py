from fastapi import APIRouter
from owlready2 import *

onto = get_ontology("data/system_rekomendacji_extra.owl").load()

router = APIRouter()

@router.get("/owl/users", tags=["users"])
async def get_all_users():
    global onto
    return [ind.name for ind in list(onto.get_instances_of(onto["Uzytkownik"]))]

@router.post("/owl/users/{username}", tags=["users"]) 
async def create_individual(username : str):
    global onto
    onto.Uzytkownik(username)
    sync_reasoner(onto, infer_property_values = True)