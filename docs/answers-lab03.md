# Giải đáp Thảo luận Lab 03

1. **Merge base là gì?**
   - Merge base là commit chung gần nhất giữa hai nhánh (ví dụ: nhánh feature và nhánh master). Git dựa vào merge base để so sánh sự thay đổi của cả hai bên và tiến hành tự động gộp mã nguồn.

2. **Vì sao nhánh `master` và `release/*` bắt buộc phải dùng `git revert` thay vì `git reset` khi muốn hoàn tác?**
   - Vì `master` và `release/*` là các nhánh public đã chia sẻ cho nhiều người dùng. `git reset` làm viết lại lịch sử commit (dời con trỏ), gây ra đứt gãy lịch sử cho những người làm chung. Trong khi đó, `git revert` tạo một commit mới đảo ngược thay đổi, giúp giữ nguyên lịch sử commit an toàn cho cả nhóm