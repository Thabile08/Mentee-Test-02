def multiply_numbers(a, b):
    """
    Problem 1:
    Write a function that takes two numbers (a and b)
    and returns their product.
    """
    # two integers
    # use the multiplication sign to get the product
    # create a variable that is going to store the calculation

    product = a * b
    return product

print(multiply_numbers(5, 3))


def is_positive(n):
    """
    Problem 2:
    Return True if 'n' is positive, otherwise return False.
    """
    # check if the given number is postive or negative
    # the number is less 0 it should be negative
    # the number that is greater than 0 is postive

    number = 0

    if n > number :
        return True
    elif n < number:
        return False
    


def count_letters(word):
    """
    Problem 3:
    Return how many characters are in a given word.
    """
    # counting the number of letters in a word
    # use a built in function that count the number of letters in a string

    count = len(word)
    return count


def smallest_number(numbers):
    """
    Problem 4:
    Return the smallest number in a list.
    """
    small_number = min(numbers)
    return small_number


def capitalize_word(word):
    """
    Problem 5:
    Capitalize the first letter of a given word.
    """
    sentence = word.capitalize()
    return sentence


def sum_list(numbers):
    """
    Problem 6:
    Return the sum of all numbers in a list.
    If the list is empty, return 0.
    """
    
    num = sum(numbers)

    if num == sum(numbers):
        return num
    else:
        return 0


def contains_number(n, numbers):
    """
    Problem 7:
    Return True if n appears in the list, otherwise False.
    """
    if n in numbers:
        return True
    else:
        return False


def square_number(n):
    """
    Problem 8:
    Return the square of a given number.
    """
    sqr = n**2
    return sqr


def remove_spaces(text):
    """
    Problem 9:
    Return the string with all spaces removed.
    """
    word = text.replace(" ", "")
    return word


def repeat_word(word, times):
    """
    Problem 10:
    Repeat a given word a certain number of times.
    """
    rep_word = word * times
    return rep_word


def count_words(sentence):
    """
    Problem 11 (Harder):
    Count how many words are in a given sentence.
    """
    sent = sentence.split()
    print(sent)
    splited_sent = len(sent)
    return splited_sent


def second_largest(numbers):
    """
    Problem 12 (Harder):
    Return the second largest number in a list.
    If fewer than 2 unique numbers, return None.
    """
    
    duplicate_num = list(set(numbers))

    if len(duplicate_num) < 2:
        return None
    
    duplicate_num.sort()

    return duplicate_num[-2]

    
    
