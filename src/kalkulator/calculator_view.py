from kalkulator.calculator import Calculator
from kalkulator.validator import Validator

from kalkulator.view import *
from kalkulator.get_input import *



def calculator_view():
    calc = Calculator()
    validator = Validator()
    
    try:
        show_header()
        prompt_input_operand1()
        operand1 = get_operand()
        operand1 = validator.validate_operand(operand1)
        
        prompt_input_operator()
        operator = get_operator()
        operator = validator.validate_operator(operator)
        
        prompt_input_operand2()
        operand2 = get_operand()
        operand2 = validator.validate_operand(operand2)
        
        result = calc.perform_operation(operator, operand1, operand2)
        
        show_result(operand1, operator, operand2, result)
        
    except ValueError as e:
        show_error(str(e))
    
    prompt_exit()
