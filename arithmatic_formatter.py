def arithmetic_arranger(problems):
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = []
  for problem in problems:
    operations = problem.split(' ')
    try:
        operand1 = int(operations[0])
        operand2 = int(operations[2])
    except ValueError:
        return "Error: Numbers must only contain digits."
    operator = operations[1]

    if operator != ('+' or '-'):
      return "Error: Operator must be '+' or '-'."

    if (len(operations[2]) or len(operations[1])) > 5:
      return "Error: Numbers cannot be more than four digits."

    if operator == "+":
      sum = operand1 + operand2
    else:
      sum = operand1 - operand2

    diff_rtrn_crg = abs(len(operations[0]) - len(operations[2]))
    arr = [' '] * diff_rtrn_crg


    if len(operations[0]) > len(operations[2]):
        x=0
    elif len(operations[0]) < len(operations[2]):
        y=0


  return arranged_problems

    # return arithmetic_arranger

#Sum=["1 + 2", "2 * 13"]
print(arithmetic_arranger(["11 + 2","112 + 34"]))
#
#
#
# def arithmetic_arranger(problems):
#   if len(problems) > 5:
#     return "Error: Too many problems."
#   for problem in problems:
#     operations = problem.split(' ')
#     operand1 = int(operations[0])
#     operand2 = int(operations[2])
#     operator = operations[1]
#
#     if operator != '+' or '-':
#       return "Error: Operator must be '+' or '-'."
#
#     if not operations[0].isnumeric() and operations[2].isnumeric():
#       return "Error: Numbers must only contain digits."
#
#     if (len(operations[2]) or len(operations[1])) > 5:
#       return "Error: Numbers cannot be more than four digits."
#
#     if operator == "+":
#       sum = operand1 + operand2
#     else:
#       sum = operand1 - operand2
#
#     diff_rtrn_crg = abs(len(operand1) - len(operand2))
#     arr = [''] * diff_rtrn_crg
#
#     if len(operand1) > len(operand2):
#       print(operand1)
#       arr.append(operand2)
#       print(* arr)
#       for dot in range(len(arr)):
#         print('-')
#       print(sum)
#     elif len(operand1) < len(operand2):
#       print(operand2)
#       arr.append(operand1)
#       print(* arr)
#       for dot in range(len(arr)):
#         print('-')
#       print(sum)
#
#
#
#
#     return arranged_problems
