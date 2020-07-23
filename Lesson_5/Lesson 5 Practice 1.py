a = ["Alex", "John", "Phil", "Artur", "Kane"]


def upper_case(tryam):
    z = tryam.upper()
    return(z)


def lower_case(tryam):
    z = tryam.lower()
    return(z)


print(list(map(upper_case, a)))
print(list(map(lower_case, a)))


