def arithmetic_arranger(problems, show_answers= False):
    # Not more than five problems
    if len(problems) > 5:
      return 'Error: Too many problems.'
    
    top_lines = []
    bottom_lines = []
    dash_lines = [] 
    result_lines = []   