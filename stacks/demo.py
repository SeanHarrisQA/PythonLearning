from Stack import Stack

stack = Stack()

stack.push('Sean')
stack.push('Jimmy')
stack.push('Jovi')
print(stack)
print(stack.peek())
stack.pop()
print(stack)
print(stack.size())
print(stack.is_empty())
stack.pop()
stack.pop()
print(stack)
print(stack.size())
print(stack.is_empty())

def reverse_string(string):
    reverse_stack = Stack()
    string_reversed = ''
    for letter in string:
        reverse_stack.push(letter)
    while (not reverse_stack.is_empty()):
        string_reversed += reverse_stack.pop()
    return string_reversed

print(reverse_string("We will conquer COVID-19"))
print(reverse_string(reverse_string("We will conquer COVID-19")))

# Function that takes two brackets and checks to see whether they are the coorect match using a dictionary
def is_match(ch1, ch2):
    # This function only gets called from is_balanced when a closing bracket is found
    # If the closing bracket matches the last opening bracket then it returns true
    match_dict = {
        '(':')',
        '{':'}',
        '[':']'
    }
    return match_dict[ch1] == ch2

def is_balanced(string):
    stack = Stack()
    for character in string:
        # The next character can either be an opening character or a closing character, if it is a closing character then it must match the previous opening partner
        if character=='(' or character=='{' or character == '[':
            stack.push(character)
        if character==')' or character=='}' or character == ']':
            if stack.size()==0:
                # If stack size = 0 then no opening bracket has been added before a closing bracket so the use of parentheses is incorrect
                return False
            if not is_match(stack.pop(), character):
                # If a closing bracket is found then the previous bracket must be its opening partner
                return False
    return stack.size() == 0


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
