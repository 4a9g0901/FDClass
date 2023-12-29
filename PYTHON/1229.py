class Library :
    def __init__ (self, Title, ID, Author, Publishing, Publication, Lend, LendDate, ReturnDate, location, Name, NameID, Email):
        self.Title = Title
        self._ID = ID
        self.Author = Author
        self.Publishing = Publishing
        self.Publication = Publication
        self.Lend = Lend
        self.LendDate = LendDate
        self.ReturnDate = ReturnDate
        self.location = location
        self.Name = Name
        self.NameID = NameID
        self.Email = Email

    def Total(self):
        print("印出所有書本 :")
        return self.Title


library = Library( 'C_Language' , '1A5BBC', 'Charlie Li' ,'2014.11.12','2014.11.12', 'Nano','Nano', 'Nano', 'A5-5', '李勇材','4a9g0901','4a9g0901@stust.edu.tw')
library2 = Library( 'GGG_Language' , '1AG5BBC', 'GGCharlie Li' ,'GG2014.11.12','GG2014.11.12', 'Nano','Nano', 'Nano', 'A5-5', '李勇材','4a9g0901','4a9g0901@stust.edu.tw')


print(library._ID)

print(library.Total())












