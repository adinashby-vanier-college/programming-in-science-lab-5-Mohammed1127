def hollow_square(n):
    result = ""
    i = 1
    while i <= n:
        if i == 1 or i == n:  
            result += "*" * n
        else:  
            result += "*" + " " * (n - 2) + "*"
        if i != n:  
            result += "\n"
        i += 1
    return result


def number_pattern(n):
    i = 1
    result = ""
    while i <= n:
        j = 1
        while j <= i:
            result += str(j)
            j += 1
        if i != n:  
            result += "\n"
        i += 1
    return result


def sum_of_natural_numbers(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


def centered_star_pyramid(n):
    result = ""
    i = 1
    while i <= n:
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        result += spaces + stars
        if i != n:  
            result += "\n"
        i += 1
    return result
