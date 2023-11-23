import unittest


class Paint:
    def __init__(self, image):
        self.image = image

        if not self.is_rectangular():
            raise ValueError("The image is not rectangular.")

    def is_rectangular(self):
        row_lengths = {len(row) for row in self.image}
        return len(row_lengths) == 1

    def is_valid_coordinate(self, x, y):
        valid_boundaries_horizontal = 0 <= x < len(self.image)
        valid_boundaries_vertical = 0 <= y < len(self.image[0])
        return valid_boundaries_horizontal and valid_boundaries_vertical

    def paint_pixel(self, x, y, new_color):
        self.image[x][y] = new_color

    def generate_adjacent_pixels(self, x, y):
        left = (x - 1, y)
        right = (x + 1, y)
        bottom = (x, y + 1)
        top = (x, y - 1)
        return [left, right, bottom, top]

    def fill_connected_pixels(self, x, y, original_color, new_color):
        if not self.is_valid_coordinate(x, y) or self.image[x][y] != original_color:
            return

        self.paint_pixel(x, y, new_color)
        adjacent_pixels = self.generate_adjacent_pixels(x, y)

        for x_, y_ in adjacent_pixels:
            self.fill_connected_pixels(x_, y_, original_color, new_color)

    def paint_bucket(self, pixel, new_color):
        x, y = pixel

        if not self.is_valid_coordinate(x, y):
            raise ValueError("Invalid pixel coordinates.")

        original_color = self.image[x][y]

        if original_color == new_color:
            return

        self.fill_connected_pixels(x, y, original_color, new_color)

    def print_image(self):
        for row in self.image:
            print(" ".join(row))


class TestPaint(unittest.TestCase):
    def setUp(self):
        self.image = [
            [".", "#", "#", "#", ".", "."],
            [".", "#", ".", ".", "#", "."],
            [".", "#", "#", "#", ".", "."],
            [".", "#", ".", ".", ".", "."],
        ]
        self.image_processing = Paint(self.image)

    def test_paint_bucket_first_sample(self):
        expected_image = [
            [".", "O", "O", "O", ".", "."],
            [".", "O", ".", ".", "#", "."],
            [".", "O", "O", "O", ".", "."],
            [".", "O", ".", ".", ".", "."],
        ]
        self.image_processing.paint_bucket((0, 1), "O")
        self.assertEqual(self.image_processing.image, expected_image)

    def test_paint_bucket_second_sample(self):
        expected_image = [
            [".", "#", "#", "#", ".", "."],
            [".", "#", "o", "o", "#", "."],
            [".", "#", "#", "#", ".", "."],
            [".", "#", ".", ".", ".", "."],
        ]
        self.image_processing.paint_bucket((1, 3), "o")
        self.assertEqual(self.image_processing.image, expected_image)

    def test_paint_bucket_third_sample(self):
        expected_image = [
            [".", "#", "#", "#", ".", "."],
            [".", "#", "#", "#", "#", "."],
            [".", "#", "#", "#", ".", "."],
            [".", "#", ".", ".", ".", "."],
        ]
        self.image_processing.paint_bucket((1, 3), "#")
        self.assertEqual(self.image_processing.image, expected_image)


if __name__ == "__main__":
    unittest.main()
