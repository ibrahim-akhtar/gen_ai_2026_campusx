from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    # name: str = 'abc' # for default name
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=4, decription='A decimal values representing the cgpa of the student')

new_student = {'name' : 'nitish'}
# new_student = {'name' : 32}
# the above will throw error: Input should be a  valid string


# for default name
# new_student = {}


new_student = {'name' : 'nitish', 'age':'32', 'email':'abc@gmail.com', 'cgpa':5}
# '32' - valid
# pydantic type converts it implicitly


student = Student(**new_student)

print(student)
print(student.name)

student_dict = dict(student)
print(student_dict['name'])

student_json = student.model_dump_json()