# 1. List of integers and sum

def sum_of_integers():
    nums = input("Enter integers separated by spaces: ").split()
    int_list = [int(n) for n in nums]
    print(f"List: {int_list}")
    print(f"Sum: {sum(int_list)}")

# 2. Tuple of favorite books and print each

def print_favorite_books():
    books = ("1984", "To Kill a Mockingbird", "The Hobbit", "Pride and Prejudice", "The Great Gatsby")
    print("Favorite Books:")
    for book in books:
        print(book)

# 3. Dictionary for person info

def person_info():
    person = {}
    person['name'] = input("Enter your name: ")
    person['age'] = input("Enter your age: ")
    person['favorite_color'] = input("Enter your favorite color: ")
    print("Person Info:", person)

# 4. Sets and intersection

def sets_intersection():
    set1 = set(map(int, input("Enter integers for set 1 (space separated): ").split()))
    set2 = set(map(int, input("Enter integers for set 2 (space separated): ").split()))
    common = set1 & set2
    print(f"Common elements: {common}")

# 5. List comprehension for odd-length words

def odd_length_words():
    words = ["apple", "banana", "pear", "grape", "kiwi", "orange"]
    odd_words = [word for word in words if len(word) % 2 == 1]
    print(f"Words with odd number of characters: {odd_words}")

# 6. List operations demonstration
def list_operations():
    my_list = []
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    my_list.insert(1, 15)  # Insert 15 at second position (index 1)
    my_list.extend([50, 60, 70])
    my_list.pop()  # Remove last element
    my_list.sort()
    index_30 = my_list.index(30)
    print(f"Final list: {my_list}")
    print(f"Index of 30: {index_30}")

if __name__ == "__main__":
    print("Task 1: List and Sum")
    sum_of_integers()
    print("\nTask 2: Favorite Books")
    print_favorite_books()
    print("\nTask 3: Person Info")
    person_info()
    print("\nTask 4: Sets Intersection")
    sets_intersection()
    print("\nTask 5: Odd Length Words")
    odd_length_words()
    print("\nTask 6: List Operations")
    list_operations()
