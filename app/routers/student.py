# app/routers/student.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.student import Student
from app.schemas.student import CreateStudent, UpdateStudent

router = APIRouter()

@router.post("/create-student", response_model=CreateStudent)
async def create_student(student: CreateStudent, db: Session = Depends(get_db)):
    new_student = Student(name=student.name, matriculation_number=student.matriculation_number)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return student

@router.get("/get-student", response_model=CreateStudent)
async def get_student(
    student_id: int = None,
    name: str = None,
    matriculation_number: str = None,
    db: Session = Depends(get_db),):
    if student_id:
        db_item = db.query(Student).filter(Student.id == student_id).first()
    elif name:
        db_item = db.query(Student).filter(Student.name == name).first()
    elif matriculation_number:
        db_item = db.query(Student).filter(Student.matriculation_number == matriculation_number).first()
    else:
        raise HTTPException(status_code=400, detail="Please provide a valid search parameter.")

    if db_item is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return CreateStudent(name=db_item.name, matriculation_number=db_item.matriculation_number)

@router.get("/get-students")
async def get_students(db:Session = Depends(get_db)):
    return db.query(Student).all()

@router.put("/update-student/{student_id}", response_model=CreateStudent)
async def update_student(student_id: int, student: UpdateStudent, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    if student.name:
        db_student.name = student.name
    if student.matriculation_number:
        db_student.matriculation_number = student.matriculation_number

    db.commit()
    db.refresh(db_student)
    return db_student

@router.delete("/delete-student/{student_id}")
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(db_student)
    db.commit()
    return {"detail": f"Student with id {student_id} deleted successfully"}
