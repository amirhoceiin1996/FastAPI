from fastapi import APIRouter, HTTPException
from dependencies import SessionDep
from models import Student, Klass, Parent
from schemas.student import StudentCreateSchema, StudentResponseSchema
from schemas.klass import ClassSchema
from schemas.parent import ParentSchema

router = APIRouter(prefix="/students")


@router.get("/", response_model=list[StudentResponseSchema])
def get_all_students(session: SessionDep):
    from sqlmodel import select
    
    statement = select(Student)
    students = session.exec(statement).all()
    
    response_list = []
    for student in students:
        klass = session.get(Klass, student.class_id)
        parent = session.get(Parent, student.parent_id)
        
        response_list.append(
            StudentResponseSchema(
                id=student.id,
                name=student.name,
                grade=student.grade,
                is_active=student.is_active,
                created_at=student.created_at,
                class_info=ClassSchema(
                    id=klass.id,
                    name=klass.name,
                    teacher_name=klass.teacher_name
                ),
                parent=ParentSchema(
                    id=parent.id,
                    name=parent.name,
                    phone_number=parent.phone_number
                )
            )
        )
    
    return response_list


@router.post("/", response_model=StudentResponseSchema, status_code=201)
def create_student(student_data: StudentCreateSchema, session: SessionDep):
    klass = session.get(Klass, student_data.class_id)
    if not klass:
        raise HTTPException(
            status_code=404, 
            detail="Class or Parent not found"
        )
    
    parent = session.get(Parent, student_data.parent_id)
    if not parent:
        raise HTTPException(
            status_code=404, 
            detail="Class or Parent not found"
        )
    
    new_student = Student(
        name=student_data.name,
        age=student_data.age,
        grade=student_data.grade,
        class_id=student_data.class_id,
        parent_id=student_data.parent_id
    )
    
    session.add(new_student)
    session.commit()
    session.refresh(new_student)
    
    response = StudentResponseSchema(
        id=new_student.id,
        name=new_student.name,
        grade=new_student.grade,
        is_active=new_student.is_active,
        created_at=new_student.created_at,
        class_info=ClassSchema(
            id=klass.id,
            name=klass.name,
            teacher_name=klass.teacher_name
        ),
        parent=ParentSchema(
            id=parent.id,
            name=parent.name,
            phone_number=parent.phone_number
        )
    )
    
    return response


@router.get("/{student_id}", response_model=StudentResponseSchema)
def get_student(student_id: int, session: SessionDep):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    klass = session.get(Klass, student.class_id)
    parent = session.get(Parent, student.parent_id)
    
    response = StudentResponseSchema(
        id=student.id,
        name=student.name,
        grade=student.grade,
        is_active=student.is_active,
        created_at=student.created_at,
        class_info=ClassSchema(
            id=klass.id,
            name=klass.name,
            teacher_name=klass.teacher_name
        ),
        parent=ParentSchema(
            id=parent.id,
            name=parent.name,
            phone_number=parent.phone_number
        )
    )
    
    return response