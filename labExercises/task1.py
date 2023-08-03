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
    roles= {1:"tutor",2:"estudiante de postdoctorado", 3:"estudiante de pregrado"}
    print(f"{'-'*60}BIENVENIDO{'-'*60}")
    print(f""" {' '*40}Este es el sistema de bases de datos de la Universidad de Antioquía \n
          {' '*40}Estas son las acciones que puede realizar \n
          {' '*40}1) Ingresar como tutor\n
          {' '*40}2) Ingresar como estudiante de Postdoctorado\n
          {' '*40}3) ingresar como estudiante de Pregrado \n
          {' '*40}4) Salir""")
    rol= int(input("Ingrese el número de su rol: \n"))
    if rol:
        print(f'Bienvenido, ha ingresado como {roles[rol]}')
        if rol==1:
            print("Por favor ingrese sesión")
            nombre=input("Nombre: ")
            edad=int(input("Edad: "))
            contact=input("Detalles de contacto: ")
            lecturerID=int(input("Ingrese su ID: "))
            lecturer= Lecturer(nombre,edad,contact,lecturerID)
            accion= int(input(""" Digite el número correspondiente a la acción que desea realizar\n
                              1) Actualizar modulos\n
                              2) Añadir estudiantes a su lista\n """))
            if accion==1:
                modulo=input("Ingrese el modulo que desea ingresar: ")
                lecturer.insertModule(modulo)
            elif accion==2:
                estudiante=input("Ingrese el estudiantes que desea agregar: ")
                lecturer.insertPos(estudiante)

        elif rol==2:
            print("Por favor ingrese sesión")
            nombre=input("Nombre: ")
            edad=int(input("Edad: "))
            contact=input("Detalles de contacto: ")
            studentID=int(input("Ingrese su ID: "))
            year=int(input("Ingrese el año de ingreso: "))
            tutor= input("Ingrese su tutor: ")
            postStudent: Postgraduate(nombre,edad,contact,studentID,year,tutor)
            accion= int(input(""" Digite el número correspondiente a la acción que desea realizar\n
                              1) Actualizar titulos que se han publicado\n
                              2) Ingresar laboratorios de investigación\n
                               """))
            if accion==1:
                modulo=input("Ingrese el titulo que desea ingresar: ")
                postStudent.insertPaper(modulo)
            elif accion==2:
                laboratorio=input("Ingrese el laboratorio de investigación que desea agregar: ")
                postStudent.insertLab(laboratorio)
        elif rol==3:
            print("Por favor ingrese sesión")
            nombre=input("Nombre: ")
            edad=int(input("Edad: "))
            contact=input("Detalles de contacto: ")
            studentID=int(input("Ingrese su ID: "))
            year=int(input("Ingrese el año de ingreso: "))
            tutor= input("Ingrese su tutor: ")
            undergraduateStudent: Undergraduate(nombre,edad,contact,studentID,year,tutor)
            accion= int(input(""" Digite el número correspondiente a la acción que desea realizar\n
                              1) Ingresar libros\n
                              2) Eliminar libros\n """))
            if accion==1:
                bookName=input("Ingrese el titulo del libro que desea ingresar: ")
                dueDate= input("Ingrese la fecha de vencimiento")
                undergraduateStudent.borrowBook(bookName,dueDate)
            elif accion==2:
                bookName=input("Ingrese el titulo del libro que desea devolver: ")
                undergraduateStudent.returnBook(bookName)
        elif rol==4:
            pass
    pass
