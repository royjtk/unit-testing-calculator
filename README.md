# Aplikasi Kalkulator Sederhana

Aplikasi sederhana untuk demonstrasi unit testing dan pelaporan hasil pengujian.

## Kebutuhan Sistem

- Python 3.13.x
- Poetry (package manager) 2.1.2

## Pengaturan Proyek

```bash
# Instalasi dependensi
poetry install
```

## Menjalankan Aplikasi

```bash
poetry run python src/kalkulator/main.py
```

## Pengujian dan Laporan

### Menjalankan Pengujian Dasar

```bash
poetry run pytest
```

### Menjalankan Pengujian dengan Laporan HTML

```bash
poetry run pytest --html=test_report.html --self-contained-html --css=tests/assets/style.css --cov=src
```

Laporan pengujian akan menghasilkan:
- Daftar tes yang dijalankan beserta deskripsinya
- Status keberhasilan setiap tes (passed/failed)
- **Laporan cakupan kode (code coverage)** yang menunjukkan persentase kode yang diuji
- Detail waktu eksekusi setiap pengujian

### Fitur Pengujian

Pengujian dibagi menjadi beberapa kategori:
1. **Fungsi Kalkulator** - Menguji operasi matematika dasar
   - Penjumlahan, Pengurangan, Perkalian, Pembagian
   - Penanganan kasus khusus (pembagian dengan nol)

2. **Validasi Input** - Memastikan input yang diterima valid
   - Validasi operand (harus berupa angka dalam rentang tertentu)
   - Validasi operator (harus salah satu dari +, -, *, /)

## Struktur Proyek

```
kalkulator/
├── src/              # Kode sumber aplikasi yang di test
├── tests/            # Pengujian
│   ├── conftest.py   # Konfigurasi pengujian dan formatter laporan
│   ├── assets/       # Asset untuk laporan HTML
│   └── test_*.py     # File pengujian
└── test_report.html  # Laporan hasil pengujian (setelah dijalankan)
```

## Membangun Aplikasi

```bash
poetry run pyinstaller --onefile src/kalkulator/main.py
```

[![CI/CD Pipeline](https://github.com/username/kalkulator/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/username/kalkulator/actions/workflows/ci-cd.yml)