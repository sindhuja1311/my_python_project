import unittest
import os
import sys
import io

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from my_python_project.main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__  # Fix: Corrected to restore sys.stdout
        self.assertEqual(captured_output.getvalue().strip(), "Hello from Jenkins CI/CD Pipeline!")

if __name__ == "__main__":
    unittest.main()
