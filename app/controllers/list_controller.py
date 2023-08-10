from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from config.init_db import SessionLocal, Base, engine
from .lists_schema import List, ListCreate
from models.list_sql import create_list, get_lists, get_list, delete_list, update_list, patch_list


Base.metadata.create_all(bind=engine)
#remover ações de banco do controller
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/lists",
                   tags=["lists"],
                   responses={404: {"Description": "List Not Found"}, 201 : {"Description": "Successfully created"}},
        )


@router.get("/")
def get_all_lists(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    all_lists = get_lists(db=db, skip=skip, limit=limit)

    return all_lists


@router.get("/{list_id}")
def get(list_id: int, db: Session = Depends(get_db)):
    get_list_by_id = get_list(db=db, list_id=list_id)
    
    if get_list_by_id:    
        return get_list_by_id
    
    raise HTTPException(status_code=404, detail="List Not Found")
    

@router.post("/", response_model=List, status_code=201)
def create(user_list: ListCreate, db: Session = Depends(get_db)):
    try:
        db_user = create_list(lists=user_list, db=db)
        return db_user

    except Exception as e:
        return e


@router.delete("/{list_id}", status_code=204)
def delete(list_id: int, response: Response, db: Session = Depends(get_db)):
    deleted = delete_list(list_id=list_id, db=db)
    
    if deleted:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    
    raise HTTPException(status_code=404, detail="List Not Found")

@router.put("/{list_id}")
def update(list_id: int, response: Response, new_list: ListCreate, db: Session = Depends(get_db)):
    updated, new_list = update_list(list_id=list_id, db=db, lists=new_list)
    
    if updated:
        response.status_code = status.HTTP_200_OK
        return response.status_code, new_list
    
    raise HTTPException(status_code=404, detail="List Not Found")


@router.patch("/{list_id}")
def patch(list_id: int, response: Response, patch_item: dict, db: Session = Depends(get_db)):
    patched, patched_item = patch_list(list_id=list_id, db=db, piece_list=patch_item)

    if patched:
        response.status_code = status.HTTP_200_OK
        return response.status_code, patched_item

    raise HTTPException(status_code=404, detail="List Not Found")
