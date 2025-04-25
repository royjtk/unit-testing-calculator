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
