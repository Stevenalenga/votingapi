from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(
    prefix="/user",
    tags=['User']
)

# /users/
# /users


@router.get("/")
def user():
    return {"hello user"}


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def Create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hash password = userpassword
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_User(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} was not found")

        response.status_code = status.HTTP_404_NOT_FOUND

        return {"message": f"post with {id} was not found"}
    return user
