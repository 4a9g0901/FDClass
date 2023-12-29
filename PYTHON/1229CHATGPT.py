class Book:
    def __init__(self, title, author, publishing, publication):
        # 書籍基本資訊
        self.title = title
        self.author = author
        self.publishing = publishing
        self.publication = publication

        # 借閱狀態
        self.is_lent = False
        self.lend_date = None
        self.return_date = None

        # 借閱者資訊
        self.borrower_name = None
        self.borrower_id = None
        self.borrower_email = None

class Library:
    def __init__(self):
        # 以書名為鍵值的字典，儲存圖書館中的書籍
        self.books = {}

    def add_book(self, title, author, publishing, publication):
        # 新增書籍到圖書館
        book = Book(title, author, publishing, publication)
        self.books[title] = book

    def lend_book(self, title, borrower_name, borrower_id, borrower_email, lend_date, return_date):
        # 借閱書籍
        if title in self.books and not self.books[title].is_lent:
            # 更新書籍狀態和借閱者資訊
            self.books[title].is_lent = True
            self.books[title].lend_date = lend_date
            self.books[title].return_date = return_date
            self.books[title].borrower_name = borrower_name
            self.books[title].borrower_id = borrower_id
            self.books[title].borrower_email = borrower_email
            print(f"{title} 已借出給 {borrower_name}")

    def return_book(self, title):
        # 歸還書籍
        if title in self.books and self.books[title].is_lent:
            # 更新書籍狀態和清空借閱者資訊
            self.books[title].is_lent = False
            self.books[title].lend_date = None
            self.books[title].return_date = None
            self.books[title].borrower_name = None
            self.books[title].borrower_id = None
            self.books[title].borrower_email = None
            print(f"{title} 已歸還")

    def display_books(self):
        # 顯示圖書館中所有書籍的狀態
        for title, book in self.books.items():
            status = "已借出" if book.is_lent else "可借閱"
            print(f"書名: {title}, 作者: {book.author}, 狀態: {status}")

# 使用範例
library = Library()
library.add_book("Python Basics", "John Smith", "ABC Publishing", "2020-01-01")
library.add_book("Data Science 101", "Jane Doe", "XYZ Publishing", "2019-05-15")

library.display_books()

library.lend_book("Python Basics", "Alice", "A12345", "alice@email.com", "2023-01-01", "2023-02-01")

library.display_books()

library.return_book("Python Basics")

library.display_books()
