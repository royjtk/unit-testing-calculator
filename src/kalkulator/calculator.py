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

    def perform_operation(self, operator, operand1, operand2):
        """Menangani operasi perhitungan berdasarkan operator."""
        if operator == '+':
            return self.add(operand1, operand2)
        elif operator == '-':
            return self.subtract(operand1, operand2)
        elif operator == '*':
            return self.multiply(operand1, operand2)
        elif operator == '/':
            return self.divide(operand1, operand2)