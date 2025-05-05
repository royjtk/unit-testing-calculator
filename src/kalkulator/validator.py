class Validator:
    def validate_operand(self, operand):
        if not self.is_number(operand):
            raise ValueError("Error: Operand harus berupa angka.")
        if not self.is_number_in_range(operand):
            raise ValueError("Error: Angka harus berada dalam rentang -32,768 hingga 32,767.")
        return operand

    def validate_operator(self, operator):
        if operator not in ['+', '-', '*', '/']:
            raise ValueError("Error: Operator yang valid hanya +, -, *, /.")
        return operator
    
    def is_not_zero_divisor(self, operand):
        if operand == 0:
            raise ValueError("Error: Pembagi tidak boleh nol.")
        return operand

    def is_number(self, operand):
        return isinstance(operand, (int, float))
        
    def is_number_in_range(self, operand):
        return operand >= -32768 and operand <= 32767