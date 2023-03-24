expression = input("Expression: ")
equation = expression.split(" ")

match equation[1]:
    case "+":
        print(float(equation[0]) + float(equation[2]))
    case "-":
        print(float(equation[0]) - float(equation[2]))
    case "*":
        print(float(equation[0]) * float(equation[2]))
    case "/":
        print(float(equation[0]) / float(equation[2]))