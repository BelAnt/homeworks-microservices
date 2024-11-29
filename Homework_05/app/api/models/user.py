from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    username: str = Field(..., min_length=2, max_length=256)  # additional validation for the inputs
    firstname: str = Field(..., min_length=1, max_length=50)
    lastname: str = Field(..., min_length=1, max_length=50)
    email: str = Field(..., min_length=1, max_length=50)
    phone: str = Field(..., min_length=1, max_length=50)


class UserDB(UserSchema):
    id: int
    username: str
    firstname: str
    lastname: str
    email: str
    phone: str
