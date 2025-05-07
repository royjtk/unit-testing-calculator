def show_header():
    """Menampilkan header kalkulator sederhana."""
    print("====== Kalkulator Sederhana ======")

def show_result(operand1, operator, operand2, result):
    """Menampilkan hasil perhitungan."""
    print(f"Hasil: {operand1} {operator} {operand2} = {result}")

def show_error(message):
    """Menampilkan pesan error."""
    print(f"Error: {message}")

def prompt_exit():
    """Menampilkan pesan untuk keluar."""
    print("Tekan tombol apa saja untuk keluar...")
    
def prompt_input_operand1():
    """Menampilkan pesan untuk input operand pertama."""
    print("Masukkan operand pertama: ")

def prompt_input_operator():
    """Menampilkan pesan untuk input operator."""
    print("Masukkan operator (+, -, *, /): ")
    
def prompt_input_operand2():
    """Menampilkan pesan untuk input operand kedua."""
    print("Masukkan operand kedua: ")
