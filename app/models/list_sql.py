from controllers.lists_schema import ListCreate
from .list_model import ListModel
from sqlalchemy.orm import Session


def create_list(db: Session, lists: ListCreate):
    db_user = ListModel(name=lists.name, description=lists.description, items=lists.items)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


def get_lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ListModel).offset(skip).limit(limit).all()


def get_list(list_id: int, db: Session):
    return db.query(ListModel).filter(ListModel.id == list_id).first()


def delete_list(list_id: int, db: Session):
   deleted = db.query(ListModel).filter(ListModel.id == list_id).delete()
   db.commit()
   return deleted


def update_list(list_id: int, db: Session, lists: ListCreate):
    new_list = ListModel(name=lists.name, description=lists.description, items=lists.items)
    
    updated = db.query(ListModel).filter(ListModel.id == list_id).update({
        "name": new_list.name, 
        "description": new_list.description,
        "items": new_list.items},
        synchronize_session="evaluate"
    )
    
    if updated:
        db.commit()
    
    return updated, new_list


def patch_list(list_id: int, db: Session, piece_list: dict):

    patched = False

    if piece_list.get("name") and type(piece_list.get("name")) == str:
        patched = db.query(ListModel).filter(ListModel.id == list_id).update({
            "name": piece_list.get("name")},
            synchronize_session="evaluate"
        )

    elif piece_list.get("description") and type(piece_list.get("description")) == str:
        patched = db.query(ListModel).filter(ListModel.id == list_id).update({
            "description": piece_list.get("description")},
            synchronize_session="evaluate"
        )

    elif piece_list.get("items") and type(piece_list.get("items")) == dict:
        patched = db.query(ListModel).filter(ListModel.id == list_id).update({
            "items": piece_list.get("items")},
            synchronize_session="evaluate"
        )

    if patched:
        db.commit()

    return patched, piece_list
