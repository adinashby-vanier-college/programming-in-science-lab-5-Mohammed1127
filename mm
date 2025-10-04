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

print(number_pattern(4))
