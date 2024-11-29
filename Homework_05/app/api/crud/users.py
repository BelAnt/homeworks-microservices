from app.api.models.user import UserSchema
from app.db import users, database


async def post(payload: UserSchema):
    query = users.insert().values(username=payload.username, firstname=payload.firstname, lastname=payload.lastname,
                                  email=payload.email, phone=payload.phone)
    return await database.execute(query)


async def get(id: int):
    query = users.select().where(id == users.c.id)
    return await database.fetch_one(query)


async def get_all():
    query = users.select()
    return await database.fetch_all(query)


async def put(id: int, payload=UserSchema):
    query = (
        users.update().where(id == users.c.id).values(username=payload.username, firstname=payload.firstname,
                                                      lastname=payload.lastname, email=payload.email,
                                                      phone=payload.phone)
        .returning(users.c.id)
    )
    return await database.execute(query)


async def delete(id: int):
    query = users.delete().where(id == users.c.id)
    return await database.execute(query)
