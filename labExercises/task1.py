class Person:
    def __init__(self,name,age,contact_details):
        self.name = name
        self.age = age
        self.contact_details = contact_details

class Student(Person):
    def __init__(self, name, age, contact_details,studentID,year):
        super().__init__(name, age, contact_details)
        self.studentID = studentID
        self.year = year
        self.enrolledModules=[]

    def insertModules(self, modules):
        self.enrolledModules.append(modules)

class Lecturer(Person):
    def __init__(self,name,age,contact_details, officeID):
        super().__init__(name,age,contact_details)
        self.officeID=officeID
        self.moduleTeach=[]
        self.postList=[]

    def insertPos(self,student):
        if isinstance(student,Postgraduate):
            self.postList.append(student)
        else:
            print("The lecturer only be able to add Postgraduate students")

    def insertModule(self,module):
        self.moduleTeach.append(module)

class Postgraduate(Student):
    def __init__(self, name, age, contact_details, studentID, year,lecturer):
        super().__init__(name, age, contact_details, studentID, year)
        self.lecturer=lecturer
        self.ResearchLab=[]
        self.papers =[]
    def insertLab(self,lab):
        self.ResearchLab.append(lab)
    def insertPaper(self,paper):
        self.papers.append(paper)

class Undergraduate(Student):
    def __init__(self, name, age, contact_details, studentID, year,title,lecturer):
        super().__init__(name, age, contact_details, studentID, year)
        self.title=title
        self.lecturer=lecturer
        self.books={}

    def borrowBook(self, bookName,dueDate):
        self.books[bookName]=dueDate

    def returnBook(self,bookName):
        if bookName in self.books:
            del self.books[bookName]

if __name__=="__main__":
    pass
    