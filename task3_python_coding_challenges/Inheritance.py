class Human:
    def __init__(self, FirstName, LastName, University):
        self.FirstName = FirstName
        self.LastName = LastName
        self.University = University


class Student(Human):
    def __init__(self, FirstName, LastName, University, Skype):
        super().__init__(FirstName, LastName, University)
        self.Skype = Skype

class Researcher(Human):
    def __init__(self, FirstName, LastName, University, Courses):
        super().__init__(FirstName, LastName, University)
        self.Courses = Courses


FirstPerson = Student("Frida","Jacobsson","MAH","frida96")
SecondPerson = Researcher("Aleksander","Fabijan","MAH",["DA712","DA374"])

print(FirstPerson.FirstName)