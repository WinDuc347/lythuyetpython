# Python Thinking – Tóm tắt Session 4

Session 4 có 4 bài tập. Chủ đề chính là **hàm (function)**: định nghĩa hàm bằng `def`, truyền tham số, trả giá trị bằng `return`, và kết hợp hàm với `if / elif / else`. Bài 4.3 và 4.4 có sẵn code test tự chấm điểm.

## 1. Exercise 4.1 – Đổi nhiệt độ và báo trạng thái nước
[Exercise 4.1](../Session%204/Exercise%204.1.py)

| Hàm | Việc nó làm |
|---|---|
| `F_to_C(temp)` | Đổi độ F sang độ C theo công thức `(temp - 32) / 1.8` và **trả về** kết quả. |
| `alert_user(temp)` | Không trả về gì, chỉ **in** thông báo theo nhiệt độ (°C). |

Các nhánh của `alert_user`:
- trên 100 °C: `"Water is boiling."`
- từ 85 đến 90 °C: `"Ready to make tea."`
- từ 40 đến 45 °C: `"Perfect for a foot bath."`
- còn lại: in nhiệt độ đã làm tròn bằng `int(temp + 0.5)`

Với `temp = 100` (°F), nhiệt độ đổi ra là khoảng 37,8 °C, nên chương trình in:
```
The water is currently  38 °C.
```

Vài điểm cần để ý:
- Bài này cho thấy hai kiểu hàm: hàm **trả về giá trị** (`F_to_C`) và hàm **chỉ in ra màn hình** (`alert_user`).
- Điều kiện là `temp > 100`, nên đúng 100 °C sẽ không được tính là "boiling".
- `int(temp + 0.5)` chỉ làm tròn đúng với số dương. Với số âm nên dùng `round()`.

## 2. Exercise 4.2 – Thưởng theo điểm trung bình
[Exercise 4.2](../Session%204/Exercise%204.2.py)

| Hàm | Việc nó làm |
|---|---|
| `average(s1..s5)` | Tính trung bình 5 điểm. |
| `has_zero(s1..s5)` | Trả `True` nếu có ít nhất một điểm bằng 0 (dùng `or`). |
| `reward_class(avg, has_zero)` | In mức thưởng. |

Cách chia mức thưởng:
- có điểm 0 **hoặc** trung bình < 12: `"No reward."`
- từ 12 đến dưới 16: `"Free coupons."`
- từ 16 đến dưới 20: `"Free meal."`
- đúng 20: `"We will contact the exam ombuds..."` (điểm tuyệt đối thì "đáng ngờ")

Cả 5 điểm đều là 20 nên chương trình in câu "ombuds".

Vài điểm cần để ý:
- **Lỗi tiềm ẩn (shadowing):** dòng `average = average(...)` và `has_zero = has_zero(...)` ghi đè tên hàm bằng kết quả. Nếu gọi `average(...)` thêm một lần nữa sẽ bị `TypeError: 'float' object is not callable`. Nên đặt tên biến khác, ví dụ `avg = average(...)`.
- Ở nhánh `else`, đã chắc chắn `avg >= 12` rồi, nên viết lại `avg >= 12 and` là thừa.
- Có thể rút gọn `has_zero` thành một dòng: `return s1 == 0 or s2 == 0 or ...`.

## 3. Exercise 4.3 – Tính chi phí sinh viên (có test, đạt 17/17)
[Exercise 4.3](../Session%204/Exercise%204.3.py)

| Hàm | Quy tắc |
|---|---|
| `supermarket(weekday, bought_alcohol)` | Thứ Hai tiêu 40, ngày khác tiêu 10. Có mua rượu thì **nhân đôi**. |
| `buy_textbooks(willingness_to_pay, accokaart)` | Mức 0: 0, mức 1: 200, mức 2: 400, mức 3: 700. Có thẻ ACCO (mức 2 và 3) thì giảm 10% nhưng phải trả thêm 30 tiền thẻ: 390 và 660. |
| `calc_fine(alcohol_level)` | Dưới 0,005: 0. Từ 0,005 đến 0,008: 50. Trên 0,008 đến 0,015: `(100000·x − 450) / 7`, tức tăng tuyến tính từ 50 lên 150. Trên 0,015: 250. |

Chương trình chính: `80 + 700 + 250 = 1030`, đúng với test 4.

Vài điểm cần để ý:
- `if` lồng trong `elif` (bài sách).
- Biến `expenses` được gán trước rồi mới sửa (`expenses *= 2`), nên không phải viết 4 nhánh riêng.
- Kết quả tiền phạt là số thực (`float`). Test so sánh bằng `==` và vẫn qua (`150.0`, `100.0`), nhưng nhìn chung so sánh số thực bằng `==` rất dễ sai do sai số làm tròn.
- Dấu `;` ở `return 0;` không gây lỗi, nhưng Python không cần nó.

## 4. Exercise 4.4 – Trận đấu Pokémon (có test, đạt 20/20)
[Exercise 4.4](../Session%204/Exercise%204.4.py)

| Hàm | Quy tắc |
|---|---|
| `attack_is_valid(attack)` | Hợp lệ nếu `attack > 0`. |
| `defense_is_valid(attack, defense)` | Hợp lệ nếu `0 < defense <= attack`. |
| `calc_damage(attack, defense, is_critical)` | Sát thương = `attack − defense`, tối thiểu là 1 (khi `defense >= attack`). Đòn chí mạng thì nhân đôi. |
| `calc_hitpoints(damage, current_hitpoints)` | Trả về **chuỗi**: `"Target has fainted"` nếu HP ≤ 0, nếu không thì `"Target has X hitpoints left"` (dùng `str()` để ghép số vào chuỗi). |
| `heal(current, max)` | Nếu mất từ 10 HP trở lên thì hồi ngẫu nhiên `random.randint(1, 10)`, nếu không thì trả 0. |

Vài điểm cần để ý:
- Dùng `import random` để lấy số ngẫu nhiên.
- Có thể `return` sớm trong `if`, rồi `return False` ở cuối. Không cần `else`.
- Hàm có thể trả về nhiều kiểu: `bool`, `int`, `str`.
- Có thể rút gọn: `return attack > 0` thay cho cả khối `if`.

## Tổng kết
Session 4 dạy cách **chia chương trình thành nhiều hàm nhỏ**:
- `def` và tham số
- `return` khác `print` thế nào
- kết hợp hàm với `if / elif / else` lồng nhau
- toán tử logic `and / or`
- ghép chuỗi bằng `str()`
- module `random`
- đọc và làm cho code test tự chấm điểm chạy qua

Lưu ý quan trọng nhất: **đừng đặt tên biến trùng tên hàm** (như ở bài 4.2).

---

Cảm ơn chủ nhân
