# Aplikasi Kalkulator Sederhana

Aplikasi kalkulator sederhana dengan fitur pengujian (unit testing) dan pelaporan hasil tes.

## Kebutuhan Sistem

- Python 3.13.x
- Poetry (package manager)

## Pengaturan Proyek

### 1. Instalasi Dependensi

Instal semua dependensi menggunakan Poetry:

```bash
poetry install
```

Dependensi utama:
- pytest: untuk unit testing
- pytest-html: untuk pelaporan hasil pengujian
- pytest-cov: untuk analisis cakupan kode
- pyinstaller: untuk membangun aplikasi menjadi file executable

### 2. Menjalankan Aplikasi

```bash
poetry run python src/kalkulator/main.py
```

## Pengujian

### Menjalankan Unit Test

```bash
poetry run pytest
```

### Menjalankan Unit Test dengan Laporan HTML

```bash
poetry run pytest --html=test_report.html --self-contained-html --cov=src
```

Parameter:
- `--html=test_report.html`: Menghasilkan laporan dalam format HTML
- `--self-contained-html`: Membuat laporan HTML yang mandiri (semua CSS/JS dimasukkan)
- `--cov=src`: Menghasilkan laporan cakupan kode untuk direktori `src`

### Struktur Pengujian

Pengujian dibagi menjadi beberapa bagian:
- `test_calculator.py`: Pengujian fungsi kalkulasi (tambah, kurang, kali, bagi)
- `test_validate_operand.py`: Pengujian validasi operand
- `test_validate_operator.py`: Pengujian validasi operator

## Membangun Aplikasi (Build)

Untuk membuat file executable (EXE) dari aplikasi:

```bash
poetry run pyinstaller --onefile src/kalkulator/main.py
```

File executable akan tersedia di folder `dist/`.

## Struktur Proyek

```
kalkulator/
├── src/
│   └── kalkulator/
│       ├── __init__.py
│       ├── calculator.py     # Implementasi fungsi kalkulator
│       ├── validator.py      # Validasi input
│       ├── calculator_view.py # Tampilan kalkulator
│       └── main.py           # Entry point aplikasi
├── tests/
│   ├── __init__.py
│   ├── conftest.py           # Konfigurasi pengujian
│   ├── test_calculator.py    # Pengujian fungsi kalkulator
│   ├── test_validate_operand.py # Pengujian validasi operand
│   └── test_validate_operator.py # Pengujian validasi operator
├── pyproject.toml           # Konfigurasi Poetry
├── poetry.lock              # Dependensi yang terkunci
└── README.md                # Dokumentasi proyek
```