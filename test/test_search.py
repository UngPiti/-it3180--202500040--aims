import unittest

def search_by_name(products, keyword):
    """Hàm tìm kiếm sản phẩm theo tên (không phân biệt hoa thường)"""
    return [p for p in products if keyword.lower() in p["title"].lower()]

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.products = [
            {"id": 1, "title": "Python Programming"},
            {"id": 2, "title": "Data Structures and Algorithms"},
            {"id": 3, "title": "Clean Code"}
        ]

    def test_search_exact_match(self):
        # Kiểm tra tìm kiếm khớp chính xác
        result = search_by_name(self.products, "Clean Code")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 3)

    def test_search_case_insensitive(self):
        # Kiểm tra tìm kiếm không phân biệt chữ hoa/thường
        result = search_by_name(self.products, "python")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Python Programming")

    def test_search_no_result(self):
        # Kiểm tra trường hợp không tìm thấy kết quả
        result = search_by_name(self.products, "Nonexistent")
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()