# routers/students.py
from fastapi import APIRouter, HTTPException
from dependencies import SessionDep
from models import Student, Klass
from schemas.student import (
    StudentCreateSerializer, 
    StudentResponseSerializer,
    ClassSerializer
)

router = APIRouter()


@router.get("/students", response_model=list[StudentResponseSerializer])
def get_all_students(session: SessionDep):
    
    from sqlmodel import select
    
    statement = select(Student)
    students = session.exec(statement).all()
    
    response_list = []
    for student in students:
        klass = session.get(Klass, student.class_id)
        response_list.append(
            StudentResponseSerializer(
                id=student.id,
                name=student.name,
                grade=student.grade,
                class_info=ClassSerializer(
                    id=klass.id,
                    name=klass.name,
                    teacher_name=klass.teacher_name
                )
            )
        )
    
    return response_list


@router.post("/students", response_model=StudentResponseSerializer, status_code=201)
def create_student(student_data: StudentCreateSerializer, session: SessionDep):
    klass = session.get(Klass, student_data.class_id)
    if not klass:
        raise HTTPException(status_code=404, detail="Class not found")
    
    new_student = Student(
        name=student_data.name,
        age=student_data.age,
        grade=student_data.grade,
        class_id=student_data.class_id
    )
    
    session.add(new_student)
    session.commit()
    session.refresh(new_student)
    
    response = StudentResponseSerializer(
        id=new_student.id,
        name=new_student.name,
        grade=new_student.grade,
        class_info=ClassSerializer(
            id=klass.id,
            name=klass.name,
            teacher_name=klass.teacher_name
        )
    )
    
    return response


@router.get("/students/{student_id}", response_model=StudentResponseSerializer)
def get_student(student_id: int, session: SessionDep):
    
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    klass = session.get(Klass, student.class_id)
    
    response = StudentResponseSerializer(
        id=student.id,
        name=student.name,
        grade=student.grade,
        class_info=ClassSerializer(
            id=klass.id,
            name=klass.name,
            teacher_name=klass.teacher_name
        )
    )
    
    return response