
def is_zero(char):
    if ord(char) == 48:
        return True
    else:
        return False

def is_one(char):
    if ord(char) == 49:
        return True
    else:
        return False

def is_two(char):
    if ord(char) == 50:
        return True
    else:
        return False

def is_three(char):
    if ord(char) == 51:
        return True
    else:
        return False

def is_four(char):
    if ord(char) == 52:
        return True
    else:
        return False

def is_five(char):
    if ord(char) == 53:
        return True
    else:
        return False

def is_six(char):
    if ord(char) == 54:
        return True
    else:
        return False

def is_seven(char):
    if ord(char) == 55:
        return True
    else:
        return False

def is_eight(char):
    if ord(char) == 56:
        return True
    else:
        return False

def is_nine(char):
    if ord(char) == 57:
        return True
    else:
        return False

def is_digit_num(char):
    if (
        is_zero(char) or
        is_one(char) or
        is_two(char) or
        is_three(char) or
        is_four(char) or
        is_five(char) or
        is_six(char) or
        is_seven(char) or
        is_eight(char) or
        is_nine(char)
    ):
        return True
    else:
        return False
 
def is_positive_int(user_str):
    for char in user_str:
        if (is_digit_num(char)):
            return True
        else:
            return False

def is_integer(user_str):
    '''Función que determina si un string contiene unicamente carácteres numéricos'''
    is_int = True
    allowed_chars = ['0','1','2','3','4','5','6','7','8','9']
    for char in user_str:
        if allowed_chars.count(char) < 1:
            is_int = False
            break
    return is_int


user_input = input('Digite un entero positivo: ')

# if is_positive_int(user_input):
#     print (user_input + ' SI es un numero entero positivo')
# else:
#     print (user_input + ' NO es un numero entero positivo')

if is_integer(user_input):
    print (user_input + ' SI es un numero entero positivo')
else:
    print (user_input + ' NO es un numero entero positivo')
