class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks 
    def result(self):
        if self.marks >= 50:
            return "pass"
        else:
            return "fail"
