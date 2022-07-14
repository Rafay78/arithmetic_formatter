# def arithmetic_arranger(problems, ans = True):
#   arranged_problems = ""
#
#   if len(problems)>5:
#     arranged_problems = "Error: Too many problems."
#     return arranged_problems
#
#   i = 0
#   d = dict()
#   l = list()
#   for s in problems:
#     s = s.split()
#     #print(s)
#     if s[1] != '+' and s[1] != '-':
#       print(arranged_problems)
#       arranged_problems += "Error: Operator must be '+' or '-'."
#       return arranged_problems
#
#     if len(s[0])>4 or len(s[2])>4:
#       arranged_problems = "Error: Numbers cannot be more than four digits."
#       return arranged_problems
#
#     try:
#       al = len(s[0])
#       bl = len(s[2])
#       a = int(s[0])
#       b = int(s[2])
#       if s[1] == '+':
#         c = a + b
#       else:
#         c = a - b
#       sp = max(al, bl) + 2
#       l = [al, a, bl, b, c, s[1], sp]
#       d[i] = l
#       i = i + 1
#
#     except:
#       arranged_problems = "Error: Numbers must only contain digits."
#       return arranged_problems
#   j = 0
#   # print(d)
#   for k,v in d.items():
#     print(k,v)
#     space = v[6] - v[0]
#     while(space):
#       arranged_problems = arranged_problems + " "
#       space = space - 1
#     arranged_problems = arranged_problems + str(v[1])
#     # print(str(v[1]))
#     if j < len(problems)-1:
#       for q in range(4):
#         arranged_problems = arranged_problems + " "
#     j = j + 1
#
#   arranged_problems = arranged_problems + '\n'
#
#   j = 0
#   for k,v in d.items():
#     print(k,v)
#     arranged_problems = arranged_problems + v[5] + " "
#     if v[2] < v[0]:
#       space = v[0] - v[2]
#       while space:
#         arranged_problems = arranged_problems + " "
#         space = space - 1
#     arranged_problems = arranged_problems + str(v[3])
#     if j < len(problems)-1:
#       for q in range(4):
#         arranged_problems = arranged_problems + " "
#     j = j + 1
#
#   arranged_problems = arranged_problems + '\n'
#
#   j = 0
#   for k,v in d.items():
#     print(k,v)
#     dash = v[6]
#     while dash:
#       arranged_problems = arranged_problems + '-'
#       dash = dash - 1
#     if j < len(problems)-1:
#       for q in range(4):
#         arranged_problems = arranged_problems + " "
#     j = j + 1
#
#   if ans == True:
#     arranged_problems = arranged_problems + '\n'
#     j = 0
#     for k,v in d.items():
#       cl = len(str(v[4]))
#       space = v[6] - cl
#       while space:
#         arranged_problems = arranged_problems + " "
#         space = space - 1
#       arranged_problems  = arranged_problems + str(v[4])
#       if j < len(problems)-1:
#         for q in range(4):
#           arranged_problems = arranged_problems + " "
#       j = j + 1
#
#   # print(arranged_problems)
#
#   return arranged_problems
#
# print(arithmetic_arranger(["32 + 698", "3801 + 2", "45 + 43", "123 + 49"]))











def arithmetic_arranger(problems):
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = ''
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
