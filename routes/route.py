from fastapi import APIRouter
from models.cats import Cat
from config.database import collection_name
from schema.schemas import individual_serializer, list_serial
from bson import ObjectId

router = APIRouter()

# GET all cats
@router.get("/cats")
def read_cats():
    cats = list(collection_name.find())
    return list_serial(cats)

# GET a specific cat by id
@router.get("/cats/{cat_id}")
def read_cat(cat_id: str):
    cat = collection_name.find_one({'_id': ObjectId(cat_id)})
    if cat:
        return individual_serializer(cat)
    return {'message': 'Cat not found'}

# POST a new cat
@router.post("/cats")
def create_cat(cat: Cat):
    new_cat = collection_name.insert_one(dict(cat))
    cat = collection_name.find_one({'_id': new_cat.inserted_id})
    return individual_serializer(cat)

# PUT update a cat
@router.put("/cats/{cat_id}")
def update_cat(cat_id: str, cat: Cat):
    updated_cat = collection_name.update_one(
        {'_id': ObjectId(cat_id)},
        {'$set': dict(cat)}
    )
    if updated_cat.modified_count:
        cat = collection_name.find_one({'_id': ObjectId(cat_id)})
        return individual_serializer(cat)
    return {'message': 'Cat not found'}

# DELETE a cat
@router.delete("/cats/{cat_id}")
def delete_cat(cat_id: str):
    deleted_cat = collection_name.delete_one({'_id': ObjectId(cat_id)})
    if deleted_cat.deleted_count:
        return {'message': 'Cat deleted successfully'}
    return {'message': 'Cat not found'}

# DELETE all cats
@router.delete("/cats")
def delete_all_cats():
    deleted_cats = collection_name.delete_many({})
    if deleted_cats.deleted_count:
        return {'message': 'All cats deleted successfully'}
    return {'message': 'No cats found'}