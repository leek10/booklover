import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        # Add a book and test if it is in 'book_list'
        book_lover = BookLover("Josh", "josh@example.com", "Fiction")
        book_lover.add_book("Lonesome Dove", 5)
        self.assertTrue(book_lover.has_read("Lonesome Dove"))
    
    def test_2_add_book(self):
        # Add the same book twice and test if it is in 'book_list' only once
        book_lover = BookLover("Josh", "josh@example.com", "Fiction")
        book_lover.add_book("Song of Achilles", 2)
        book_lover.add_book("Song of Achilles", 2)
        expected = 1
        self.assertEqual(book_lover.num_books_read(), expected)
    
    def test_3_has_read(self):
        # Pass a book in the list and test if the answer is 'True'
        book_lover = BookLover("Josh", "josh@example.com", "Fiction")
        book_lover.add_book("The Great Gatsby", 3)
        self.assertTrue(book_lover.has_read("The Great Gatsby"))
        
    def test_4_has_read(self):
        # Pass a book NOT in the list and use 'assert False' to test the answer is 'True'
        book_lover = BookLover("Josh", "josh@example.com", "Fiction")
        book_lover.add_book("The Hunger Games", 2)
        book_lover.add_book("Lord of the Flies", 4)
        self.assertFalse(book_lover.has_read("Heart of Darkness"))
    
    def test_5_num_books_read(self):
        # Add some books to the list and test num_books matches as expected
        book_lover = BookLover("Josh", "josh@example.com", "Fiction")
        book_lover.add_book("The Handmaid's Tale", 1)
        book_lover.add_book("Flowers for Algernon", 2)
        book_lover.add_book("The Road", 3)
        book_lover.add_book("To Kill a Mockingbird", 5)
        book_lover.add_book("One Flew Over the Cuckoo's Nest", 5)
        expected = 5
        self.assertEqual(book_lover.num_books_read(), expected)
        
    def test_6_fav_books(self):
        # Add some books with ratings ranging from 1-5 to the list (make sure some < 3 and some > 3)
        book_lover = BookLover("Josh", "josh@example.com", "Fiction")
        book_lover.add_book("Huckleberry Finn", 1)
        book_lover.add_book("Tuesdays with Morrie", 2)
        book_lover.add_book("Gone with the Wind", 4)
        book_lover.add_book("Little Women", 4)
        book_lover.add_book("Moby Dick", 5)
        self.assertTrue(all(book_lover.fav_books()["book_rating"] > 3))
        
if __name__ == '__main__':
    unittest.main(verbosity = 3)
    
    
 