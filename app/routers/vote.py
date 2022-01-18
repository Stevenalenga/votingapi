from fastapi import FASTAPI, Response, status, HTTPException, Depends, APIRouter
from .. import schemas, database, models, Oauth2
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/vote",
    tags="Vote"
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def Vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)

    found_vote = vote_query.first()
    if(vote.voted == True):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user{current_user.id } has already voted on Post {vote.post_id}")

        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()

        return {"message": "user has successfully voted"}

    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="vote does not exist")

        vote_query.delete(synchronize_session=False)
        db.commit()

        return{"message":  "successfully deleted vote"}