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
            
