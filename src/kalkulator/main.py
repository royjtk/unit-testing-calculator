class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Error: Pembagi tidak boleh nol.")
        return a / b


class Validator:
    def validate_operand(self, operand):
        if not isinstance(operand, (int, float)):
            raise ValueError("Error: Operand harus berupa angka.")
        if operand < -32768 or operand > 32767:
            raise ValueError("Error: Angka harus berada dalam rentang -32,768 hingga 32,767.")
        return operand

    def validate_operator(self, operator):
        if operator not in ['+', '-', '*', '/']:
            raise ValueError("Error: Operator yang valid hanya +, -, *, /.")
        return operator


def run_calculator():
    calc = Calculator()
    validator = Validator()
    
    try:
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


if __name__ == "__main__":
    print("=== Kalkulator Sederhana ===")
    run_calculator()