"""52100819_P2

"""
from typing import Dict
from typing import List, Union

# Question 1
def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2

def add_numbers_extended(num1: float, num2: float) -> float:
    return num1 + num2

# Example usage:
result_int = add_numbers(5, 3)
result_float = add_numbers_extended(2.5, 1.3)

print("Sum of integers:", result_int)
print("Sum of floats:", result_float)


# Question 2
def filter_even_numbers(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num % 2 == 0]

def filter_even_integers(numbers: List[Union[int, float]]) -> List[int]:
    return [int(num) for num in numbers if isinstance(num, (int, float)) and int(num) % 2 == 0]

# Example usage:
integers_list = [1, 2, 3, 4, 5, 6]
filtered_even_integers = filter_even_numbers(integers_list)
print("Filtered even integers:", filtered_even_integers)

mixed_list = [1.5, 2, 3.5, 4, 5, 6.5]
filtered_even_integers_from_mixed = filter_even_integers(mixed_list)
print("Filtered even integers from mixed list:", filtered_even_integers_from_mixed)

# Question 3
class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        """
        Initialize a Book object with a title, author, and number of pages.

        Parameters:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - pages (int): The number of pages in the book.
        """
        self.title = title
        self.author = author
        self.pages = pages

    def get_book_info(self) -> str:
        """
        Get a formatted string containing the title and author of the book.

        Returns:
        - str: A formatted string with book information.
        """
        return f"Title: {self.title}, Author: {self.author}"

    def is_long(self) -> bool:
        """
        Check if the book has more than 300 pages.

        Returns:
        - bool: True if the book has more than 300 pages, False otherwise.
        """
        return self.pages > 300

# Example usage:
book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", pages=180)
book2 = Book(title="War and Peace", author="Leo Tolstoy", pages=1200)

print(book1.get_book_info())
print(f"Is book1 long? {book1.is_long()}")

print(book2.get_book_info())
print(f"Is book2 long? {book2.is_long()}")


# Question 4
def count_word_occurrences(input_string: str) -> Dict[str, int]:
    word_occurrences = {}
    words = input_string.split()

    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitivity
        word = word.strip('.,?!')  # Remove punctuation

        if word:
            word_occurrences[word] = word_occurrences.get(word, 0) + 1

    return word_occurrences

# Example usage:
text = "This is a simple example. This example is meant to be simple."

word_counts = count_word_occurrences(text)
print(word_counts)