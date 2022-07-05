
class Member:
  
  ## PARENT CLASS
  def __init__(self,id, name, username, phone_number, dob):   ## to initialise data members
    self.id=id
    self.name=name
    self.username=username
    self.phone_number=phone_number
    self.dob=dob
  def update_info_by_id(self,id, name, username, phone_number, dob):  ## updating values
    self.id=id
    self.name=name
    self.username=username
    self.phone_number=phone_number
    self.dob=dob
  def display_info_by_id (self,id):
    print("Unique id : ",self.id)
    print("Name : ",self.name)
    print("Username : ",self.username)
  def contact_details(self):
    print("Phone Number :  ",self.phone_number) 
  def display_age(self):
    age=2022-int(self.dob[-4:])
    print("Age  :  ",age)
    return age

class Professor(Member):  ## CHILD CLASS FOR PROFESSOR

  attendance=0
  field=""
  def __init__(self,id, name, username, phone_number, dob):
    super().__init__(id, name, username, phone_number, dob)
  def travel_ticket_discount(self,ticket_price,age):
    if age<=12:
      print("No money. Ticket price: ",0)
    if age>=13 and age<=25:
      print("Half fare. Ticket price: ",ticket_price/2)

    if age>=26:
      print("Full Money: Ticket price: ",ticket_price)

  def attendance_is_ok(self):
    if self.attendance>=90:
      print("Attendance : okay")
    else: 
      print("Attendance : not okay")
 
class Student(Member):  ## CHILD CLASS FOR STUDENT

  attendance=0
  branch=""
  def __init__(self,id, name, username, phone_number, dob):
    super().__init__(id, name, username, phone_number, dob)
  def travel_ticket_discount(self,ticket_price,age):
    if age<=12:
      print("No money. Ticket price: ",0)
    if age>=13 and age<=25:
      print("Half fare. Ticket price: ",ticket_price/2)

    if age>=26:
      print("Full Money: Ticket price: ",ticket_price)

  def attendance_is_ok(self):
    if self.attendance>=75:
      
      print("Attendance : okay")
    else: 
      print("Attendance :   not okay")

class Main():
  def main():
    print("STUDENT DETAILS ::::::::::")
    obj_stud=Student(0,None,None,None,None)
    obj_stud.branch="Mechanical"
    obj_stud.attendance=85
    Id=id(obj_stud)   ## creat a unique id fro this object
    obj_stud.update_info_by_id(Id,"Ayush Gautam","ayushg20","987654321","25/09/2001")
    obj_stud.display_info_by_id(200243)
    obj_stud.contact_details()
    obj_stud.attendance_is_ok()
    age=obj_stud.display_age()
    obj_stud.travel_ticket_discount(1000,age)
    print("\n")
    print("PROFESSOR DETAILS ::::::::")
    
    obj_prof=Professor(0,None,None,None,None)
    obj_prof.field="Research"
    obj_prof.attendance=90
    Id=id(obj_prof)    ## create a unique id for this object
    obj_prof.update_info_by_id(Id,"SK Singh","sksingh","123456789","12/07/1983")
    obj_prof.display_info_by_id(1234)
    obj_prof.contact_details()
    obj_prof.attendance_is_ok()
    age=obj_prof.display_age()
    obj_prof.travel_ticket_discount(1000,age)
  if __name__=="__main__":
    main()  
