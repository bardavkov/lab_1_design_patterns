from datetime import datetime
from typing import List, Any


class Course:

  def __init__(self,title:str,start_date:datetime,end_date:datetime,description:str,lectures:list[str],assignments:list[str],limit:int,students_num:int):
    self.title=title
    self.start_date=start_date
    self.limit = limit
    self.end_date=end_date
    self.description=description
    self.lectures=lectures
    self.assignments=assignments
    self.students = []
    
  
  def add_student(self, student: Any):
    if self.limit > len(self.students):
      student.enroll(self)
      self.students.append(student)
      print(f'Student {student.name} as been added to the course {self.title}')
    else:
      print('Too many students')

  def delete_student(self, student):
    student.unenroll(self.title)
    self.students.remove(student)
    
   


class Student:
  """docs"""
  def __init__(self, name:str,
               address:str,
               phone_number:str,
               email:str,
               student_number:int) -> None:
    self.name = name
    self.address = address
    self.phone_number = phone_number
    self.email = email
    self.student_number = student_number
    self.average_mark = 0.0
    self.courses: List[Course] = []
    self.course_progress = []

  def taken_courses(self) -> List[Course]:
    return self.courses

  def enroll(self, course: Course) -> None:
    self.courses.append(course)

  def unenroll(self, course_title):
    """"""
    self.courses = list(filter(lambda x: x.title == course_title, self.courses))
    print(f'Student {self.name} unenrolled from {course.title}')

  

class CourseProgres:
  """Implement docstring!!!!"""
  def __init__(self, received_marks: dict,
               visited_lectures: int,
               notes:dict[str]):
    self.received_marks = received_marks
    self.visited_lectures = visited_lectures
    self.assignments = {}
    self.notes = notes

    
  def get_final_mark(self)->float:
    
    final_mark=sum(self.received_marks.values())/len(self.received_marks)
    return final_mark

  def get_progress_to_date(self, date: datetime):
    marks = [value["mark"] for key, value in self.assignments if date >= key]
    return sum(marks) / len(marks)


  
class Lector:
  def __init__(self,name:str,address:str,phone_number:str,email:str, salary: float, course: Course):
    self.name=name
    self.address=address
    self.phone_number=phone_number
    self.email=email
    self.salary=salary
    self.course = course

  def check_assignment(assignment: dict) -> None:
    if assignment["is_done"]:
      assignment["mark"] = 5.0


assignment_1 = {"title": "testing", "description" : "testing", "is_done": False, "mark": 0.0}
assignment_2 = {"title": "testing", "description" : "testing", "is_done": False, "mark": 0.0}


student_1=Student('Illia','lviv','099023','1234@gmail.com',1234)
course_1=Course('lol',(1,9,2022),(1,12,2022),'nothing',['math','english','programming'],['create proffesionals','develop games','play football'],11,10)
student_progress_1=CourseProgres({"english":100,"math":88,"programming":90},3,{'math':True,'english':False,'programming':True})




print(student_progress_1.get_final_mark())
