import unittest


def is_palindrome(input_string) -> bool:
    if not isinstance(input_string, str):
        print("Error: Input is not a string.")
        return False
    return input_string == input_string[::-1]


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("arara"))
        self.assertTrue(is_palindrome("reviver"))
        self.assertTrue(is_palindrome("radar"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("renan"))
        self.assertFalse(is_palindrome("nextly"))


if __name__ == "__main__":
    unittest.main()
