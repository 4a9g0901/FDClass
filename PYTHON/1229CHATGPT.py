class Library:
    def __init__(self, Title, ID, Author, Publishing, Publication, Lend, LendDate, ReturnDate, location, Name, NameID, Email):
        self.books = []  # 使用列表來存儲多本書的實例
        self.add_book(Title, ID, Author, Publishing, Publication, Lend, LendDate, ReturnDate, location, Name, NameID, Email)

    def add_book(self, Title, ID, Author, Publishing, Publication, Lend, LendDate, ReturnDate, location, Name, NameID, Email):
        # 新增書籍到列表中
        book = {
            'Title': Title,
            'ID': ID,
            'Author': Author,
            'Publishing': Publishing,
            'Publication': Publication,
            'Lend': Lend,
            'LendDate': LendDate,
            'ReturnDate': ReturnDate,
            'location': location,
            'Name': Name,
            'NameID': NameID,
            'Email': Email
        }
        self.books.append(book)

    def Total(self):
        print("印出所有書本 :")
        for book in self.books:
            print(book['Title'])
        return [book['Title'] for book in self.books]

# 建立 Library 實例
library = Library('C_Language', '1A5BBC', 'Charlie Li', '2014.11.12', '2014.11.12', 'Nano', 'Nano', 'Nano', 'A5-5', '李勇材', '4a9g0901', '4a9g0901@stust.edu.tw')
library2 = Library('GGG_Language', '1AG5BBC', 'GGCharlie Li', 'GG2014.11.12', 'GG2014.11.12', 'Nano', 'Nano', 'Nano', 'A5-5', '李勇材', '4a9g0901', '4a9g0901@stust.edu.tw')

# 使用 Total 方法印出所有書本的訊息
print(library.Total())
