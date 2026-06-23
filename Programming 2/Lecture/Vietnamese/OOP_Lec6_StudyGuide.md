# Lec6: Đối tượng (Object) và Lớp (Class) trong C++ — Hướng dẫn Ôn tập

---

## 1. THẺ KHÁI NIỆM: Định nghĩa Lớp (Class) & Vòng đời Đối tượng (Object) trong C++

### 1.1 Định nghĩa

Trong C++, một **lớp (class)** là một kiểu do người dùng định nghĩa, đóng gói **thành phần dữ liệu (data members)** (trạng thái/thuộc tính) và **hàm thành phần (member functions)** (hành vi/thao tác) vào một khối đơn vị có tên. Cú pháp:

```
class tên_lớp { Danh_sách_Thành_phần };
```

Trong đó `Danh_sách_Thành_phần` bao gồm `Biến_Thành_phần | Hàm_Thành_phần`. Từ khuôn mẫu này, bạn tạo ra các **đối tượng (objects)** (thể hiện) bằng cách khai báo một biến có kiểu lớp đó: `tên_lớp định_danh;`

> [!success]- Show Answer — Cú pháp Hình thức Định nghĩa Lớp
> > ```
> > class tên_lớp { Danh_sách_Thành_phần };  // Lớp (Class)
> > tên_lớp định_danh;                        // Đối tượng (Object)
> > Danh_sách_Thành_phần ::= Biến_Thành_phần | Hàm_Thành_phần
> > ```

### 1.2 Vấn đề Nó Giải Quyết

Trước khi có lớp (class) trong C, bạn quản lý dữ liệu liên quan bằng struct nhưng các hàm tồn tại riêng rẽ. Nếu cần một `Point` với tọa độ x,y, bạn viết một struct và các hàm độc lập như `getX(Point* p)`. Không có cơ chế nào đảm bảo chỉ các hàm được phép mới thao tác trên dữ liệu.

Lớp (class) giải quyết:
- **Đóng gói (Bundling)** — dữ liệu và các hàm thao tác trên nó nằm trong cùng một ranh giới
- **Kiểm soát truy cập (Access control)** — bạn khai báo những gì bên ngoài có thể chạm vào (public) so với những gì là nội bộ (private)
- **Vòng đời tự động (Automatic lifecycle)** — hàm tạo (constructor) và hàm hủy (destructor) xử lý khởi tạo và dọn dẹp
- **Ngữ nghĩa sao chép (Copy semantics)** — bạn kiểm soát cách các đối tượng được nhân bản (sâu (deep) vs. nông (shallow))
- **An toàn kiểu (Type safety)** — trình biên dịch đảm bảo ai có thể gọi cái gì trên đối tượng nào

> [!success]- Show Answer — Struct vs. Class: khác biệt thực tế
> > Trong C++, `struct` và `class` gần như giống hệt nhau. Điểm khác biệt DUY NHẤT: `struct` mặc định là `public`, `class` mặc định là `private`. Theo quy ước, `struct` được dùng cho các túi dữ liệu thụ động, `class` cho các kiểu đóng gói có bất biến (invariants).

### 1.3 Cách Hoạt Động (từng bước)

1. Bạn **định nghĩa** một lớp, liệt kê các thành phần dữ liệu private và các hàm thành phần public.
2. **Trình biên dịch** cấp phát bộ nhớ cho vtable và mã của lớp; chưa có bộ nhớ dữ liệu.
3. Khi bạn **khai báo** một đối tượng (ví dụ: `Point p;`), hàm tạo (constructor) chạy, cấp phát bộ nhớ cho từng đối tượng cho các thành phần dữ liệu.
4. Mỗi đối tượng có **bản sao riêng** của mọi thành phần dữ liệu (non-static). Tất cả các đối tượng **chia sẻ** một bản sao mã của hàm thành phần.
5. Các **nhãn truy cập (access labels)** (public/private/protected) được thực thi tại thời điểm biên dịch — không phải lúc chạy.
6. Khi một đối tượng ra khỏi phạm vi (stack) hoặc bị `delete` (heap), **hàm hủy (destructor)** chạy.
7. Bộ nhớ của đối tượng được thu hồi; danh tính của nó không còn tồn tại.

> [!success]- Show Answer — Dấu vết Vòng đời
> > ```
> > định nghĩa lớp → trình biên dịch ghi lại bố cục
> >                        ↓
> > gọi hàm tạo → bộ nhớ được cấp phát, các thành phần được khởi tạo → đối tượng RA ĐỜI
> >                        ↓
> > gọi hàm thành phần → thông điệp được nhận, trạng thái được thay đổi
> >                        ↓
> > gọi hàm hủy → dọn dẹp, giải phóng bộ nhớ → đối tượng CHẾT
> > ```

### 1.4 Ví dụ Cụ Thể (lớp Transcript cho hệ thống đăng ký đại học)

```cpp
class Transcript {
private:
    char studentID[20];
    char courseCode[20];
    float grade;
    int credits;
public:
    Transcript(const char* sid, const char* cc, float g, int cr);
    float getGrade() const;
    int getCredits() const;
    void setGrade(float newGrade);
    float calculateGradePoint() const;
};
```

Một trường đại học tạo một đối tượng `Transcript` cho mỗi cặp sinh viên–khóa học. Mỗi bảng điểm giữ `grade`, `studentID`, v.v. riêng của nó. Mã của phương thức `calculateGradePoint()` được viết một lần nhưng thực thi trên mỗi bảng điểm một cách độc lập. Phương thức `setGrade()` cung cấp khả năng thay đổi có kiểm soát — giáo sư không thể trực tiếp ghi `transcript.grade = 4.0;` vì `grade` là private.

> [!success]- Show Answer — Dấu vết: điều gì xảy ra với `Transcript t("A123", "CS101", 3.5, 4);`?
> > 1. Hàm tạo chạy: sao chép "A123" vào `studentID`, "CS101" vào `courseCode`, lưu `grade=3.5`, `credits=4`.
> > 2. Đối tượng `t` tồn tại với bản sao riêng của cả bốn thành phần dữ liệu.
> > 3. Mã cho `getGrade()`, `getCredits()`, `setGrade()`, `calculateGradePoint()` được chia sẻ với tất cả các đối tượng Transcript khác.
> > 4. Chỉ các thành phần `public` mới có thể gọi được từ bên ngoài — `t.getGrade()` hoạt động; truy cập trực tiếp `t.grade` là lỗi biên dịch.

### 1.5 Nó KHÔNG Phải Là

- **KHÔNG tự động an toàn bộ nhớ như Java/C#.** C++ cung cấp cho bạn con trỏ thô, `new`/`delete` thủ công, và không có bộ gom rác. Quên `delete` gây rò rỉ bộ nhớ; gọi `delete` hai lần gây treo máy (crash).
- **KHÔNG cung cấp sao chép sâu (deep copy) tự động.** Hàm tạo sao chép (copy constructor) do trình biên dịch sinh ra thực hiện **sao chép nông (shallow copy)** — nếu lớp của bạn có con trỏ trỏ đến bộ nhớ động, cả hai đối tượng sẽ trỏ đến cùng một bộ nhớ. Đây chính là vấn đề **Quy tắc Ba (Rule of Three)**: nếu bạn cần hàm hủy (destructor), hàm tạo sao chép (copy constructor), hoặc toán tử gán (assignment operator), bạn gần như chắc chắn cần cả ba.
- **KHÔNG tương đương với struct trong C.** Một struct trong C không có hàm thành phần, không có kiểm soát truy cập, không có hàm tạo, không có hàm hủy.
- **KHÔNG giống với đối tượng (object).** Lớp (class) là bản thiết kế; đối tượng (object) là thể hiện. Nhiều sinh viên nhầm lẫn `Point` (lớp) với `Point p` (đối tượng).

> [!success]- Show Answer — Quy tắc Ba (Rule of Three)
> > Nếu lớp của bạn cần bất kỳ một trong: hàm hủy (destructor), hàm tạo sao chép (copy constructor), hoặc toán tử gán sao chép (copy assignment operator), thì gần như chắc chắn nó cần CẢ BA. Các phiên bản do trình biên dịch sinh ra thực hiện sao chép nông (shallow copy), điều này rất tai hại khi bạn sở hữu bộ nhớ động.

---

## 2. CÚ PHÁP ĐỊNH NGHĨA LỚP

### 2.1 Cấu trúc Cơ bản

```cpp
class tên_lớp { Danh_sách_Thành_phần };
```

- `Danh_sách_Thành_phần` bao gồm không hoặc nhiều biến thành phần và hàm thành phần
- `tên_lớp định_danh;` tạo một đối tượng (một thể hiện) của lớp đó
- Dấu **chấm phẩy** sau dấu ngoặc nhọn đóng là BẮT BUỘC

> [!success]- Show Answer — Lớp hợp lệ tối thiểu
> > ```cpp
> > class Empty { };
> > // Lớp không có thành phần nào — vẫn là C++ hợp lệ. Chiếm 1 byte.
> > ```

### 2.2 Ví dụ Lớp Point (ĐẦY ĐỦ từ bài giảng)

```cpp
class Point {
private:
    int x, y;  // tọa độ — ẩn khỏi người ngoài
public:
    Point(int xVal = 0, int yVal = 0) { x = xVal; y = yVal; }
    int getX() { return x; }
    int getY() { return y; }
};
```

Đây là `Lec6_ex1-Point.cpp` từ bài giảng. Các quan sát chính:
- `x` và `y` là `private` — không có mã bên ngoài nào có thể đọc hoặc ghi chúng trực tiếp.
- `Point(int xVal = 0, int yVal = 0)` là một hàm tạo (constructor) với các giá trị tham số mặc định. Điều này làm cho `Point p;` hợp lệ (mặc định là `Point(0,0)`).
- `getX()` và `getY()` là `public` — chúng tạo thành giao diện truy cập chỉ-đọc.
- Không có phương thức setter — Point này là bất biến sau khi xây dựng (không có `setX`/`setY`).

> [!success]- Show Answer — Dấu vết: `Point p(5,10); cout << p.getX();`
> > 1. Hàm tạo `Point(5,10)` chạy: `x = 5`, `y = 10`.
> > 2. `p.getX()` gọi phương thức public.
> > 3. Phương thức trả về `p.x` là `5`.
> > 4. In ra `5`.
> > 5. Truy cập trực tiếp `p.x` sẽ là lỗi biên dịch — `x` là private.

### 2.3 Hàm Thành phần (Member Functions)

Một **hàm thành phần (member function)** (còn gọi là **phương thức (method)**) là một hàm có định nghĩa hoặc nguyên mẫu xuất hiện bên trong định nghĩa lớp.

Quy tắc quan trọng: **Mã hàm được CHIA SẺ giữa tất cả các đối tượng; thành phần dữ liệu thì KHÔNG được chia sẻ.**

```
Point P(5,10);   // P có x=5, y=10 riêng
Point Q(20,10);  // Q có x=20, y=10 riêng
Point R(50,60);  // R có x=50, y=60 riêng

// Trong bộ nhớ:
// P: [x=5][y=10]  ——+
// Q: [x=20][y=10] ——+——→ mã được chia sẻ: getX() { return x; }, getY() { return y; }
// R: [x=50][y=60] ——+
//
// Mỗi đối tượng lưu trữ x,y riêng. Mã getX/getY tồn tại MỘT LẦN.
```

> [!success]- Show Answer — Tại sao mã được chia sẻ?
> > Hiệu quả bộ nhớ. Nếu bạn có 10.000 đối tượng Point, bạn không muốn 10.000 bản sao của `getX()` trong RAM. Trình biên dịch sinh ra một bản sao của mỗi hàm thành phần. Tại thời điểm gọi, địa chỉ của đối tượng được truyền ngầm (qua con trỏ `this`) để hàm biết cần truy cập dữ liệu của đối tượng nào.

> [!success]- Show Answer — Thành phần dữ liệu static là ngoại lệ
> > Một thành phần dữ liệu `static` ĐƯỢC chia sẻ giữa tất cả các đối tượng. Nó thuộc về lớp, không thuộc về bất kỳ thể hiện cụ thể nào. Chỉ tồn tại một bản sao bất kể có bao nhiêu đối tượng được tạo ra.

### 2.4 Hàm Nội Tuyến (Inline Functions)

Ba kiểu trong C++:

| Kiểu | Vị trí Định nghĩa | inline? |
|---|---|---|
| **Trong dòng (In-line)** | Bên trong thân lớp | Ngầm định inline |
| **Ngoài dòng (Out-of-line)** | Bên ngoài thân lớp | KHÔNG inline (trừ khi thêm từ khóa `inline`) |
| **Ngoài dòng + inline** | Bên ngoài thân lớp với từ khóa `inline` | Tường minh inline |

Ví dụ trong bài giảng:

```cpp
class Point {
    ...
public:
    void setX(int valX) { x = valX; }   // Trong dòng: định nghĩa BÊN TRONG lớp → ngầm định inline
    void setY(int valY);                  // Ngoài dòng: chỉ KHAI BÁO ở đây
    void delta(int dx, int dy);           // Ngoài dòng: chỉ KHAI BÁO ở đây
};

void Point::setY(int valY) {            // Định nghĩa ngoài dòng
    y = valY;
}

inline void Point::delta(int dx, int dy) {  // Ngoài dòng + từ khóa inline
    x += dx;
    y += dy;
}
```

> [!success]- Show Answer — Bỏ qua kiểu trả về trong ngoài dòng — tại sao không tốt
> > Bài giảng đề cập "Bỏ qua tên thì được phép nhưng đừng làm vậy." Đối với định nghĩa ngoài dòng, bạn BẮT BUỘC phải bao gồm kiểu trả về. Đối với định nghĩa trong dòng, kiểu trả về vẫn được yêu cầu — slide bài giảng có thể đang đề cập đến điều gì khác hoặc chứa một lỗi. Luôn viết đầy đủ kiểu trả về.

> [!success]- Show Answer — inline là một gợi ý, không phải mệnh lệnh
> > Trình biên dịch quyết định có thực sự nội tuyến (inline) hay không. `inline` là một gợi ý rằng bạn muốn thân hàm được chèn tại vị trí gọi (tránh chi phí gọi hàm). Trình biên dịch có thể bỏ qua nó. Các trình biên dịch hiện đại tự động nội tuyến mạnh mẽ với các cờ tối ưu hóa.

> [!success]- Show Answer — Khi nào BẮT BUỘC phải dùng ngoài dòng?
> > Khi định nghĩa hàm phụ thuộc vào các kiểu hoặc lớp chưa được định nghĩa đầy đủ tại điểm định nghĩa lớp (các tình huống khai báo trước (forward declaration)), hoặc khi bạn muốn tách giao diện (.h) khỏi cài đặt (.cpp).

### 2.5 Hàm Thành phần Hằng số (Constant Member Functions)

Một hàm thành phần `const` **đảm bảo** rằng trạng thái của đối tượng hiện tại KHÔNG bị thay đổi.

**Cú pháp:** `const` đặt SAU danh sách tham số:

```cpp
class Point {
public:
    int getX() const { return x; }   // const: sẽ KHÔNG thay đổi đối tượng này
    int getY() const { return y; }   // const: sẽ KHÔNG thay đổi đối tượng này
};
```

Các quy tắc chính:
- Chỉ các hàm thành phần `const` mới có thể được gọi trên các đối tượng `const`.
- Một hàm thành phần `const` không thể thay đổi BẤT KỲ thành phần dữ liệu nào (non-static).
- Một hàm thành phần `const` không thể gọi các hàm thành phần không phải `const` trên cùng một đối tượng.
- Tham khảo bài giảng: `Lec6_ex4_ConstantMember_Function.cpp`

> [!success]- Show Answer — Đối tượng const, phương thức non-const = lỗi biên dịch
> > ```cpp
> > const Point p(5, 10);
> > p.getX();        // OK: getX() là const
> > p.setX(20);      // LỖI: setX() KHÔNG phải const, không thể gọi trên đối tượng const
> > ```

> [!success]- Show Answer — Ngoại lệ từ khóa mutable
> > Một thành phần dữ liệu được khai báo `mutable` CÓ THỂ được sửa đổi bên trong hàm thành phần `const`. Điều này dành cho các giá trị được lưu trong bộ nhớ đệm, bộ đếm tham chiếu, mutex — siêu dữ liệu không làm thay đổi trạng thái logic của đối tượng.

---

## 3. KIỂM SOÁT TRUY CẬP THÀNH PHẦN

### 3.1 Ba Bổ từ (Modifiers)

```cpp
class tên_lớp {
public:      // có thể truy cập từ bất kỳ đâu
protected:   // có thể truy cập từ lớp này và các lớp dẫn xuất
private:     // chỉ có thể truy cập từ lớp này (MẶC ĐỊNH trong class)
};
```

> [!success]- Show Answer — Mức truy cập mặc định
> > Trong một `class`, các thành phần là `private` theo mặc định cho đến khi gặp một nhãn truy cập khác. Trong một `struct`, các thành phần là `public` theo mặc định.

### 3.2 Bảng Quy tắc Truy cập

| Loại Thành phần | Thành phần cùng Lớp | Bạn (Friend) | Thành phần Lớp dẫn xuất | Hàm không phải Thành phần |
|---|---|---|---|---|
| Private (Mặc định) | X | X | — | — |
| Protected | X | X | X | — |
| Public | X | X | X | X |

- **X** = được phép truy cập
- **—** = bị từ chối truy cập
- Một `friend` (bạn) KHÔNG phải là thành phần — nó là một thực thể bên ngoài được cấp quyền truy cập đặc biệt.

> [!success]- Show Answer — Truy cập là theo LỚP, không phải theo ĐỐI TƯỢNG
> > Một hàm thành phần của `Point` có thể truy cập các thành phần private của BẤT KỲ đối tượng `Point` nào được truyền vào nó — không chỉ `this`. Hai đối tượng của cùng một lớp có thể chạm vào dữ liệu private của nhau:
> > ```cpp
> > class Point {
> > private: int x, y;
> > public:
> >     void copyFrom(const Point& other) { x = other.x; y = other.y; } // OK!
> > };
> > ```

### 3.3 Quy tắc Thực hành

- **Thành phần public:** truy cập bằng toán tử dấu chấm `.` — `p.getX();`
- **Thành phần Private/Protected từ bên ngoài:** HOÀN TOÀN KHÔNG ĐƯỢC TRUY CẬP. `p.x` là lỗi biên dịch nếu `x` là private.

> [!success]- Show Answer — Quan niệm sai lầm phổ biến
> > "Nếu tôi có con trỏ, tôi có thể vượt qua private không?" KHÔNG. Kiểm soát truy cập được thực thi tại thời điểm biên dịch. Ngay cả với con trỏ thô và ép kiểu, hành vi không xác định (undefined behavior) là kết quả — trình biên dịch giả định bạn tuân theo các quy tắc.

### 3.4 Ví dụ Point ex2 (y public, x private)

```cpp
class Point {
private:
    int x;
public:
    int y;
    int getX() { return x; }
    int getY() { return y; }
    void setX(int xVal) { x = xVal; }
    void setY(int yVal) { y = yVal; }
};

Point p;
p.setX(300);
p.setY(500);
cout << "x = " << p.getX() << endl;   // hoạt động: getX() là public
cout << "y = " << p.y << endl;         // hoạt động: y là public
// p.x = 300;                          // LỖI: x là private
```

Đây là `Lec6_ex2-Point.cpp` từ bài giảng. Các giá trị được in: `x = 300`, `y = 500`.

> [!success]- Show Answer — Tại sao ai đó lại để y là public?
> > Nhìn chung là thực hành tồi, nhưng bài giảng dùng nó để minh họa sự tương phản. Để `y` là public có nghĩa là bất kỳ ai cũng có thể ghi `p.y = -999;` mà không có kiểm tra. Để nó là private với một setter cho phép kiểm tra: `void setY(int val) { if (val >= 0) y = val; }`.

### 3.5 Lớp Bạn (Friend Class)

Một **lớp bạn (friend class)** có toàn quyền truy cập vào TẤT CẢ các thành phần (private VÀ protected) của lớp cấp quyền.

**Cú pháp:** `friend class B;` bên trong định nghĩa của lớp A.

Ví dụ đầy đủ từ `Lec6_ex3_FriendClass.cpp`:

```cpp
#include <iostream>

class A {
private:
    int a;
public:
    A() { a = 10; }
    void seta(int value);
    friend class B;      // B bây giờ là bạn của A
};

void A::seta(int value) { a = value; }

class B {
private:
    int b;
public:
    void showA(A& x) {
        std::cout << "A::a=" << x.a;   // B truy cập thành phần PRIVATE a của A
    }
};

int main() {
    A a;
    B b;
    a.seta(15);
    b.showA(a);   // in ra: A::a=15
    return 0;
}
```

> [!success]- Show Answer — Tình bạn (Friendship) KHÔNG có tính đối xứng
> > `friend class B` bên trong `A` có nghĩa là B có thể truy cập các thành phần của A. Nó KHÔNG có nghĩa là A có thể truy cập các thành phần của B. Nếu A cũng cần truy cập vào B, thì B phải khai báo riêng `friend class A`.

> [!success]- Show Answer — Tình bạn (Friendship) KHÔNG có tính bắc cầu
> > Nếu A kết bạn với B, và B kết bạn với C, thì C KHÔNG phải là bạn của A. Mỗi tình bạn được cấp độc lập.

> [!success]- Show Answer — Tình bạn (Friendship) KHÔNG có tính kế thừa
> > Nếu A kết bạn với B, và `class D : public B {}`, thì D KHÔNG phải là bạn của A. Các lớp dẫn xuất không kế thừa tình bạn.

> [!success]- Show Answer — Hàm bạn (Friend functions)
> > Bạn cũng có thể khai báo từng hàm riêng lẻ làm bạn: `friend void foo(A& a);` — cấp cho hàm cụ thể đó quyền truy cập vào các thành phần private của A.

---

## 4. HÀM TẠO (CONSTRUCTORS)

### 4.1 Mục đích

Một **hàm tạo (constructor)** được gọi để TẠO một đối tượng. Nó khởi tạo các thành phần dữ liệu của đối tượng và thiết lập trạng thái ban đầu của nó. Được khai báo với: `tênlớp(...);`

Các đặc điểm chính:
- Cùng tên với lớp
- KHÔNG có kiểu trả về (thậm chí không phải `void`)
- Được gọi tự động khi một đối tượng được tạo — bạn KHÔNG BAO GIỜ gọi nó một cách tường minh trên một đối tượng đã tồn tại
- Có thể được nạp chồng (overloaded) (nhiều hàm tạo với danh sách tham số khác nhau)

> [!success]- Show Answer — Một hàm tạo có thể thất bại không?
> > Một hàm tạo KHÔNG THỂ trả về một giá trị lỗi. Nếu việc khởi tạo thất bại, cách chuẩn duy nhất để báo hiệu là ném một ngoại lệ (throw an exception). Hàm hủy (destructor) sẽ KHÔNG được gọi cho một đối tượng được xây dựng một phần nếu hàm tạo ném ngoại lệ.

### 4.2 Các Loại

| Loại | Mô tả | Ví dụ |
|---|---|---|
| **Hàm tạo mặc định (Default constructor)** | Không có tham số (hoặc tất cả tham số có giá trị mặc định) | `Point()` hoặc `Point(int x=0, int y=0)` |
| **Hàm tạo thay thế (có tham số)** | Nhận tham số | `Point(int x, int y)` |
| **Hàm tạo nạp chồng (Overloaded constructors)** | Nhiều hàm tạo với danh sách tham số khác nhau | `Point()` và `Point(int, int)` cùng tồn tại |
| **Hàm tạo sao chép (Copy constructor)** | Khởi tạo với một đối tượng khác cùng lớp | `Point(const Point& other)` |

> [!success]- Show Answer — Hàm tạo mặc định với tất cả tham số mặc định
> > `Point(int xVal = 0, int yVal = 0)` hoạt động như CẢ hàm tạo mặc định LẪN hàm tạo có tham số. `Point p;` gọi nó với các giá trị mặc định, `Point p(5,10);` gọi nó với các giá trị tường minh. Nhưng hãy cẩn thận: nếu bạn thêm một hàm tạo khác như `Point(int xVal)`, bạn có nguy cơ gây mơ hồ khi gọi `Point p;`.

### 4.3 Hàm tạo Sao chép (Copy Constructor)

Tạo một đối tượng bằng cách khởi tạo nó với một đối tượng CÙNG LỚP đã được tạo trước đó.

**Cú pháp:** `ClassName(const ClassName& other);`

- Tham số PHẢI là một tham chiếu (không phải theo giá trị — điều đó sẽ gây đệ quy vô hạn)
- Tham số NÊN là `const` (bạn đang sao chép, không sửa đổi nguồn)
- Nếu bạn KHÔNG định nghĩa hàm tạo sao chép, **trình biên dịch sẽ sinh ra một hàm** thực hiện **sao chép NÔNG (SHALLOW copy)** (sao chép từng thành phần của giá trị/con trỏ)

> [!success]- Show Answer — Khi nào trình biên dịch KHÔNG sinh ra hàm tạo sao chép?
> > Trong C++ hiện đại, trình biên dịch có thể ngầm định xóa (implicitly delete) hàm tạo sao chép nếu: một thành phần có hàm tạo sao chép bị xóa, một thành phần là kiểu chỉ-di-chuyển (move-only type), hoặc một lớp cơ sở có hàm tạo sao chép private/không thể truy cập.

### 4.4 Ví dụ về Các Lời Gọi Hàm tạo

```cpp
Point p;                          // hàm tạo mặc định
Point a(p), b = p;                // hàm tạo sao chép (cả hai cú pháp)
Point c(20, 30);                  // hàm tạo thay thế (có tham số)
Point figure[3];                  // hàm tạo mặc định được gọi 3 lần
Point figure[2] = {p, c};        // hàm tạo sao chép được gọi hai lần
```

> [!success]- Show Answer — `Point b = p;` — điều này có gọi hàm tạo sao chép không?
> > CÓ. Mặc dù có dấu `=`, đây là khởi tạo, KHÔNG phải gán. `Point b = p;` gọi hàm tạo sao chép vì `b` đang được tạo ra. Điều này khác với:
> > ```cpp
> > Point b;      // hàm tạo mặc định
> > b = p;        // TOÁN TỬ GÁN (assignment operator) (không phải hàm tạo sao chép) — khác!
> > ```

> [!success]- Show Answer — Tất cả các tình huống gọi hàm tạo sao chép
> > 1. `ClassName a(b);` — khởi tạo trực tiếp
> > 2. `ClassName a = b;` — khởi tạo sao chép
> > 3. Truyền đối tượng theo giá trị vào hàm: `void foo(ClassName obj);`
> > 4. Trả về đối tượng theo giá trị từ hàm: `ClassName bar() { ClassName c; return c; }`

---

## 5. CON TRỎ ĐẾN ĐỐI TƯỢNG & HÀM HỦY (DESTRUCTORS)

### 5.1 Con trỏ đến Đối tượng Lớp

```cpp
Student *p;                    // khai báo con trỏ — chưa có đối tượng
p = new Student;               // cấp phát động — hàm tạo được gọi
if (!p)                        // kiểm tra nếu cấp phát thất bại (con trỏ null)
    // không thể tạo Student

Point *figure = new Point[10]; // mảng 10 Points — hàm tạo mặc định được gọi 10 lần
```

> [!success]- Show Answer — `if (!p)` trong C++ hiện đại
> > Theo mặc định, `new` ném `std::bad_alloc` khi thất bại thay vì trả về `nullptr`. Kiểm tra `if (!p)` mong đợi phiên bản `nothrow`: `p = new(std::nothrow) Student;`

> [!success]- Show Answer — Con trỏ Tĩnh (Static) vs. Động (Dynamic)
> > ```cpp
> > Point p(5, 10);           // tĩnh: đối tượng trên stack
> > Point* pp = &p;           // con trỏ đến đối tượng tĩnh — KHÔNG cần delete cho pp
> > Point* dp = new Point;    // động: đối tượng trên heap — PHẢI delete dp
> > ```

### 5.2 Hàm hủy (Destructors)

Được gọi khi một đối tượng sắp bị **xóa/phá hủy**. Thực hiện dọn dẹp — giải phóng bộ nhớ động, đóng tệp, giải phóng tài nguyên.

**Khai báo:** `~tênlớp();` — KHÔNG có tham số, KHÔNG có kiểu trả về.

```cpp
class Point {
public:
    ~Point() { cout << "Destructor called." << endl; }
};
```

- Chỉ MỘT hàm hủy trên mỗi lớp (không thể nạp chồng — không có tham số nghĩa là không có chữ ký để phân biệt)
- Hàm hủy được gọi tự động khi:
  - Đối tượng trên stack ra khỏi phạm vi
  - `delete` được gọi trên một đối tượng heap
  - `delete[]` được gọi trên một mảng đối tượng heap
  - Vòng đời của đối tượng tạm thời kết thúc

> [!success]- Show Answer — Thứ tự thực thi bên trong thân hàm hủy
> > 1. Thân hàm hủy thực thi (mã của bạn trong `~ClassName() { ... }`)
> > 2. Hàm hủy của các đối tượng thành phần chạy (theo thứ tự ngược với khai báo)
> > 3. Hàm hủy của lớp cơ sở chạy (trong trường hợp kế thừa)

> [!success]- Show Answer — Hàm hủy ảo (Virtual destructor)
> > Nếu lớp của bạn được thiết kế để làm lớp cơ sở, hãy khai báo hàm hủy là `virtual`. Nếu không có nó, việc xóa một đối tượng dẫn xuất thông qua con trỏ lớp cơ sở chỉ gọi hàm hủy của lớp cơ sở — gây rò rỉ tài nguyên của lớp dẫn xuất. Thông tin thêm trong Lec7/Lec8.

---

## 6. SAO CHÉP SÂU (DEEP COPY) vs SAO CHÉP NÔNG (SHALLOW COPY) (QUAN TRỌNG)

### 6.1 Định nghĩa từ Bài giảng

| Loại | Cơ chế | Sơ đồ Bộ nhớ |
|---|---|---|
| **Sao chép sâu (Deep copy)** | Sao chép NỘI DUNG của dữ liệu | Hai khối bộ nhớ độc lập |
| **Sao chép nông (Shallow copy)** | Sao chép CON TRỎ (địa chỉ) | Hai con trỏ đến cùng một bộ nhớ |

```cpp
// Sao chép NÔNG — sao chép con trỏ, KHÔNG phải dữ liệu
char name[] = "John Smith";
char *cp = name;               // cp trỏ đến cùng mảng với name

// Sao chép SÂU — sao chép dữ liệu thực tế
char name[] = "John Smith";
char *cp = new char[30];
strcpy(cp, name);              // cp có bản sao RIÊNG của các ký tự
```

> [!success]- Show Answer — Hình ảnh sao chép nông
> > ```
> > Nông:     name ──→ ['J']['o']['h']['n'][' ']['S']['m']['i']['t']['h']['\0']
> >           cp   ──→  (cùng bộ nhớ)
> >
> > Sâu:      name ──→ ['J']['o']['h']['n'][' ']['S']['m']['i']['t']['h']['\0']
> >           cp   ──→ ['J']['o']['h']['n'][' ']['S']['m']['i']['t']['h']['\0']  (bản sao riêng)
> > ```

### 6.2 Vấn đề Sao chép Student (Ví dụ bài giảng ĐẦY ĐỦ)

```cpp
#include <string>

class Course {
private:
    string name;
public:
    Course() {}
    Course(const string& cname);
};

class Student {
private:
    Course *coursesTaken;
    unsigned numCourses;
public:
    Student(unsigned nCourses);
    ~Student();
};

Student::Student(unsigned nCourses) {
    coursesTaken = new Course[nCourses];
    numCourses = nCourses;
}

Student::~Student() {
    delete[] coursesTaken;
}
```

**LỖI (BUG):**

```cpp
int nCourses = 7;
Student x(nCourses);   // Hàm tạo: cấp phát mảng 7 Courses → x.coursesTaken
Student y(x);          // Hàm tạo sao chép: DO TRÌNH BIÊN DỊCH SINH RA → sao chép nông!
```

**Điều gì xảy ra:**
- Hàm tạo sao chép do trình biên dịch sinh ra thực hiện **sao chép nông (shallow copy)** của `coursesTaken` (chỉ sao chép địa chỉ con trỏ, KHÔNG phải nội dung mảng).
- Cả `x.coursesTaken` và `y.coursesTaken` đều trỏ đến **CÙNG một mảng các đối tượng Course**.
- Khi hàm hủy của `x` chạy, nó gọi `delete[] coursesTaken` — mảng được giải phóng.
- Khi hàm hủy của `y` chạy, nó gọi `delete[] coursesTaken` trên **CÙNG vùng bộ nhớ đã được giải phóng**.
- **XÓA KÉP (DOUBLE DELETE) → TREO MÁY (CRASH) / hành vi không xác định (undefined behavior).**

> [!success]- Show Answer — Sơ đồ bộ nhớ của lỗi
> > ```
> > Sau Student x(7):
> >   x.coursesTaken ──→ [Course0][Course1][Course2][Course3][Course4][Course5][Course6]
> >
> > Sau Student y(x):  (sao chép nông!)
> >   x.coursesTaken ──→ [Course0][Course1][Course2][Course3][Course4][Course5][Course6]
> >   y.coursesTaken ──→ (cùng mảng!)
> >
> > Sau ~x():
> >   mảng bị XÓA — cả hai con trỏ bây giờ là TREO (DANGLING)
> >
> > Sau ~y():
> >   delete[] trên con trỏ TREO → TREO MÁY!
> > ```

### 6.3 Giải pháp: Hàm tạo Sao chép Tùy chỉnh

```cpp
Student(const Student &s) {
    numCourses = s.getNumCourses();
    coursesTaken = new Course[numCourses];    // 1. CẤP PHÁT một mảng mới, riêng biệt
    for (int i = 0; i < numCourses; i++)
        coursesTaken[i] = s.getCourse(i);     // 2. SAO CHÉP từng Course vào mảng mới
}
```

**Kết quả mong muốn:** `x.coursesTaken` và `y.coursesTaken` bây giờ trỏ đến **các mảng khác nhau** — mỗi mảng có bản sao riêng của các đối tượng Course. Hàm hủy trên `x` chỉ xóa mảng của `x`; mảng của `y` vẫn nguyên vẹn.

> [!success]- Show Answer — Sơ đồ bộ nhớ của cách sửa
> > ```
> > Sau Student x(7):
> >   x.coursesTaken ──→ [C0][C1][C2][C3][C4][C5][C6]
> >
> > Sau Student y(x):  (sao chép sâu!)
> >   x.coursesTaken ──→ [C0][C1][C2][C3][C4][C5][C6]
> >   y.coursesTaken ──→ [C0][C1][C2][C3][C4][C5][C6]  (mảng riêng biệt!)
> >
> > Sau ~x(): mảng của x bị xóa. Mảng của y vẫn hợp lệ.
> > Sau ~y(): mảng của y bị xóa. Không có xóa kép.
> > ```

> [!success]- Show Answer — Còn toán tử gán sao chép (copy assignment operator) thì sao?
> > Vấn đề tương tự tồn tại cho gán. Nếu bạn viết:
> > ```cpp
> > Student y(7);
> > Student x(5);
> > x = y;  // toán tử gán do trình biên dịch sinh ra = SAO CHÉP NÔNG!
> > ```
> > Bạn cũng cần một `Student& operator=(const Student& s)` tùy chỉnh. Đây chính là Quy tắc Ba (Rule of Three) đầy đủ.

> [!success]- Show Answer — Các phương thức trợ giúp cần thiết cho cách sửa
> > ```cpp
> > unsigned getNumCourses() const { return numCourses; }
> > Course getCourse(int i) const { return coursesTaken[i]; }
> > ```

---

## 7. LỚP HỢP THÀNH (COMPOSITE CLASSES)

### 7.1 Định nghĩa

Một **lớp hợp thành (composite class)** là một lớp chứa các thành phần dữ liệu là **các đối tượng của các lớp khác**. Khi một lớp chứa các **thể hiện (instances)**, **tham chiếu (references)**, hoặc **con trỏ (pointers)** đến các lớp khác, nó là một lớp hợp thành.

Ví dụ:
- Một `Circle` chứa một `Point` (tâm)
- Một `Figure` chứa một mảng các `Point`
- Một `Car` chứa một `Engine`, 4 đối tượng `Wheel`
- Một bản ghi `Student` chứa một `Date` (ngày sinh), `Address`, v.v.

> [!success]- Show Answer — Hợp thành vs. thành phần là con trỏ đến lớp
> > ```cpp
> > class Circle {
> >     Point center;        // hợp thành: Point là thành phần TRỰC TIẾP
> >     double radius;
> > };
> >
> > class Drawing {
> >     Point* points;       // con trỏ đến mảng: vẫn là hợp thành
> >     int numPoints;
> > };
> > ```

### 7.2 Thứ tự Xây dựng/Hủy bỏ Được Định nghĩa Trước

Các quy tắc này được **đảm bảo bởi chuẩn C++** và KHÔNG THỂ thay đổi:

1. **Thứ tự xây dựng (Construction order):**
   - Hàm tạo cho TẤT CẢ các đối tượng thành phần thực thi theo **thứ tự chúng xuất hiện trong định nghĩa lớp** (KHÔNG phải thứ tự trong danh sách khởi tạo (initializer list)!).
   - Tất cả các hàm tạo thành phần thực thi **TRƯỚC** thân của hàm tạo lớp bao ngoài.

2. **Thứ tự hủy bỏ (Destruction order):**
   - Hàm hủy được gọi theo **thứ tự NGƯỢC** với hàm tạo.
   - Thân của hàm hủy lớp bao ngoài thực thi **TRƯỚC** các hàm hủy của các đối tượng thành phần của nó.

> [!success]- Show Answer — Hình ảnh hóa thứ tự xây dựng
> > ```cpp
> > class Composite {
> >     MemberA a;   // được khai báo TRƯỚC → hàm tạo chạy TRƯỚC
> >     MemberB b;   // được khai báo THỨ HAI → hàm tạo chạy THỨ HAI
> >     MemberC c;   // được khai báo THỨ BA → hàm tạo chạy THỨ BA
> > public:
> >     Composite() : c(1), a(2), b(3) {  // thứ tự danh sách khởi tạo KHÔNG QUAN TRỌNG
> >         // thân hàm chạy SAU tất cả các hàm tạo thành phần
> >     }
> >     ~Composite() {
> >         // thân hàm chạy TRƯỚC
> >     }  // sau đó ~c(), sau đó ~b(), sau đó ~a() — NGƯỢC với thứ tự khai báo
> > };
> > ```
> > Danh sách khởi tạo ghi `c, a, b` — nhưng thực tế thực thi là `a, b, c` (thứ tự khai báo).

> [!success]- Show Answer — Hình ảnh hóa thứ tự hủy bỏ
> > ```
> > Xây dựng:  a() → b() → c() → thân Composite
> > Hủy bỏ:   ~thân Composite → ~c() → ~b() → ~a()
> > ```

> [!success]- Show Answer — Tại sao thứ tự ngược?
> > Bởi vì các đối tượng được xây dựng sau có thể phụ thuộc vào các đối tượng được xây dựng trước. Trong quá trình hủy bỏ, các phụ thuộc phải được tháo gỡ một cách an toàn — đối tượng phụ thuộc vẫn phải tồn tại khi phụ thuộc của nó bị hủy.

### 7.3 Bài tập từ Bài giảng

Bài giảng yêu cầu bạn **viết một chương trình để kiểm tra thứ tự này**. Đây là nội dung cần viết:

> [!success]- Show Answer — Chương trình kiểm tra thứ tự xây dựng/hủy bỏ
> > ```cpp
> > #include <iostream>
> > using namespace std;
> >
> > class A {
> > public:
> >     A()  { cout << "A() "; }
> >     ~A() { cout << "~A() "; }
> > };
> >
> > class B {
> > public:
> >     B()  { cout << "B() "; }
> >     ~B() { cout << "~B() "; }
> > };
> >
> > class C {
> >     A a;  // được khai báo TRƯỚC
> >     B b;  // được khai báo THỨ HAI
> > public:
> >     C()  { cout << "C() "; }
> >     ~C() { cout << "~C() "; }
> > };
> >
> > int main() {
> >     C obj;
> >     return 0;
> > }
> > // Đầu ra mong đợi: A() B() C() ~C() ~B() ~A()
> > ```

---

## 8. KHUÔN MẪU CÚ PHÁP CẦN GHI NHỚ

### Khuôn mẫu 1: Định nghĩa Lớp Cơ bản với private/public

```cpp
class ClassName {
private:
    // thành phần dữ liệu — mỗi đối tượng có bản sao riêng
    int data1;
    double data2;
public:
    // hàm thành phần — được chia sẻ giữa tất cả các đối tượng
    ClassName(int d1, double d2);
    int getData1() const;
    void setData2(double val);
};  // ← CHẤM PHẨY BẮT BUỘC
```

### Khuôn mẫu 2: Hàm Thành phần Trong dòng (Inline) vs. Ngoài dòng (Out-of-line)

```cpp
class Point {
private:
    int x, y;
public:
    void setX(int valX) { x = valX; }         // Trong dòng: định nghĩa BÊN TRONG lớp
    void setY(int valY);                        // Ngoài dòng: chỉ KHAI BÁO ở đây
    int getX() const { return x; }             // Trong dòng + const
};

void Point::setY(int valY) { y = valY; }       // ĐỊNH NGHĨA ngoài dòng
```

### Khuôn mẫu 3: Hàm Thành phần const

```cpp
class Point {
    int x, y;
public:
    int getX() const { return x; }    // const SAU danh sách tham số
    int getY() const;                  // const trong CẢ khai báo LẪN định nghĩa
};

int Point::getY() const {             // const PHẢI xuất hiện trong định nghĩa nữa
    return y;
}
```

### Khuôn mẫu 4: Hàm tạo (Mặc định, Thay thế, Sao chép)

```cpp
class Point {
    int x, y;
public:
    Point() { x = 0; y = 0; }                       // Mặc định: không tham số
    Point(int xVal, int yVal) { x = xVal; y = yVal; } // Thay thế: có tham số
    Point(const Point& other) { x = other.x; y = other.y; } // Hàm tạo sao chép
};
```

### Khuôn mẫu 5: Hàm hủy (Destructor)

```cpp
class Student {
    Course* coursesTaken;
public:
    ~Student() {                   // Không tham số, không kiểu trả về
        delete[] coursesTaken;     // Dọn dẹp bộ nhớ động
        coursesTaken = nullptr;    // Ngăn con trỏ treo (phòng thủ)
    }
};
```

### Khuôn mẫu 6: Mẫu Hàm tạo Sao chép Sâu (Deep Copy Constructor)

```cpp
class MyClass {
    int* data;
    int size;
public:
    MyClass(int s) : size(s) {
        data = new int[size];
    }

    MyClass(const MyClass& other) {       // 1. Sao chép các thành phần đơn giản
        size = other.size;
        data = new int[size];             // 2. Cấp phát bộ nhớ MỚI
        for (int i = 0; i < size; i++)    // 3. Sao chép từng phần tử
            data[i] = other.data[i];      // 4. (đối với đối tượng: sao chép/di chuyển)
    }

    ~MyClass() {
        delete[] data;
    }
};
```

### Khuôn mẫu 7: Khai báo Lớp Bạn (Friend Class)

```cpp
class A {
private:
    int secret;
public:
    A() : secret(42) {}
    friend class B;    // B có toàn quyền truy cập vào TẤT CẢ thành phần của A
};

class B {
public:
    void reveal(A& a) {
        cout << a.secret;  // truy cập thành phần PRIVATE của A — được phép
    }
};
```

### Khuôn mẫu 8: Bộ khởi tạo-Hàm tạo cho Lớp Hợp thành

```cpp
class Engine {
    int horsepower;
public:
    Engine(int hp) : horsepower(hp) {}
};

class Car {
    Engine engine;   // hợp thành: đối tượng thành phần
    int year;
public:
    Car(int hp, int y) : engine(hp), year(y) {   // danh sách khởi tạo (initializer list)
        // engine đã được xây dựng trước khi thân hàm này chạy
    }
};
```

---

## 9. BẪY THI CỬ

### Bẫy 1: Quên dấu chấm phẩy sau dấu ngoặc nhọn đóng của lớp
```cpp
class Point {
    int x, y;
}  // ← THIẾU CHẤM PHẨY! Lỗi biên dịch: "expected ';' after class definition"
```

> [!success]- Show Answer
> > Mọi định nghĩa lớp phải kết thúc bằng `};`. Đây là lỗi cú pháp phổ biến nhất trong mã viết tay khi thi. Thông báo lỗi của trình biên dịch sẽ gây nhầm lẫn vì nó nghĩ dòng tiếp theo là một phần của lớp.

### Bẫy 2: Hàm tạo sao chép mặc định thực hiện sao chép NÔNG → xóa kép với các thành phần động
Nếu lớp của bạn có `new` trong hàm tạo và `delete` trong hàm hủy, hàm tạo sao chép do trình biên dịch sinh ra sẽ sao chép con trỏ, không phải dữ liệu. Hai đối tượng sẽ chia sẻ cùng một bộ nhớ động. Khi cả hai ra khỏi phạm vi, hàm hủy thứ hai sẽ treo máy.

> [!success]- Show Answer
> > LUÔN tự hỏi: "Lớp của tôi có sở hữu bộ nhớ động (`new`/`new[]`) không?" Nếu có, bạn CẦN một hàm tạo sao chép tùy chỉnh, toán tử gán sao chép tùy chỉnh, và hàm hủy tùy chỉnh (Quy tắc Ba - Rule of Three).

### Bẫy 3: delete vs delete[]
`new` → `delete`. `new[]` → `delete[]`. Trộn lẫn chúng gây ra hành vi không xác định (undefined behavior) — chỉ có hàm hủy của phần tử đầu tiên chạy nếu bạn dùng `delete` trên một mảng.

```cpp
Student* s = new Student;       // đơn lẻ
delete s;                       // đúng
Student* arr = new Student[10]; // mảng
delete[] arr;                   // đúng — KHÔNG phải delete arr;
```

> [!success]- Show Answer
> > Dùng `delete` trên mảng `new[]` chỉ gọi hàm hủy cho phần tử đầu tiên. Hàm hủy của 9 phần tử còn lại không bao giờ được gọi — rò rỉ tài nguyên tiềm ẩn. Bố cục bộ nhớ cũng khác, nên bộ cấp phát có thể treo máy.

### Bẫy 4: Thứ tự bộ khởi tạo-hàm tạo phụ thuộc vào thứ tự KHAI BÁO, KHÔNG phải thứ tự danh sách khởi tạo
```cpp
class X {
    int a;  // được khai báo TRƯỚC
    int b;  // được khai báo THỨ HAI
public:
    X() : b(1), a(b) {}  // danh sách khởi tạo: b trước a
    // Thứ tự THỰC TẾ: a(b) sau đó b(1) — a nhận giá trị b chưa được khởi tạo!
};
```
`a` được khởi tạo với `b` trước khi `b` được khởi tạo → hành vi không xác định (undefined behavior).

> [!success]- Show Answer
> > Luôn viết bộ khởi tạo theo thứ tự khai báo. Trình biên dịch sẽ không cảnh báo bạn theo mặc định — hãy dùng `-Wreorder` (GCC/Clang) hoặc `/W4` (MSVC) để phát hiện điều này.

### Bẫy 5: inline là một gợi ý, không phải mệnh lệnh
Trình biên dịch quyết định có nội tuyến hay không. Viết `inline` không đảm bảo nội tuyến. Ngoài ra, các hàm inline quá lớn làm tăng kích thước mã và có thể gây khó khăn cho việc gỡ lỗi.

> [!success]- Show Answer
> > Trong các bài thi, câu trả lời đúng là: "`inline` là một gợi ý cho trình biên dịch. Trình biên dịch có thể chọn nội tuyến hoặc không dựa trên cài đặt tối ưu hóa và độ phức tạp của hàm."

### Bẫy 6: Hàm thành phần const KHÔNG thể thay đổi BẤT KỲ thành phần dữ liệu nào
```cpp
void foo() const {
    x = 5;   // LỖI: không thể gán cho thành phần trong hàm const
    bar();   // LỖI nếu bar() KHÔNG phải const
}
```

> [!success]- Show Answer
> > Mọi truy cập thành phần dữ liệu bên trong hàm thành phần `const` đều ngầm thông qua `const this`. Trình biên dịch coi tất cả các thành phần là `const` trong hàm. `mutable` là cách thoát duy nhất.

### Bẫy 7: Truy cập là theo LỚP, không phải theo ĐỐI TƯỢNG
Một hàm thành phần có thể truy cập các thành phần private của BẤT KỲ đối tượng nào cùng lớp, không chỉ `this`:
```cpp
class Point {
    int x;
public:
    void steal(const Point& other) { x = other.x; }  // HỢP LỆ
};
```

> [!success]- Show Answer
> > Đây là một mẹo thi phổ biến. "Phương thức `foo` của lớp `A` có thể truy cập thành phần private `x` của một đối tượng `A` khác được truyền làm tham số không?" CÓ. Kiểm soát truy cập ở ranh giới lớp, không phải ranh giới đối tượng.

### Bẫy 8: Lớp bạn (friend classes) phá vỡ tính đóng gói (encapsulation)
Cấp quyền bạn (friendship) cho phép truy cập hoàn toàn vào TẤT CẢ các thành phần private và protected. Điều này phá vỡ tính đóng gói của lớp cấp quyền đối với bạn đó. Hãy sử dụng một cách tiết kiệm và có chủ đích.

> [!success]- Show Answer
> > Trong các câu hỏi lý thuyết: tình bạn (friendship) là một sự vi phạm tính đóng gói có chủ đích, hẹp — nó nên được dùng như biện pháp cuối cùng, không phải là mẫu mặc định.

### Bẫy 9: Lớp hợp thành — hàm tạo thành phần chạy TRƯỚC thân hàm tạo lớp bao ngoài
```cpp
class Outer {
    Inner i;
public:
    Outer() {   // khi thân hàm này chạy, i đã được XÂY DỰNG HOÀN TOÀN
        // i an toàn để sử dụng
    }
};
```

> [!success]- Show Answer
> > Điều này có nghĩa là bạn có thể sử dụng an toàn các đối tượng thành phần bên trong thân hàm tạo lớp bao ngoài. Nguy hiểm là nghĩ rằng các thành phần chưa được khởi tạo — thực tế là CHÚNG ĐÃ được khởi tạo.

### Bẫy 10: Hàm hủy chạy theo thứ tự ngược với hàm tạo
Đối tượng rào cản: thứ tự xây dựng là a→b→c; hủy bỏ là ~c→~b→~a. Ngữ nghĩa ngăn xếp (LIFO).

> [!success]- Show Answer
> > Trong trường hợp hợp thành + kế thừa kết hợp: lớp cơ sở được xây dựng trước, sau đó các thành phần theo thứ tự khai báo, sau đó thân lớp dẫn xuất. Hủy bỏ: thân lớp dẫn xuất, sau đó các thành phần (ngược), sau đó lớp cơ sở (ngược).

### Bẫy 11: Không định nghĩa hàm tạo = trình biên dịch sinh ra hàm tạo mặc định
Nếu bạn định nghĩa ZERO hàm tạo, trình biên dịch sẽ sinh ra một hàm tạo mặc định. Nếu bạn định nghĩa BẤT KỲ hàm tạo nào (thậm chí một hàm có tham số), trình biên dịch sẽ KHÔNG sinh ra hàm tạo mặc định. Khi đó `ClassName obj;` sẽ thất bại nếu không có hàm tạo mặc định nào tồn tại.

```cpp
class Point {
    int x, y;
public:
    Point(int xVal, int yVal) { x = xVal; y = yVal; }  // chỉ có hàm tạo có tham số
};
Point p;   // LỖI: không có hàm tạo mặc định!
```

> [!success]- Show Answer
> > Điều này đặc biệt nguy hiểm với mảng: `Point arr[5];` yêu cầu một hàm tạo mặc định cho mỗi phần tử. Nếu chỉ có hàm tạo có tham số tồn tại, điều này sẽ không biên dịch được.

### Bẫy 12: Con trỏ đến đối tượng động cần delete tường minh
Đối tượng trên stack tự động bị hủy. Đối tượng trên heap được cấp phát bằng `new` PHẢI được `delete` thủ công. Quên dẫn đến rò rỉ bộ nhớ.

```cpp
void func() {
    Point p;                   // tự động bị hủy khi func() kết thúc
    Point* pp = new Point;     // KHÔNG tự động bị hủy → RÒ RỈ BỘ NHỚ
}  // p bị hủy, đối tượng mà pp trỏ tới vẫn trên heap — bị rò rỉ!
```

> [!success]- Show Answer
> > Bản thân con trỏ `pp` (4/8 byte trên stack) tự động bị hủy. Đối tượng Point mà nó TRỎ TỚI (trên heap) KHÔNG tự động bị hủy. Đó là sự rò rỉ.

### Bẫy 13: Hàm tạo sao chép được gọi trong bốn tình huống sau
1. `ClassName a(b);` — khởi tạo trực tiếp
2. `ClassName a = b;` — khởi tạo sao chép (KHÔNG phải gán!)
3. Truyền đối tượng theo giá trị cho tham số hàm
4. Trả về đối tượng theo giá trị từ một hàm

> [!success]- Show Answer — `=` trong khởi tạo vs. gán
> > ```cpp
> > ClassName a = b;    // Hàm tạo SAO CHÉP (Copy CONSTRUCTOR) — a đang được TẠO RA
> > ClassName a;        // Hàm tạo mặc định (Default constructor)
> > a = b;              // TOÁN TỬ GÁN SAO CHÉP (Copy ASSIGNMENT OPERATOR) — a đã tồn tại
> > ```
> > Các toán tử khác nhau, các lời gọi hàm khác nhau. Phân biệt quan trọng trong các kỳ thi.

### Bẫy 14: Định nghĩa ngoài dòng cần tiền tố ClassName::
```cpp
class Point {
    void setY(int valY);         // khai báo bên trong lớp
};

void setY(int valY) { }         // LỖI: đây là hàm TOÀN CỤC, không phải Point::setY
void Point::setY(int valY) { }  // ĐÚNG: được định tố bằng ClassName::
```

> [!success]- Show Answer
> > Không có tiền tố `Point::`, trình biên dịch nghĩ bạn đang định nghĩa một hàm tự do có cùng tên. Bộ liên kết (linker) sẽ phàn nàn về việc thiếu định nghĩa của `Point::setY`.

### Bẫy 15: Bạn (Friend) KHÔNG đối xứng, KHÔNG bắc cầu, KHÔNG kế thừa
- **KHÔNG đối xứng:** A kết bạn B KHÔNG có nghĩa B kết bạn A
- **KHÔNG bắc cầu:** A kết bạn B và B kết bạn C KHÔNG có nghĩa A kết bạn C
- **KHÔNG kế thừa:** A kết bạn B; class D: public B; D KHÔNG phải là bạn của A

> [!success]- Show Answer
> > "Friend có phải là đường một chiều không?" CÓ. "Lớp dẫn xuất của tôi có kế thừa tình bạn của tôi không?" KHÔNG. Mỗi tình bạn phải được cấp một cách tường minh.

### Bẫy 16: Toán tử gán cũng là sao chép nông theo mặc định
Giống như hàm tạo sao chép, `operator=` do trình biên dịch sinh ra thực hiện sao chép nông. Nếu bạn có các thành phần động, bạn cần một cái tùy chỉnh.

> [!success]- Show Answer
> > Quy tắc Ba (Rule of Three): nếu bạn cần một hàm hủy, bạn gần như chắc chắn cần một hàm tạo sao chép tùy chỉnh VÀ một toán tử gán sao chép tùy chỉnh. Bài giảng này tập trung vào hàm tạo sao chép, nhưng logic tương tự áp dụng cho `operator=`.

### Bẫy 17: Không khởi tạo con trỏ trong hàm tạo
```cpp
class Student {
    Course* coursesTaken;
public:
    Student(int n) {
        coursesTaken = new Course[n];  // tốt
    }
    Student() {
        // coursesTaken KHÔNG ĐƯỢC KHỞI TẠO → con trỏ treo/hoang dã (dangling/wild pointer)
        // ~Student() sẽ delete[] một địa chỉ ngẫu nhiên → TREO MÁY
    }
};
```

> [!success]- Show Answer
> > Luôn khởi tạo con trỏ — hoặc là `nullptr` hoặc là bộ nhớ hợp lệ. Một con trỏ chưa được khởi tạo trong `delete[]` của hàm hủy chắc chắn gây treo máy.

---

## 10. BÀI TẬP THỰC HÀNH VIẾT MÃ

### Bài tập 1: Dấu vết Hàm tạo/Hàm hủy

Cho đoạn mã sau, hãy viết đầu ra chính xác theo thứ tự:

```cpp
#include <iostream>
using namespace std;

class A {
    int id;
public:
    A(int i) : id(i) { cout << "A(" << id << ") "; }
    ~A() { cout << "~A(" << id << ") "; }
};

class B {
    A a1, a2;
public:
    B(int x, int y) : a1(x), a2(y) { cout << "B() "; }
    ~B() { cout << "~B() "; }
};

int main() {
    B obj(10, 20);
    return 0;
}
```

> [!success]- Show Answer
> > ```
> > A(10) A(20) B() ~B() ~A(20) ~A(10)
> > ```
> > Giải thích:
> > 1. `a1` được khai báo TRƯỚC → `A(10)` chạy
> > 2. `a2` được khai báo THỨ HAI → `A(20)` chạy
> > 3. Thân `B()` chạy
> > 4. Thân `~B()` chạy
> > 5. `~a2` chạy (thứ tự ngược) → `~A(20)`
> > 6. `~a1` chạy → `~A(10)`

### Bài tập 2: Lỗi Sao chép Sâu — Tìm và Sửa

Đoạn mã sau bị treo. Xác định lỗi và viết phiên bản đã sửa:

```cpp
class Array {
    int* data;
    int len;
public:
    Array(int l) : len(l) {
        data = new int[len];
        for (int i = 0; i < len; i++) data[i] = i;
    }
    ~Array() { delete[] data; }
    void print() const {
        for (int i = 0; i < len; i++) cout << data[i] << " ";
        cout << endl;
    }
};

int main() {
    Array a(5);
    Array b(a);       // Dòng này gây ra treo máy cuối cùng
    a.print();
    b.print();
    return 0;
}  // TREO MÁY: xóa kép (double delete) trên data
```

> [!success]- Show Answer
> > **Lỗi:** Không có hàm tạo sao chép tùy chỉnh. Hàm tạo do trình biên dịch sinh ra thực hiện sao chép nông con trỏ `data`. Cả `a` và `b` đều có `data` trỏ đến cùng một mảng. Khi `main()` kết thúc, `~a()` delete[] mảng, sau đó `~b()` delete[] cùng vùng bộ nhớ đã được giải phóng → treo máy.
> >
> > **Sửa:**
> > ```cpp
> > class Array {
> >     int* data;
> >     int len;
> > public:
> >     Array(int l) : len(l) {
> >         data = new int[len];
> >         for (int i = 0; i < len; i++) data[i] = i;
> >     }
> >     Array(const Array& other) : len(other.len) {     // hàm tạo sao chép tùy chỉnh
> >         data = new int[len];
> >         for (int i = 0; i < len; i++) data[i] = other.data[i];
> >     }
> >     ~Array() { delete[] data; }
> >     void print() const {
> >         for (int i = 0; i < len; i++) cout << data[i] << " ";
> >         cout << endl;
> >     }
> > };
> > ```

### Bài tập 3: Thứ tự Hàm tạo Lớp Hợp thành

Đầu ra của chương trình này là gì?

```cpp
#include <iostream>
using namespace std;

struct X {
    X()  { cout << "X "; }
    ~X() { cout << "~X "; }
};

struct Y {
    Y()  { cout << "Y "; }
    ~Y() { cout << "~Y "; }
};

struct Z {
    Y y;   // được khai báo TRƯỚC
    X x;   // được khai báo THỨ HAI
    Z()  { cout << "Z "; }
    ~Z() { cout << "~Z "; }
};

int main() {
    Z z;
    return 0;
}
```

> [!success]- Show Answer
> > ```
> > Y X Z ~Z ~X ~Y
> > ```
> > `y` được khai báo trước `x`, nên `Y()` chạy trước, sau đó `X()`, sau đó thân `Z()`. Hủy bỏ: thân `~Z()`, sau đó `~x`, sau đó `~y` (ngược với thứ tự khai báo).

### Bài tập 4: Truy cập Lớp Bạn

Viết một cặp lớp `Bank` và `Account` sao cho:
- `Account` có các thành phần private: `double balance` và `int accountNumber`
- `Account` có một hàm tạo nhận hai giá trị đó
- `Bank` là bạn (friend) của `Account` và có thể đọc VÀ sửa đổi `balance` trực tiếp
- `Bank` có một phương thức `transfer(Account& from, Account& to, double amount)` trừ từ `from` và cộng vào `to` (truy cập `balance` trực tiếp)
- Mã bên ngoài (main) KHÔNG THỂ chạm vào `balance` trực tiếp

> [!success]- Show Answer
> > ```cpp
> > #include <iostream>
> > using namespace std;
> >
> > class Account {
> > private:
> >     double balance;
> >     int accountNumber;
> > public:
> >     Account(int num, double bal) : accountNumber(num), balance(bal) {}
> >     void display() const {
> >         cout << "Account " << accountNumber << ": $" << balance << endl;
> >     }
> >     friend class Bank;
> > };
> >
> > class Bank {
> > public:
> >     void transfer(Account& from, Account& to, double amount) {
> >         if (from.balance >= amount) {
> >             from.balance -= amount;   // truy cập trực tiếp vào balance private
> >             to.balance += amount;     // nhờ khai báo friend
> >             cout << "Transferred $" << amount << endl;
> >         } else {
> >             cout << "Insufficient funds." << endl;
> >         }
> >     }
> > };
> >
> > int main() {
> >     Account a1(1001, 500.0);
> >     Account a2(1002, 100.0);
> >     Bank bank;
> >     bank.transfer(a1, a2, 200.0);
> >     a1.display();  // Account 1001: $300
> >     a2.display();  // Account 1002: $300
> >     // a1.balance = 1000;  // LỖI: balance là private
> >     return 0;
> > }
> > ```

### Bài tập 5: Săn lỗi Hàm Thành phần const

Tìm tất cả các lỗi biên dịch trong đoạn mã này:

```cpp
class Counter {
    int count;
    int step;
public:
    Counter(int s) : count(0), step(s) {}
    void increment() const { count += step; }
    int getCount() { return count; }
    void display() const {
        cout << "Count: " << count << endl;
        increment();
    }
};

int main() {
    const Counter c(5);
    cout << c.getCount() << endl;
    c.display();
    return 0;
}
```

> [!success]- Show Answer
> > Ba lỗi:
> >
> > 1. **`void increment() const { count += step; }`** — LỖI: sửa đổi `count` bên trong hàm thành phần `const`. Bỏ `const` khỏi `increment()`.
> > 2. **`void display() const { ... increment(); }`** — LỖI: gọi `increment()` không phải const từ một hàm `const`. Sửa bằng cách bỏ `const` khỏi `display()` hoặc bỏ lời gọi `increment()`.
> > 3. **`const Counter c(5); cout << c.getCount();`** — LỖI: `getCount()` không phải `const`, không thể gọi trên đối tượng `const`. Sửa: `int getCount() const { return count; }`
> >
> > Đã sửa:
> > ```cpp
> > class Counter {
> >     int count;
> >     int step;
> > public:
> >     Counter(int s) : count(0), step(s) {}
> >     void increment() { count += step; }
> >     int getCount() const { return count; }
> >     void display() const { cout << "Count: " << count << endl; }
> > };
> > ```

### Bài tập 6: Nhận dạng Trong dòng (Inline) vs Ngoài dòng (Out-of-line)

Với mỗi hàm, hãy xác định nó thuộc loại: trong dòng, ngoài dòng (không inline), hoặc ngoài dòng với từ khóa inline.

```cpp
class Widget {
    int val;
public:
    Widget() { val = 0; }                           // (a)
    Widget(int v);                                    // (b)
    int getVal() const { return val; }                // (c)
    void setVal(int v);                                // (d)
    void doubleVal();                                  // (e)
};

Widget::Widget(int v) { val = v; }                   // (b)

void Widget::setVal(int v) { val = v; }               // (d)

inline void Widget::doubleVal() { val *= 2; }         // (e)
```

> [!success]- Show Answer
> > (a) `Widget()` — **Trong dòng (In-line)** (định nghĩa bên trong thân lớp, ngầm định inline)
> > (b) `Widget(int v)` — **Ngoài dòng (Out-of-line)** (định nghĩa bên ngoài, không có từ khóa `inline`)
> > (c) `getVal()` — **Trong dòng (In-line)** (định nghĩa bên trong thân lớp, ngầm định inline)
> > (d) `setVal(int v)` — **Ngoài dòng (Out-of-line)** (định nghĩa bên ngoài, không có từ khóa `inline`)
> > (e) `doubleVal()` — **Ngoài dòng với từ khóa inline** (định nghĩa bên ngoài, có từ khóa `inline` tường minh)

### Bài tập 7: Con trỏ đến Đối tượng — Dấu vết Đầy đủ

```cpp
#include <iostream>
using namespace std;

class Tracker {
    static int nextID;
    int id;
public:
    Tracker() : id(nextID++) {
        cout << "ctor " << id << endl;
    }
    Tracker(const Tracker& other) : id(nextID++) {
        cout << "copy ctor " << id << " from " << other.id << endl;
    }
    ~Tracker() { cout << "dtor " << id << endl; }
    int getID() const { return id; }
};

int Tracker::nextID = 1;

int main() {
    Tracker t1;
    Tracker* p = new Tracker;
    Tracker* arr = new Tracker[2];
    Tracker t2(t1);
    delete p;
    delete[] arr;
    return 0;
}
```

Viết đầu ra ĐẦY ĐỦ theo thứ tự.

> [!success]- Show Answer
> > ```
> > ctor 1
> > ctor 2
> > ctor 3
> > ctor 4
> > copy ctor 5 from 1
> > dtor 2
> > dtor 4
> > dtor 3
> > dtor 5
> > dtor 1
> > ```
> > Dấu vết:
> > - `t1`: ctor id=1 (stack)
> > - `new Tracker`: ctor id=2 (heap, đơn lẻ)
> > - `new Tracker[2]`: ctor id=3, ctor id=4 (mảng heap)
> > - `t2(t1)`: copy ctor id=5 từ id=1 của t1
> > - `delete p`: dtor id=2 (đối tượng heap đơn lẻ)
> > - `delete[] arr`: dtor 4 sau đó dtor 3 (thứ tự ngược với xây dựng mảng)
> > - `return 0`: t2 bị hủy (dtor 5), sau đó t1 bị hủy (dtor 1) — đối tượng stack theo thứ tự ngược
