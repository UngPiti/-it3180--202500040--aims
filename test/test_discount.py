import unittest

def calculate_discount(price, discount_percent):
    """Hàm tính toán giảm giá mẫu"""
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount must be non-negative")
    return price * (1 - discount_percent / 100)

class TestDiscount(unittest.TestCase):
    def test_calculate_discount_normal(self):
        # Kiểm tra tính toán giảm giá thông thường (ví dụ: giảm 20% cho sản phẩm 200)
        result = calculate_discount(200.0, 20)
        self.assertEqual(result, 160.0)

    def test_calculate_discount_zero(self):
        # Kiểm tra khi không giảm giá (0%)
        result = calculate_discount(150.0, 0)
        self.assertEqual(result, 150.0)

    def test_calculate_discount_invalid_price(self):
        # Kiểm tra ngoại lệ khi giá trị âm
        with self.assertRaises(ValueError):
            calculate_discount(-50.0, 10)

if __name__ == '__main__':
    unittest.main()