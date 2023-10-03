from typing import Optional

from pydantic import BaseModel, EmailStr


class UserSchemaAdd(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr



class UpdateUserParams(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None

    async def get_params_dict(self):
        params = dict()
        if self.first_name and self.first_name != "":
            params["first_name"] = self.first_name
        if self.last_name and self.last_name != "":
            params["last_name"] = self.last_name
        if self.password and self.password != "":
            params["password"] = self.password
        if self.email and self.email != "":
            params["email"] = self.email
        return params



