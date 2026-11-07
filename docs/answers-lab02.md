===================================================================
LAB 02: PROBLEM MODELING AND ENCAPSULATION - ANSWERS
Course: IT3180 / Object-Oriented Programming (AIMS Project)
===================================================================

1. QUESTION 1: PURPOSE OF ENCAPSULATION (TÍNH ĐÓNG GÓI)
-------------------------------------------------------------------
Q: Tại sao cần áp dụng Encapsulation (Tính đóng gói) cho các lớp như DigitalVideoDisc và Cart?
A:
- Đảm bảo an toàn dữ liệu (Data Hiding / Information Hiding): Ngăn chặn việc truy cập hoặc sửa đổi trực tiếp các thuộc tính của đối tượng từ bên ngoài (ví dụ: giấu mảng các đĩa DVD trong lớp Cart hoặc các thông tin gia của DVD).
- Kiểm soát quyền truy cập và hợp lệ hóa dữ liệu: Cho phép thông qua các hàm Getters/Setters hoặc các phương thức nghiệp vụ để kiểm tra dữ liệu trước khi thay đổi (ví dụ: không cho phép thêm quá 20 đĩa DVD vào Cart, không đặt giá trị cost bị âm).
- Dễ dàng bảo trì và mở rộng code: Khi cấu trúc dữ liệu bên trong lớp thay đổi (ví dụ: chuyển từ mảng cố định sang ArrayList), mã nguồn của các lớp bên ngoài (như Aims) không bị ảnh hưởng.

2. QUESTION 2: ACCESSORS & MUTATORS (GETTERS & SETTERS)
-------------------------------------------------------------------
Q: Có nên tạo Setter/Mutator cho tất cả các thuộc tính không? Vì sao?
A: 
- Không nên tạo Setter cho tất cả các thuộc tính.
- Lý do: Một số thuộc tính phụ thuộc vào quy trình nghiệp vụ (Business Rules). Ví dụ:
  + Đối với Cart: Danh sách đĩa DVD không nên sửa trực tiếp qua hàm setCart(), mà phải thay đổi thông qua các hành vi nghiệp vụ như addDigitalVideoDisc() và removeDigitalVideoDisc() để kiểm tra giới hạn 20 đĩa.
  + Đối với ID hoặc các thông tin định danh: Thường chỉ đọc (Read-only) sau khi khởi tạo qua Constructor, không nên cho phép sửa đổi qua Setter.

3. QUESTION 3: CLASS DESIGN & BEHAVIORS (THIẾT KẾ CART & DVD)
-------------------------------------------------------------------
Q: Giải thích vai trò của 3 lớp chính trong gói AIMS Mini Project:
A:
- DigitalVideoDisc: Đại diện cho thực thể đĩa DVD. Lưu trữ các thuộc tính dữ liệu (title, category, director, length, cost) và cung cấp các hàm lấy thông tin (Getters).
- Cart: Đại diện cho giỏ hàng của người dùng. Quản lý mảng/danh sách các đĩa DVD, thực hiện các thao tác thêm đĩa (addDigitalVideoDisc), xóa đĩa (removeDigitalVideoDisc) và tính tổng tiền (totalCost).
- Aims: Chứa hàm main() - giao diện dòng lệnh (CLI) là điểm khởi chạy hệ thống, tạo các đối tượng DVD, Cart và giả lập các thao tác của người dùng.

4. QUESTION 4: CART CAPACITY LIMIT (GIỚI HẠN GIỎ HÀNG)
-------------------------------------------------------------------
Q: Làm thế nào để đảm bảo lớp Cart không nhận quá 20 đĩa DVD?
A:
- Trong phương thức addDigitalVideoDisc(DigitalVideoDisc disc), kiểm tra số lượng đĩa hiện tại (qtyOrdered):
  + Nếu qtyOrdered < MAX_NUMBERS_ORDERED (20): Thêm đĩa vào mảng, tăng qtyOrdered thêm 1 và in thông báo "The disc has been added".
  + Nếu qtyOrdered >= 20: Không thêm đĩa và in ra thông báo lỗi "The cart is almost full".