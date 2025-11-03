from fastapi import APIRouter, HTTPException
from dependencies import SessionDep
from models import Parent
from schemas.parent import ParentSchema, ParentCreateSerializer

router = APIRouter(prefix="/parents")


@router.get("/", response_model=list[ParentSchema])
def get_all_parents(session: SessionDep):
    from sqlmodel import select
    
    statement = select(Parent)
    parents = session.exec(statement).all()
    
    return [
        ParentSchema(
            id=parent.id,
            name=parent.name,
            phone_number=parent.phone_number
        )
        for parent in parents
    ]


@router.post("/", response_model=ParentSchema, status_code=201)
def create_parent(parent_data: ParentCreateSerializer, session: SessionDep):
    new_parent = Parent(
        name=parent_data.name,
        phone_number=parent_data.phone_number
    )
    
    session.add(new_parent)
    session.commit()
    session.refresh(new_parent)
    
    return ParentSchema(
        id=new_parent.id,
        name=new_parent.name,
        phone_number=new_parent.phone_number
    )


@router.get("/{parent_id}", response_model=ParentSchema)
def get_parent(parent_id: int, session: SessionDep):
    parent = session.get(Parent, parent_id)
    if not parent:
        raise HTTPException(status_code=404, detail="Parent not found")
    
    return ParentSchema(
        id=parent.id,
        name=parent.name,
        phone_number=parent.phone_number
    )