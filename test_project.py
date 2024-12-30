from project import add_book, view_books, rate_review_book, delete_book

def test_add_book():
    assert add_book("The Night Circus", "Erin Morgenstern", "Fantasy", 5, "Amazing book!")=="The Night Circus by Erin Morgenstern added to the collection!\n"


def test_delete_book1():
    add_book("To Kill a Mockingbird", "Harper Lee", "Fiction", 5, "A timeless classic!")
    result = delete_book("To Kill a Mockingbird")
    assert result == "To Kill a Mockingbird has been deleted from the collection!\n"


def test_delete_book2():
    delete = delete_book("Pride and Prejudice")
    assert delete == "Pride and Prejudice is not found in the collection!\n"


def test_view_books():
    add_book("The Da Vinci Code", "Dan Brown", "Thriller", 4, "A masterpiece!")
    result = view_books()
    assert "The Da Vinci Code" in result


def test_rate_review_book():
    add_book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 2, "Boring!")
    assert rate_review_book("The Hobbit", 3, "Not boring")=="The Hobbit has been rated and reviewed!\n"

