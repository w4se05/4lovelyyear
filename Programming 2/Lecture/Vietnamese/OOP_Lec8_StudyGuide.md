# Lec8: Tính kế thừa (Inheritance) trong C++ — Hướng dẫn học tập

---

## 1. THẺ KHÁI NIỆM: Cơ chế kế thừa trong C++

### 1.1 Bản chất

Kế thừa (Inheritance) trong C++ là một **cơ chế ngôn ngữ** cho phép xây dựng một lớp mới (lớp dẫn xuất/Derived class) từ một lớp đã tồn tại (lớp cơ sở/Base class). Lớp dẫn xuất **tự động kế thừa TẤT CẢ các thành phần dữ liệu và hàm** của lớp cơ sở, cùng với các thành phần do chính nó khai báo thêm. C++ cung cấp ba hình thức kế thừa — `public`, `protected` và `private` — mỗi hình thức kiểm soát cách các thành phần của lớp cơ sở được hiển thị trong lớp dẫn xuất.

Cú pháp C++ chính: `class NewClass : access_specifier BaseClass { /* thành phần mới */ };`
- `access_specifier` là một trong các từ khóa `public`, `protected` hoặc `private` (mặc định là `private` đối với `class`, `public` đối với `struct`).
- Khác với bài giảng khái niệm (Lec7), Lec8 cung cấp **các quy tắc chính xác** về khả năng truy cập thành phần sau kế thừa.

### 1.2 Vấn đề được giải quyết (Xa hơn "Is-A")

Biết rằng một `Student` IS A `Person` là chưa đủ. Bạn cần câu trả lời cụ thể cho:

- **Mức truy cập sau kế thừa**: Nếu `Person::name` là `protected`, nó có còn là `protected` trong `Student` dưới kế thừa `public` không? Dưới kế thừa `private`?
- **Chuỗi hàm tạo (Constructor chaining)**: Làm thế nào `Student("Alice", 12345)` gọi `Person("Alice")`? Điều gì xảy ra nếu `Person` không có hàm tạo mặc định (default constructor)?
- **Bài toán kim cương (Diamond problem)**: `GradAssistant` kế thừa từ cả `Student` và `Employee`, cả hai đều kế thừa từ `Person`. `GradAssistant` có một hay hai `Person`? Làm thế nào để giải quyết sự mơ hồ (ambiguity)?
- **Quy tắc chuyển đổi con trỏ**: Có thể gán `Person*` cho `Student*` không? Khi nào an toàn? Khi nào bắt buộc?
- **Cơ chế ghi đè (Overriding) trong C++**: Điều gì xảy ra khi lớp cơ sở và lớp dẫn xuất có các hàm cùng tên? Làm thế nào để vẫn gọi được phiên bản của lớp cơ sở?

Bài giảng này trả lời tất cả các câu hỏi trên với các quy tắc C++ chính xác.

### 1.3 Cách hoạt động (Từng bước)

1. **Định nghĩa lớp cơ sở** với các thành phần được đánh dấu `private`, `protected` hoặc `public`.
2. **Khai báo lớp dẫn xuất** chọn bộ xác định truy cập kế thừa: `public`, `protected` hoặc `private`.
3. **Khi tạo đối tượng**, trình biên dịch xâu chuỗi các hàm tạo: hàm tạo lớp cơ sở chạy ĐẦU TIÊN, sau đó đến các đối tượng thành viên theo thứ tự khai báo, cuối cùng là thân hàm tạo lớp dẫn xuất.
4. **Khi hủy**, thứ tự đảo ngược chính xác: thân hàm hủy lớp dẫn xuất → hàm hủy thành viên → hàm hủy lớp cơ sở.
5. **Truy cập thành phần** được giải quyết tại thời điểm biên dịch dựa trên cả mức truy cập gốc của thành phần VÀ bộ xác định truy cập kế thừa.
6. **Đối với kế thừa bội (Multiple inheritance)**, nếu tồn tại sự mơ hồ (cùng tên thành phần từ hai đường dẫn lớp cơ sở), trình biên dịch yêu cầu phân giải phạm vi tường minh (explicit scope resolution).
7. **Đối với kế thừa hình kim cương** với chung một tổ tiên, các lớp cơ sở ảo (`virtual` base classes) đảm bảo một THỂ HIỆN DUY NHẤT được chia sẻ của lớp cơ sở chung.

### 1.4 Ví dụ cụ thể (Hệ thống Nhân sự Đại học)

```
                 Person (name, id, getContactInfo())
                /                          \
        Student (major, gpa)          Employee (salary, department)
                \                          /
           GradAssistant (stipend, supervisor)
```

- `Person` là lớp cơ sở chung với `name` và `id`.
- `Student` kế thừa từ `Person` và thêm `major`, `gpa`.
- `Employee` (hoặc `Salaried`) kế thừa từ `Person` và thêm `salary`, `department`.
- `GradAssistant` kế thừa từ CẢ `Student` và `Employee`.

**Không có kế thừa ảo (virtual inheritance)**, `GradAssistant` có HAI đối tượng con `Person` (một từ `Student`, một từ `Employee`). Gọi `setAge()` hoặc `getAge()` bị mơ hồ — `Person` nào?

**Có kế thừa ảo** (`class Student : virtual public Person`, `class Employee : virtual public Person`), `GradAssistant` có MỘT `Person` được chia sẻ. Sự mơ hồ được giải quyết.

### 1.5 Nó KHÔNG phải là

- **Bộ xác định truy cập kế thừa (`public`, `protected`, `private`) KHÔNG giống với bộ xác định truy cập thành phần.** Bộ xác định truy cập thành phần kiểm soát ai có thể truy cập một thành phần. Bộ xác định truy cập kế thừa kiểm soát cách các thành phần đó được **hiển thị thêm** trong lớp dẫn xuất.
- **Kế thừa KHÔNG giống với quan hệ bạn bè (friendship).** Lớp dẫn xuất KHÔNG tự động trở thành `friend` của lớp cơ sở — nó không thể truy cập trực tiếp các thành phần `private` của lớp cơ sở.
- **Lớp dẫn xuất KHÔNG kế thừa các hàm tạo, hàm hủy, hàm tạo sao chép (copy constructor) hoặc toán tử gán (assignment operator).** Nó phải tự định nghĩa (hoặc trình biên dịch tự sinh), và hàm tạo lớp dẫn xuất phải gọi hàm tạo lớp cơ sở.

---

## 2. LỚP CƠ SỞ VÀ LỚP DẪN XUẤT

### 2.1 Định nghĩa

- **Lớp cơ sở (Base class)**: Một lớp đã được định nghĩa trước, được sử dụng để định nghĩa các lớp mới. Nó cung cấp nền tảng về dữ liệu và hành vi.
- **Lớp dẫn xuất (Derived class)**: Một lớp kế thừa TẤT CẢ các thành phần dữ liệu và hàm của một lớp cơ sở, ngoài các thành phần do chính nó khai báo thêm.

> **Chi tiết quan trọng**: Lớp dẫn xuất kế thừa TẤT CẢ các thành phần, bao gồm cả các thành phần `private`. Các thành phần `private` của lớp cơ sở TỒN TẠI bên trong đối tượng dẫn xuất nhưng KHÔNG thể truy cập trực tiếp bằng mã của lớp dẫn xuất.

### 2.2 Kế thừa đơn (Single Inheritance)

- Thực hiện mối quan hệ **"is-a"**.
- Lớp dẫn xuất có chính xác **MỘT** lớp cơ sở.
- Hình thành một hệ thống phân cấp dạng cây sạch sẽ (chưa có vấn đề kim cương hoặc mơ hồ).

### 2.3 Cú pháp khai báo

```
class class_name : access_specifier base_class {
    // danh sách thành phần bổ sung (tùy chọn)
};
```

Trong đó `access_specifier` là một trong:
- `public` — phổ biến nhất, bảo toàn mức truy cập thành phần của lớp cơ sở
- `protected` — giới hạn các thành phần public được kế thừa thành protected
- `private` — giới hạn tất cả thành phần được kế thừa thành private (MẶC ĐỊNH cho từ khóa `class`)

### 2.4 Ví dụ từ bài giảng

**Ví dụ 1 — Hệ thống phân cấp Student:**
```
Student (name, id)
  ├── Undergraduate (year, major, minor)
  └── Graduate (advisor, thesis, research)
```
Mỗi lớp dẫn xuất IS A Student với chuyên môn hóa bổ sung.

**Ví dụ 2 — Hệ thống phân cấp Ấn phẩm:**
```
Publication (publisher, date)
  ├── Magazine (circulation, # of issues per year)
  └── Book (ISBN, author)
```

**Ví dụ 3 — Các góc nhìn khác nhau về một Employee:**
Một `Employee` có thể được xem theo hai chiều trực giao:

| Chiều | Biến thể |
|-----------|----------|
| **Loại hình lao động** | Toàn thời gian vs Bán thời gian |
| **Thâm niên** | Vĩnh viễn vs Tạm thời (hành vi BHXH khác nhau) |

Điều này minh họa rằng kế thừa là về việc mô hình hóa **các góc nhìn thay thế** của cùng một khái niệm cốt lõi, không chỉ một hệ thống phân cấp duy nhất.

---

## 3. THỨ TỰ THỰC THI HÀM TẠO & HÀM HỦY

### 3.1 Thứ tự hàm tạo

**Hàm tạo lớp cơ sở LUÔN được thực thi ĐẦU TIÊN.**

Thứ tự xây dựng đầy đủ cho một đối tượng dẫn xuất:
1. **Hàm tạo lớp cơ sở** — đầu tiên
2. **Các đối tượng thành viên** — theo thứ tự khai báo (không phải thứ tự danh sách khởi tạo!)
3. **Thân hàm tạo lớp dẫn xuất** — cuối cùng

Điều này có nghĩa là khi thân hàm tạo lớp dẫn xuất chạy, phần cơ sở và tất cả các đối tượng thành viên đã được khởi tạo hoàn toàn và an toàn để sử dụng.

### 3.2 Thứ tự hàm hủy

**NGƯỢC CHÍNH XÁC** với xây dựng:
1. **Thân hàm hủy lớp dẫn xuất** — đầu tiên
2. **Hàm hủy thành viên** — theo thứ tự khai báo ngược
3. **Hàm hủy lớp cơ sở** — cuối cùng

### 3.3 Tham khảo bài giảng

Xem `Lec8_ex2-Employee.cpp` để theo dõi cụ thể thứ tự xây dựng/hủy.

**Cách ghi nhớ:** "Hàm tạo: cơ sở trước, dẫn xuất sau. Hàm hủy: dẫn xuất trước, cơ sở sau." — Giống như xây nhà móng trước nhưng phá nhà mái trước.

---

## 4. GHI ĐÈ (OVERRIDING)

### 4.1 Định nghĩa

Một hàm trong lớp dẫn xuất có **cùng tên hàm** sẽ **ghi đè** (override/hide/shadow) hàm trong lớp cơ sở.

Khi bạn gọi `obj.functionName()` trên một đối tượng dẫn xuất, phiên bản dẫn xuất chạy — phiên bản cơ sở bị ẩn.

### 4.2 Truy cập các hàm bị ghi đè

Bạn vẫn có thể lấy lại hàm cơ sở bị ghi đè bằng cách sử dụng **toán tử phân giải phạm vi (scope resolution operator)** `::`:

```cpp
class Base {
public:
    void display() { /* phiên bản cơ sở */ }
};

class Derived : public Base {
public:
    void display() { /* ghi đè phiên bản cơ sở */ }
    void test() {
        display();           // gọi Derived::display()
        Base::display();     // gọi Base::display() một cách tường minh
    }
};
```

> **Quan trọng:** Không có `Base::`, gọi `display()` bên trong `Derived` sẽ đệ quy gọi `Derived::display()` — dẫn đến đệ quy vô hạn. Toán tử phân giải phạm vi là rất cần thiết.

---

## 5. CÁC LOẠI THÀNH PHẦN CỦA LỚP (Ôn tập + Sơ đồ)

### 5.1 `private`

- Có thể truy cập bởi: chính **lớp** đó + **bạn (friends)** của lớp đó.
- KHÔNG thể truy cập bởi các lớp dẫn xuất.
- KHÔNG thể truy cập bởi các hàm/thể hiện bên ngoài.

### 5.2 `protected`

- Có thể truy cập bởi: chính **lớp** đó + **bạn** + **các lớp dẫn xuất**.
- KHÔNG thể truy cập bởi các hàm/thể hiện bên ngoài.
- **Mục đích:** Chia sẻ với các lớp dẫn xuất mà không hiển thị ra công chúng.

### 5.3 `public`

- Có thể truy cập bởi: **mọi người** — lớp, bạn, lớp dẫn xuất, thể hiện bên ngoài.

### 5.4 Sơ đồ trực quan (từ bài giảng)

```
Có thể truy cập bởi      Public              Có thể truy cập bởi
lớp dẫn xuất VÀ thể hiện ────►   Protected ◄──── chỉ lớp dẫn xuất
                                     ▲
                                     │
                               Private ──── KHÔNG thể truy cập
                                             (bởi lớp dẫn xuất)
```

**Bảng tóm tắt:**

| Truy cập thành phần | Cùng lớp | Bạn (Friends) | Lớp dẫn xuất | Bên ngoài/Thể hiện |
|---------------|:----------:|:-------:|:---------------:|:-----------------:|
| `public`      | Có | Có | Có | Có |
| `protected`   | Có | Có | Có | Không |
| `private`     | Có | Có | Không | Không |

---

## 6. CÁC LOẠI KẾ THỪA (PHẦN QUAN TRỌNG)

Đây là phần quan trọng nhất cho các kỳ thi. Loại kế thừa xác định mức truy cập mà các thành phần được kế thừa có trong lớp dẫn xuất.

### 6.1 Kế thừa `public` (PHỔ BIẾN NHẤT)

**Ánh xạ:**
- Base `public` → **public** trong dẫn xuất
- Base `protected` → **protected** trong dẫn xuất
- Base `private` → **không thể truy cập** (tồn tại nhưng không thể chạm tới)

**Truy cập bên ngoài:** Các hàm bên ngoài CÓ thể truy cập các thành phần `public` được kế thừa.

**Ví dụ bài giảng:**
```cpp
// Lec8_ex3-public-inher.cpp
int main() {
    p = aStack.removeFirst();  // HOẠT ĐỘNG — removeFirst() là public trong dẫn xuất
}
```

### 6.2 Kế thừa `private` (MẶC ĐỊNH cho `class`)

**Ánh xạ:**
- Base `public` → **PRIVATE** trong dẫn xuất
- Base `protected` → **PRIVATE** trong dẫn xuất
- Base `private` → **không thể truy cập**

**Truy cập bên ngoài:** Các hàm bên ngoài KHÔNG thể truy cập BẤT CỨ ĐIỀU GÌ được kế thừa. Mọi thứ đều là private.

**Ví dụ bài giảng:**
```cpp
// Lec8_ex4-private-inher.cpp
int main() {
    p = aStack.removeFirst();  // LỖI — thành phần được kế thừa giờ là PRIVATE
}
```

> **Hiệu ứng dây chuyền:** Các lớp cháu (grandchildren) kế thừa từ lớp dẫn xuất này qua `public` nhưng KHÔNG THẤY gì có thể truy cập được từ lớp cơ sở gốc. Kế thừa `private` cắt đứt chuỗi kế thừa cho tất cả các hậu duệ tiếp theo.

### 6.3 Kế thừa `protected`

**Ánh xạ:**
- Base `public` → **PROTECTED** trong dẫn xuất
- Base `protected` → **PROTECTED** trong dẫn xuất
- Base `private` → **không thể truy cập**

**Truy cập bên ngoài:** Các hàm bên ngoài KHÔNG thể truy cập các thành phần được kế thừa. Chỉ các lớp dẫn xuất sâu hơn mới có thể.

**Ví dụ bài giảng:**
```cpp
// Lec8_ex5-protected-inher.cpp
int main() {
    p = aStack1.removeFirst();  // LỖI — thành phần được kế thừa giờ là PROTECTED, không phải public
}
```

### 6.4 Bảng tóm tắt (Bảng chính cho các kỳ thi)

| Loại kế thừa | Base `public` → | Base `protected` → | Base `private` → | Truy cập bên ngoài vào thành phần kế thừa? |
|:---:|:---:|:---:|:---:|:---:|
| **public** | `public` | `protected` | không thể truy cập | CÓ (với các thành phần vốn là public) |
| **private** | `private` | `private` | không thể truy cập | KHÔNG |
| **protected** | `protected` | `protected` | không thể truy cập | KHÔNG |

**Cách ghi nhớ:** Bộ xác định kế thừa giới hạn mức truy cập tối đa. Kế thừa `private` giới hạn mọi thứ ở mức `private`. Kế thừa `protected` giới hạn mọi thứ ở mức `protected`. Kế thừa `public` không giới hạn gì — các mức truy cập được bảo toàn.

---

## 7. HÀM TẠO TRONG LỚP DẪN XUẤT

### 7.1 Quy tắc

Khi một đối tượng của lớp dẫn xuất được tạo, hàm tạo của lớp dẫn xuất **PHẢI ĐẦU TIÊN** gọi hàm tạo của lớp cơ sở (tường minh hoặc ngầm định).

### 7.2 Bộ khởi tạo-hàm tạo (Constructor-Initializers / ctor-initializer)

**Cú pháp:**
```cpp
class_name::class_name(param-list) : ctor-initializer {
    // thân hàm
}
```

**ctor-initializer** truyền tham số cho các hàm tạo lớp cơ sở và/hoặc bộ khởi tạo thành viên:

```cpp
// ví dụ ctor-initializer:
Student::Student(string n, int i, string m)
    : Person(n, i),      // khởi tạo lớp cơ sở Person
      major(m)            // khởi tạo thành viên
{
    // thân — lớp cơ sở và thành viên đã được khởi tạo
}
```

### 7.3 Tại sao dùng ctor-initializer?

**Không có nó:**
- Hàm tạo **mặc định** của lớp cơ sở sẽ được gọi.
- Bạn sau đó sẽ cần **các hàm truy cập** (setter) để thiết lập các thành phần dữ liệu cụ thể.
- Điều này lãng phí — lớp cơ sở được khởi tạo với giá trị mặc định, sau đó bị ghi đè ngay lập tức.

**Trường hợp quan trọng — lớp cơ sở KHÔNG có hàm tạo mặc định:**
- Nếu lớp cơ sở KHÔNG có hàm tạo mặc định, ctor-initializer là **BẮT BUỘC**.
- Trình biên dịch sẽ KHÔNG biên dịch mã lớp dẫn xuất nếu thiếu nó.
- Lỗi: no matching function for call to `BaseClass::BaseClass()`.

**Ví dụ (biên dịch thất bại nếu không có ctor-initializer):**
```cpp
class Person {
    string name;
public:
    Person(string n) : name(n) {}   // KHÔNG có hàm tạo mặc định
};

class Student : public Person {
    // Student(string n) { }       // LỖI — không thể gọi Person::Person()
    Student(string n) : Person(n) { }  // BẮT BUỘC ctor-initializer
};
```

### 7.4 Hàm hủy (Destructor)

Các hàm hủy được gọi **ngầm định** bắt đầu từ **lớp dẫn xuất cuối cùng** và di chuyển theo hướng về lớp cơ sở. Bạn không bao giờ cần gọi tường minh hàm hủy lớp cơ sở — trình biên dịch xử lý chuỗi tự động.

**Tham khảo bài giảng:** `Lec8_ex6-ctor_derived.cpp`, `Lec8_ex7-ctor_init.cpp`

---

## 8. TƯƠNG THÍCH VÀ CHUYỂN ĐỔI CON TRỎ

### 8.1 Quy tắc tương thích

- Một đối tượng của lớp **dẫn xuất** có thể được coi là một đối tượng của lớp **cơ sở** của nó (một `Student` IS A `Person`).
- **Điều ngược lại KHÔNG đúng.** Bạn không thể coi một `Person` là một `Student` — `Person` có thể không có `major` hoặc `gpa`.

### 8.2 Phạm vi lớp lồng nhau (Nested Class Scope)

- Một thành phần lớp cơ sở public hoặc protected bị **ẩn** khỏi lớp dẫn xuất có thể được truy cập bằng toán tử phân giải phạm vi: `base_class::member`.
- **Lớp cơ sở KHÔNG thể truy cập các thành phần của lớp dẫn xuất của nó.** Kế thừa là một chiều.

### 8.3 Chuyển đổi ngầm định của con trỏ dẫn xuất sang con trỏ cơ sở

**Upcasting (dẫn xuất → cơ sở):** Luôn an toàn, luôn ngầm định.

```cpp
Point3D * cp = new Point3D;   // Point3D kế thừa từ Point
Point * p;
p = cp;                        // OK — dẫn xuất→cơ sở, chuyển đổi ngầm định
```

**Downcasting (cơ sở → dẫn xuất):** KHÔNG ngầm định. Cần ép kiểu tường minh. RỦI RO.

```cpp
Point3D *cp1;
cp1 = p;                       // LỖI — cơ sở→dẫn xuất, KHÔNG ngầm định
cp1 = (Point3D*) p;            // Cú pháp OK NHƯNG rủi ro — có thể sai kiểu
```

### 8.4 Tại sao Downcasting rủi ro

Con trỏ cơ sở có thể trỏ tới:
- Một đối tượng cơ sở thực tế (không phải đối tượng dẫn xuất)
- Một lớp dẫn xuất **KHÁC** (con trỏ `Point3D` từ một đối tượng `Point2D`)

Lớp dẫn xuất được kỳ vọng chứa **nhiều hơn** (thuộc tính & hành vi) so với đối tượng cơ sở. Nếu con trỏ không thực sự trỏ tới một `Point3D`, việc truy cập các thành phần bổ sung đó là **hành vi không xác định (undefined behavior)**.

> **Thực hành tốt nhất:** Buộc người dùng lớp phải sử dụng ép kiểu tường minh thường dẫn đến **mã kém chất lượng**. Ưu tiên dùng `dynamic_cast` (với RTTI) nếu cần downcasting — nó kiểm tra tại thời điểm chạy và trả về `nullptr` nếu thất bại.

---

## 9. KẾ THỪA BỘI (MULTIPLE INHERITANCE)

### 9.1 Khái niệm

Một lớp có thể có **nhiều hơn một** lớp cơ sở. Lớp dẫn xuất kế thừa từ tất cả các lớp cơ sở đồng thời.

### 9.2 Ví dụ từ bài giảng — GraduateAssistant

```
        Student                 Employee / Salaried
            \                        /
             →  GraduateAssistant  ←
```

`GradAssistant` kế thừa từ CẢ `Student` VÀ `Employee/Salaried`. Nó có tất cả các thành phần của cả hai — `name` từ `Student`, `salary` từ `Employee`, cộng với `stipend` và `supervisor` riêng.

### 9.3 Vấn đề mơ hồ (Ambiguity Problem)

Nếu `Student` và `Salaried` ĐỀU có phương thức `setAge()` (kế thừa từ `Person` qua hai đường dẫn riêng biệt), gọi `setAge()` trên một `GradAssistant` là mơ hồ:

```cpp
GradAssistant ga;
ga.setAge(25);  // LỖI — Student::setAge() hay Salaried::setAge()?
```

**Tham khảo bài giảng:** `Lec8_ex8_GradAssistant.cpp`

### 9.4 Giải pháp: Lớp cơ sở ảo (Virtual Base Classes)

Khai báo lớp cơ sở chung là **virtual** trong các lớp trung gian:

```cpp
class Student : virtual public Person { /* ... */ };
class Employee : virtual public Person { /* ... */ };
```

**Sơ đồ (từ bài giảng):**
```
                Person
              virtual   virtual
             /               \
       Employee             Student
            \                /
             →  Salaried    ←
                    \
                 GradAssistant
```

**Những gì kế thừa ảo (virtual inheritance) đảm bảo:**
- Chỉ có **MỘT THỂ HIỆN DUY NHẤT** của lớp cơ sở chung (`Person`).
- `GradAssistant` chỉ có MỘT đối tượng con `Person`, được chia sẻ bởi cả `Student` và `Employee`.
- Sự mơ hồ được **giải quyết** — `getAge()` trong `GradAssistant::display()` không còn mơ hồ nữa.
- Từ khóa `virtual` cho phép trình biên dịch quyết định hàm và biến nào để truy cập (vì giờ chỉ còn một bản sao).

**Quy tắc quan trọng:** Với các lớp cơ sở ảo, **lớp dẫn xuất xa nhất (most-derived class)** phải khởi tạo lớp cơ sở ảo. `GradAssistant` phải gọi trực tiếp hàm tạo của `Person`, không dựa vào `Student` hoặc `Employee` để làm điều đó.

**Tham khảo bài giảng:** `Lec8_ex9_GradAssistant.cpp`

> **Cách ghi nhớ:** *Kế thừa ảo = tổ tiên được chia sẻ.* Không có `virtual`, mỗi đường dẫn kế thừa có bản sao riêng. Có `virtual`, tất cả đường dẫn chia sẻ một bản sao.

---

## 10. CÁC MẪU CÚ PHÁP PHẢI HỌC THUỘC

### Mẫu 1: Khai báo kế thừa đơn (Cả 3 loại)

```cpp
// public inheritance — bảo toàn mức truy cập lớp cơ sở
class Derived : public Base {
    // public được kế thừa giữ nguyên public, protected giữ nguyên protected
};

// private inheritance — mọi thứ trở thành private
class Derived : private Base {
    // public và protected được kế thừa đều trở thành private
};

// protected inheritance — mọi thứ trở thành protected
class Derived : protected Base {
    // public và protected được kế thừa đều trở thành protected
};
```

### Mẫu 2: Bộ khởi tạo hàm tạo truyền đối số cho lớp cơ sở

```cpp
class Base {
    int a, b;
public:
    Base(int x, int y) : a(x), b(y) {}  // KHÔNG có hàm tạo mặc định
};

class Derived : public Base {
    int c;
public:
    Derived(int x, int y, int z)
        : Base(x, y),     // BẮT BUỘC — lớp cơ sở không có hàm tạo mặc định
          c(z)             // bộ khởi tạo thành viên
    { }
};
```

### Mẫu 3: Khai báo lớp cơ sở ảo (Giải pháp kim cương)

```cpp
class Person {
public:
    string name;
    int age;
    Person(string n, int a) : name(n), age(a) { }
    void setAge(int a) { age = a; }
    int getAge() { return age; }
};

class Student : virtual public Person {
    string major;
public:
    Student(string n, int a, string m) : Person(n, a), major(m) { }
};

class Employee : virtual public Person {
    double salary;
public:
    Employee(string n, int a, double s) : Person(n, a), salary(s) { }
};

class GradAssistant : public Student, public Employee {
    double stipend;
public:
    GradAssistant(string n, int a, string m, double s, double st)
        : Person(n, a),                  // LỚP DẪN XUẤT XA NHẤT khởi tạo lớp cơ sở ảo
          Student(n, a, m),              // Lời gọi Person() ở đây bị BỎ QUA
          Employee(n, a, s),             // Lời gọi Person() ở đây bị BỎ QUA
          stipend(st)
    { }
};
```

### Mẫu 4: Upcast và Downcast con trỏ

```cpp
Derived d;
Base* bp = &d;           // upcast — NGẦM ĐỊNH, luôn an toàn

Derived* dp = bp;        // LỖI — không có downcast ngầm định
Derived* dp = (Derived*) bp;  // ép kiểu C — biên dịch được NHƯNG RỦI RO
Derived* dp = static_cast<Derived*>(bp);   // an toàn hơn một chút, vẫn không có kiểm tra runtime
Derived* dp = dynamic_cast<Derived*>(bp);  // an toàn nhất — nullptr nếu sai kiểu
```

### Mẫu 5: Ghi đè với phân giải phạm vi dự phòng

```cpp
class Base {
public:
    void display() { cout << "Base"; }
};

class Derived : public Base {
public:
    void display() { cout << "Derived"; }
    void showBoth() {
        display();           // Derived::display()
        Base::display();     // Base::display() — phân giải phạm vi dự phòng
    }
};
```

### Mẫu 6: Theo dõi thứ tự hàm tạo/hàm hủy

```cpp
class A {
public:
    A() { cout << "A ctor "; }
    ~A() { cout << "A dtor "; }
};
class B {
public:
    B() { cout << "B ctor "; }
    ~B() { cout << "B dtor "; }
};
class C : public A {
    B memberB;
public:
    C() { cout << "C ctor "; }
    ~C() { cout << "C dtor "; }
};

// Kết quả: A ctor → B ctor → C ctor → C dtor → B dtor → A dtor
// Quy tắc: Hàm tạo cơ sở → thành viên (theo thứ tự khai báo) → thân dẫn xuất
//          Hàm hủy: ngược chính xác
```

### Mẫu 7: Kế thừa bội với phân giải mơ hồ

```cpp
class A : public B1, public B2, public B3 {
public:
    void setup() {
        B1::x = 5;            // phân giải — chọn x của B1
        B2::x = 10;           // phân giải — chọn x của B2
        B1::getValue();       // phân giải — chọn getValue() của B1
    }
};
```

### Mẫu 8: Tóm tắt hiệu ứng của bộ xác định truy cập

```cpp
// Dùng làm tham chiếu nhanh khi theo dõi:

// NẾU kế thừa public:
//    Base public    → giữ nguyên public
//    Base protected → giữ nguyên protected
//    Base private   → không thể truy cập

// NẾU kế thừa protected:
//    Base public    → trở thành protected
//    Base protected → trở thành protected
//    Base private   → không thể truy cập

// NẾU kế thừa private:
//    Base public    → trở thành private
//    Base protected → trở thành private
//    Base private   → không thể truy cập
```

---

## 11. BẪY THI CỬ

### Bẫy 1 — Bộ xác định truy cập trên kế thừa ≠ Bộ xác định truy cập trên thành phần
`class D : public B { }` — `public` kiểm soát CÁCH các thành phần của lớp cơ sở được hiển thị. Nó KHÔNG làm cho các thành phần private của B trở thành public. `public`/`protected`/`private` trên kế thừa là một khái niệm riêng biệt với `public`/`protected`/`private` trên từng thành phần riêng lẻ.

### Bẫy 2 — Hiệu ứng dây chuyền của kế thừa Private
Nếu `class B : private A { }` và `class C : public B { }`, thì `C` KHÔNG THẤY gì từ `A` một cách trực tiếp. Kế thừa `private` đã biến mọi thứ từ `A` thành các thành phần private của `B`, mà `C` không thể truy cập. Chuỗi bị cắt đứt.

### Bẫy 3 — Các thành phần private của lớp cơ sở vẫn tồn tại dù không được kế thừa
Một thành phần `private` của lớp cơ sở TỒN TẠI trong bố trí bộ nhớ của đối tượng dẫn xuất. Nó chỉ đơn giản là không thể truy cập trực tiếp bằng tên từ lớp dẫn xuất. Bạn có thể truy cập nó gián tiếp thông qua các hàm `public`/`protected` được kế thừa của lớp cơ sở thao tác trên nó.

### Bẫy 4 — Lớp cơ sở ảo: Lớp dẫn xuất xa nhất phải khởi tạo
Với các lớp cơ sở ảo, **lớp dẫn xuất xa nhất** chịu trách nhiệm gọi hàm tạo lớp cơ sở ảo. Các lời gọi hàm tạo đến lớp cơ sở ảo từ các lớp trung gian (`Student`, `Employee`) bị trình biên dịch **bỏ qua**. Quên khởi tạo lớp cơ sở ảo trong lớp dẫn xuất xa nhất dẫn đến việc hàm tạo mặc định của lớp cơ sở ảo được gọi (hoặc lỗi biên dịch nếu không có hàm tạo mặc định).

### Bẫy 5 — Không có Downcast ngầm định
`Person* p = new Student; Student* s = p;` — KHÔNG BIÊN DỊCH ĐƯỢC. Downcast không bao giờ ngầm định. Phải dùng ép kiểu tường minh (`static_cast<Student*>(p)` hoặc `dynamic_cast<Student*>(p)`). Ngay cả `static_cast` cũng nguy hiểm nếu `p` không thực sự trỏ tới một `Student`.

### Bẫy 6 — Ctor-Initializer BẮT BUỘC khi lớp cơ sở không có hàm tạo mặc định
Nếu lớp cơ sở chỉ định nghĩa một hàm tạo có tham số (không có mặc định), lớp dẫn xuất PHẢI dùng ctor-initializer để gọi nó. Trình biên dịch sẽ không tự sinh lời gọi đến một hàm tạo mặc định không tồn tại.

### Bẫy 7 — Mơ hồ kim cương khi không có `virtual`
Không có kế thừa ảo, `GradAssistant` (kế thừa từ cả `Student` và `Employee`, cả hai đều kế thừa từ `Person`) có HAI bản sao của `Person`. Bất kỳ truy cập nào đến một thành phần của `Person` mà không định rõ đều bị mơ hồ. Bạn phải dùng `Student::Person::member` hoặc `Employee::Person::member` — nhưng có HAI bản sao, điều này gần như chắc chắn không phải điều bạn muốn.

### Bẫy 8 — Thứ tự hàm hủy NGƯỢC với thứ tự hàm tạo
Dễ quên khi bị áp lực. Hàm tạo: cơ sở → thành viên → thân dẫn xuất. Hàm hủy: thân dẫn xuất → thành viên → cơ sở. Không phải "cơ sở đầu và cuối" — nó đảo ngược.

### Bẫy 9 — Ghi đè ≠ Thay thế
Khi lớp dẫn xuất định nghĩa `void display()` và lớp cơ sở cũng có `void display()`, phiên bản cơ sở bị **ẩn**, không bị xóa. Cả hai cùng tồn tại. Dùng `Base::display()` để truy cập phiên bản bị ẩn. Điều này rất quan trọng khi gọi `display()` từ bên trong lớp dẫn xuất — không có `Base::`, bạn gọi phiên bản dẫn xuất (có thể đệ quy vô hạn).

### Bẫy 10 — Hàm tạo và hàm hủy KHÔNG được kế thừa
Lớp dẫn xuất KHÔNG kế thừa các hàm tạo, hàm hủy, hàm tạo sao chép, hoặc toán tử gán của lớp cơ sở. Lớp dẫn xuất phải tự định nghĩa (hoặc trình biên dịch tự sinh). Hàm tạo dẫn xuất phải gọi hàm tạo cơ sở tường minh hoặc ngầm định.

### Bẫy 11 — Kế thừa Protected biến các thành phần Public thành Protected
Sau kế thừa `protected`, ngay cả các thành phần vốn là `public` của lớp cơ sở cũng trở thành `protected`. Các thể hiện bên ngoài KHÔNG thể truy cập chúng. Chỉ các lớp dẫn xuất sâu hơn mới có thể.

### Bẫy 12 — Kế thừa mặc định cho `class` là `private`
```cpp
class D : B { };  // tương đương: class D : private B { }
```
```cpp
struct D : B { }; // tương đương: struct D : public B { }
```
Quên bộ xác định truy cập trong khai báo `class` mặc định là kế thừa `private`, điều này hầu như không bao giờ là điều bạn muốn.

### Bẫy 13 — Thứ tự khởi tạo thành viên ≠ Thứ tự danh sách khởi tạo
Các thành viên được khởi tạo theo **thứ tự khai báo**, không phải thứ tự chúng xuất hiện trong ctor-initializer. Nếu `b` được khai báo trước `a`, thì `: a(valA), b(valB)` sẽ khởi tạo `b` trước và `a` sau. Điều này có thể gây ra lỗi tinh vi khi một thành viên phụ thuộc vào thành viên khác.

### Bẫy 14 — Tương thích: Dẫn xuất có thể vào Cơ sở, nhưng Cơ sở không thể vào Dẫn xuất
Một hàm mong đợi `Base&` có thể chấp nhận một đối tượng `Derived`. Một hàm mong đợi `Derived&` KHÔNG thể chấp nhận một đối tượng `Base`. Lớp dẫn xuất có mọi thứ lớp cơ sở có (cộng thêm), nhưng không phải ngược lại. Truyền một `Base` vào nơi mong đợi `Derived` sẽ để các trường bổ sung của `Derived` không được khởi tạo.

### Bẫy 15 — Quyền truy cập bạn bè không lan truyền qua kế thừa
Quan hệ bạn bè (Friendship) KHÔNG được kế thừa. Nếu `class B` là bạn của `class A`, và `class D` kế thừa từ `B`, thì `D` KHÔNG tự động là bạn của `A`. Ngược lại, nếu `A` có bạn `F`, các lớp dẫn xuất của `A` KHÔNG tự động coi `F` là bạn cho các thành phần private của riêng chúng.

### Bẫy 16 — Ẩn (Hiding) so với Ghi đè (Overriding)
Trong trường hợp không có `virtual`, một hàm có cùng tên trong lớp dẫn xuất sẽ ẩn (các) hàm của lớp cơ sở. TẤT CẢ các overload của lớp cơ sở với tên đó đều bị ẩn, không chỉ hàm có chữ ký khớp. Để đưa chúng trở lại phạm vi, dùng `using Base::functionName;` trong lớp dẫn xuất.

### Bẫy 17 — Phân giải phạm vi trong kế thừa bội
Khi hai lớp cơ sở định nghĩa một thành phần có cùng tên, MỌI truy cập đến tên đó thông qua lớp dẫn xuất phải được định rõ với `Base1::` hoặc `Base2::`. Không có quy tắc "cái nào khai báo trước thắng" trong C++ tiêu chuẩn — sự mơ hồ là lỗi biên dịch cho đến khi được giải quyết tường minh.

---

## 12. BÀI TẬP VIẾT TAY

### Bài tập 1: Hiệu ứng của Kế thừa Public/Private/Protected lên lớp cháu

**Tình huống:** Cho lớp cơ sở:
```cpp
class Animal {
public:
    void eat();
protected:
    int age;
private:
    int dna;
};
```

Lớp dẫn xuất `Mammal` kế thừa từ `Animal` (cả ba loại kế thừa bên dưới). Một lớp khác `Dog` kế thừa `public` từ `Mammal`. Với MỖI loại kế thừa giữa `Animal` và `Mammal`, hãy theo dõi những gì `Dog` có thể truy cập và những gì `main()` có thể truy cập.

> [!success]- Hiển thị đáp án
> **Trường hợp 1: `class Mammal : public Animal`**
> - `eat()` → `public` trong Mammal → `public` trong Dog → main() CÓ thể gọi
> - `age` → `protected` trong Mammal → `protected` trong Dog → main() KHÔNG thể truy cập
> - `dna` → không thể truy cập trong Mammal → không thể truy cập trong Dog
>
> **Trường hợp 2: `class Mammal : private Animal`**
> - `eat()` → `private` trong Mammal → không thể truy cập trong Dog → main() KHÔNG thể gọi
> - `age` → `private` trong Mammal → không thể truy cập trong Dog → main() KHÔNG thể truy cập
> - `dna` → không thể truy cập → không thể truy cập
> - Mọi thứ từ Animal bị cắt khỏi Dog!
>
> **Trường hợp 3: `class Mammal : protected Animal`**
> - `eat()` → `protected` trong Mammal → `protected` trong Dog → main() KHÔNG thể gọi
> - `age` → `protected` trong Mammal → `protected` trong Dog → main() KHÔNG thể truy cập
> - `dna` → không thể truy cập → không thể truy cập
> - Dog CÓ thể truy cập `eat()` và `age` nội bộ, nhưng client KHÔNG thể

### Bài tập 2: Ctor-Initializer bắt buộc khi lớp cơ sở không có hàm tạo mặc định

**Tình huống:** Sửa lỗi biên dịch:

```cpp
class Vehicle {
    int maxSpeed;
public:
    Vehicle(int ms) { maxSpeed = ms; }   // không có hàm tạo mặc định
};

class Car : public Vehicle {
    int doors;
public:
    Car(int ms, int d) {                 // LỖI BIÊN DỊCH
        doors = d;
    }
};
```

> [!success]- Hiển thị đáp án
> ```cpp
> class Car : public Vehicle {
>     int doors;
> public:
>     Car(int ms, int d)
>         : Vehicle(ms),    // BẮT BUỘC — lớp cơ sở không có hàm tạo mặc định
>           doors(d)         // khởi tạo thành viên
>     { }
> };
> ```
> Lỗi là do `Car(int, int)` đã cố gắng gọi ngầm `Vehicle()` vốn không tồn tại. Ctor-initializer `: Vehicle(ms)` sửa lỗi này bằng cách truyền tường minh tham số cho hàm tạo lớp cơ sở.

### Bài tập 3: Bài toán kim cương KHÔNG có Virtual

**Tình huống:** Theo dõi lỗi biên dịch:

```cpp
class Person {
public:
    string name;
    void setName(string n) { name = n; }
};

class Student : public Person {
public:
    int studentID;
};

class Employee : public Person {
public:
    double salary;
};

class GradAssistant : public Student, public Employee {
public:
    void setup() {
        setName("Alice");   // (A) — LỖI BIÊN DỊCH: mơ hồ
        name = "Alice";     // (B) — LỖI BIÊN DỊCH: mơ hồ
    }
};
```

Giải thích sự mơ hồ và sửa nó KHÔNG dùng virtual (chỉ phân giải lớp cơ sở tường minh).

> [!success]- Hiển thị đáp án
> `GradAssistant` có HAI đối tượng con `Person` — một qua `Student` và một qua `Employee`. Cả hai đều chứa `name` và `setName()`. Trình biên dịch không biết bạn muốn cái nào.
>
> **Sửa không dùng virtual:**
> ```cpp
> void setup() {
>     Student::setName("Alice");     // dùng bản sao Person của Student
>     Student::name = "Alice";       // dùng bản sao Person của Student
>     // HOẶC
>     Employee::setName("Alice");    // dùng bản sao Person của Employee
> }
> ```
> Nhưng lưu ý: điều này tạo ra HAI tên riêng biệt — một trong Person của Student và một trong Person của Employee. Chúng có thể khác nhau. Lớp cơ sở ảo là giải pháp đúng đắn.

### Bài tập 4: Bài toán kim cương CÓ Virtual

**Tình huống:** Viết lại hệ thống phân cấp từ Bài tập 3 sử dụng lớp cơ sở ảo để `GradAssistant` có một `name` duy nhất.

> [!success]- Hiển thị đáp án
> ```cpp
> class Person {
> public:
>     string name;
>     void setName(string n) { name = n; }
>     Person(string n) : name(n) { }
> };
>
> class Student : virtual public Person {
> public:
>     int studentID;
>     Student(string n, int id) : Person(n), studentID(id) { }
> };
>
> class Employee : virtual public Person {
> public:
>     double salary;
>     Employee(string n, double s) : Person(n), salary(s) { }
> };
>
> class GradAssistant : public Student, public Employee {
> public:
>     double stipend;
>     GradAssistant(string n, int id, double s, double st)
>         : Person(n),              // LỚP DẪN XUẤT XA NHẤT khởi tạo lớp cơ sở ảo
>           Student(n, id),         // Person(n) ở đây bị BỎ QUA
>           Employee(n, s),         // Person(n) ở đây bị BỎ QUA
>           stipend(st)
>     { }
>
>     void setup() {
>         setName("Alice");   // GIỜ biên dịch tốt — một Person duy nhất
>         name = "Alice";     // GIỜ biên dịch tốt — một Person duy nhất
>     }
> };
> ```
> Với kế thừa `virtual`, `GradAssistant` có MỘT `Person` được chia sẻ. Mọi sự mơ hồ được giải quyết.

### Bài tập 5: Ép kiểu con trỏ — Lên và Xuống

**Tình huống:** Đánh dấu mỗi dòng là OK (biên dịch + an toàn), LỖI (không biên dịch), hoặc RỦI RO (biên dịch nhưng không an toàn):

```cpp
class Shape { public: virtual void draw(); };
class Circle : public Shape { public: double radius; void draw() override; };
class Square : public Shape { public: double side; void draw() override; };

int main() {
    Circle c;
    Square sq;

    Shape* s1 = &c;                 // (1)
    Circle* c1 = s1;                // (2)
    Circle* c2 = (Circle*) s1;      // (3)
    Shape* s2 = &sq;
    Circle* c3 = (Circle*) s2;      // (4)
}
```

> [!success]- Hiển thị đáp án
> **(1):** OK — Upcast từ `Circle*` lên `Shape*`, ngầm định và an toàn.
>
> **(2):** LỖI — Downcast không ngầm định. Biên dịch thất bại.
>
> **(3):** RỦI RO — Ép kiểu C biên dịch được nhưng `s1` thực sự trỏ tới một `Circle`, nên tình cờ an toàn. Nhưng trình biên dịch không kiểm tra.
>
> **(4):** RỦI RO — `s2` trỏ tới một `Square`, nhưng bị ép thành `Circle*`. Ép kiểu biên dịch được, nhưng truy cập `c3->radius` là **hành vi không xác định** — `Square` không có `radius` tại offset đó. Đây là hiểm họa downcast kinh điển.

### Bài tập 6: Phân giải mơ hồ kế thừa bội

**Tình huống:** Triển khai hàm `setup()` với phân giải tường minh thích hợp:

```cpp
class Scanner {
public:
    int resolution;
    void start() { cout << "Scanner started"; }
};

class Printer {
public:
    int resolution;
    void start() { cout << "Printer started"; }
};

class AllInOne : public Scanner, public Printer {
public:
    void setup() {
        // (1) Đặt Scanner resolution thành 600
        // (2) Đặt Printer resolution thành 1200
        // (3) Gọi start() của Scanner
        // (4) Gọi start() của Printer
    }
};
```

> [!success]- Hiển thị đáp án
> ```cpp
> void setup() {
>     Scanner::resolution = 600;    // (1) phạm vi tường minh
>     Printer::resolution = 1200;   // (2) phạm vi tường minh
>     Scanner::start();             // (3) phạm vi tường minh
>     Printer::start();             // (4) phạm vi tường minh
> }
> ```
> Không có `Scanner::` và `Printer::`, cả `resolution` và `start()` đều là lỗi biên dịch mơ hồ. C++ yêu cầu phân giải phạm vi tường minh cho các thành phần xung đột trong kế thừa bội.

### Bài tập 7: Thứ tự xây dựng — Thành phần + Kế thừa

**Tình huống:** Cho các lớp bên dưới, hãy viết đầu ra của chương trình:

```cpp
class Engine {
public:
    Engine() { cout << "Engine ctor "; }
    ~Engine() { cout << "Engine dtor "; }
};

class Vehicle {
public:
    Vehicle() { cout << "Vehicle ctor "; }
    ~Vehicle() { cout << "Vehicle dtor "; }
};

class Car : public Vehicle {
    Engine myEngine;
public:
    Car() { cout << "Car ctor "; }
    ~Car() { cout << "Car dtor "; }
};

int main() {
    Car c;
    return 0;
}
```

> [!success]- Hiển thị đáp án
> **Đầu ra:** `Vehicle ctor Engine ctor Car ctor Car dtor Engine dtor Vehicle dtor`
>
> **Thứ tự hàm tạo:** Base `Vehicle` đầu tiên → thành viên `Engine` (theo thứ tự khai báo) → thân `Car`.
>
> **Thứ tự hàm hủy:** Ngược chính xác — thân `Car` → `Engine` → `Vehicle`.

### Bài tập 8: Thiết kế hoàn chỉnh từ đầu — Hệ thống Thư viện

**Tình huống:** Thiết kế một hệ thống thư viện với kế thừa.

Yêu cầu:
- Tất cả các mục có `title`, `callNumber` và phương thức `checkout(string patron)`.
- `Book` thêm `author` và `ISBN`.
- `Journal` thêm `volume` và `issueNumber`.
- `DigitalMedia` thêm `fileSize` và `format`.
- `AudioBook` IS A `Book` VÀ IS A `DigitalMedia` — nó cần `narrator` và `duration`.

Viết toàn bộ khai báo lớp bao gồm các hàm tạo. Sử dụng kế thừa ảo khi cần.

> [!success]- Hiển thị đáp án
> ```cpp
> class LibraryItem {
> protected:
>     string title;
>     string callNumber;
> public:
>     LibraryItem(string t, string cn) : title(t), callNumber(cn) {}
>     virtual void checkout(string patron) {
>         cout << title << " checked out to " << patron;
>     }
>     virtual ~LibraryItem() {}
> };
>
> class Book : virtual public LibraryItem {
> protected:
>     string author;
>     string ISBN;
> public:
>     Book(string t, string cn, string a, string isbn)
>         : LibraryItem(t, cn), author(a), ISBN(isbn) {}
> };
>
> class DigitalMedia : virtual public LibraryItem {
> protected:
>     double fileSize;
>     string format;
> public:
>     DigitalMedia(string t, string cn, double fs, string fmt)
>         : LibraryItem(t, cn), fileSize(fs), format(fmt) {}
> };
>
> class Journal : public LibraryItem {
>     int volume;
>     int issueNumber;
> public:
>     Journal(string t, string cn, int v, int i)
>         : LibraryItem(t, cn), volume(v), issueNumber(i) {}
> };
>
> class AudioBook : public Book, public DigitalMedia {
>     string narrator;
>     double duration;
> public:
>     AudioBook(string t, string cn, string a, string isbn,
>               double fs, string fmt, string narr, double dur)
>         : LibraryItem(t, cn),    // lớp dẫn xuất xa nhất khởi tạo lớp cơ sở ảo
>           Book(t, cn, a, isbn),  // Lời gọi LibraryItem() bị bỏ qua
>           DigitalMedia(t, cn, fs, fmt), // Lời gọi LibraryItem() bị bỏ qua
>           narrator(narr),
>           duration(dur)
>     {}
>
>     void checkout(string patron) override {
>         cout << "Audiobook \"" << title << "\" (narrated by "
>              << narrator << ") checked out to " << patron;
>     }
> };
> ```
>
> **Giải thích thiết kế:**
> - `LibraryItem` là lớp cơ sở ảo vì `AudioBook` kế thừa từ CẢ `Book` VÀ `DigitalMedia`, cả hai đều dẫn xuất từ `LibraryItem` → bài toán kim cương.
> - `Book` dùng `virtual public` để `AudioBook` có MỘT `LibraryItem`.
> - `DigitalMedia` dùng `virtual public` vì lý do tương tự.
> - `AudioBook` phải gọi tường minh `LibraryItem(t, cn)` với tư cách là lớp dẫn xuất xa nhất.

### Bài tập 9: Theo dõi mức truy cập qua nhiều thế hệ

**Tình huống:** Theo dõi mỗi lần truy cập được đánh số là HỢP LỆ hay KHÔNG HỢP LỆ:

```cpp
class A {
private:   int a1;
protected: int a2;
public:    int a3;
};

class B : protected A {
public:
    void testB() {
        a1 = 1;    // (1)
        a2 = 2;    // (2)
        a3 = 3;    // (3)
    }
};

class C : public B {
public:
    void testC() {
        a1 = 1;    // (4)
        a2 = 2;    // (5)
        a3 = 3;    // (6)
    }
};

int main() {
    B b;
    b.a2 = 5;     // (7)
    b.a3 = 5;     // (8)

    C c;
    c.a3 = 5;     // (9)
}
```

> [!success]- Hiển thị đáp án
> **(1):** KHÔNG HỢP LỆ — `a1` là `private` trong A, không thể truy cập trong B.
>
> **(2):** HỢP LỆ — `a2` là `protected` trong A → `protected` trong B (kế thừa protected bảo toàn protected) → có thể truy cập trong B.
>
> **(3):** HỢP LỆ — `a3` là `public` trong A → `protected` trong B (kế thừa protected giới hạn ở protected) → có thể truy cập trong B.
>
> **(4):** KHÔNG HỢP LỆ — `a1` là `private` trong A → không thể truy cập trong B → vẫn không thể truy cập trong C.
>
> **(5):** HỢP LỆ — `a2` là `protected` trong A → `protected` trong B → `protected` trong C (kế thừa public bảo toàn nó) → có thể truy cập trong C.
>
> **(6):** HỢP LỆ — `a3` là `public` trong A → `protected` trong B → `protected` trong C (kế thừa public bảo toàn nó) → có thể truy cập trong C.
>
> **(7):** KHÔNG HỢP LỆ — `a2` là `protected` trong B → bên ngoài main() không thể truy cập.
>
> **(8):** KHÔNG HỢP LỆ — `a3` là `protected` trong B → bên ngoài main() không thể truy cập (đã bị giới hạn bởi kế thừa protected).
>
> **(9):** KHÔNG HỢP LỆ — `a3` là `protected` trong C → bên ngoài main() không thể truy cập. Kế thừa protected từ A→B đã vĩnh viễn biến các thành phần vốn là public thành protected, và kế thừa public B→C không thể "hoàn tác" điều đó.
