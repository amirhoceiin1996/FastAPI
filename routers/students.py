from models.students import Student
from dependencies import SessionDep
from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from datetime import datetime
from schemas.students import UserOut, UserIn, Status_check

router = APIRouter()


@router.get('/students', response_model=list[UserOut])
def read_all_users(session: SessionDep) -> list[Student]:
    students = session.exec(select(Student)).all()
    return students 

@router.get("/students/{id}", response_model=UserOut)
def read_user(id: int, session:SessionDep) -> UserOut:
    id = session.get(Student, id)
    if not id:
        raise HTTPException(status_code=404, detail="User Not Found!")
    return id
 


@router.post("/students", response_model=Status_check, status_code=status.HTTP_201_CREATED)
def create_student(std: UserIn, session: SessionDep):
    existing = session.exec(select(Student).where(Student.name == std.name)).first()
    if existing:
        raise HTTPException(status_code=409, detail="Student with this name already exists!")

    student = Student(**std.model_dump())

    session.add(student)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to create student: {str(e)}")

    session.refresh(student)

    return Status_check(
        status="success",
        message="Student created successfully.",
        data=UserOut.model_validate(student)
    )


@router.delete("/students/{id}")
def delete_user(id: int, session:SessionDep):
    id = session.get(Student, id)
    if not id:
        raise HTTPException(status_code=404, detail="User not found!")
    session.delete(id)
    session.commit()
    return {"OK": True}
