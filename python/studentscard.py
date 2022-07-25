class Stud:
    @staticmethod
    def getInt(*msg):
        while(True):
            try:
                value = int(input(*msg))
                return value
            except:
                print('Incorrect input')

    @staticmethod
    def getFloat(*msg):
        while(True):
            try:
                value = float(input(*msg))
                return value
            except:
                print('Incorrect input')


class Student:
    def __init__(self, name, maths, physics, chemistry, english, programing) -> None:
        self.__name       = name
        self.__maths      = maths
        self.__physics    = physics
        self.__chemistry  = chemistry
        self.__english    = english
        self.__programing = programing

    @property
    def name(self):
        return self.__name

    @property
    def maths(self):
        return self.__maths

    @property
    def physics(self):
        return self.__physics

    @property
    def chemistry(self):
        return self.__chemistry

    @property
    def english(self):
        return self.__english

    @property
    def programing(self):
        return self.__programing

    @maths.setter
    def maths(self, newMark):
        self.__maths = newMark

    @maths.setter
    def physics(self, newMark):
        self.__physics = newMark

    @maths.setter
    def chemistry(self, newMark):
        self.__chemistry = newMark

    @maths.setter
    def english(self, newMark):
        self.__english = newMark

    @maths.setter
    def programming(self, newMark):
        self.__programming = newMark

    def display(self):
        print('Name :', self.__name)
        print('Marks:')
        print('Maths:', self.__maths)
        print('Physics:', self.__physics)
        print('Chemistry:', self.__chemistry)
        print('English:', self.__english)
        print('Programing:', self.__programing)


class Report:
    students = dict()

    @staticmethod
    def create():
        rollno = Stud.getInt('Rollno: ')
        if Report.students.get(rollno):
            print('Student already exist')
        else:
            name = input('Name: ')
            print('Enter marks')
            maths       = Stud.getFloat('Maths: ')
            physics     = Stud.getFloat('Physics: ')
            chemistry   = Stud.getFloat('Chemistry: ')
            english     = Stud.getFloat('English: ')
            programing  = Stud.getFloat('Programing: ')
            student  = Student(name, maths, physics, chemistry, english, programing)
            Report.students[rollno] = student
            print('Student added successfully')

    @staticmethod
    def delete():
        rollno = Stud.getInt('Rollno: ')
        if Report.students.get(rollno):
            del Report.students[rollno]
            print('Student deleted successfully')
        else:
            print('Student does not exist')

    @staticmethod
    def modify():
        rollno = Stud.getInt('Rollno: ')
        if Report.students.get(rollno):
            student = Report.students.get(rollno)
            student.display()
            while(True):
                opt = Stud.getInt(f'''
Choose Mark to edit:
    1. Maths
    2. Physics
    3. Chemistry
    4. English
    5. Programing
    6. Exit
    > '''
                )
                match opt:
                    case 1: student.maths = Stud.getFloat('Maths: ')
                    case 2: student.physics = Stud.getFloat('Physics: ')
                    case 3: student.chemistry = Stud.getFloat('Chemistry: ')
                    case 4: student.english = Stud.getFloat('English: ')
                    case 5: student.programing = Stud.getFloat('Programing: ')
                    case 6: break
                    case _: print('Invalid input')
        else:
            print('Student does not exist')

    @staticmethod
    def listAllStudents():
        if len(Report.students) > 0:
            print('Student details: ')
            for rollno, student in Report.students.items():
                print('\nRollno: ', rollno)
                student.display()
        else:
            print('No records')

    @staticmethod
    def showStudent():
        rollno = Stud.getInt('Rollno: ')
        if Report.students.get(rollno):
            print('\nRollno: ', rollno)
            Report.students[rollno].display()
        else:
            print('Student does not exist')


while(True):
    opt = Stud.getInt('''
    1. Create Student Record
    2. Delete Student Record
    3. Modify Marks
    4. Display all Students
    5. Display a student record
    6. Exit
    
    > ''')

    match opt:
        case 1: Report.create()
        case 2: Report.delete()
        case 3: Report.modify()
        case 4: Report.listAllStudents()
        case 5: Report.showStudent()
        case 6: break
        case _: print('Invalid input') 