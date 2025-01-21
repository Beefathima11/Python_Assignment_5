# def calculate(value1, value2=10, value3=None):
#     """
#     Function to either sum or multiply based on the third argument.
#
#     Parameters:
#         value1 (int/float): The first required argument.
#         value2 (int/float, optional): The second argument, defaults to 10.
#         value3 (int/float, optional): The third argument, defaults to None.
#
#     Returns:
#         None
#     """
#     if value3 is None:
#         print("Sum:", value1 + value2)
#     else:
#         print("Product:", value1 * value2 * value3)
#
# # Example usage:
# calculate(5)
# calculate(6, 20)
# calculate(5, 20, 6)

# def filter_long_strings(strings):
#     """
#     Filters strings with a length greater than or equal to 5.
#
#     Parameters:
#         strings (list): A list of strings.
#
#     Returns:
#         list: A new list containing strings with a length >= 5.
#     """
#     return [string for string in strings if len(string) >= 5]
#
# # Example usage:
# example_list = ["apple", "cat", "banana", "dog", "elephant"]
# result = filter_long_strings(example_list)
# print(result)
#
# def evaluate_expression(expression):
#     """
#     Evaluates a given mathematical expression.
#
#     Parameters:
#         expression (str): A mathematical expression as a string.
#
#     Returns:
#         float/int: The result of evaluating the expression.
#     """
#     try:
#         result = eval(expression)
#         return result
#     except Exception as e:
#         return f"Error: {e}"
#
# # Example usage:
# expression = "9 * 67 + 8"
# # result = evaluate_expression(expression)
# # print(f"The result of the expression '{expression}' is: {result}")
# def is_prime(number):
#     """
#     Checks if a number is a prime number.
#
#     Parameters:
#         number (int): The number to check.
#
#     Returns:
#         bool: True if the number is prime, False otherwise.
#     """
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# def filter_primes(numbers):
#     """
#     Filters the prime numbers from a given list using the filter function.
#
#     Parameters:
#         numbers (list): A list of integers.
#
#     Returns:
#         list: A list of prime numbers.
#     """
#     return list(filter(is_prime, numbers))
#
# # Example usage:
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17]
# prime_numbers = filter_primes(numbers)
# print(f"Prime numbers: {prime_numbers}")
#
# def convert_to_uppercase(strings):
#     """
#     Converts a list of strings to uppercase using the map() function.
#
#     Parameters:
#         strings (list): A list of strings.
#
#     Returns:
#         list: A new list with all strings converted to uppercase.
#     """
#     return list(map(str.upper, strings))
#
# # Example usage:
# strings = ["apple", "banana", "cherry", "date"]
# uppercase_strings = convert_to_uppercase(strings)
# print(uppercase_strings)

# Function to count the total number of words in a file
def count_words(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            content = file.read()
            # Split the content into words
            words = content.split()
            # Count the total number of words
            word_count = len(words)
            print(f"The total number of words in {file_path} is: {word_count}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File path (replace with your file name)
file_path = 'assignment_5.py'

# Count the words in the file
count_words(file_path)

# Function to convert a string to an integer
# def string_to_integer():
#     try:
#         # Prompt user for input
#         user_input = input("Enter a string to convert to an integer: ")
#         # Attempt to convert the input to an integer
#         number = int(user_input)
#         print(f"The converted integer is: {number}")
#     except ValueError:
#         print("Error: The input is not a valid integer.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#
# # Call the function
# string_to_integer()
# Function to check for negative integers in a list
# def check_for_negatives():
#     try:
#         # Prompt the user to input a list of integers (comma-separated)
#         user_input = input("Enter a list of integers, separated by commas: ")
#
#         # Convert the input into a list of integers
#         numbers = [int(x.strip()) for x in user_input.split(",")]
#
#         # Check for negative integers
#         for number in numbers:
#             if number < 0:
#                 raise ValueError(f"Negative integer found: {number}")
#
#         print("All integers are non-negative!")
#     except ValueError as e:
#         # Handle the case where input contains non-integer values or a negative integer is found
#         print(f"Error: {e}")
#     except Exception as e:
#         # Handle unexpected errors
#         print(f"An unexpected error occurred: {e}")
#
#
# # Call the function
# check_for_negatives()

# Function to compute the average of a list of integers
# def compute_average():
#     try:
#         # Prompt the user to input a list of integers (comma-separated)
#         user_input = input("Enter a list of integers, separated by commas: ")
#
#         # Convert the input into a list of integers
#         numbers = [int(x.strip()) for x in user_input.split(",")]
#
#         # Compute the average
#         if len(numbers) == 0:
#             raise ValueError("The list is empty. Cannot compute the average.")
#
#         average = sum(numbers) / len(numbers)
#         print(f"The average of the integers is: {average}")
#     except ValueError as e:
#         # Handle invalid input or empty list
#         print(f"Error: {e}")
#     except Exception as e:
#         # Handle any unexpected exceptions
#         print(f"An unexpected error occurred: {e}")
#     finally:
#         # Message indicating the program has finished running
#         print("Program execution has completed.")
#
#
# # Call the function
# compute_average()

# Function to write a string to a file
def write_to_file():
    try:
        # Prompt the user to input the filename
        filename = input("Enter the filename: ")

        # Open the file in write mode (this will create the file if it doesn't exist)
        with open(filename, 'w') as file:
            # Write a string to the file
            file.write("Hello, this is a test string written to the file.")

        # If no exception occurs, print a welcome message
        print("The string has been successfully written to the file.")

    except IOError:
        # Handle file-related errors (e.g., permission issues)
        print("Error: There was a problem accessing the file. Please check permissions.")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        # Print a message indicating that the program has finished
        print("Program execution has completed.")


# Call the function
write_to_file()


