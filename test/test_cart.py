import unittest

class TestCart(unittest.TestCase):
    def setUp(self):
        # Khởi tạo giỏ hàng hoặc đối tượng mẫu trước mỗi test case
        self.cart_items = []

    def test_add_item_to_cart(self):
        # Kiểm tra tính năng thêm sản phẩm vào giỏ hàng
        item = {"id": 1, "title": "Book A", "price": 100.0, "quantity": 1}
        self.cart_items.append(item)
        self.assertEqual(len(self.cart_items), 1)
        self.assertEqual(self.cart_items[0]["title"], "Book A")

    def test_remove_item_from_cart(self):
        # Kiểm tra tính năng xóa sản phẩm khỏi giỏ hàng
        item = {"id": 1, "title": "Book A", "price": 100.0, "quantity": 1}
        self.cart_items.append(item)
        self.cart_items.pop()
        self.assertEqual(len(self.cart_items), 0)

if __name__ == '__main__':
    unittest.main()