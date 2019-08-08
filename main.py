def is_number(char):
    try:
        return type(int(char)) == int
    except ValueError:
        return False


if is_number("2") == True:
    print("okey")
else:
    print('failed')

if is_number("k") == False:
    print("okey")
else:
    print('failed')


def is_operator(char):
    return char in list('-+/*')


if is_operator("-") == True:
    print("okey")
else:
    print('failed')

if is_operator("9") == False:
    print("okey")
else:
    print('failed')

if is_operator("k") == False:
    print("okey")
else:
    print('failed')


# 34+54
# i = 3
# добавляем в массив 3
# i = 4
# если последний символ в массивые - цифра , и текуший символ цифра ,то соединяем их
# в массиве 34
# i = +
# так как символ оператор , то добавляем его в массив,в массиве 34,+
# i = 5
# добавляем в массив , так как это цифра
# i = 4
# если последний символ в массивые - цифра , и текуший символ цифра ,то соединяем их
# в массиве 34,+,54
def split_notation(str):
    result = []
    for i in list(str):
        if is_number(i):
            if len(result) > 0 and is_number(result[-1]):
                result.append(result.pop() + i)
            else:
                result.append(i)
        elif is_operator(i):
            result.append(i)
    return result


if split_notation("34+54") == ["34", "+", "54"]:
    print('okey')
else:
    print('failed')

if split_notation("304+54") == ["304", "+", "54"]:
    print('okey')
else:
    print('failed')



# 304+54*2 должно проеобразоваться в 304542*+
# 1. i=304 добавляем в стек операндов
# 2. i=+ добавляем в стек операций
# 3. i=54 добавляем в стек операндов
# 4. i=* добавляем в стек операций
# 5. i=2 добавляем в стек операндов
# в стеке операндов :  304,54,2
# в стекее операций : *,+
def rpn(str):
    stack_operators = []
    result = []
    notation = split_notation(str)
    operations_priority = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    for i in notation:
        if is_number(i):
            result.append(i)
            if len(stack_operators) > 0 and operations_priority[stack_operators[-1]] == 2 :
                result.append(stack_operators.pop())
        if is_operator(i):
            stack_operators.append(i)
    
    while len(stack_operators) > 0:
        result.append(stack_operators.pop())
    return result


if rpn("12 * 3 / 4 + 3 - 2") == ['12', '3', '*', '4', '/', '3', '+', '2', '-']:
    print('okey')
else:
    print('Failed')

print(rpn("12 * 3 / 4 + 3 - 2"))

def execute_operator(operand_left, operand_right, operator):
    left = int(operand_left)
    right = int(operand_right)
    if operator == '-':
        return left - right
    if operator == '+':
        return left + right
    if operator == '*':
        return left * right
    if operator == '/':
        return left / right

if execute_operator("1" , "2", "-") == - 1:
    print('okey')
else: 
    print('Failed')

def calculate(str):
    notation = rpn(str)
    print(notation)
    stack_operands = []
    for i in notation:
        if is_number(i):
            notation.append(i)
        if is_operator(i):
            operand_right = stack_operands.pop()
            operand_left = stack_operands.pop()
            result = execute_operator(operand_left, operand_right, i)
            stack_operands.append(result)
    return stack_operands.pop()

print(calculate("12 * 3 / 4 + 3 - 2"))