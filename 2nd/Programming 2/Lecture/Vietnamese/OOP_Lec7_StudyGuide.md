# Lec7: Tính kế thừa (Inheritance) (Khái niệm) — Hướng dẫn học tập

---

## 1. THẺ KHÁI NIỆM (CONCEPT CARD)

### 1.1 Định nghĩa

Tính kế thừa (Inheritance) là một cơ chế trong đó một lớp mới (lớp con / lớp dẫn xuất) tự động tiếp nhận toàn bộ dữ liệu và hành vi của một lớp hiện có (siêu lớp / lớp cơ sở), sau đó có thể thêm hoặc sửa đổi những gì cần thiết. Đây là một thuộc tính tự nhiên của sự phân loại (classification) — ý tưởng rằng một phạm trù này là sự tinh chỉnh của một phạm trù rộng hơn.

Trong Lập trình hướng đối tượng (OOP): nếu "A kế thừa từ B", các đối tượng (objects) của lớp A có quyền truy cập vào các thuộc tính (attributes) và phương thức (methods) của lớp B mà không cần định nghĩa lại chúng.

### 1.2 Vấn đề Nó Giải Quyết

- **Trùng lặp mã nguồn (Code duplication).** Không có tính kế thừa, nếu `Student` và `Professor` dùng chung 80% mã nguồn (tên, ID, địa chỉ, email), bạn phải sao chép mã đó trong cả hai lớp. Khi một lỗi được tìm thấy trong logic dùng chung, bạn phải sửa ở mọi vị trí. Quên sửa một chỗ gây ra sự sai lệch.
- **Tái sử dụng thiết kế có sẵn** giúp giảm chi phí phát triển và kiểm thử phần mềm.
- **Thiết kế mô-đun (Modular design).** Một lớp mới kế thừa dữ liệu và chức năng của một lớp hiện có, thúc đẩy một hệ thống phân cấp lớp có cấu trúc, phân tầng.
- **Cho phép tính đa hình (Polymorphism).** Một lớp cơ sở có thể định nghĩa một giao diện chung; các lớp dẫn xuất có thể được xử lý thống nhất thông qua con trỏ hoặc tham chiếu của lớp cơ sở.

### 1.3 Cách Hoạt Động

1. Xác định dữ liệu và hành vi chung giữa các khái niệm liên quan và đặt chúng trong một **lớp cơ sở** (base class / superclass).
2. Tạo các **lớp dẫn xuất** (derived classes / subclasses) kế thừa từ lớp cơ sở.
3. Lớp dẫn xuất tự động có tất cả các thành viên `public` và `protected` của lớp cơ sở.
4. Lớp dẫn xuất có thể thêm các thành viên **mới** mà chỉ nó cần.
5. Lớp dẫn xuất có thể **ghi đè** (override) các phương thức của lớp cơ sở để tùy chỉnh hành vi.
6. Một đối tượng dẫn xuất **có thể** được sử dụng ở bất kỳ đâu mà một đối tượng cơ sở được mong đợi — một `Student` LÀ (IS A) một `Person`. Đây là mối quan hệ "is-a".
7. Tính kế thừa hoạt động theo ba chiều: chia sẻ tĩnh (static) vs động (dynamic), chia sẻ ngầm (implicit) vs tường minh (explicit), chia sẻ theo từng đối tượng (per-object) vs theo từng nhóm (per-group).

### 1.4 Ví dụ Cụ Thể

Một hệ thống nhân sự đại học. `Person` là lớp cơ sở với `name`, `id`, `address` và `getContactInfo()`. `Administrator` kế thừa từ `Person` và thêm `department`, `clearanceLevel`. `Faculty` kế thừa từ `Person` và thêm `coursesTaught`, `officeHours`. `Student` kế thừa từ `Person` và thêm `major`, `gpa`, `coursesEnrolled`.

Hệ thống đăng ký lưu trữ một danh sách các con trỏ `Person*`. Nó gọi `getContactInfo()` trên mỗi đối tượng mà không cần biết kiểu cụ thể — tính kế thừa đảm bảo hàm tồn tại. Mỗi lớp dẫn xuất có thể ghi đè `getContactInfo()` để trả về thông tin theo vai trò cụ thể.

### 1.5 Nó KHÔNG Phải Là Gì

- **KHÔNG phải "sao chép mã nguồn."** Lớp con không nhận được một bản sao của lớp cơ sở. Nó thực sự **chia sẻ** định nghĩa của lớp cơ sở. Các thay đổi đối với lớp cơ sở sẽ lan truyền đến tất cả các lớp con.
- **KHÔNG phải là hợp thành (composition) ("has-a").** Tính kế thừa mô hình hóa "is-a" (`Car` LÀ MỘT `Vehicle`). Hợp thành mô hình hóa "has-a" (`Car` CÓ MỘT `Engine`). Đừng sử dụng kế thừa khi hợp thành hợp lý hơn.
- **KHÔNG phải lúc nào cũng là công cụ tái sử dụng mã nguồn.** Trong trường hợp các lớp trừu tượng (abstract classes), kế thừa là về việc định nghĩa một giao diện thiết kế chung — đôi khi không có bất kỳ mã thực thi nào. Đây là một cơ chế chia sẻ đặc tả (specification), không chỉ là cơ chế chia sẻ cài đặt (implementation).

---

## 2. BỔ SUNG CHO BÀI GIẢNG TRƯỚC (Ôn tập Lec6 từ Lec7)

### 2.1 Tự động Sinh Hàm tạo (Constructor Auto-Generation)

- Nếu bạn **không** định nghĩa **bất kỳ** hàm tạo nào, trình biên dịch **sinh ra** một hàm tạo mặc định (default constructor) khởi tạo các thành viên theo mặc định. Tương tự với hàm hủy (destructor): nếu bạn không viết, trình biên dịch sẽ sinh ra một hàm hủy không làm gì cả.
- Nếu bạn định nghĩa **bất kỳ** hàm tạo nào (ngay cả hàm tạo có tham số), trình biên dịch **không** sinh ra hàm tạo mặc định. Gọi `ClassName obj;` mà không có hàm tạo mặc định được viết tay sẽ trở thành lỗi biên dịch.
- Nguyên tắc tương tự áp dụng cho **hàm tạo sao chép** (copy constructor): nếu bạn không viết, trình biên dịch sinh ra một hàm tạo sao chép theo từng thành viên (shallow copy).

### 2.2 Bổ từ Truy cập (Access Modifiers) — Cấp Lớp vs Cấp Đối tượng

Các bổ từ truy cập (`private`, `protected`, `public`) hoạt động ở **cấp lớp** (class level), KHÔNG phải **cấp đối tượng** (object level).

Điều này có nghĩa là: hai đối tượng của **cùng một lớp** có thể truy cập các thành viên `private` và `protected` của nhau. Trình biên dịch kiểm tra quyền truy cập dựa trên **phạm vi lớp** (class scope), không phải trên từng thể hiện cụ thể.

**Ví dụ Date kèm giải thích đầy đủ:**

```cpp
class Date {
private:
    int month, day, year;
public:
    Date(int mo, int dy, int yr) {
        month = mo;
        day = dy;
        year = yr;
    }

    Date(Date & d) {
        month = d.month;   // ← Tại sao điều này OK? month là PRIVATE trong Date!
        day = d.day;       // ← Tương tự — truy cập thành viên private của d
        year = d.year;     // ← Tương tự
    }
};
```

**Giải thích:** Bổ từ `private` thực thi nguyên lý **Đóng gói** (Encapsulation). "Thế giới bên ngoài" không nên trực tiếp thao túng trạng thái nội bộ của một đối tượng `Date`, vì cài đặt nội bộ của `Date` có thể thay đổi theo thời gian (ví dụ: bạn có thể chuyển từ ba trường `int` sang một dấu thời gian `long` duy nhất).

Khi một thể hiện của `Date` truy cập nội bộ của **một** thể hiện `Date` **khác** — cả hai thể hiện luôn "biết" chi tiết cài đặt của `Date`. Cả hai đều được biên dịch dựa trên cùng một định nghĩa lớp `Date`. Nếu logic nội bộ của `Date` thay đổi, chỉ cần thay đổi mã của một lớp `Date` duy nhất — và mọi thứ bên trong nó được cập nhật đồng bộ.

Quyền truy cập theo cấp lớp này chính là điều làm cho các **hàm tạo sao chép**, **toán tử gán** (assignment operators), `operator==` và các hàm thành viên khác chấp nhận các đối tượng cùng kiểu có thể viết được mà không cần getter và setter cho mọi trường private.

**Sự kiện quan trọng cho kỳ thi:** Nếu bạn thấy `obj.privateField` bên trong một hàm thành viên của cùng lớp — nó là HỢP LỆ (LEGAL). Nếu bạn thấy nó bên ngoài (trong `main()`, trong một hàm không phải bạn (non-friend), trong một lớp khác không phải bạn) — đó là LỖI BIÊN DỊCH (COMPILE ERROR).

---

## 3. PHÂN LOẠI (CLASSIFICATION) VÀ CHIA SẺ (SHARING)

### 3.1 Phân loại

Phân loại (Classification) xuất phát từ nhu cầu phổ quát của con người để mô tả **tính đồng nhất** (uniformities) giữa các tập hợp thể hiện. Chúng ta nhóm các thứ tương tự vào các phạm trù, sau đó là các phạm trù con, tạo thành các hệ thống phân cấp. Phân loại là ý tưởng nền tảng để hiểu về tính kế thừa.

**Sơ đồ — Hệ thống phân cấp Phân loại vs Kế thừa:**

```
            Animal
          /        \
     Mammal         Bird
    /      \          \
People     Dog      Sparrow
 /    \      |
man  woman  Rex
 |      |
John   Mary
```

- **Phân loại:** Animal → Mammal → People → man → John. Mỗi mũi tên có nghĩa là "là một loại của." John là một thể hiện cụ thể (đối tượng) ở lá của cây phân loại.
- **Kế thừa:** Animal là lớp cơ sở. Mammal và Bird kế thừa từ Animal. People và Dog kế thừa từ Mammal. man và woman kế thừa từ People. John và Mary là các **đối tượng** (thể hiện), không phải lớp — chúng ở dưới cùng của cây nơi phân loại kết thúc và việc tạo thể hiện bắt đầu.

Sự khác biệt: phân loại đi tận cùng đến các thể hiện riêng lẻ. Kế thừa (trong OOP) dừng lại ở cấp lớp — các lớp kế thừa từ các lớp; các thể hiện được tạo ra từ các lớp.

### 3.2 Ba Khía cạnh của Phân loại / Kế thừa

Kế thừa phục vụ ba mục đích riêng biệt trong thiết kế hướng đối tượng:

1. **Tính chung (Commonality):** Lớp cơ sở nắm bắt **thông tin chung** (thuộc tính) và **đặc điểm chung** (thao tác) được chia sẻ bởi tất cả các lớp dẫn xuất. Ví dụ: `Person` nắm bắt `name` và `getContactInfo()` mà mọi `Student`, `Faculty` và `Administrator` đều chia sẻ.

2. **Tùy chỉnh (Customization):** Một lớp hiện có được sử dụng để tạo ra một **phiên bản tùy chỉnh** — một biến thể chuyên biệt hóa thêm hoặc sửa đổi hành vi. Ví dụ: `SalariedEmployee` tùy chỉnh `Employee::calculatePay()` để chia lương năm cho 12 thay vì tính lương theo giờ.

3. **Giao diện Thiết kế Chung (Common Design Interface):** Một lớp cơ sở có thể định nghĩa các **yêu cầu thiết kế** cho các lớp dẫn xuất bằng cách chỉ định các hàm thành viên mà mọi lớp dẫn xuất **PHẢI** cung cấp. Lớp cơ sở khai báo "cái gì"; các lớp dẫn xuất cung cấp "làm thế nào." Đây là bản chất của các lớp trừu tượng và trong C++, các hàm ảo thuần túy (pure virtual functions).

### 3.3 Chia sẻ (Sharing)

Chia sẻ phổ biến trong thế giới thực, và do đó cực kỳ quan trọng trong hướng đối tượng:
- Nhìn xung quanh: mọi người chia sẻ phương tiện di chuyển (xe buýt), nhà ở (chung cư), kiến thức (sách), cơ sở hạ tầng (đường xá).
- Trong OOP, **kế thừa là một kỹ thuật thúc đẩy chia sẻ**.

**Chia sẻ có nghĩa là gì trong kế thừa:**
- Kế thừa có nghĩa là **các lớp mới có thể được dẫn xuất từ các lớp hiện có**.
- Một **lớp con kế thừa** các thuộc tính và thao tác của một siêu lớp; nó cũng có thể định nghĩa thêm các thuộc tính và thao tác khác.
- Kế thừa có thể được xem như một cơ chế **chuyên biệt hóa** (specialization): các thể hiện của lớp con là các chuyên biệt hóa của các thể hiện siêu lớp (một `Square` là một `Rectangle` chuyên biệt hóa).
- Kế thừa có thể được xem như một cơ chế **tổng quát hóa** (generalization): một siêu lớp tổng quát hóa các thể hiện của lớp con (một `Vehicle` là sự tổng quát hóa của `Car`, `Truck`, `Motorcycle`).
- **Khả năng của một lớp chia sẻ hành vi của một lớp khác mà không cần định nghĩa lại một cách tường minh.**
- **Một cách tiếp cận cho phép các lớp được tạo ra dựa trên một lớp cũ.**

### 3.4 Ba Chiều của Chia sẻ

Chia sẻ thông qua kế thừa có thể được phân loại theo ba chiều độc lập:

| Chiều | Các lựa chọn | Ý nghĩa |
|-----------|---------|-------------|
| **Tĩnh (Static) vs Động (Dynamic)** | Tĩnh: cố định khi tạo đối tượng. Động: xác định khi đối tượng nhận thông điệp. | Trong chia sẻ tĩnh, hành vi mà một đối tượng kế thừa được cố định khi đối tượng được khởi tạo. Trong chia sẻ động (dựa trên ủy quyền), hành vi có thể thay đổi tại thời điểm chạy. |
| **Ngầm (Implicit) vs Tường minh (Explicit)** | Ngầm: hệ thống tự động thực hiện. Tường minh: lập trình viên chỉ đạo các mẫu. | Trong chia sẻ ngầm, ngôn ngữ/thời gian chạy xử lý việc chia sẻ (ví dụ: kế thừa C++ theo mặc định). Trong chia sẻ tường minh (ủy quyền), lập trình viên thủ công chuyển tiếp các lời gọi. |
| **Theo từng Đối tượng (Per Object) vs Theo từng Nhóm (Per Group)** | Theo đối tượng: hành vi gắn với một đối tượng duy nhất. Theo nhóm: hành vi được chỉ định cho toàn bộ lớp. | Hầu hết các ngôn ngữ OOP sử dụng kế thừa theo nhóm (cấp lớp). Các ngôn ngữ dựa trên nguyên mẫu sử dụng chia sẻ theo từng đối tượng. |

**Quan trọng:** Kế thừa trong C++ chủ yếu là **tĩnh, ngầm và theo nhóm**. Cấu trúc kế thừa của một lớp dẫn xuất được cố định tại thời điểm biên dịch, trình biên dịch tự động phân giải các thành viên được kế thừa và hành vi được định nghĩa cho toàn bộ lớp — không phải từng đối tượng riêng lẻ.

### 3.5 Mục đích của Kế thừa

1. **Tái sử dụng thiết kế hiện có** giúp giảm chi phí phát triển và kiểm thử phần mềm. Thay vì xây dựng một mô-đun tính lương từ đầu cho nhân viên theo giờ, nhân viên hưởng lương và nhân viên hợp đồng, bạn xây dựng một lớp cơ sở `Employee` và dẫn xuất các biến thể.

2. **Thiết kế Mô-đun:** Một lớp mới kế thừa dữ liệu và chức năng của một lớp hiện có, thúc đẩy:
   - Sự phân tách mối quan tâm rõ ràng hơn
   - Các đơn vị nhỏ hơn, dễ kiểm thử hơn
   - Bảo trì dễ dàng hơn — sửa lớp cơ sở, tất cả các lớp dẫn xuất đều được hưởng lợi

---

## 4. KẾ THỪA (INHERITANCE) LÀ GÌ?

### 4.1 Các Định nghĩa

Kế thừa có một số định nghĩa tương đương nhấn mạnh các khía cạnh khác nhau:

1. **Kế thừa là một cơ chế để diễn tả sự tương đồng.** Khi hai lớp chia sẻ cấu trúc hoặc hành vi, kế thừa khai báo một cách tường minh mối quan hệ đó trong mã nguồn thay vì sao chép nó.

2. **Kế thừa là một thuộc tính tự nhiên của sự phân loại.** Phân loại một cách tự nhiên bao hàm kế thừa — nếu `Dog` được phân loại dưới `Mammal`, thì mọi `Dog` vốn dĩ sở hữu các thuộc tính của `Mammal` (máu nóng, lông, đẻ con).

3. **Kế thừa là một cơ chế cho phép (một lớp) A kế thừa các thuộc tính của (một lớp) B.** Đây là định nghĩa trực tiếp, mang tính thao tác: bất cứ thứ gì B có, A đều nhận được (tuân theo các quy tắc truy cập).

### 4.2 Trong OOP

Nếu "A kế thừa từ B" (tương đương: A được dẫn xuất từ B):
- Các đối tượng của lớp A có quyền truy cập vào **tất cả** các thuộc tính và phương thức `public` và `protected` của lớp B **mà không cần định nghĩa lại chúng**.
- Lớp A có thể thêm các thuộc tính và phương thức **riêng** của nó.
- Lớp A có thể **ghi đè** các phương thức của B để cung cấp cài đặt riêng.
- Một đối tượng của lớp A **là** một đối tượng của lớp B — khả năng thay thế ở cấp độ kiểu.

---

## 5. SIÊU LỚP (SUPERCLASS) VÀ LỚP CON (SUBCLASS)

### 5.1 Định nghĩa

- Nếu lớp **A** kế thừa từ lớp **B**, thì:
  - **B** được gọi là **siêu lớp** (superclass / lớp cơ sở / lớp cha) của A.
  - **A** được gọi là **lớp con** (subclass / lớp dẫn xuất / lớp con) của B.
- Các đối tượng của một lớp con có thể được sử dụng ở **bất kỳ đâu** mà các đối tượng của siêu lớp tương ứng được mong đợi — đây được gọi là **nguyên lý khả năng thay thế** (substitutability principle): một đối tượng lớp con có cùng hành vi chữ ký như một đối tượng siêu lớp (và có thể có thêm).

### 5.2 Sơ đồ Ví dụ từ Bài giảng

```
                Person
              /   |    \
    Administrator Faculty Student
```

- `Person` là **siêu lớp**: nắm bắt `name`, `id`, `address`, `getInfo()`.
- `Administrator`, `Faculty`, `Student` là các **lớp con**: mỗi lớp kế thừa mọi thứ từ `Person` và thêm dữ liệu cũng như hành vi chuyên biệt hóa riêng.
- Một hàm mong đợi tham số `Person*` có thể chấp nhận `Student*`, `Faculty*` hoặc `Administrator*` — chương trình không cần biết kiểu dẫn xuất cụ thể.

### 5.3 Lớp con như Cơ chế Tái sử dụng

Lớp con đề cập đến **hai loại** tái sử dụng:

1. **Kế thừa đặc tả (Inheritance of specification):** Lớp con kế thừa **giao diện** — tập hợp các chữ ký phương thức public/protected mà siêu lớp khai báo. Đây là điều cho phép tính đa hình.

2. **Kế thừa cài đặt (Inheritance of implementation):** Lớp con kế thừa **mã nguồn thực tế** (thân phương thức) từ siêu lớp. Lớp con không cần phải cài đặt lại hành vi được kế thừa trừ khi nó muốn tùy chỉnh.

Sự kết hợp của cả hai làm cho các lớp con trở thành một cơ chế tái sử dụng mạnh mẽ: bạn nhận được hợp đồng thiết kế VÀ mã nguồn hoạt động mà không trùng lặp.

---

## 6. CÁC KHÍA CẠNH QUAN TRỌNG CỦA LỚP CON

### 6.1 Khả năng Sửa đổi (Modifiability)

**Mức độ khả năng sửa đổi** xác định cách các thuộc tính và phương thức được kế thừa từ một siêu lớp có thể được sửa đổi trong lớp con. Có hai loại sửa đổi:

1. **Sửa đổi trạng thái đối tượng** (thuộc tính / thành viên dữ liệu)
2. **Sửa đổi hành vi đối tượng** (thao tác / hàm thành viên)

Mỗi loại có các mức sửa đổi được cho phép riêng.

### 6.2 Thuộc tính — Bốn Mức Sửa đổi

| Mức | Tên | Mô tả |
|-------|------|-------------|
| 1 | **Không định nghĩa lại (No redefinition)** | Sửa đổi **không được phép** dưới bất kỳ hình thức nào. Thuộc tính được kế thừa bị niêm phong — lớp con không thể thay đổi kiểu, tầm nhìn, giá trị khởi tạo hoặc miền giá trị của nó. |
| 2 | **Định nghĩa lại tùy ý (Arbitrary redefinition)** | Được phép định nghĩa lại **không có ràng buộc**. Lớp con có thể thay đổi kiểu, mức truy cập, giá trị khởi tạo của thuộc tính — bất cứ thứ gì. |
| 3 | **Định nghĩa lại có ràng buộc (Constrained redefinition)** | **Miền giá trị** (domain) của thuộc tính bị ràng buộc. Lớp con có thể định nghĩa lại thuộc tính nhưng phải nằm trong giới hạn. Ví dụ: thuộc tính `numWheels` trong `Vehicle` có miền [0..∞); `Bicycle` ràng buộc nó thành [2..2]. |
| 4 | **Định nghĩa lại ẩn (Hidden redefinition)** | Các định nghĩa của thuộc tính bị **ẩn** trong lớp con để tránh xung đột tên. Lớp con có thể định nghĩa thuộc tính riêng với cùng tên và phiên bản được kế thừa bị che khuất. Phiên bản của lớp con là phiên bản hiển thị. |

**Lưu ý kỳ thi:** Trong C++ tiêu chuẩn, các thuộc tính trong một lớp dẫn xuất **ẩn** (che khuất) các thuộc tính cùng tên trong lớp cơ sở — điều này tương ứng với mức 4 (Định nghĩa lại ẩn). Mức 1 (không định nghĩa lại) là những gì từ khóa `final` thực hiện trong các ngôn ngữ khác.

### 6.3 Thao tác — Hai Loại Sửa đổi

1. **Định nghĩa lại tùy ý:** Tất cả các thay đổi đối với thao tác đều được phép — lớp con có thể viết lại hoàn toàn thân hàm, thay đổi kiểu tham số, thay đổi kiểu trả về — không có hạn chế. Đây là mô hình cho phép nhất.

2. **Định nghĩa lại có ràng buộc:** Các phần của chữ ký phương thức trong lớp con phải là **kiểu con** (subtypes) của các phần tương ứng trong phương thức siêu lớp. Cụ thể:
   - **Kiểu trả về** (Return type) phải là hiệp biến (covariant) — cùng kiểu hoặc một kiểu con.
   - **Kiểu tham số** (Parameter types) phải là đối biến (contravariant) — cùng kiểu hoặc một kiểu cha.
   - Ràng buộc này đảm bảo **an toàn kiểu** — một đối tượng lớp con được sử dụng thông qua tham chiếu siêu lớp vẫn phải hoạt động như mong đợi.

**Điều này cực kỳ quan trọng đối với việc ghi đè (overriding) và nạp chồng (overloading) phương thức.** Khi bạn ghi đè, bạn không thể tùy ý thay đổi mọi phần của chữ ký. Trong C++ cụ thể:
- Ghi đè yêu cầu khớp chữ ký hàm (tên + kiểu tham số + tính const).
- Kiểu trả về có thể là hiệp biến (con trỏ/tham chiếu đến kiểu dẫn xuất).
- Vi phạm định nghĩa lại có ràng buộc khiến phương thức trở thành một **nạp chồng mới** (new overload) thay vì ghi đè, điều này thay đổi hành vi đa hình.

### 6.4 Xung đột Tên (Naming Conflicts)

**Xung đột tên** xảy ra khi các thuộc tính hoặc phương thức được định nghĩa trong một lớp con có **cùng tên** với các thuộc tính hoặc phương thức trong siêu lớp.

- **Giữa siêu lớp và lớp con:** Nếu một lớp con định nghĩa một thành viên với cùng tên như một thành viên trong siêu lớp, phiên bản của lớp con thắng. Phiên bản được kế thừa bị **ẩn** (che khuất), không bị xóa.
- **Giải quyết:** Xung đột tên được giải quyết bằng cách **GHI ĐÈ** (OVERRIDING). Phiên bản của lớp con ghi đè phiên bản của siêu lớp.
- Để truy cập phiên bản siêu lớp bị ẩn, sử dụng **toán tử phân giải phạm vi** (scope resolution operator): `SuperclassName::memberName`.

**Ví dụ:**
```cpp
class Base {
public:
    void display() { cout << "Base display"; }
};

class Derived : public Base {
public:
    void display() { cout << "Derived display"; }  // overrides Base::display
    void test() {
        display();          // calls Derived::display
        Base::display();    // calls Base::display (explicit scope)
    }
};
```

---

## 7. CÁC LOẠI KẾ THỪA (CATEGORIES OF INHERITANCE)

### 7.1 Kế thừa Toàn phần / Một phần (Whole / Partial Inheritance)

| Loại | Định nghĩa |
|----------|------------|
| **Kế thừa Toàn phần (Whole Inheritance)** | Một lớp kế thừa **TẤT CẢ** các thuộc tính và thao tác từ siêu lớp của nó. Không có gì bị loại bỏ. |
| **Kế thừa Một phần (Partial Inheritance)** | Chỉ **MỘT SỐ** thuộc tính được kế thừa; các thuộc tính khác bị **loại bỏ** (bị loại trừ). Lớp con chọn lọc những gì để kế thừa. |

**Trong C++:** Kế thừa là **toàn phần** — một lớp dẫn xuất kế thừa mọi thứ (tuân theo các quy tắc truy cập: các thành viên private được kế thừa nhưng không thể truy cập trực tiếp). Kế thừa một phần là một **khái niệm lý thuyết** — không phải C++ tiêu chuẩn.

### 7.2 Kế thừa Mặc định / Nghiêm ngặt (Default / Strict Inheritance)

| Loại | Định nghĩa |
|----------|------------|
| **Kế thừa Mặc định (Default Inheritance)** | Các thuộc tính và ràng buộc được kế thừa **có thể được sửa đổi** bởi lớp con. Đây là trường hợp bình thường trong C++ — các lớp dẫn xuất có thể ghi đè phương thức, thay đổi mức truy cập, v.v. |
| **Kế thừa Nghiêm ngặt (Strict Inheritance)** | Kế thừa **không cho phép** người dùng sửa đổi các thuộc tính hoặc ràng buộc được kế thừa. Các thành viên được kế thừa bị đóng băng — không thể ghi đè hoặc định nghĩa lại. |

**Trong C++:** Mặc định, C++ sử dụng kế thừa mặc định (có thể ghi đè). C++11 giới thiệu từ khóa `final` để chọn kế thừa nghiêm ngặt: `class Derived final : public Base { };` ngăn chặn việc dẫn xuất thêm; `void foo() final { }` ngăn chặn việc ghi đè phương thức cụ thể đó.

### 7.3 Kế thừa Đơn (Single / Simple Inheritance)

Một lớp chỉ có thể kế thừa từ **MỘT** siêu lớp. Hệ thống phân cấp kế thừa tạo thành một **cây** — mỗi nút có tối đa một nút cha.

```
         A
       / | \
      B  C  D
     / \    |
    E   F   G
```

- Mỗi lớp có chính xác một siêu lớp trực tiếp (ngoại trừ gốc).
- Sạch sẽ, đơn giản, không có vấn đề mơ hồ.
- Được hỗ trợ bởi tất cả các ngôn ngữ OOP.
- Mặc định, C++ sử dụng kế thừa đơn.

### 7.4 Kế thừa Bội (Multiple Inheritance)

Một lớp có thể có **NHIỀU HƠN MỘT** siêu lớp. Hệ thống phân cấp kế thừa tạo thành một **đồ thị có hướng không chu trình** (directed acyclic graph - DAG) thay vì một cây.

```
      B1      B2      B3
      |       |       |
      +---+---+---+---+
              |
              A
```

**Sơ đồ từ bài giảng:** `B1`, `B2`, `B3` đều có `int x` và `getValue()`. Lớp `A` kế thừa từ cả ba.

**Vấn đề chính — Xung đột Tên (Naming Conflicts):** Nếu các thuộc tính hoặc phương thức được định nghĩa trong **một** siêu lớp có cùng tên với các thuộc tính hoặc phương thức trong **một** siêu lớp **khác**, thì lớp dẫn xuất kế thừa cái nào?

Ví dụ:
```cpp
class B1 { public: int x; int getValue(); };
class B2 { public: int x; int getValue(); };
class B3 { public: int x; int getValue(); };
class A : public B1, public B2, public B3 { };
```

Khi `A` tham chiếu `x` hoặc gọi `getValue()`, trình biên dịch gặp phải **sự mơ hồ** (ambiguity) — ba siêu lớp mỗi lớp đóng góp một ứng cử viên. Các phương pháp giải quyết được trình bày trong Phần 8.

**Ưu điểm:** Mô hình hóa mạnh mẽ — một `TeachingAssistant` LÀ MỘT `Student` VÀ LÀ MỘT `Employee`.
**Nhược điểm:** Sự mơ hồ, vấn đề kim cương (diamond problem), độ phức tạp tăng lên.

---

## 8. GIẢI QUYẾT XUNG ĐỘT (CONFLICT RESOLUTION) TRONG KẾ THỪA BỘI

Khi nhiều siêu lớp định nghĩa các thành viên có cùng tên, lớp dẫn xuất phải giải quyết xung đột.

### 8.1 Phương pháp 1: Sử dụng Thứ tự Siêu lớp

Nếu nhiều thuộc tính hoặc phương thức có cùng tên xuất hiện trong các siêu lớp khác nhau, các thuộc tính hoặc phương thức trong lớp **ĐẦU TIÊN** trong danh sách các siêu lớp sẽ được kế thừa.

**Được thực hiện BỞI TRÌNH BIÊN DỊCH** — tự động, không cần can thiệp của lập trình viên.

**Ví dụ:** Nếu thứ tự kế thừa là `class A : public B1, public B2, public B3`:
- `x` → nghĩa là `x` của `B1` (đầu tiên trong danh sách)
- `getValue()` → nghĩa là `getValue()` của `B1` (đầu tiên trong danh sách)
- Đây là quy tắc **ưu tiên từ trái sang phải**.

**Ưu điểm:** Không cần nỗ lực từ lập trình viên, trình biên dịch xử lý nó.
**Nhược điểm:** Tinh vi — thay đổi thứ tự của các lớp cơ sở sẽ thay đổi hành vi. Lập trình viên phải nhớ thứ tự. Không phải tất cả trình biên dịch C++ đều cài đặt điều này (tiêu chuẩn C++ không định nghĩa đây là cách giải quyết mặc định — trong C++ tiêu chuẩn, sự mơ hồ vẫn tồn tại cho đến khi được giải quyết một cách tường minh).

### 8.2 Phương pháp 2: Xác định bởi Người dùng

Người dùng có thể kế thừa các thuộc tính hoặc phương thức xung đột nhưng phải **ĐẶT TÊN LẠI MỘT CÁCH TƯỜNG MINH** (EXPLICITLY RENAME) trong lớp con bằng cách sử dụng toán tử phân giải phạm vi.

**Được thực hiện BỞI NGƯỜI DÙNG** — lập trình viên chọn một cách tường minh phiên bản của lớp cơ sở nào để sử dụng.

**Cú pháp:**
```cpp
class A : public B1, public B2, public B3 {
public:
    // Tường minh chọn phiên bản nào để kế thừa:
    using B1::x;             // x đến từ B1
    using B2::getValue();    // getValue() đến từ B2, v.v.
};

// HOẶC, trong mã nguồn:
void someFunction() {
    B1::x = 10;              // B1's x
    B2::x = 20;              // B2's x
    int v = B3::getValue();  // B3's getValue()
}
```

**Trong C++:** C++ tiêu chuẩn sử dụng phương pháp 2 — người dùng giải quyết sự mơ hồ với phân giải phạm vi (`BaseClass::member`). Chỉ đơn giản truy cập `x` hoặc `getValue()` mà không định rõ là **lỗi biên dịch** (tham chiếu mơ hồ). Phương pháp 1 (trình biên dịch chọn cái đầu tiên trong danh sách) KHÔNG phải cách C++ tiêu chuẩn giải quyết xung đột kế thừa bội.

---

## 9. LỚP TRỪU TƯỢNG (ABSTRACT CLASS)

### 9.1 Định nghĩa

Một **lớp trừu tượng** (abstract class) là một lớp **KHÔNG CÓ BẤT KỲ THỂ HIỆN NÀO** (WITHOUT ANY INSTANCE). Bạn không thể tạo đối tượng của một lớp trừu tượng. Nó tồn tại thuần túy để phân loại và làm cơ sở cho kế thừa.

**Ví dụ:** `Mammal` là một lớp trừu tượng. Bạn không bao giờ tạo một đối tượng "động vật có vú" chung chung — bạn tạo một `Dog`, một `Cat`, một `Human`. Mammal chỉ tồn tại để nắm bắt các đặc điểm chung (máu nóng, lông, đẻ con, tuyến vú) và phục vụ như một siêu lớp cho các loài cụ thể.

Cũng có thể có một sự phân loại **mà không có bất kỳ mã nguồn (có thể thực thi) nào đằng sau nó** — lớp trừu tượng có thể chỉ định nghĩa giao diện (các khai báo thuần túy) với không có cài đặt nào.

### 9.2 Định nghĩa Chính thức

Lớp A được gọi là **lớp trừu tượng** nếu:
1. Nó **chỉ được sử dụng NHƯ một siêu lớp** cho các lớp khác.
2. Lớp A chỉ **xác định các THUỘC TÍNH** — nó không bao giờ được sử dụng để tạo đối tượng trực tiếp.
3. **Các lớp dẫn xuất PHẢI định nghĩa** các thuộc tính (cài đặt giao diện) của A.

Trong C++, một lớp trừu tượng được cài đặt với các **hàm ảo thuần túy** (pure virtual functions): `virtual void func() = 0;`. Điều này buộc mọi lớp dẫn xuất cụ thể phải cung cấp cài đặt riêng của nó. Cố gắng khởi tạo một lớp trừu tượng là lỗi biên dịch.

### 9.3 Tái sử dụng

Nhiều người coi kế thừa như một **công cụ tái sử dụng mã nguồn** — kế thừa các cài đặt hiện có để tránh viết lại.

Trong bối cảnh các lớp trừu tượng, kế thừa phục vụ như một **công cụ tái sử dụng mã nguồn** theo một nghĩa khác:
- Lớp trừu tượng cung cấp một **hợp đồng thiết kế** — một kiến trúc có thể tái sử dụng.
- Các lớp dẫn xuất cung cấp các **cài đặt** phù hợp với hợp đồng.
- Mã nguồn ở cấp lớp trừu tượng (ví dụ: các thuật toán gọi các hàm ảo) được tái sử dụng trên tất cả các lớp dẫn xuất mà không cần sửa đổi.

Ví dụ: Một lớp trừu tượng `Shape` định nghĩa một `draw()` ảo thuần túy. Một engine kết xuất lặp qua các con trỏ `Shape*` và gọi `draw()` trên mỗi đối tượng. Mã nguồn của engine kết xuất được viết một lần và tái sử dụng cho mọi kiểu hình — `Circle`, `Rectangle`, `Triangle` — mà không cần thay đổi.

---

## 10. KẾ THỪA (INHERITANCE) vs PHÂN LOẠI (CLASSIFICATION)

Hai khái niệm này có liên quan chặt chẽ nhưng không đồng nhất:

| Khía cạnh | Phân loại (Classification) | Kế thừa (Inheritance) |
|--------|---------------|-------------|
| **Hướng** | Nhóm từ trên xuống thành các phạm trù | Từ dưới lên: các lớp dẫn xuất kế thừa từ lớp cơ sở |
| **Phạm vi** | Đi tận cùng đến các thể hiện riêng lẻ (John LÀ MỘT man) | Dừng lại ở cấp lớp (hệ thống phân cấp lớp) |
| **Mối quan hệ** | "là một loại của" | "dẫn xuất từ / kế thừa từ" |
| **Cấp thực thể** | Có thể mô tả mối quan hệ giữa các lớp VÀ các thể hiện | Chỉ mô tả mối quan hệ giữa các lớp |

**Hiểu biết chính từ bài giảng:**
- **Phân loại bao hàm kế thừa** — cụ thể là kế thừa **toàn phần** và **đơn**. Khi bạn phân loại sinh vật, các loài kế thừa tất cả các thuộc tính của chi (toàn phần), và mỗi loài có chính xác một chi (đơn).
- **Kế thừa có thể ảnh hưởng đến sự rõ ràng của phân loại** — cụ thể khi **kế thừa bội** và **kế thừa một phần** được sử dụng. Một lớp kế thừa từ ba lớp cơ sở không liên quan làm mờ hệ thống phân cấp phân loại sạch sẽ. Kế thừa một phần (chọn lọc loại bỏ các thành viên) phá vỡ giả định rằng một lớp con có mọi thứ mà siêu lớp của nó có.

---

## 11. KHAI BÁO LỚP DẪN XUẤT (Xem trước Cú pháp)

```cpp
class derived_class_name : access_specifier base_class_name {
    // các thành viên bổ sung...
};
```

**Các thành phần:**
- `derived_class_name`: tên của lớp mới (lớp con)
- `access_specifier`: `public`, `protected` hoặc `private` — xác định cách các thành viên của lớp cơ sở được hiển thị trong lớp dẫn xuất (chi tiết đầy đủ trong Lec8)
- `base_class_name`: lớp hiện có đang được kế thừa

**Ví dụ:**
```cpp
class Student : public Person { /* ... */ };          // kế thừa public
class Faculty : protected Person { /* ... */ };        // kế thừa protected
class Administrator : private Person { /* ... */ };    // kế thừa private
```

**Lưu ý:** Đây là xem trước cú pháp. Sự khác biệt về ngữ nghĩa giữa kế thừa `public`, `protected` và `private` được trình bày chi tiết trong Lec8 (Kế thừa trong C++).

---

## 12. CÁC MẪU CÚ PHÁP PHẢI GHI NHỚ (MUST-MEMORIZE SYNTAX TEMPLATES)

### Mẫu 1: Khai báo Lớp Cơ sở
```cpp
class BaseClassName {
protected:                          // có thể truy cập bởi các lớp dẫn xuất, KHÔNG phải bên ngoài
    int sharedData;
public:
    BaseClassName();                // hàm tạo mặc định
    BaseClassName(int d);           // hàm tạo có tham số
    void commonMethod();            // được kế thừa nguyên vẹn bởi lớp dẫn xuất
    virtual void customizable();    // được thiết kế để ghi đè
};
```

### Mẫu 2: Khai báo Lớp Dẫn xuất (Kế thừa Đơn)
```cpp
class DerivedClassName : public BaseClassName {
private:
    int extraData;                  // trạng thái bổ sung
public:
    DerivedClassName();             // hàm tạo mặc định
    DerivedClassName(int baseData, int extraData);  // phải khởi tạo lớp cơ sở
    void customizable() override;   // GHI ĐÈ phiên bản cơ sở
    void extraMethod();             // hành vi mới không có trong lớp cơ sở
};
```

### Mẫu 3: Khai báo Kế thừa Bội
```cpp
class Derived : public Base1, public Base2, public Base3 {
public:
    // Giải quyết xung đột tên một cách tường minh:
    void setup() {
        Base1::x = 5;               // phân biệt: sử dụng x của Base1
        Base2::x = 10;              // phân biệt: sử dụng x của Base2
        Base1::getValue();          // phân biệt: gọi phiên bản của Base1
    }
};
```

### Mẫu 4: Lớp Trừu tượng (Khái niệm)
```cpp
class AbstractBase {
public:
    virtual void mustImplement() = 0;   // ảo thuần túy → làm cho lớp trở nên trừu tượng
    virtual ~AbstractBase() { }         // hàm hủy ảo để xóa an toàn
    // AbstractBase obj;                // LỖI — không thể khởi tạo
};
```

### Mẫu 5: Giải quyết Xung đột bởi Người dùng (Kế thừa Bội)
```cpp
class A : public B1, public B2, public B3 {
public:
    void resolve() {
        B1::x = value;            // tường minh sử dụng phiên bản của B1
        int v = B2::getValue();   // tường minh sử dụng phiên bản của B2
    }
};
```

---

## 13. BẪY KỲ THI (EXAM TRAPS)

### Bẫy 1 — Truy cập Theo Lớp, Không Phải Theo Đối tượng (Ôn tập Lec6)
Hai đối tượng của cùng một lớp có thể truy cập các thành viên `private` của nhau. Đây là lý do tại sao `Date(Date& d) { month = d.month; }` biên dịch được. Kiểm soát truy cập được kiểm tra tại ranh giới lớp, không phải ranh giới thể hiện.

### Bẫy 2 — Lớp Dẫn xuất KHÔNG Kế thừa Hàm tạo, Hàm hủy, Hàm tạo Sao chép hoặc Toán tử Gán
Các hàm thành viên đặc biệt này phải được định nghĩa (hoặc do trình biên dịch sinh ra) cho chính lớp dẫn xuất. Hàm tạo dẫn xuất phải **gọi** hàm tạo cơ sở (tường minh hoặc ngầm). Một lớp dẫn xuất KHÔNG tự động nhận được một bản sao của hàm tạo cơ sở.

### Bẫy 3 — Các Thành viên Private của Lớp Cơ sở Không thể Truy cập trong Lớp Dẫn xuất
Các thành viên `private` của lớp cơ sở được kế thừa (chúng tồn tại trong bộ nhớ của đối tượng dẫn xuất) nhưng **không thể truy cập trực tiếp** trong lớp dẫn xuất. Sử dụng `protected` nếu các lớp dẫn xuất cần truy cập. Truy cập thông qua getter/setter từ lớp cơ sở là cách duy nhất để tiếp cận các thành viên private.

### Bẫy 4 — Xung đột Tên được Giải quyết bằng Ghi đè, Không Phải Nạp chồng
Nếu cả lớp cơ sở và lớp dẫn xuất đều định nghĩa `void display()`, phiên bản dẫn xuất **ẩn** (che khuất) phiên bản cơ sở. Phiên bản cơ sở không tham gia vào quá trình phân giải nạp chồng trong lớp dẫn xuất. Truy cập phiên bản cơ sở bị ẩn bằng `BaseClassName::display()`. Cả hai phiên bản đều tồn tại — phiên bản của lớp dẫn xuất chỉ thắng theo các quy tắc tra cứu tên.

### Bẫy 5 — "Is-a" vs "Has-a"
- Kế thừa mô hình hóa **"is-a"**: một `Car` LÀ MỘT `Vehicle`.
- Hợp thành mô hình hóa **"has-a"**: một `Car` CÓ MỘT `Wheel`. (Các đối tượng thành viên)
Đừng sử dụng kế thừa khi hợp thành là mối quan hệ đúng đắn. Đây là một lỗi thiết kế phổ biến dẫn đến các hệ thống phân cấp mong manh.

### Bẫy 6 — Lớp Trừu tượng Không thể được Khởi tạo
Một lớp trừu tượng chỉ tồn tại như một lớp cơ sở. Bạn CÓ THỂ viết `AbstractBase* ptr;` (con trỏ thì ổn) nhưng KHÔNG THỂ viết `AbstractBase obj;` (một đối tượng là lỗi biên dịch). Các lớp trừu tượng dành cho việc phân loại và định nghĩa giao diện, không phải tạo đối tượng.

### Bẫy 7 — Lớp Trừu tượng ≠ Lớp với Hàm tạo Protected
Một lớp trừu tượng là một khái niệm thiết kế — "một lớp không có thể hiện, chỉ được sử dụng như một lớp cơ sở." Bài giảng trình bày điều này về mặt **khái niệm**. Trong C++, tính trừu tượng được cài đặt với các hàm ảo thuần túy (`= 0`), không phải với các thủ thuật kiểm soát truy cập. Một lớp có hàm tạo `protected` có thể ngăn chặn việc khởi tạo trực tiếp, nhưng đó là một cơ chế khác — đừng nhầm lẫn hai cái.

### Bẫy 8 — Xung đột Tên trong Kế thừa Bội
Khi hai (hoặc nhiều) lớp cơ sở mỗi lớp có một thành viên với cùng tên (`int x`), lớp dẫn xuất phải giải quyết sự mơ hồ. Trình biên dịch KHÔNG tự động chọn một cái. Sử dụng phân giải phạm vi: `Base1::x` để chỉ định cái nào. Truy cập không định rõ là lỗi biên dịch.

### Bẫy 9 — Kế thừa Mặc định vs Nghiêm ngặt Là Sự Phân biệt Khái niệm
Trong C++, kế thừa mặc định (có thể ghi đè) là chuẩn mực. Kế thừa nghiêm ngặt (đóng băng/không thể thay đổi) đạt được với `final` trong C++11 trở đi. Bài giảng trình bày cả hai như các loại khái niệm — đừng cho rằng kế thừa nghiêm ngặt là một tính năng có sẵn của mọi ngôn ngữ.

### Bẫy 10 — Kế thừa Toàn phần vs Một phần
C++ sử dụng kế thừa **toàn phần** — một lớp dẫn xuất kế thừa mọi thứ từ lớp cơ sở (tuân theo các quy tắc truy cập). Kế thừa một phần (chọn lọc loại bỏ các thành viên riêng lẻ) là một khái niệm lý thuyết được thảo luận cho đầy đủ. Trong các kỳ thi, nếu được hỏi "C++ có hỗ trợ kế thừa một phần không?", câu trả lời là không.

### Bẫy 11 — Ghi đè Không Phải Là Thay thế
Khi một lớp dẫn xuất ghi đè một phương thức cơ sở, phương thức cơ sở **vẫn tồn tại**. Nó bị ẩn khỏi phạm vi tên của lớp dẫn xuất nhưng có thể truy cập thông qua `Base::method()`. Cả hai cài đặt cùng tồn tại trong bảng ảo (vtable) / bố cục lớp.

### Bẫy 12 — Giải quyết Xung đột bởi Thứ tự Trình biên dịch vs Người dùng
Phương pháp 1 (trình biên dịch giải quyết theo thứ tự) là một cách tiếp cận khái niệm được thảo luận trong bài giảng nhưng KHÔNG phải cách C++ tiêu chuẩn xử lý xung đột kế thừa bội. Trong C++ tiêu chuẩn, người dùng PHẢI giải quyết một cách tường minh với phân giải phạm vi (Phương pháp 2). Đừng nhầm lẫn lựa chọn lý thuyết với hành vi tiêu chuẩn C++.

### Bẫy 13 — Hệ quả của Nguyên lý Khả năng Thay thế
Một `Derived*` có thể được gán cho một `Base*` (ép kiểu lên — luôn an toàn). Nhưng chiều ngược lại (ép kiểu xuống từ `Base*` thành `Derived*`) KHÔNG tự động an toàn — con trỏ cơ sở có thể thực sự trỏ đến một lớp dẫn xuất khác. Trong C++, điều này yêu cầu `dynamic_cast`.

### Bẫy 14 — Cây Phân loại ≠ Hệ thống Phân cấp Kế thừa
Phân loại có thể mô tả cả mối quan hệ lớp-với-lớp VÀ lớp-với-thể hiện. Kế thừa chỉ mô tả mối quan hệ lớp-với-lớp. Đừng viết `class John : public Person` trong một kỳ thi — John là một thể hiện, không phải một lớp.

---

## 14. BÀI TẬP VIẾT TAY (HAND-CODING DRILLS)

### Bài tập 1: Xác định Hệ thống Phân cấp Kế thừa

**Tình huống:** "Một ứng dụng chia sẻ xe có `Driver` (với `licensePlate`, `rating`) và `Rider` (với `paymentMethod`, `homeAddress`). Cả hai đều có `name`, `phoneNumber` và `profilePhoto`."

Xác định lớp cơ sở và các lớp dẫn xuất. Những thuộc tính nào nằm ở mỗi lớp?

> [!success]- Hiển thị Đáp án
> **Lớp cơ sở:** `User`
> - `name`, `phoneNumber`, `profilePhoto`
>
> **Lớp dẫn xuất:** `Driver`
> - Kế thừa tất cả của `User`
> - Thêm: `licensePlate`, `rating`
>
> **Lớp dẫn xuất:** `Rider`
> - Kế thừa tất cả của `User`
> - Thêm: `paymentMethod`, `homeAddress`

---

### Bài tập 2: Bổ từ Truy cập — Cấp Lớp vs Cấp Đối tượng

```cpp
class BankAccount {
private:
    double balance;
    int accountNumber;
public:
    BankAccount(double bal, int accNum) {
        balance = bal;
        accountNumber = accNum;
    }
    BankAccount(const BankAccount& other) {
        balance = other.balance;          // Dòng (A) có hợp lệ không?
        accountNumber = other.accountNumber; // Dòng (B) có hợp lệ không?
    }
    bool isRicherThan(const BankAccount& other) {
        return balance > other.balance;   // Dòng (C) có hợp lệ không?
    }
};
```

Giải thích tại sao các dòng (A), (B) và (C) biên dịch hoặc không biên dịch.

> [!success]- Hiển thị Đáp án
> **Dòng (A):** HỢP LỆ. Hàm tạo sao chép là một thành viên của `BankAccount`, vì vậy nó có thể truy cập `other.balance` mặc dù `balance` là `private`. Kiểm soát truy cập là theo lớp — hai đối tượng `BankAccount` có thể thấy các thành viên private của nhau.
>
> **Dòng (B):** HỢP LỆ. Lý luận tương tự như (A). `other.accountNumber` là `private` nhưng được truy cập từ bên trong hàm thành viên của `BankAccount`.
>
> **Dòng (C):** HỢP LỆ. `isRicherThan` là một thành viên của `BankAccount`. Nó có thể truy cập `other.balance` — `other` là cùng lớp.
>
> **Hiểu biết chính:** Nếu `main()` cố gắng `cout << acc1.balance;`, điều đó sẽ là BẤT HỢP LỆ vì `main()` nằm ngoài lớp. Nhưng bên trong bất kỳ hàm thành viên nào của `BankAccount`, truy cập các thành viên private của một `BankAccount` khác hoàn toàn ổn.

---

### Bài tập 3: Giải quyết Xung đột Tên (Ghi đè + Phân giải Phạm vi)

```cpp
class Logger {
public:
    void log(const char* msg) {
        cout << "[LOG] " << msg << endl;
    }
};

class TimestampLogger : public Logger {
public:
    void log(const char* msg) {
        // (a) In thời gian hiện tại, sau đó ủy quyền cho log của lớp cơ sở
        // (b) In thông báo HAI LẦN chỉ sử dụng log của lớp cơ sở
    }
};
```

Cài đặt thân hàm `log()` để thỏa mãn (a) và (b).

> [!success]- Hiển thị Đáp án
> ```cpp
> void log(const char* msg) {
>     // (a) Thêm tiền tố tùy chỉnh + ủy quyền cho lớp cơ sở
>     cout << "[14:30:00] ";
>     Logger::log(msg);
>
>     // (b) In thông báo hai lần qua lớp cơ sở
>     // Logger::log(msg);
>     // Logger::log(msg);
> }
> ```
> Nếu không có `Logger::`, `log(msg)` sẽ đệ quy gọi chính `TimestampLogger::log()` dẫn xuất — đệ quy vô hạn và tràn stack. Toán tử phân giải phạm vi rất cần thiết để gọi phiên bản **cơ sở**.

---

### Bài tập 4: Sự Mơ hồ trong Kế thừa Bội

```cpp
class Bluetooth {
public:
    int version;
    void connect() { cout << "BT connect v" << version; }
};

class WiFi {
public:
    float version;
    void connect() { cout << "WiFi connect v" << version; }
};

class SmartSpeaker : public Bluetooth, public WiFi {
public:
    void setup() {
        // (1) Gán 5 cho version của Bluetooth
        // (2) Gán 2.4 cho version của WiFi
        // (3) Gọi connect() của Bluetooth
        // (4) Gọi connect() của WiFi
    }
};
```

Cài đặt `setup()` với sự phân biệt thích hợp.

> [!success]- Hiển thị Đáp án
> ```cpp
> void setup() {
>     Bluetooth::version = 5;       // (1) phạm vi tường minh
>     WiFi::version = 2.4f;         // (2) phạm vi tường minh
>     Bluetooth::connect();         // (3) phạm vi tường minh
>     WiFi::connect();              // (4) phạm vi tường minh
> }
> ```
> Nếu không có `Bluetooth::` và `WiFi::`, cả `version` và `connect()` đều **mơ hồ**. Trình biên dịch không thể đoán bạn muốn cái nào. Đây là **giải quyết xung đột bởi người dùng** (Phương pháp 2 từ bài giảng) — phân giải phạm vi tường minh.

---

### Bài tập 5: Kế thừa Bội — Giải quyết Dựa trên Thứ tự

Cho ba lớp cơ sở:
```cpp
class B1 {
public:
    int x;
    int getValue() { return x; }
};
class B2 {
public:
    int x;
    int getValue() { return x * 2; }
};
class B3 {
public:
    int x;
    int getValue() { return x * 3; }
};
```

Nếu một ngôn ngữ sử dụng **Phương pháp 1** (trình biên dịch giải quyết theo thứ tự, từ trái sang phải), `x` nào và `getValue()` nào mà `class A : public B3, public B1, public B2` kế thừa?

> [!success]- Hiển thị Đáp án
> Theo Phương pháp 1 (giải quyết dựa trên thứ tự, từ trái sang phải):
> - `x` → `x` của **B3** (đầu tiên trong danh sách kế thừa)
> - `getValue()` → `getValue()` của **B3** (đầu tiên trong danh sách kế thừa)
>
> Thứ tự là `B3`, `B1`, `B2` trong khai báo `class A : public B3, public B1, public B2`. B3 là đầu tiên → các thành viên của B3 thắng.
>
> **Nhắc nhở kỳ thi:** Phương pháp 1 là lý thuyết. Trong C++ tiêu chuẩn, đây sẽ là lỗi biên dịch — bạn phải sử dụng phân giải phạm vi (Phương pháp 2) để phân biệt.

---

### Bài tập 6: Mức Khả năng Sửa đổi — Xác định Loại

Ghép mỗi tình huống với mức sửa đổi đúng:

| Tình huống | Loại |
|----------|----------|
| Một lớp dẫn xuất định nghĩa `int speed` mặc dù lớp cơ sở đã có `int speed` | ? |
| Lớp cơ sở `Vehicle` có `int numWheels`; `Motorcycle` ràng buộc nó thành chính xác 2 | ? |
| Lớp cơ sở đánh dấu một thành viên là `final` — các lớp dẫn xuất không thể chạm vào nó | ? |
| Một lớp dẫn xuất thay đổi kiểu của `price` từ `int` thành `double` mà không có bất kỳ ràng buộc nào | ? |

> [!success]- Hiển thị Đáp án
> - "Một lớp dẫn xuất định nghĩa `int speed` mặc dù lớp cơ sở đã có `int speed`" → **Định nghĩa lại ẩn** (Mức 4). Lớp dẫn xuất ẩn thuộc tính được kế thừa bằng thuộc tính riêng của nó.
> - "`Motorcycle` ràng buộc `numWheels` thành chính xác 2" → **Định nghĩa lại có ràng buộc** (Mức 3). Miền giá trị của thuộc tính bị ràng buộc.
> - "Lớp cơ sở đánh dấu một thành viên là `final` — không thể chạm vào" → **Không định nghĩa lại** (Mức 1). Sửa đổi không được phép.
> - "Thay đổi `price` từ `int` thành `double` không có ràng buộc" → **Định nghĩa lại tùy ý** (Mức 2). Bất kỳ định nghĩa lại nào cũng được cho phép mà không có ràng buộc.
>
> **Bối cảnh:** Bốn mức này mô tả phổ khả năng sửa đổi thuộc tính trong lớp con — từ hoàn toàn niêm phong (1) đến hoàn toàn mở (2), với các mức độ ràng buộc khác nhau ở giữa.

---

### Bài tập 7: Kế thừa Toàn phần vs Một phần (Khái niệm)

Một lớp cơ sở `Vehicle` có: `int speed`, `int fuelCapacity`, `float emissions`, `void startEngine()`, `void accelerate()`.

1. Nếu `ElectricCar` sử dụng kế thừa **toàn phần**, nó kế thừa những gì?
2. Nếu `ElectricCar` sử dụng kế thừa **một phần** (loại bỏ `fuelCapacity` và `emissions`), nó kế thừa những gì?
3. C++ sử dụng mô hình nào?

> [!success]- Hiển thị Đáp án
> **1. Kế thừa toàn phần:** `ElectricCar` kế thừa TẤT CẢ năm thành viên: `speed`, `fuelCapacity`, `emissions`, `startEngine()`, `accelerate()`. Nó sau đó có thể ghi đè hoặc thêm vào chúng, nhưng không có gì bị loại bỏ.
>
> **2. Kế thừa một phần:** `ElectricCar` chỉ kế thừa: `speed`, `startEngine()`, `accelerate()`. `fuelCapacity` và `emissions` bị loại bỏ (bị loại trừ). Lớp con chỉ giữ lại những gì nó cần.
>
> **3. C++ sử dụng kế thừa toàn phần.** Một lớp dẫn xuất kế thừa mọi thứ từ lớp cơ sở (tuân theo các quy tắc truy cập). Không có cơ chế nào để chọn lọc loại bỏ các thành viên được kế thừa riêng lẻ.

---

### Bài tập 8: Xác định Lớp Trừu tượng

Hãy xem xét các mô tả lớp sau. Lớp nào là lớp trừu tượng?

| Lớp | Mô tả | Trừu tượng? |
|-------|-------------|-----------|
| `Animal` | Có `eat()`, `sleep()`. Không có thể hiện — chỉ `Dog`, `Cat`, `Bird` được tạo. | |
| `Person` | Có `name`, `age`. Các thể hiện như `Student s("John", 20)` được tạo. | |
| `Shape` | Có `draw()`. Chỉ `Circle`, `Square`, `Triangle` được khởi tạo. | |
| `Printable` | Có giao diện `print()`. Tồn tại chỉ để khai báo một hợp đồng cho các lớp khác. | |

> [!success]- Hiển thị Đáp án
> - `Animal` → **Trừu tượng.** Chỉ được sử dụng như một siêu lớp. Không có thể hiện trực tiếp. Tồn tại để phân loại.
> - `Person` → **KHÔNG trừu tượng.** `Student s("John", 20)` tạo một thể hiện trực tiếp. Nó là một lớp cụ thể.
> - `Shape` → **Trừu tượng.** `draw()` có thể là ảo thuần túy. Chỉ các hình cụ thể được khởi tạo.
> - `Printable` → **Trừu tượng.** Tồn tại chỉ như một hợp đồng thiết kế / giao diện. Không có thể hiện trực tiếp hoặc mã thực thi — phân loại không có mã đằng sau nó.
>
> **Chính:** Một lớp trừu tượng được định nghĩa bởi cách sử dụng của nó — nếu nó chỉ được sử dụng NHƯ một siêu lớp và không bao giờ để tạo đối tượng, nó là trừu tượng.

---

### Bài tập 9: Kế thừa vs Phân loại — Xác định Loại Mối quan hệ

Cho sơ đồ này:
```
        Vehicle
        /     \
      Car    Motorcycle
      /  \
  Sedan SUV
    |
  HondaCivic
```

1. `Sedan → HondaCivic` là phân loại, kế thừa, hay cả hai?
2. `Vehicle → Car` là phân loại, kế thừa, hay cả hai?
3. Một `HondaCivic` cụ thể với VIN `XYZ123` là một ví dụ của phân loại hay khởi tạo?
4. Tại sao kế thừa bội "ảnh hưởng đến sự rõ ràng của phân loại"?

> [!success]- Hiển thị Đáp án
> 1. `Sedan → HondaCivic` là **cả hai** phân loại VÀ kế thừa (đơn, toàn phần). `HondaCivic` LÀ MỘT `Sedan`. Đây là phân loại sạch sẽ.
> 2. `Vehicle → Car` là **cả hai** phân loại VÀ kế thừa. `Car` LÀ MỘT `Vehicle`. Kế thừa đơn sạch sẽ.
> 3. Một `HondaCivic` cụ thể với VIN `XYZ123` là một **thể hiện** (đối tượng), không phải một lớp. Đây là **từ phân loại đến khởi tạo** — điểm mà cây không còn là các lớp và bắt đầu là các đối tượng.
> 4. Kế thừa bội "ảnh hưởng đến sự rõ ràng của phân loại" vì một lớp bây giờ có **nhiều cha**. `TeachingAssistant` đi vào đâu trong một cây sạch sẽ? Nó LÀ MỘT `Student` VÀ LÀ MỘT `Employee`. Hệ thống phân cấp phân loại không còn là một cây sạch sẽ và trở thành một đồ thị — khó suy luận hơn.

---

### Bài tập 10: Kế thừa Mặc định vs Nghiêm ngặt (So sánh Khái niệm)

So sánh hành vi của kế thừa mặc định và nghiêm ngặt cho lớp cơ sở này:

```cpp
class Base {
public:
    int data;
    void process() { data *= 2; }
};
```

1. Dưới kế thừa **mặc định**, một lớp dẫn xuất có thể làm gì với `data` và `process()`?
2. Dưới kế thừa **nghiêm ngặt**, những hạn chế nào được áp dụng?
3. Trong C++, từ khóa nào cho phép kế thừa nghiêm ngặt trên `process()`?

> [!success]- Hiển thị Đáp án
> 1. **Kế thừa mặc định:** Lớp dẫn xuất có thể tự do:
>    - Gán lại `data` cho bất kỳ giá trị `int` nào
>    - Ghi đè `process()` với một cài đặt mới
>    - Thay đổi mức truy cập của các thành viên được kế thừa
>    - Thêm các thành viên mới bên cạnh các thành viên được kế thừa
> 2. **Kế thừa nghiêm ngặt:** Lớp dẫn xuất:
>    - Không thể ghi đè `process()` — nó bị đóng băng
>    - Không thể sửa đổi các ràng buộc trên `data`
>    - Tất cả các thành viên được kế thừa giữ nguyên định nghĩa và hành vi gốc của chúng
> 3. Trong C++11+, từ khóa `final`: `void process() final { data *= 2; }` ngăn các lớp dẫn xuất ghi đè `process()`. Đây là cơ chế C++ cho kế thừa nghiêm ngặt trên các phương thức riêng lẻ. Để ngăn toàn bộ lớp bị kế thừa: `class Base final { };`.

---

### Bài tập 11: Ba Khía cạnh của Phân loại — Ghép Mô tả

Ghép mỗi tình huống thiết kế với khía cạnh đúng của phân loại/kế thừa:

| Tình huống | Khía cạnh |
|----------|--------|
| Tất cả các lớp con của `Employee` chia sẻ `name`, `id`, `getDetails()` | ? |
| `SalariedEmployee` thay đổi `calculatePay()` để chia lương cho 12 thay vì sử dụng mức lương theo giờ | ? |
| `Shape` khai báo `draw()` nhưng không cung cấp cài đặt — mỗi lớp con phải cài đặt nó | ? |

> [!success]- Hiển thị Đáp án
> - "Tất cả các lớp con của `Employee` chia sẻ `name`, `id`, `getDetails()`" → **Tính chung (Commonality).** Lớp cơ sở nắm bắt thông tin chung và các đặc điểm được chia sẻ trên các lớp dẫn xuất.
> - "`SalariedEmployee` thay đổi `calculatePay()`" → **Tùy chỉnh (Customization).** Một lớp hiện có (`Employee`) được sử dụng để tạo một phiên bản tùy chỉnh (`SalariedEmployee`) với hành vi đã được sửa đổi.
> - "`Shape` khai báo `draw()` nhưng không cung cấp cài đặt" → **Giao diện Thiết kế Chung (Common Design Interface).** Lớp cơ sở định nghĩa các yêu cầu thiết kế cho các lớp dẫn xuất bằng cách chỉ định các hàm thành viên PHẢI được cung cấp.

---

### Bài tập 12: Ba Chiều của Chia sẻ — Phân loại

Phân loại mỗi cơ chế chia sẻ được mô tả theo ba chiều (tĩnh/động, ngầm/tường minh, theo đối tượng/theo nhóm):

| Cơ chế | Tĩnh/Động | Ngầm/Tường minh | Theo Đối tượng/Theo Nhóm |
|-----------|---------------|-------------------|---------------------|
| Kế thừa lớp C++: `class Dog : public Animal` | ? | ? | ? |
| Ủy quyền nguyên mẫu JavaScript (đối tượng `dog` ủy quyền cho `animal`) | ? | ? | ? |

> [!success]- Hiển thị Đáp án
> - **Kế thừa lớp C++:** **Tĩnh** (cố định tại thời điểm biên dịch), **Ngầm** (trình biên dịch tự động phân giải), **Theo Nhóm** (được định nghĩa ở cấp lớp cho tất cả các thể hiện).
> - **Ủy quyền nguyên mẫu JavaScript:** **Động** (chuỗi nguyên mẫu được duyệt tại thời điểm chạy khi thuộc tính được truy cập), **Ngầm** (tra cứu xảy ra tự động), **Theo Đối tượng** (mỗi đối tượng có thể có nguyên mẫu riêng; thay đổi `dog.__proto__` tại thời điểm chạy thay đổi hành vi cho đối tượng duy nhất đó).
>
> **Sự kiện kỳ thi:** Bài giảng trình bày ba chiều này để cho thấy rằng mô hình kế thừa của C++ chỉ là một điểm trong một không gian thiết kế rộng lớn hơn. Hiểu các lựa chọn thay thế giúp bạn nhận ra những gì C++ LÀM VÀ KHÔNG làm.

---

### Bài tập 13: Tự động Sinh Hàm tạo (Ôn tập Lec6 từ Lec7)

Cho lớp này:

```cpp
class Widget {
private:
    int value;
public:
    Widget(int v) { value = v; }
};
```

1. `Widget` có hàm tạo mặc định không?
2. `Widget w;` có biên dịch không? Tại sao hoặc tại sao không?
3. Nếu không có hàm tạo nào được định nghĩa cả, `Widget w;` có biên dịch không? Tại sao?

> [!success]- Hiển thị Đáp án
> 1. **Không.** `Widget` định nghĩa một hàm tạo có tham số `Widget(int)`. Vì lập trình viên đã viết BẤT KỲ hàm tạo nào, trình biên dịch KHÔNG sinh ra hàm tạo mặc định.
> 2. **Không.** `Widget w;` cố gắng gọi hàm tạo mặc định, mà không tồn tại. Lỗi biên dịch: không có hàm phù hợp cho lời gọi `Widget::Widget()`.
> 3. **Có.** Nếu không có hàm tạo nào được định nghĩa cả, trình biên dịch sẽ sinh ra một hàm tạo mặc định. `Widget w;` sẽ biên dịch và `value` sẽ không được khởi tạo (giá trị rác cho các kiểu dựng sẵn).
>
> **Quy tắc:** Viết bất kỳ hàm tạo nào → trình biên dịch ngừng sinh hàm tạo mặc định. Logic tương tự áp dụng cho việc tự động sinh hàm hủy.

---

### Bài tập 14: Hợp thành vs Kế thừa — Quyết định Thiết kế

Bạn đang thiết kế một lớp `Library`. Nó lưu trữ một bộ sưu tập các đối tượng `Book`. `Library` có nên kế thừa từ `Book` hay chứa một mảng `Book` như một thành viên?

Giải thích với "is-a" vs "has-a."

> [!success]- Hiển thị Đáp án
> **Một `Library` KHÔNG NÊN kế thừa từ `Book`.**
>
> - **Kiểm tra "Is-a":** Một `Library` có phải là một `Book` không? **Không.** Một thư viện là một bộ sưu tập của sách, không phải một loại sách cụ thể. Kế thừa sẽ mô hình hóa rằng một `Library` LÀ MỘT `Book`, điều này là sai.
> - **Kiểm tra "Has-a":** Một `Library` CÓ các đối tượng `Book` không? **Có.** Một thư viện chứa sách như một phần của trạng thái của nó.
>
> **Giải pháp:** Sử dụng hợp thành — `Library` có một thành viên như `Book* books` (mảng) hoặc `vector<Book> books`.
>
> **Nguyên tắc chung:** Nếu bạn có thể nói "X LÀ MỘT Y," hãy sử dụng kế thừa. Nếu bạn có thể nói "X CÓ MỘT Y," hãy sử dụng hợp thành. Áp dụng sai kế thừa tạo ra các hệ thống phân cấp mong manh, khó hiểu.

---

### Bài tập 15: Nguyên lý Khả năng Thay thế

```cpp
class Person {
public:
    string name;
    virtual void introduce() { cout << "I am " << name; }
};

class Student : public Person {
public:
    int studentID;
    void introduce() override { cout << "Student " << name << " #" << studentID; }
};

void greet(Person& p) {
    p.introduce();
}

int main() {
    Student s;
    s.name = "Alice";
    s.studentID = 12345;
    greet(s);             // (A) Hợp lệ?
    Person* ptr = &s;     // (B) Hợp lệ?
    Student* sptr = ptr;  // (C) Hợp lệ? (Giả sử ép kiểu tường minh)
}
```

Trả lời: (A) có hợp lệ không? (B) có hợp lệ không? (C) có an toàn không? Giải thích từng cái.

> [!success]- Hiển thị Đáp án
> **Dòng (A):** HỢP LỆ. `greet()` mong đợi một `Person&`. Một `Student` LÀ MỘT `Person`, vì vậy một đối tượng `Student` có thể được truyền vào nơi một tham chiếu `Person` được mong đợi. Đây là nguyên lý khả năng thay thế. Lời gọi phân giải thành `Student::introduce()` (điều phối động).
>
> **Dòng (B):** HỢP LỆ. Ép kiểu lên từ `Student*` lên `Person*` luôn an toàn và ngầm định. `ptr` bây giờ trỏ đến đối tượng con `Person` của `s`.
>
> **Dòng (C):** KHÔNG AN TOÀN (lỗi biên dịch nếu không có ép kiểu). Ép kiểu xuống từ `Person*` trở lại `Student*` yêu cầu một ép kiểu tường minh vì trình biên dịch không thể đảm bảo rằng `ptr` thực sự trỏ đến một `Student`. Nếu `ptr` trỏ đến một `Person` đơn thuần, việc ép kiểu sẽ thành công về mặt cú pháp nhưng truy cập `studentID` sẽ là hành vi không xác định.
