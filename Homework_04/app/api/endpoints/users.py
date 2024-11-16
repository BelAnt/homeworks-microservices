from typing import Any, List
from fastapi import APIRouter, HTTPException, Path

from app.api.crud import users
from app.api.models.user import UserSchema, UserDB

router = APIRouter()


@router.post("/", response_model=UserDB, status_code=201)
async def create_user(payload: UserSchema):
    row_id = await users.post(payload)

    response_object = {
        "id": row_id,
        "username": payload.username,
        "firstname": payload.firstname,
        "lastname": payload.lastname,
        "email": payload.email,
        "phone": payload.phone
    }
    return response_object


@router.get("/{user_id}/", response_model=UserDB)
async def read_user(user_id: int = Path(..., gt=0), ):
    row = await users.get(user_id)
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    return row


@router.put("/{user_id}/", response_model=UserDB)
async def update_user(payload: UserSchema, user_id: int = Path(..., gt=0)):  # Ensures the input is greater than 0
    row = await users.get(user_id)
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    row_id = await users.put(user_id, payload)
    response_object = {
        "id": row_id,
        "username": payload.username,
        "firstname": payload.firstname,
        "lastname": payload.lastname,
        "email": payload.email,
        "phone": payload.phone
    }
    return response_object


@router.delete("/{user_id}/", response_model=UserDB)
async def delete_user(user_id: int = Path(..., gt=0)):
    row = await users.get(user_id)
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    await users.delete(user_id)

    return row
