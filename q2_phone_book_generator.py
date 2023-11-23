import json

from faker import Faker


class DataGenerator:
    def __init__(self, locale):
        self.fake = Faker(locale)
        self.data = []
        self.names_pool = set()

    def generate_unique_pool(self, num_entries):
        while len(self.names_pool) < num_entries:
            name = self.fake.name()
            self.names_pool.add(name)

    def generate_entries(self, num_entries):
        self.generate_unique_pool(num_entries)

        for name in self.names_pool:
            phone = self.fake.phone_number()
            entry = {"name": name, "phone": phone}
            self.data.append(entry)

    def save_to_json(self, file_path):
        sorted_data = sorted(self.data, key=lambda x: x["name"])

        with open(file_path, "w") as file:
            json.dump(sorted_data, file, indent=2, sort_keys=True, ensure_ascii=False)
        print(f"Entries saved to {file_path}")


if __name__ == "__main__":
    generator = DataGenerator("en")
    generator.generate_entries(10000)
    generator.save_to_json("phone_book.json")
