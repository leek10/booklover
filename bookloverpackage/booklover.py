import pandas as pd

class BookLover:
    
    def __init__(self, name: str, email: str, fav_genre: str):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({"book_name": [], "book_rating": []})
        
    def add_book(self, book_name, book_rating):
        if self.book_list[self.book_list["book_name"] == book_name].empty:
            new_book = pd.DataFrame({"book_name": [book_name], "book_rating": [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
            self.num_books += 1
        else:
            print(f'The book "{book_name}" is already in the list!')
        
    def has_read(self, book_name):
        for name in self.book_list["book_name"]:
            if name == book_name:
                return True
        return False
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list["book_rating"] > 3]
    

     