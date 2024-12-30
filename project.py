import json

def load_books():
    try:
        with open("books.json", "r") as file:
            books=json.load(file)
    except FileNotFoundError:
        books=[]
    return books


def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file, indent=2)


def add_book(name, author, genre, rating, review):
    books=load_books()
    book={
        "Title": name,
        "Author": author,
        "Genre": genre,
        "Rating": rating,
        "Review": review
    }
    books.append(book)
    save_books(books)
    return f"{name} by {author} added to the collection!\n"


def delete_book(name):
    books=load_books()
    for book in books:
        if book["Title"].lower()==name.lower():
            books.remove(book)
            save_books(books)
            return f"{name} has been deleted from the collection!\n"
    return f"{name} is not found in the collection!\n"


def view_books():
    books=load_books()
    if not books:
        return "\nNo books in the collection!\n"
    result=""
    print("\nDisplaying all the books in the collection!\n")
    for book in books:
        result+=(
            f"Title: {book['Title']}\n"
            f"Author: {book['Author']}\n"
            f"Genre: {book['Genre']}\n"
            f"Rating: {book['Rating']}\n"
            f"Review: {book['Review']}\n\n"
        )
    return result


def rate_review_book(name, rating, review):
    books=load_books()
    for book in books:
        if book["Title"].lower()==name.lower():
            book["Rating"]=rating
            book["Review"]=review
            save_books(books)
            return f"{name} has been rated and reviewed!\n"

    return f"{name} is not found in the collection!\n"


def main():
    while True:
        print("**THE DIGITAL BOOK LIBRARY**")
        print("1. Add a book")
        print("2. View all books")
        print("3. Rate and review a book")
        print("4. Delete a book")
        print("5. Exit program")

        choice=input("Enter your choice: ").strip()

        match choice:
            case "1":
                name=input("Enter the name of the book: ").strip()
                author=input("Enter the author of the book: ").strip()
                genre=input("Enter the genre of the book: ").strip()
                rating=float(input("Enter your rating of the book (1-5): "))
                review=input("Enter your review of the book: ").strip()
                print(add_book(name, author, genre, rating, review))

            case "2":
                print(view_books())

            case "3":
                name=input("Enter the name of the book you want to rate and review: ").strip()
                rating=float(input("Enter your rating of the book (1-5): "))
                review=input("Enter your review of the book: ").strip()
                print(rate_review_book(name, rating, review))

            case "4":
                name=input("Enter the book you want to delete from the collection: ").strip()
                print(delete_book(name))

            case "5":
                print("Exiting the The Digital Book Library")
                break

            case _:
                print("Invalid option. Please try again!")


if __name__ == "__main__":
    main()
