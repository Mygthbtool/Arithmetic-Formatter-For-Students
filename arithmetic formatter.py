def arithmetic_arranger(problems, show_answers= False):
    # Not more than five problems
    if len(problems) > 5:
      return 'Error: Too many problems.'
    
    top_lines = []
    bottom_lines = []
    dash_lines = [] 
    result_lines = []   

    for problem in problems:
        convrted_problem = problem.split()
        first_num = convrted_problem[0]
        operator = convrted_problem[1]
        second_num = convrted_problem[2]
        # Operator must be '+' or '-'
        if operator == '*' or operator == '/':
            return "Error: Operator must be '+' or '-'."
            break

        # Numbers must only contain digits
        if not (first_num.isdigit() and second_num.isdigit()):
            return 'Error: Numbers must only contain digits.'
            break
        # Numbers cannot be more than four digits
        if len(first_num) > 4 or len(second_num) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            break

        max_length = max(len(first_num), len(second_num))

        top_line = first_num.rjust(max_length + 2)
        bottom_line = operator + ' ' + second_num.rjust(max_length)
        dashes = '-' * (max_length + 2)

        top_lines.append(top_line) 
        bottom_lines.append(bottom_line)
        dash_lines.append(dashes)

        if show_answers == True:
            if operator == '+':
                result = int(first_num) + int(second_num)
            if operator == '-':
                result = int(first_num) - int(second_num)

            result_line = (str(result)).rjust(max_length + 2)

            result_lines.append((result_line))

    arranged_problems = '    '.join(top_lines) + "\n" + '    '.join(bottom_lines) + "\n" + '    '.join(dash_lines)    
    if show_answers:
        arranged_problems += '\n' + '    '.join(result_lines)

    return arranged_problems

print(f'\n{arithmetic_arranger()}')
