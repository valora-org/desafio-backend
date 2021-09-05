def capitalize(words):
    uppercase = ""
    for n in words:
        uppercase += n.capitalize() + " "
    return uppercase[0:-1]

def get_numbers_as_str(n):
    return str("".join(filter(str.isdigit, n)))