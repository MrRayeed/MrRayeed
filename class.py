class student:
    grade=6
    name="stupid"

    def introduction(self):
        print("hi I am a student")


    def details(self):
        print("My name is",self.name)
        print("I am in grade",self.grade)


ob=student()
ob.introduction()
ob.details()