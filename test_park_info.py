import unittest
from park_info import get_park_code

class TestParkInfo(unittest.TestCase):
    
    def test_valid_park_code(self):
        # Arrange
        code = "AH"
        
        # Act
        result = get_park_code(code)
        
        # Assert
        self.assertEqual(result, "Kent Coast")

    def test_invalid_park_code(self):
        # Arrange
        code = "ZZ"
        
        # Act
        result = get_park_code(code)
        
        # Assert
        self.assertEqual(result, "\nIncorrect entry. Please try again.")
        
    def test_lowercase_park_code(self):
        # Arrange
        code = "ah"
        
        # Act
        result = get_park_code(code)
        
        # Assert
        self.assertEqual(result, "Kent Coast")
    
if __name__ == "__main__":
    unittest.main()