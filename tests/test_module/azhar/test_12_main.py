import unittest
from unittest.mock import patch
import sys
import os
import importlib.util


class TestMain(unittest.TestCase):
    
    def setUp(self):
        # Menyimpan path asli
        self.original_path = list(sys.path)
        # Menambahkan direktori src ke path untuk memastikan import berfungsi
        sys.path.insert(0, os.path.abspath('src'))
        
    def tearDown(self):
        # Mengembalikan path asli
        sys.path = self.original_path
    
    def test_main_as_main(self):
        """TC27. Menguji main app berjalan dengan memanggil modul calculator_view() ketika __name__ == '__main__'"""
        # Melakukan patch pada fungsi calculator_view
        with patch('kalkulator.calculator_view.calculator_view') as mock_view:
            # Memuat modul main secara dinamis
            main_path = os.path.abspath('src/kalkulator/main.py')
            spec = importlib.util.spec_from_file_location('__main__', main_path)
            main_module = importlib.util.module_from_spec(spec)
            
            # Mengatur __name__ menjadi '__main__' langsung pada modul
            main_module.__name__ = '__main__'
            
            # Mengeksekusi modul
            spec.loader.exec_module(main_module)
            
            # Memverifikasi bahwa calculator_view telah dipanggil
            mock_view.assert_called_once()
    
    def test_main_as_import(self):
        """TC28. Mengecek bahwa calculator_view tidak dipanggil ketika diimpor sebagai modul"""
        with patch('kalkulator.calculator_view.calculator_view') as mock_view:
            # Memuat modul main secara dinamis tetapi dengan nama berbeda
            main_path = os.path.abspath('src/kalkulator/main.py')
            spec = importlib.util.spec_from_file_location('not_main', main_path)
            main_module = importlib.util.module_from_spec(spec)
            
            # Mengeksekusi modul (dengan __name__ != '__main__')
            spec.loader.exec_module(main_module)
            
            # Memverifikasi bahwa calculator_view TIDAK dipanggil
            mock_view.assert_not_called()


if __name__ == "__main__":
    unittest.main()