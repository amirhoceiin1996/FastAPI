from fastapi import APIRouter, HTTPException
from dependencies import SessionDep
from models import Klass
from schemas.klass import ClassCreateSerializer, ClassResponseSerializer

router = APIRouter()


@router.get("/classes", response_model=list[ClassResponseSerializer])
def get_all_classes(session: SessionDep):
    
    from sqlmodel import select
    
    statement = select(Klass)
    classes = session.exec(statement).all()
    
    return [
        ClassResponseSerializer(
            id=klass.id,
            name=klass.name,
            teacher_name=klass.teacher_name
        )
        for klass in classes
    ]


@router.post("/classes", status_code=201)
def create_class(class_data: ClassCreateSerializer, session: SessionDep):
    
    new_class = Klass(
        name=class_data.name,
        teacher_name=class_data.teacher_name
    )
    
    session.add(new_class)
    session.commit()
    session.refresh(new_class)
    
    return {
        "status": "success",
        "data": {
            "id": new_class.id,
            "name": new_class.name,
            "teacher_name": new_class.teacher_name
        }
    }


@router.get("/classes/{class_id}", response_model=ClassResponseSerializer)
def get_class(class_id: int, session: SessionDep):
    
    klass = session.get(Klass, class_id)
    if not klass:
        raise HTTPException(status_code=404, detail="Class not found")
    
    return ClassResponseSerializer(
        id=klass.id,
        name=klass.name,
        teacher_name=klass.teacher_name
    )