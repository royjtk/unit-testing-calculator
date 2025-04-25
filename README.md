Berikut adalah panduan lengkap untuk membuat lingkungan pengembangan (env), membangun aplikasi Python, dan menambahkan unit testing beserta lingkungan pengujian (testing env), dari awal hingga proses build menjadi file EXE. Saya akan menggunakan **Poetry** untuk manajemen proyek dan dependensi, **PyInstaller** untuk membangun aplikasi EXE, serta **pytest** untuk unit testing.

### Langkah 0: Instalasi Python

1. **Unduh Python**:
   Unduh installer Python terbaru dari [python.org](https://www.python.org/downloads/)
   - Pilih versi Python 3.13.x yang sesuai dengan sistem operasi Anda

2. **Jalankan Installer**:
   - Centang opsi "Add Python to PATH" pada awal instalasi
   - Pilih "Customize Installation" untuk opsi konfigurasi lebih lanjut
   - Pada Advanced Options, pastikan "pip" dan "py launcher" tercentang
   - Klik "Install" untuk memulai instalasi

3. **Verifikasi Instalasi**:
   Buka Command Prompt atau PowerShell dan jalankan perintah:
   ```bash
   python --version
   pip --version
   ```
   Pastikan versi Python yang terinstal adalah 3.13.x dan pip sudah terinstal dengan benar.


### Langkah 1: Membuat Proyek dengan Poetry

1. **Instal Poetry**:
   Jika Anda belum menginstal **Poetry**, Anda bisa menginstalnya dengan perintah berikut:
   ```bash
   pip install poetry
   ```

2. **Membuat Proyek Baru**:
   Setelah Poetry terinstal, buat proyek Python baru:
   ```bash
   poetry new kalkulator
   cd kalkulator
   ```

   Struktur proyek dasar yang dihasilkan oleh Poetry:
   ```
   kalkulator/
   ├── kalkulator/
   │   ├── __init__.py
   │   └── main.py
   ├── pyproject.toml
   ├── README.rst
   └── tests/
       └── test_main.py
   ```

3. **Menentukan versi python yang digunakan di pyproject.toml**:
   pada file `pyproject.toml` ubah bagian `requires-python = ">=3.13"` menjadi `requires-python = ">=3.13,<3.14"`


### Langkah 2: Menambahkan Dependensi yang Diperlukan

1. **Menambahkan Dependensi untuk PyInstaller dan pytest**:
   Anda perlu menambahkan **PyInstaller** untuk mengonversi skrip Python ke file EXE dan **pytest** untuk unit testing.

   Menambahkan dependensi menggunakan Poetry:
   ```bash
   poetry add pyinstaller pytest
   ```

2. **Verifikasi Dependensi**:
   Pastikan semua dependensi telah ditambahkan di file `pyproject.toml`. Contoh setelah menambahkan dependensi:
   ```toml
   [tool.poetry.dependencies]
   python = "^3.9"
   pyinstaller = "^5.0"

   [tool.poetry.dev-dependencies]
   pytest = "^7.0"
   ```

### Langkah 3: Implementasi Aplikasi Kalkulator

Buka file `kalkulator/main.py` dan implementasikan aplikasi kalkulator Anda seperti yang telah dijelaskan sebelumnya.

#### Contoh Aplikasi Kalkulator (dalam `main.py`):
```python
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
```

### Langkah 4: Menambahkan Unit Testing

1. **Buat Unit Test di Direktori `tests/`**:
   Di dalam direktori `tests/`, buat file pengujian seperti `test_main.py` untuk menguji fungsi kalkulator dan validasi input.

#### Contoh Pengujian dengan **pytest** (`tests/test_main.py`): `ini harus disesuaikan lagi dengan test case yang sudah dibuat`
```python
import pytest
from kalkulator.main import Calculator, Validator


def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 3) == 2.0

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(6, 0)

def test_validate_operand():
    validator = Validator()
    assert validator.validate_operand(100) == 100
    with pytest.raises(ValueError):
        validator.validate_operand("abc")

def test_validate_operator():
    validator = Validator()
    assert validator.validate_operator("+") == "+"
    with pytest.raises(ValueError):
        validator.validate_operator("!")

```

2. **Menjalankan Unit Test dengan pytest**:
   Untuk menjalankan unit test, cukup jalankan perintah berikut di terminal:
   ```bash
   poetry run pytest
   ```

   Hasil dari pengujian akan ditampilkan di terminal, dengan pesan yang menunjukkan apakah pengujian lulus atau gagal.

3. **Contoh hasil pengujian yang ditampilkan di terminal**:
   ```bash
    PS D:\semester6\ppl\unit_test\kalkulator> poetry run pytest
    ====================================== test session starts ======================================
    platform win32 -- Python 3.13.3, pytest-8.3.5, pluggy-1.5.0
    rootdir: D:\semester6\ppl\unit_test\kalkulator
    configfile: pyproject.toml
    platform win32 -- Python 3.13.3, pytest-8.3.5, pluggy-1.5.0
    configfile: pyproject.toml
    collected 7 items                                                                                         

    tests\test_main.py .......                                                                 [100%]

    ======================================= 7 passed in 0.04s =======================================
   ```

### Langkah 5: Menambahkan Pengujian Lingkungan (Test Environment)

1. **Menggunakan Virtual Environment dengan Poetry**:
   Poetry secara otomatis mengelola virtual environment, sehingga saat Anda menjalankan perintah `poetry run`, itu akan bekerja di dalam lingkungan yang terisolasi.

2. **Memulai Lingkungan Pengujian**:
   Untuk menjalankan aplikasi dalam lingkungan pengujian, pastikan untuk menggunakan perintah `poetry run` saat mengeksekusi aplikasi atau pengujian.
   ```bash
   poetry run python kalkulator/main.py
   ```

### Langkah 6: Membangun EXE dengan PyInstaller

1. **Menambahkan PyInstaller ke Proyek**:
   Anda telah menambahkan **PyInstaller** pada langkah 2 dengan `poetry add pyinstaller`.

2. **Membuat File EXE**:
   Setelah aplikasi berjalan dengan baik dan unit test lulus, Anda dapat membangun file EXE dengan menggunakan PyInstaller:
   ```bash
   poetry run pyinstaller --onefile kalkulator/main.py
   ```

   Ini akan menghasilkan file EXE yang dapat dijalankan di Windows di dalam folder `dist/`.

### Langkah 7: Verifikasi dan Testing EXE

1. **Menjalankan EXE**:
   Setelah proses build selesai, buka folder `dist/`, dan jalankan file `kalkulator.exe` untuk memastikan aplikasi bekerja dengan baik.

2. **Pengujian EXE**:
   Anda bisa melakukan uji fungsionalitas pada file EXE untuk memastikan semuanya bekerja sebagaimana mestinya di luar lingkungan pengembangan.

---

### Ringkasan Langkah-langkah:
1. **Buat Proyek dengan Poetry**.
2. **Tambahkan Dependensi**: Install PyInstaller dan pytest untuk build EXE dan pengujian.
3. **Implementasi Aplikasi Kalkulator**: Buat program kalkulator dengan validasi input.
4. **Buat Unit Test** menggunakan pytest.
5. **Build EXE dengan PyInstaller**.
6. **Uji Aplikasi EXE** untuk memastikan semuanya berjalan dengan baik.

Dengan mengikuti langkah-langkah ini, Anda akan memiliki aplikasi Python yang terstruktur dengan baik, diuji dengan unit testing, dan siap untuk dibangun menjadi file EXE yang dapat dijalankan di Windows.