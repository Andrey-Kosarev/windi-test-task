from pydantic import BaseModel, EmailStr

class UserBaseModel(BaseModel):
    name: str
    email: EmailStr

class CreateUserModel(UserBaseModel):
    password: str

class UserModel(UserBaseModel):
    id: int