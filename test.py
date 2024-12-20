import unittest
import transform

"""
Aquest modul executa els tests del repositori
"""

class TestStringMethods(unittest.TestCase):
    """
    Aquesta classe conté tots els tests a executar
    """

    def test_is_upper(self):
        """
        Aquest metode comprova si el text es posa en majuscules
        """
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")

    def test_is_lower(self):
        """
        Aquest metode comprova si el text es posa en minuscules
        """
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")

    def test_is_capitalize(self):
        """
        Aquest metode comprova si el text es posa en majuscula inicial
        """
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")


if __name__ == '__main__':
    unittest.main()
