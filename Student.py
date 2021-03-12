class Student:
    def __init__(self,name,sex,id,live,subject):
        self.StudentName = name
        self.StudentSex = sex
        self.StudentId = id
        self.StudentLive = live
        self.StudentSubject = subject
    def showInfo(self):
        print(self.StudentName,"\t",self.StudentSex,"\t",self.StudentId,"\t",self.StudentLive,"\t",self.StudentSubject,"\t")
       

x1=Student("Tim","Main","001","台中","Math")
x2=Student("Judy","Female","002","台北","English")
x3=Student("Andy","Main","003","高雄","Society")
x1.showInfo()
x2.showInfo()
x3.showInfo()