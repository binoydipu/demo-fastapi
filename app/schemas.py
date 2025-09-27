from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, conint


class UserCreate(BaseModel):
  email: EmailStr
  password: str

# response model
class UserOut(BaseModel):
  id: int
  email: EmailStr
  created_at: datetime


class UserLogin(BaseModel):
  email: EmailStr
  password: str


class PostBase(BaseModel):
  title: str
  content: str
  published: bool = True


class PostCreate(PostBase):
  pass


# response model
class Post(PostBase):
  id: int
  created_at: datetime
  owner_id: int
  owner: UserOut


class PostOut(BaseModel):
  Post: Post
  votes: int


class Token(BaseModel):
  access_token: str
  token_type: str


class TokenData(BaseModel):
  id: Optional[int] = None


class Vote(BaseModel):
  post_id: int
  dir: Annotated[int, conint(le=1, ge=0)]
