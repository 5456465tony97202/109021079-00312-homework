class Book:
    def __init__(self,name,edition,id,sort,language):
        self.BookName = name
        self.BookEdition = edition
        self.BookId = id
        self.BookSort = sort
        self.BookLanguage = language
    def showInfo(self):
        print(self.BookName,"\t",self.BookEdition,"\t",self.BookId,"\t",self.BookSort,"\t",self.BookLanguage,"\t")
       

x1=Book("Linear Algebra","第9版","001","教科書","英文")
x2=Book("健康與生活","初版","002","教科書","中文")
x3=Book("Frankenstein","第5版","003","原文小說","英文")
x1.showInfo()
x2.showInfo()
x3.showInfo()