

from kalkulator.calculator import Calculator
from kalkulator.validator import Validator





def calculator_view():
    calc = Calculator()
    validator = Validator()
    
    try:
        print("=== Kalkulator Sederhana ===")
        operand1 = float(input("Masukkan operand pertama: "))
        operand1 = validator.validate_operand(operand1)
        
        operator = input("Masukkan operator (+, -, *, /): ")
        operator = validator.validate_operator(operator)
        
        operand2 = float(input("Masukkan operand kedua: "))
        operand2 = validator.validate_operand(operand2)
        
        if operator == '+':
            result = calc.add(operand1, operand2)
        elif operator == '-':
            result = calc.subtract(operand1, operand2)
        elif operator == '*':
            result = calc.multiply(operand1, operand2)
        elif operator == '/':
            result = calc.divide(operand1, operand2)
        
        print(f"Hasil: {operand1} {operator} {operand2} = {result}")
    
    except ValueError as e:
        print(e)
