import math

non_decimal = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def change_base(number, base):
    if number < base:
        return non_decimal[number]
    else:
        return change_base(number//base, base) + non_decimal[number%base]
        
if __name__ == '__main__':
    for x in range(40):
        answer = change_base(x, 2)
        space = ' ' * (5 - len(answer))
        print(space + answer)