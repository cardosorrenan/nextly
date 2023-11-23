import json
import random
import time
import unittest


class PhoneBook:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []
        self.load_data()

    def load_data(self):
        with open(self.file_path, "r") as file:
            self.data = json.load(file)

    def search_phone_by_name(self, target_name: str) -> str:
        start_pos_index = 0
        end_pos_index = len(self.data) - 1
        target_phone = None

        start_time = time.time()

        while start_pos_index <= end_pos_index:
            mid_pos_index = (start_pos_index + end_pos_index) // 2
            mid_pos_name = self.data[mid_pos_index]["name"]

            if mid_pos_name == target_name:
                end_time = time.time()
                target_phone = self.data[mid_pos_index]["phone"]
                break

            elif mid_pos_name < target_name:
                start_pos_index = mid_pos_index + 1
            else:
                end_pos_index = mid_pos_index - 1

        end_time = time.time()

        print(f"\nTime taken: {end_time - start_time} seconds")

        if target_phone:
            print(f"Phone number for {target_name}: {target_phone}")
        else:
            print(f"{target_name} not found in the contacts list.")

        return target_phone


class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        self.file_path = "phone_book.json"
        self.phone_book = PhoneBook(self.file_path)

    def test_basic_search(self):
        random_person = random.choice(self.phone_book.data)
        target_phone = self.phone_book.search_phone_by_name(random_person["name"])
        self.assertEqual(target_phone, random_person["phone"])

    def test_name_not_found(self):
        target_phone = self.phone_book.search_phone_by_name("Renan Henrique Cardoso")
        self.assertIsNone(target_phone)

    def test_first_entry(self):
        first_entry = self.phone_book.data[0]
        target_phone = self.phone_book.search_phone_by_name(first_entry["name"])
        self.assertEqual(target_phone, first_entry["phone"])

    def test_last_entry(self):
        last_entry = self.phone_book.data[-1]
        target_phone = self.phone_book.search_phone_by_name(last_entry["name"])
        self.assertEqual(target_phone, last_entry["phone"])

    def test_middle_entry(self):
        mid_entry = self.phone_book.data[len(self.phone_book.data) // 2]
        target_phone = self.phone_book.search_phone_by_name(mid_entry["name"])
        self.assertEqual(target_phone, mid_entry["phone"])


if __name__ == "__main__":
    unittest.main()
