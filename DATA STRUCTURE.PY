def main():
    # Task 1: List of integers and sum
    print("\n--- Task 1: List of Integers and Sum ---")
    numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
    print("List of numbers:", numbers)
    print("Sum of numbers:", sum(numbers))
    
    # Task 2: Favorite books tuple
    print("\n--- Task 2: Favorite Books ---")
    favorite_books = ("To Kill a Mockingbird", "1984", "The Great Gatsby", 
                      "Pride and Prejudice", "The Hobbit")
    print("My favorite books:")
    for book in favorite_books:
        print(book)
    
    # Task 3: Person dictionary
    print("\n--- Task 3: Person Information ---")
    person = {
        'name': input("Enter your name: "),
        'age': int(input("Enter your age: ")),
        'favorite_color': input("Enter your favorite color: ")
    }
    print("Person information:", person)
    
    # Task 4: Common set elements
    print("\n--- Task 4: Common Set Elements ---")
    set1 = set(map(int, input("Enter integers for first set (separated by spaces): ").split()))
    set2 = set(map(int, input("Enter integers for second set (separated by spaces): ").split()))
    common_elements = set1.intersection(set2)
    print("Common elements:", common_elements)
    
    # Task 5: Odd-length words
    print("\n--- Task 5: Odd-Length Words ---")
    words = input("Enter words separated by spaces: ").split()
    odd_length_words = [word for word in words if len(word) % 2 != 0]
    print("Words with odd number of characters:", odd_length_words)

if __name__ == "__main__":
    main()