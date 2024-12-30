# Digital Book Library

#### Video Demo: [Watch Here](https://youtu.be/3Fm8iShxoAM)

#### Description:
The Digital Book Library is a Python project designed to help users manage their personal library of books. It allows users to add, delete, rate, and review books. The project utilizes a JSON file (`books.json`) to store book data.

The program provides the following features:
- **Add a Book**: Users can add a new book to the collection by providing the book's title, author, genre, rating, and a review.
- **View Books**: Users can view all the books currently in the collection, including their title, author, genre, rating, and review.
- **Rate and Review a Book**: Users can update the existing books in the collection with new ratings and reviews.
- **Delete a Book**: Users can delete any book from the collection by providing the book's title.

# Key Features:
- **Storage**: All data is stored in a JSON file, ensuring that books are not lost when the program is restarted.
- **User-Friendly Interface**: The program offers a clear and simple text-based menu to interact with the library system.
- **Input Validation**: User inputs are handled carefully, preventing errors.

# File Breakdown:
- **`project.py`**: Contains the main program logic, which handles all user interactions, data processing, and file manipulation.
  - Functions:
    - `load_books()`: Loads the list of books from the JSON file.
    - `save_books()`: Saves the current list of books back to the JSON file.
    - `add_book()`: Adds a new book to the collection by creating a directory and appending it to the list.
    - `delete_book()`: Searches and deletes a book from the collection.
    - `view_books()`: Displays all the books in the collection.
    - `rate_review_book()`: Updates the rating and review of an existing book.
    - `main()`: Handles user input and calls the corresponding functions.
- **`books.json`**: This file is used for storing the collection of books in JSON format.

# Design Decisions:
The main aim of designing this project was to ensure simplicity, while maintaining functionality.  I opted for a JSON file for storage, based on its simplicity and ability to be easily loaded and saved. The choice of a text-based menu interface allows for easy navigation, making the system easy to use. The loop for the main interface provides a consistent experience for users who wish to repeatedly perform actions until they choose to exit. I hope all users find this application fun and useful.
