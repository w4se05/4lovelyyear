# Lec10: Nạp chồng (Overloading) — Hướng dẫn ôn tập

---

## 1. THẺ KHÁI NIỆM

### 1.1 Bản chất — Cùng Tên, Chữ ký (Signature) Khác Nhau; Trình Biên Dịch Chọn Phiên Bản Đúng Tại Thời Điểm Biên Dịch

Nạp chồng (Overloading) là khả năng định nghĩa nhiều hàm (hoặc toán tử) có **cùng tên** nhưng **danh sách tham số khác nhau** — khác biệt về **số lượng**, **kiểu**, hoặc **thứ tự** của tham số. Trình biên dịch chọn phiên bản nào để gọi tại **thời điểm biên dịch** dựa trên các đối số được cung cấp. Đây là một dạng của **đa hình đặc biệt** (ad-hoc polymorphism / static dispatch polymorphism).

Nó áp dụng cho:
- **Nạp chồng hàm (Function overloading)** — hàm độc lập hoặc hàm thành viên có cùng tên, chữ ký (Signature) khác nhau
- **Nạp chồng toán tử (Operator overloading)** — gán ý nghĩa mới cho các toán tử C++ tiêu chuẩn khi sử dụng với kiểu do người dùng định nghĩa
- **Nạp chồng hàm tạo (Constructor overloading)** — nhiều hàm tạo với danh sách tham số khác nhau

### 1.2 Vấn Đề Nó Giải Quyết — Không Còn `addInts`/`addFloats`/`addDoubles`; Cú Pháp Tự Nhiên Như `a + b` Cho Kiểu Tùy Chỉnh

Không có nạp chồng (Overloading), bạn sẽ cần các tên hàm riêng biệt cho mọi tổ hợp kiểu tham số:

```cpp
// WITHOUT overloading — ugly, hard to remember, non-scalable
int    addInts(int a, int b)       { return a + b; }
float  addFloats(float a, float b) { return a + b; }
double addDoubles(double a, double b) { return a + b; }
// ... and so on for every type
```

Với nạp chồng (Overloading):

```cpp
// WITH overloading — clean, natural, compiler figures it out
int    add(int a, int b)    { return a + b; }
float  add(float a, float b) { return a + b; }
double add(double a, double b) { return a + b; }
add(3, 5);       // calls int version
add(3.0f, 5.0f); // calls float version
```

Điều này mang lại **tính biểu cảm** và **cú pháp tự nhiên**. Đối với nạp chồng toán tử (Operator overloading), nó cho phép bạn viết `c1 + c2` cho số `Complex`, `m1 + m2` cho đối tượng `Money`, `t1 < t2` cho đối tượng `Time` — làm cho các kiểu tùy chỉnh hoạt động trực quan như các kiểu có sẵn.

### 1.3 Cơ Chế Hoạt Động

1. **Trình biên dịch** kiểm tra từng đối số tại mỗi điểm gọi.
2. Với mỗi ứng viên nạp chồng cùng tên, trình biên dịch kiểm tra mức độ khớp của từng đối số với các kiểu tham số đã khai báo.
3. Mức khớp được xếp hạng (từ tốt nhất đến tệ nhất): **khớp chính xác** > **thăng hạng** (ví dụ: `char` → `int`) > **chuyển đổi chuẩn** (ví dụ: `int` → `long`, `float` → `double`) > **chuyển đổi do người dùng định nghĩa**.
4. Trình biên dịch chọn **hàm khớp tốt nhất duy nhất** trên TẤT CẢ các đối số.
5. Nếu **không có** hàm nào khớp hoặc **nhiều hơn một** hàm cùng là tốt nhất → **lỗi biên dịch**.
6. **Kiểu trả về KHÔNG phải là một phần của chữ ký (Signature)** — trình biên dịch KHÔNG dùng kiểu trả về để phân biệt các nạp chồng. Hai hàm cùng tên và cùng danh sách tham số nhưng khác kiểu trả về sẽ gây lỗi biên dịch.
7. Tất cả điều này xảy ra tại **thời điểm biên dịch** (giải quyết tĩnh), không giống như ghi đè (overriding) được giải quyết tại **thời điểm chạy** thông qua bảng ảo (vtable).

### 1.4 Ví Dụ Cụ Thể — Lớp Tiền Tệ (Currency) Cho Thương Mại Điện Tử: Giá + Thuế

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

class Currency {
    long dollars;
    int  cents;
public:
    Currency(long d = 0, int c = 0) : dollars(d), cents(c) {
        normalize();
    }

    void normalize() {
        if (cents >= 100) { dollars += cents / 100; cents %= 100; }
        if (cents < 0)    { dollars -= 1 + (-cents) / 100; cents = 100 - (-cents) % 100; }
    }

    // Overloaded + operator — adds two Currency objects naturally
    Currency operator+(const Currency& other) const {
        return Currency(dollars + other.dollars, cents + other.cents);
    }

    // Overloaded << for easy printing
    friend ostream& operator<<(ostream& os, const Currency& c) {
        os << "$" << c.dollars << "." << setw(2) << setfill('0') << c.cents;
        return os;
    }
};

int main() {
    Currency price(19, 99);     // $19.99
    Currency tax(1, 50);        // $1.50 — 7.5% sales tax
    Currency total = price + tax;

    cout << "Price:      " << price << endl;   // $19.99
    cout << "Tax:        " << tax   << endl;   // $1.50
    cout << "Total:      " << total << endl;   // $21.49
    // No addCurrency(price, tax) nonsense — just price + tax!
}
```

**Trình biên dịch làm gì**: Khi gặp `price + tax`, nó chuyển thành `price.operator+(tax)`. `operator+` được giải quyết tĩnh — trình biên dịch biết cả hai toán hạng đều là `Currency`, nên nó gọi `Currency::operator+` được định nghĩa trong lớp. Không có điều phối thời gian chạy, không có bảng ảo (vtable).

### 1.5 Nó KHÔNG phải là — KHÔNG phải Ghi đè (Overriding) (Cùng Tên + Tham Số, Thời Gian Chạy, Cần virtual)

Đây có lẽ là sự khác biệt gây nhầm lẫn nhất trong C++. Nạp chồng (Overloading) và ghi đè (overriding) khác nhau cơ bản:

| Khía cạnh | Nạp chồng (Overloading) | Ghi đè (Overriding — Đa hình) |
|-----------|--------------------------|-------------------------------|
| Tham số | **Khác nhau** — phải khác về số lượng, kiểu, hoặc thứ tự | **Giống nhau** — chữ ký (Signature) giống hệt |
| Thời điểm giải quyết | **Thời gian biên dịch** (liên kết tĩnh) | **Thời gian chạy** (liên kết động) |
| Từ khóa `virtual` | Không bắt buộc, không liên quan | Bắt buộc trong lớp cơ sở |
| Kế thừa | Không bắt buộc | Bắt buộc (quan hệ lớp cơ sở-lớp dẫn xuất) |
| Kiểu trả về | Không thể phân biệt nạp chồng (không phải một phần của chữ ký) | Phải là **hiệp biến** (cùng kiểu hoặc kiểu dẫn xuất) trong C++ |
| Cơ chế | Trình biên dịch mã hóa tên hàm với các kiểu tham số | Trình biên dịch tạo bảng ảo (vtable); lời gọi được giải quyết qua vptr tại thời gian chạy |
| Tên gọi khác | Đa hình đặc biệt (ad-hoc polymorphism), đa hình tĩnh | Đa hình bao hàm (inclusion polymorphism), đa hình động |

```cpp
class Base {
public:
    // These are OVERLOADS of each other — different parameters
    void print(int x)     { cout << "int: "   << x << endl; }
    void print(double x)  { cout << "double: " << x << endl; }
    void print(string s)  { cout << "string: " << s << endl; }

    // This would be OVERRIDDEN in a derived class (needs virtual!)
    virtual void display() { cout << "Base::display" << endl; }
};

class Derived : public Base {
public:
    // OVERRIDES Base::display — same signature, virtual, inheritance
    void display() { cout << "Derived::display" << endl; }
};
```

---

## 2. NẠP CHỒNG HÀM (FUNCTION OVERLOADING)

### 2.1 Định Nghĩa — Nhiều Hàm Cùng Tên, Tham Số Khác Nhau Về Số Lượng, Kiểu, hoặc Thứ Tự

Nạp chồng hàm (Function overloading) cho phép nhiều hàm trong **cùng phạm vi** có cùng tên, miễn là chúng có **chữ ký (Signature) khác nhau**. Chữ ký (Signature) bao gồm:
- **Tên** hàm
- **Số lượng** tham số
- **Kiểu** của tham số
- **Thứ tự** các kiểu tham số

Quy tắc chính: danh sách tham số phải **có thể phân biệt được**. Trình biên dịch dùng các kiểu đối số tại điểm gọi để xác định nạp chồng nào sẽ được gọi.

```cpp
// Valid overloading — different parameter types
void log(const char* msg);     // C-string
void log(string msg);          // std::string
void log(int code, string msg); // two params
void log(string msg, int code); // different ORDER — also valid

// INVALID — same signature, only return type differs
int  getValue();  // ERROR: redeclaration
double getValue(); // ERROR: cannot overload on return type alone
```

### 2.2 Chữ Ký (Signature) — Hàm Được Nhận Diện Bởi Tên + Số Lượng + Thứ Tự + Kiểu Của Tham Số (= CHỮ KÝ). Kiểu Trả Về KHÔNG Phải Một Phần Của Chữ Ký!

**Chữ ký (Signature)** là định danh duy nhất mà trình biên dịch sử dụng cho việc mã hóa tên (name mangling) và giải quyết nạp chồng (Overloading resolution):

```
CHỮ KÝ = tên-hàm + (số-lượng-tham-số, các-kiểu-tham-số-theo-thứ-tự)
```

**Những gì KHÔNG có trong chữ ký (Signature):**
- **Kiểu trả về** — hai hàm cùng tên và cùng tham số nhưng khác kiểu trả về là lỗi biên dịch, không phải nạp chồng.
- **Bổ từ `const` trên tham số không phải thành viên** — `void f(int)` và `void f(const int)` có cùng chữ ký (truyền theo giá trị).
- **Đối số mặc định** — `void f(int x)` và `void f(int x = 5)` là cùng một hàm (giá trị mặc định chỉ cung cấp giá trị khi bỏ qua).

```cpp
int  compute(int a);     // #1
// double compute(int a); // ERROR: redeclaration — same signature, different return type

void process(int& ref);  // #2
void process(const int& ref); // VALID overload — different parameter type (const ref vs non-const ref)

// Default arguments do NOT create overloads:
void display(int x = 10); // #3
// void display(int x);   // ERROR — this is the same function as #3
```

**Những gì CÓ trong chữ ký (Signature) (đối với hàm thành viên):**
- **Bổ từ `const` của hàm thành viên** — `void foo() const` và `void foo()` là các chữ ký khác nhau.
- **Bổ từ `volatile`**
- **Bổ từ tham chiếu `&` và `&&`** (C++11)

### 2.3 Ví Dụ Từ Bài Giảng

```cpp
void swap(unsigned long &, unsigned long &);
void swap(double &, double &);
void swap(char &, char &);
void swap(Point &, Point &);
```

**"Mỗi hàm là một hàm khác nhau!!!"**

Dù tất cả đều được gọi là `swap`, bốn hàm này là bốn hàm **riêng biệt** với bốn **địa chỉ riêng biệt** trong bộ nhớ. Trình biên dịch tạo ra các tên nội bộ khác nhau (mã hóa tên). Khi bạn gọi:

```cpp
unsigned long a = 100, b = 200;
swap(a, b);          // Compiler: "ah, unsigned long& — call swap(unsigned long&, unsigned long&)"

double x = 1.5, y = 2.5;
swap(x, y);          // Compiler: "ah, double& — call swap(double&, double&)"

char c = 'A', d = 'B';
swap(c, d);          // Compiler: "ah, char& — call swap(char&, char&)"

Point p1(0,0), p2(1,1);
swap(p1, p2);        // Compiler: "ah, Point& — call swap(Point&, Point&)"
```

Quyết định được đưa ra **tĩnh** — trình biên dịch chỉ đơn giản xem xét kiểu đã khai báo của mỗi đối số và chọn hàm khớp. Không tra cứu thời gian chạy, không có bảng ảo (vtable), không có chi phí nào ngoài một lời gọi hàm thông thường.

### 2.4 Cảnh Báo Thực Hành Kém — Các Hàm Cùng Tên Nên CÓ CHỨC NĂNG TƯƠNG TỰ

Bài giảng cảnh báo rõ ràng về việc sử dụng nạp chồng (Overloading) cho các hàm có **ngữ nghĩa khác nhau**:

```cpp
class Student {
public:
    unsigned credits();          // GET the credits
    unsigned credits(unsigned n); // SET the credits — different semantics, BAD!
};
```

Đây là **thực hành kém** vì:
- Tên `credits` gợi ý một thao tác khái niệm duy nhất — nhưng một dạng truy vấn và dạng kia thay đổi dữ liệu.
- Người đọc mã sử dụng `Student` thấy `s.credits(30)` và có thể không nhận ra ngay đây là một **setter**, không phải phép tính nào đó.
- Nạp chồng (Overloading) nên được sử dụng cho các **thao tác tương tự về mặt khái niệm** chỉ khác nhau về kiểu hoặc số lượng đầu vào.
- Getter và setter cùng tên vi phạm **nguyên tắc ít bất ngờ nhất**.

**Giải pháp tốt:**

```cpp
class Student {
public:
    unsigned getCredits() const;      // clear: this queries
    void     setCredits(unsigned n);  // clear: this mutates
};
```

Quy tắc: nếu sự khác biệt về tham số ngụ ý **hành vi khác nhau cơ bản**, hãy sử dụng **tên khác nhau**.

### 2.5 Nạp Chồng Hàm Tạo (Constructor Overloading)

Hàm tạo (Constructor) là các hàm thành viên đặc biệt — chúng có thể được nạp chồng (Overloading) như bất kỳ hàm nào khác, cho phép nhiều cách khởi tạo một đối tượng.

**Lớp Point — một hàm tạo duy nhất với giá trị mặc định:**

```cpp
class Point {
    int x, y;
public:
    Point(int xx = 0, int yy = 0) { x = xx; y = yy; }
};
```

Hàm tạo duy nhất này phục vụ ba mục đích thông qua các đối số mặc định:
- `Point p1;` — cả hai giá trị mặc định → `(0, 0)`
- `Point p2(5);` — `xx=5, yy=0`
- `Point p3(5, 10);` — `xx=5, yy=10`

**Lớp Figure — ba hàm tạo riêng biệt:**

```cpp
class Figure {
public:
    Figure() { }                                    // default constructor — no arguments
    Figure(const Point & center) { }                // create figure from a center Point
    Figure(const Point vertices[], int count) { }   // create figure from array of Points
};

int main() {
    Figure fig1[3];                  // default constructor called 3 times
    Point center(25, 50);
    Figure fig2(center);             // 2nd constructor — Point reference
    const int VCount = 5;
    Point verts[VCount];             // default Point called 5 times → all (0,0)
    Figure fig3(verts, VCount);      // 3rd constructor — Point array + count
}
```

**Dấu vết:**
- `Figure fig1[3]` — tạo mảng gồm 3 đối tượng `Figure`. Mỗi đối tượng gọi **hàm tạo mặc định** `Figure()` vì không có đối số nào được truyền.
- `Figure fig2(center)` — trình biên dịch thấy một đối số kiểu `Point` → khớp chính xác `Figure(const Point &)` → hàm tạo thứ 2.
- `Figure fig3(verts, VCount)` — trình biên dịch thấy hai đối số: `Point[]` và `int` → khớp `Figure(const Point[], int)` → hàm tạo thứ 3.

Nạp chồng hàm tạo (Constructor overloading) tuân theo cùng các quy tắc giải quyết như nạp chồng hàm (Function overloading): khớp tốt nhất thắng, sự mơ hồ là lỗi.

---

## 3. ÉP KIỂU (COERCION) (XEM LẠI)

### 3.1 Định Nghĩa — Đối Tượng hoặc Nguyên Thủy Tự Động Ép Sang Kiểu Khác (Không Chỉ Là Nạp Chồng)

**Ép kiểu (Coercion)** là việc chuyển đổi tự động/ngầm định một giá trị từ kiểu này sang kiểu khác. Đây là một **khái niệm riêng biệt** so với nạp chồng (Overloading), nhưng cả hai tương tác mật thiết trong quá trình giải quyết nạp chồng (Overloading resolution). Trình biên dịch sử dụng ép kiểu (Coercion) để *làm cho các đối số khớp* với các tham số của một ứng viên nạp chồng.

Các loại ép kiểu (Coercion):
- **Thăng hạng** (không mất dữ liệu): `char` → `int`, `float` → `double`, `bool` → `int`
- **Chuyển đổi chuẩn** (có thể mất dữ liệu): `int` → `long`, `double` → `float`, `int` → `char`
- **Chuyển đổi do người dùng định nghĩa**: thông qua hàm tạo với một đối số hoặc toán tử chuyển đổi
- **Chuyển đổi tầm thường**: `int` → `const int`, mảng → con trỏ

### 3.2 Ví Dụ — Hàm `calculate`

```cpp
void calculate(long p1, long p2, double p3, double p4);

long   a1 = 12345678;
int    a2 = 1;
double a3 = 2.3455555;
float  a4 = 3.1;

calculate(a1, a2, a3, a4); // OK — compiler coerces:
                            // a1: long → long  (exact match)
                            // a2: int  → long  (standard conversion)
                            // a3: double → double (exact match)
                            // a4: float → double (promotion)

Student s;
calculate(s, 10, 5.5, 6);  // ERROR: Student → long? No viable conversion path
```

Điểm mấu chốt: trình biên dịch thử **từng đối số riêng lẻ** với kiểu tham số mong đợi. Nếu mọi đối số đều có đường dẫn chuyển đổi hợp lệ, lời gọi thành công. Nếu **bất kỳ** đối số nào không có đường dẫn chuyển đổi khả thi → lỗi.

### 3.3 Ví Dụ Ép Kiểu (Coercion) Hàm `add` (Từ Bài Giảng)

```cpp
int add(int a, int b)     { return a + b; }
float add(float a, float b) { return 1.0 + a + b; }

int main() {
    cout << add(1, 1.0) << endl; // Which one is called?
}
```

**Giải quyết:**
- `add(1, 1.0)` — các đối số là `int` và `double`.
- Ứng viên 1: `add(int, int)` — đối số đầu khớp chính xác, đối số thứ hai cần chuyển đổi `double → int`.
- Ứng viên 2: `add(float, float)` — cả hai đối số đều cần chuyển đổi (`int → float`, `double → float`).
- Ứng viên 1 **tốt hơn** (một khớp chính xác + một chuyển đổi) so với Ứng viên 2 (hai chuyển đổi).
- Kết quả: gọi `add(int, int)`, trả về `1 + 1 = 2`. Giá trị `1.0` bị **ép kiểu (coerced)** (cắt bớt) thành `1`.

**Cảnh báo quan trọng**: ép kiểu (Coercion) có thể gây **mất dữ liệu thầm lặng**. `1.0` trở thành `1` — phần thập phân bị loại bỏ mà không có cảnh báo. Đây là lý do trình biên dịch đôi khi cảnh báo về các chuyển đổi thu hẹp.

---

## 4. GIẢI QUYẾT NẠP CHỒNG (OVERLOADING RESOLUTION)

### 4.1 Nguyên Tắc Hàm Khớp Tốt Nhất

Tiêu chuẩn C++ định nghĩa một thuật toán nghiêm ngặt cho giải quyết nạp chồng (Overloading resolution):

1. **Tập ứng viên**: Tất cả các hàm có tên đúng hiển thị tại điểm gọi (bao gồm các hàm được đưa vào bởi khai báo `using` hoặc tra cứu phụ thuộc đối số).
2. **Tập khả thi**: Các ứng viên có thể chấp nhận số lượng đối số đã cho và mỗi đối số có một chuyển đổi ngầm định hợp lệ đến kiểu tham số tương ứng.
3. **Chọn khớp tốt nhất**: Với mỗi hàm khả thi, trình biên dịch xếp hạng chuyển đổi cần thiết cho mỗi đối số. Hàm yêu cầu các chuyển đổi "tốt nhất" trên tất cả các đối số được chọn.

**Nếu không có hàm khả thi nào** → lỗi "no matching function".
**Nếu có nhiều hơn một hàm "tốt nhất" ngang nhau (hòa)** → lỗi "ambiguous call".

### 4.2 Ví Dụ 1 — `double` Mơ Hồ

```cpp
void display(int x);   // version 1
void display(float y); // version 2

int i; float f; double d;

display(i); // version 1 — int→int exact match. float would need int→float conversion.
display(f); // version 2 — float→float exact match. int would need float→int conversion.
display(d); // ERROR! double matches BOTH int and float equally poorly.
             // double→int: standard conversion (floating-integral)
             // double→float: standard conversion (floating point)
             // Neither is better → AMBIGUITY → compilation error
```

**Tại sao `double` lại mơ hồ**: Cả `int` và `float` đều "xa" `double` như nhau. Không có chuyển đổi nào được xếp hạng cao hơn chuyển đổi kia. Trình biên dịch không thể chọn, do đó báo lỗi mơ hồ.

### 4.3 Ví Dụ 2 — Các Kiểu Hỗn Hợp (Từ Bài Giảng)

```cpp
void print(float a, float b) { cout << "version 1\n"; }
void print(float a, int b)  { cout << "version 2\n"; }

int main() {
    int i = 0, j = 0;
    float f = 0.0;
    double d = 0.0;

    print(i, j);   // version 2 — why?
                   // Candidate 1: print(float, float) — both i,j need int→float conversion
                   // Candidate 2: print(float, int)  — i needs int→float, j is int→int exact
                   // Candidate 2 wins: one exact match + one conversion beats two conversions

    print(i, f);   // version 1 — why?
                   // Candidate 1: print(float, float) — i:int→float, f:float→float exact
                   // Candidate 2: print(float, int)  — i:int→float, f:float→int conversion
                   // Candidate 1 wins: one exact + one conversion beats one conversion + one conversion
                   // (the exact match on f makes v1 better)

    print(d, f);   // version 1 — why?
                   // Candidate 1: print(float, float) — d:double→float, f:float→float exact
                   // Candidate 2: print(float, int)  — d:double→float, f:float→int conversion
                   // Candidate 1 wins: same conversion for first arg, exact match for second vs conversion
}
```

Bảng tóm tắt giải quyết:

| Lời gọi | v1: `(float,float)` | v2: `(float,int)` | Người thắng | Lý do |
|---------|---------------------|-------------------|-------------|--------|
| `print(i, j)` | i: int→float, j: int→float | i: int→float, j: **chính xác** | v2 | Khớp chính xác ở j |
| `print(i, f)` | i: int→float, j: **chính xác** | i: int→float, j: float→int | v1 | Khớp chính xác ở f |
| `print(d, f)` | d: double→float, f: **chính xác** | d: double→float, f: float→int | v1 | Khớp chính xác ở f |

### 4.4 Ví Dụ 3 — Lỗi Yêu Cầu Ép Kiểu Tường Minh

```cpp
print(d, 3.5);  // ERROR — why?
                // Candidate 1: print(float, float) — d:double→float, 3.5:double→float
                // Candidate 2: print(float, int)  — d:double→float, 3.5:double→int
                // First argument identical in both. Second argument: double→float vs double→int.
                // Both are standard conversions, neither is better → AMBIGUITY

print(i, 4.5);  // ERROR — same logic
                // Candidate 1: print(float, float) — i:int→float, 4.5:double→float
                // Candidate 2: print(float, int)  — i:int→float, 4.5:double→int
                // First arg same, second arg tie → AMBIGUITY

print(d, 3.0);  // ERROR — 3.0 is a double literal
                // Same ambiguity: double→float vs double→int tie on second argument

print(i, d);    // ERROR — i:int→float (both), d:double→float vs double→int → tie
```

**Ép kiểu tường minh giải quyết sự mơ hồ:**

```cpp
print(d, float(3.5));  // version 1 — unambiguous: float(float) is exact match
print(i, int(4.5));    // version 2 — unambiguous: int(int) is exact match
print(d, float(3.0));  // version 1 — unambiguous
print(i, int(d));      // version 2 — unambiguous (d truncated to int)
```

**Bài học chính**: Khi giải quyết nạp chồng (Overloading resolution) bị mơ hồ, hãy ép kiểu tường minh các đối số để chọn nạp chồng mong muốn. Điều này báo cho trình biên dịch biết chính xác kiểu bạn định dùng, loại bỏ sự hòa.

---

## 5. NẠP CHỒNG TOÁN TỬ (OPERATOR OVERLOADING)

### 5.1 Định Nghĩa — Gán Ý Nghĩa Mới Cho Các Toán Tử Chuẩn (+, >>, =, ...) Khi Sử Dụng Với Toán Hạng Là Lớp

Nạp chồng toán tử (Operator overloading) cho phép bạn định nghĩa (hoặc định nghĩa lại) hành vi của các toán tử có sẵn trong C++ khi chúng được áp dụng cho các kiểu do người dùng định nghĩa. Bên trong, một toán tử được nạp chồng chỉ là một **hàm** với tên đặc biệt (`operator +`, `operator =`, `operator <<`, v.v.).

### 5.2 Tại Sao? — Một Cách Đặt Tên Cho Hàm; Làm Mã DỄ ĐỌC HƠN

Không có nạp chồng toán tử (Operator overloading):

```cpp
// Without operator overloading — verbose, unnatural
Complex c1(1, 2), c2(3, 4), c3;
c3 = add(multiply(c1, c2), c1);  // c3 = c1*c2 + c1 — hard to parse
```

Với nạp chồng toán tử (Operator overloading):

```cpp
// With operator overloading — clean, mathematical
Complex c1(1, 2), c2(3, 4), c3;
c3 = c1 * c2 + c1;  // immediately obvious what's happening
```

Cú pháp toán tử làm cho các kiểu tùy chỉnh cảm giác như công dân hạng nhất của ngôn ngữ. Nó giảm tải nhận thức — người đọc thấy `a + b` và hiểu đó là phép cộng, bất kể `a` và `b` là `int`, `double`, hay số `Complex`.

### 5.3 Cú Pháp Cơ Bản

```cpp
class AClass {
public:
    int operator+(AClass &a) { return 1; }
};

int main() {
    AClass a, b;
    int i;
    i = a + b;        // i = a.operator+(b); ← the compiler rewrites it this way
}
```

**Các quy tắc cú pháp chính:**
- Tên toán tử là `operator` theo sau bởi ký hiệu toán tử: `operator+`, `operator=`, `operator<<`, v.v.
- Đối với toán tử một ngôi là **hàm thành viên**: `Type operator-() const;` (không tham số — toán hạng là `*this`).
- Đối với toán tử hai ngôi là **hàm thành viên**: `Type operator+(const Type& other) const;` (một tham số — toán hạng phải; toán hạng trái là `*this`).
- Đối với toán tử hai ngôi là **hàm không phải thành viên**: `Type operator+(const Type& a, const Type& b);` (hai tham số — cả hai toán hạng tường minh).
- Lời gọi `a + b` là đường cú pháp cho `a.operator+(b)` (thành viên) hoặc `operator+(a, b)` (không phải thành viên).

### 5.4 Đã Được Nạp Chồng (Overloading) Trong C++

Toán tử `+` đã được nạp chồng (Overloading) trong C++ chuẩn:
- **Cộng số nguyên**: `int + int`
- **Cộng số thực dấu phẩy động**: `float + float`, `double + double`
- **Cộng con trỏ**: `int* + int` (số học con trỏ — thêm `int * sizeof(phần tử)` byte)

Điều này cho thấy nạp chồng toán tử (Operator overloading) không phải là điều xa lạ — nó là một **phần cơ bản** của cách C++ hoạt động. Bản thân ngôn ngữ đã sử dụng nạp chồng (Overloading) rộng rãi trong các kiểu có sẵn của nó. Bạn chỉ đơn giản là mở rộng cùng khả năng đó cho các kiểu của riêng bạn.

### 5.5 Các Toán Tử CHO PHÉP Nạp Chồng (Overloading)

**Toán tử một ngôi** (hầu hết có thể được nạp chồng như thành viên hoặc không phải thành viên):

| Danh mục | Toán tử |
|----------|---------|
| Quản lý bộ nhớ | `new`, `delete`, `new[]`, `delete[]` |
| Số học | `+`, `-` (cộng/trừ một ngôi) |
| Tăng/giảm | `++` (tiền tố (Prefix)), `++` (hậu tố (Postfix)), `--` (tiền tố (Prefix)), `--` (hậu tố (Postfix)) |
| Giải tham chiếu | `*`, `->` |
| Lấy địa chỉ | `&` |
| Logic/Bit | `!`, `~` |
| Gọi hàm / chỉ mục | `()`, `[]` |

**Toán tử hai ngôi** (hầu hết có thể được nạp chồng như thành viên hoặc không phải thành viên):

| Danh mục | Toán tử |
|----------|---------|
| Số học | `+`, `-`, `*`, `/`, `%` |
| Gán | `=`, `+=`, `-=`, `*=`, `/=`, `%=` |
| Bit | `&`, `\|`, `^`, `<<`, `>>` |
| Bit kép | `&=`, `\|=`, `^=`, `<<=`, `>>=` |
| So sánh | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Logic | `&&`, `\|\|` |
| Truy cập thành viên | `->`, `->*` |
| Luồng | `<<`, `>>` |

### 5.6 Các Toán Tử KHÔNG ĐƯỢC PHÉP Nạp Chồng (Overloading)

Bốn toán tử này **KHÔNG THỂ** được nạp chồng (Overloading) — tuyệt đối:

| Toán tử | Tên | Tại sao không thể nạp chồng |
|----------|------|---------------------------|
| `.` | Truy cập thành viên | Nền tảng cho mô hình đối tượng; nạp chồng sẽ phá vỡ ngôn ngữ |
| `.*` | Truy cập-giải tham chiếu thành viên (con trỏ-thành viên) | Cùng lý do với `.` |
| `::` | Giải quyết phạm vi | Thao tác trên tên, không phải giá trị; về cơ bản là cơ chế thời gian biên dịch |
| `?:` | Điều kiện ba ngôi (số học-IF) | Toán tử ba ngôi duy nhất; ngữ nghĩa đánh giá ngắn mạch không thể sao chép |

**Cách ghi nhớ**:
- "**Đ**ừng **n**ạp **c**hồng **n**hững **t**hứ **c**ó **d**ấu **c**hấm **v**à **d**ấu **h**ai **c**hấm" — `.`, `.*`, `::`, `?:`
- Hoặc: "Bốn toán tử bị cấm đều liên quan đến **giải quyết tên** hoặc **đánh giá điều kiện**, không phải tính toán giá trị."

### 5.7 Hạn Chế

Ba hạn chế quan trọng áp dụng cho **tất cả** nạp chồng toán tử (Operator overloading):

1. **Không thể thay đổi thứ tự ưu tiên hay tính kết hợp** — Trình biên dịch xác định thứ tự ưu tiên và tính kết hợp dựa trên **ký hiệu toán tử**, không phải kiểu toán hạng. Bạn không thể làm cho `+` gắn kết chặt hơn `*` hoặc làm cho `=` từ phải sang trái.

2. **Đối số mặc định KHÔNG THỂ được sử dụng** — Các hàm toán tử không thể có tham số mặc định. Mọi đối số phải được cung cấp tường minh tại điểm gọi (tương ứng với số lượng toán hạng trong biểu thức).

   ```cpp
   class Bad {
   public:
       // ERROR: default arguments on overloaded operator
       int operator+(int x, int y = 5);  // NOT ALLOWED
   };
   ```

3. **"Ngôi" của toán tử không thể thay đổi** — Toán tử hai ngôi vẫn là hai ngôi, toán tử một ngôi vẫn là một ngôi. Bạn không thể biến `+` thành toán tử một ngôi nhận ba toán hạng, cũng như không thể làm cho `++` thành toán tử hai ngôi.

4. **Chỉ được nạp chồng các toán tử HIỆN CÓ** — Bạn không thể phát minh ra toán tử mới (ví dụ: `**` cho lũy thừa, `$` cho thao tác tùy chỉnh). Bạn chỉ có thể nạp chồng các toán tử đã có sẵn trong ngữ pháp của ngôn ngữ C++.

---

## 6. LỚP TIME (TIỀN TỐ (PREFIX) vs HẬU TỐ (POSTFIX) ++)

### 6.1 Tiền tố (Prefix) `++a` → Trình Biên Dịch Tạo `Time::operator++()`

Toán tử tăng **tiền tố (Prefix)** (và giảm) rất đơn giản:

```cpp
class Time {
    int hours, minutes, seconds;
public:
    Time(int h = 0, int m = 0, int s = 0) : hours(h), minutes(m), seconds(s) {}

    // Prefix ++: increment and return the modified object
    Time& operator++() {
        seconds++;
        if (seconds >= 60) { seconds = 0; minutes++; }
        if (minutes >= 60) { minutes = 0; hours++; }
        return *this;  // return reference to the modified object
    }
};

int main() {
    Time t(0, 59, 59);
    ++t;    // calls t.operator++() — t becomes 1:00:00
            // Returns Time& (reference to t)
}
```

**Chữ ký (Signature)**: `Time& operator++()` — không có tham số. Trình biên dịch thấy `++t` và tạo lời gọi đến `operator++()` không tham số.

**Giá trị trả về**: Trả về **tham chiếu** (`Time&`) — điều này cho phép `++(++t)` hoạt động chính xác (tăng kép). Nó cũng tránh sao chép không cần thiết.

### 6.2 Hậu tố (Postfix) `a++` → Trình Biên Dịch Gọi `Time::operator++(int)`

Toán tử tăng **hậu tố (Postfix)** tinh tế hơn. Nó phải trả về **giá trị cũ** trước khi tăng:

```cpp
class Time {
    int hours, minutes, seconds;
public:
    Time(int h = 0, int m = 0, int s = 0) : hours(h), minutes(m), seconds(s) {}

    // Postfix ++: save old value, increment, return OLD value
    Time operator++(int) {
        Time old = *this;  // save a copy of the current state
        ++(*this);         // reuse prefix operator to do the increment
        return old;        // return the OLD value (by value, not reference!)
    }
};

int main() {
    Time t(0, 59, 59);
    Time old = t++;  // old = 0:59:59, t = 1:00:00
                     // t++ returns Time (a copy), NOT Time&
}
```

**Chữ ký (Signature)**: `Time operator++(int)` — có một **tham số `int` giả**. Đây là cơ chế C++ sử dụng để phân biệt tiền tố (Prefix) với hậu tố (Postfix).

**Giá trị trả về**: Trả về **theo giá trị** (`Time`, KHÔNG phải `Time&`). Trả về tham chiếu đến `old` cục bộ sẽ là tham chiếu treo — nó bị hủy khi hàm thoát. Hậu tố (Postfix) kém hiệu quả hơn về bản chất vì nó yêu cầu một bản sao.

| Khía cạnh | Tiền tố (Prefix) `++t` | Hậu tố (Postfix) `t++` |
|-----------|------------------------|------------------------|
| Chữ ký (Signature) | `Type& operator++()` | `Type operator++(int)` |
| Kiểu trả về | `Type&` (tham chiếu) | `Type` (giá trị/bản sao) |
| Trả về | Đối tượng đã sửa đổi (`*this`) | Giá trị cũ (bản sao) |
| Hiệu quả | Không cần sao chép | Yêu cầu sao chép trạng thái cũ |
| Chuỗi | `++(++t)` hoạt động | `(t++)++` hoạt động nhưng ngữ nghĩa kỳ lạ |

### 6.3 Tham Số `int` Giả — Trình Biên Dịch Truyền Một Hằng Số Giả Cho Đối Số `int` (Không Bao Giờ Được Dùng, Không Có Định Danh) Để Tạo Các CHỮ KÝ Khác Nhau Cho Tiền Tố (Prefix) và Hậu Tố (Postfix)

Tham số `int` giả tồn tại **chỉ để** làm cho chữ ký (Signature) khác nhau:

```cpp
// Without the dummy int — SAME SIGNATURE — would be a redefinition error
Time& operator++();      // prefix  — WRONG if both have same sig
Time  operator++();      // postfix — WRONG: return type alone doesn't distinguish overloads

// WITH the dummy int — DIFFERENT SIGNATURES — valid overloading
Time& operator++();      // prefix  — no parameters
Time  operator++(int);   // postfix — one int parameter (dummy)
```

Khi bạn viết `t++`, trình biên dịch tự động truyền một giá trị nguyên giả (thường là `0`) làm đối số `int`. Tham số thường được **bỏ không tên** (chỉ `int`, không phải `int dummy`) vì giá trị không bao giờ được sử dụng — nó tồn tại chỉ để giải quyết nạp chồng (Overloading resolution):

```cpp
Time operator++(int) {   // note: no parameter name — the int is never used
    Time old = *this;
    // ... increment ...
    return old;
}
```

Quy ước này áp dụng tương tự cho `--` (giảm tiền tố (Prefix) và hậu tố (Postfix)).

---

## 7. TOÁN TỬ GÁN (ASSIGNMENT OPERATOR) vs HÀM TẠO SAO CHÉP (COPY CONSTRUCTOR)

### 7.1 Hàm Tạo Sao Chép (Copy Constructor)

Hàm tạo sao chép (Copy constructor) khởi tạo một đối tượng **mới** như một bản sao của một đối tượng hiện có cùng kiểu:

```cpp
Transcript::Transcript(const Transcript & T) {
    count = T.count;
    courses = new string[MAXCOURSE];
    for (unsigned i = 0; i < count; i++)
        courses[i] = T.courses[i];
}
```

**Khi hàm tạo sao chép (Copy constructor) được gọi:**

```cpp
Transcript t1;                // default constructor
Transcript t2 = t1;           // COPY CONSTRUCTOR — new object being created
Transcript t3(t1);            // COPY CONSTRUCTOR — same, direct syntax
Transcript t4(t1 + t2);       // COPY CONSTRUCTOR — temporary result copied to new object
void foo(Transcript t);       // COPY CONSTRUCTOR — pass by value copies the argument
foo(t1);
Transcript bar() {
    Transcript t;
    return t;                 // COPY CONSTRUCTOR — return value copied (may be elided by RVO)
}
```

**Đặc điểm chính**: Đối tượng đang được xây dựng **chưa tồn tại** — nó không có trạng thái trước đó, vì vậy không có gì để dọn dẹp trước. Hàm tạo sao chép (Copy constructor) chỉ khởi tạo.

### 7.2 Toán Tử Gán (Assignment Operator) (MẪU ĐẦY ĐỦ Từ Bài Giảng)

Toán tử gán (Assignment operator) ghi đè một đối tượng **đã tồn tại** với giá trị của đối tượng khác:

```cpp
Transcript & Transcript::operator=(const Transcript & T) {
    if (this != &T) {                      // 1. Self-assignment check
        delete[] courses;                  // 2. Free old memory
        courses = new string[MAXCOURSE];   // 3. Allocate new memory
        count = T.count;                   // 4. Copy data
        for (int i = 0; i < count; i++)
            courses[i] = T.courses[i];
    }
    return *this;                          // 5. Return reference for chaining
}
```

**Giải thích từng bước của mẫu:**

1. **Kiểm tra tự gán (Self-assignment check)** (`if (this != &T)`): Nếu `t = t;` được viết (hoặc bí danh gây ra tự gán), bỏ qua công việc ngăn `delete[]` phá hủy dữ liệu của chính bạn trước khi bạn sao chép nó. Không có kiểm tra này, `t = t` sẽ xóa mảng, sau đó cố gắng sao chép từ mảng đã xóa (rác) — thảm họa.

2. **Giải phóng bộ nhớ cũ** (`delete[] courses`): Đối tượng đã tồn tại và sở hữu tài nguyên. Trước khi ghi đè bằng dữ liệu mới, bạn phải giải phóng tài nguyên cũ để ngăn rò rỉ bộ nhớ. Nếu bạn bỏ qua bước này và chỉ `new` lên con trỏ, vùng cấp phát cũ bị rò rỉ.

3. **Cấp phát bộ nhớ mới** (`courses = new string[MAXCOURSE]`): Lấy bộ nhớ mới cho dữ liệu đến.

4. **Sao chép dữ liệu**: Sao chép các giá trị từ đối tượng nguồn.

5. **Trả về `*this` bằng tham chiếu** (`return *this`): Trả về tham chiếu đến đối tượng đã được sửa đổi, cho phép chuỗi gán (`a = b = c`). Kiểu trả về là `Transcript &`, KHÔNG phải `Transcript` (sẽ tạo bản sao không cần thiết) và KHÔNG phải `void` (sẽ ngăn chuỗi gán).

### 7.3 Khi Nào Mỗi Cái Được Gọi

```cpp
Transcript t1;            // default constructor
Transcript t2 = t1;       // COPY CONSTRUCTOR — t2 is being created (new object)
Transcript t3(t2);        // COPY CONSTRUCTOR — t3 is being created (new object)

t2 = t1;                  // ASSIGNMENT OPERATOR — t2 already exists, being overwritten
t1 = t2 = t3;             // ASSIGNMENT — chained: t2 = t3 assigns, returns ref, then t1 = ref

// Tricky case — looks like assignment but is actually copy construction:
Transcript t4 = t1;       // COPY CONSTRUCTOR — NOT assignment! t4 is being created.
                          // The '=' here is initialization syntax, not operator=.
```

**Sự khác biệt quan trọng**:

| Tình huống | Ví dụ | Cái được gọi | Tại sao |
|-----------|-------|--------------|---------|
| Đối tượng đang được **khai báo** với bộ khởi tạo | `Transcript t2 = t1;` | Hàm tạo sao chép (Copy constructor) | `t2` không tồn tại trước dòng này |
| Đối tượng đang được **khai báo** với khởi tạo trực tiếp | `Transcript t2(t1);` | Hàm tạo sao chép (Copy constructor) | Tương tự — `t2` là mới |
| Đối tượng **đã tồn tại** ở bên trái của `=` | `t2 = t1;` | `operator=` | `t2` đã tồn tại, đang ghi đè |
| Truyền theo giá trị vào hàm | `void f(Transcript t); f(t1);` | Hàm tạo sao chép (Copy constructor) | Tham số `t` được khởi tạo như một bản sao |
| Trả về theo giá trị | `return t;` | Hàm tạo sao chép (Copy constructor) | Đối tượng giá trị trả về được khởi tạo (có thể được lược bỏ) |

---

## 8. MẪU CÚ PHÁP PHẢI GHI NHỚ

### 8.1 Nạp Chồng Hàm (Function Overloading) (Chữ Ký (Signature) Khác Nhau)

```cpp
// Same name, different parameter types
void swap(unsigned long &a, unsigned long &b) {
    unsigned long tmp = a; a = b; b = tmp;
}
void swap(double &a, double &b) {
    double tmp = a; a = b; b = tmp;
}
void swap(char &a, char &b) {
    char tmp = a; a = b; b = tmp;
}
void swap(Point &a, Point &b) {
    Point tmp = a; a = b; b = tmp;
}
```

### 8.2 Nạp Chồng Toán Tử (Operator Overloading) (Hàm Thành Viên)

```cpp
class AClass {
public:
    // Binary operator as member — left operand is *this
    int operator+(const AClass &a) const { return /* ... */; }

    // Unary operator as member — no parameters
    AClass operator-() const { return /* ... */; }
};
```

### 8.3 Toán Tử Gán (Assignment Operator) (Mẫu Đầy Đủ)

```cpp
class MyClass {
public:
    MyClass& operator=(const MyClass& other) {
        if (this != &other) {          // Self-assignment guard
            // 1. Free existing resources
            delete[] data;
            // 2. Allocate new resources
            data = new int[other.size];
            // 3. Copy data
            size = other.size;
            for (int i = 0; i < size; i++)
                data[i] = other.data[i];
        }
        return *this;                  // Enable chaining: a = b = c
    }
};
```

### 8.4 Hàm Tạo Sao Chép (Copy Constructor)

```cpp
class MyClass {
public:
    MyClass(const MyClass& other) {
        // No self-assignment check needed — this is a NEW object
        data = new int[other.size];
        size = other.size;
        for (int i = 0; i < size; i++)
            data[i] = other.data[i];
    }
};
```

### 8.5 Tiền Tố (Prefix) vs Hậu Tố (Postfix) `operator++`

```cpp
class Counter {
    int value;
public:
    // PREFIX ++x: increment, return CHANGED object by reference
    Counter& operator++() {
        value++;
        return *this;
    }

    // POSTFIX x++: return OLD value by copy, dummy int distinguishes
    Counter operator++(int) {
        Counter old = *this;   // save copy
        ++(*this);             // reuse prefix to increment
        return old;            // return OLD value
    }
};
```

### 8.6 Các Toán Tử KHÔNG THỂ Nạp Chồng (Overloading) (Ghi Nhớ Danh Sách Này)

| Toán tử | Tên |
|----------|------|
| `.`      | Truy cập thành viên |
| `.*`     | Truy cập-giải tham chiếu thành viên |
| `::`     | Giải quyết phạm vi |
| `?:`     | Điều kiện ba ngôi (số học-IF) |

**Chỉ bốn toán tử này không thể được nạp chồng.** Mọi thứ khác (`+`, `-`, `*`, `/`, `%`, `=`, `==`, `<`, `>`, `<<`, `>>`, `[]`, `()`, `new`, `delete`, `->`, v.v.) ĐỀU CÓ THỂ được nạp chồng.

---

## 9. BẪY THI CỬ

### Bẫy 1: Chỉ Riêng Kiểu Trả Về Không Thể Phân Biệt Nạp Chồng

```cpp
int  getValue();      // OK
// double getValue(); // ERROR: redeclaration — same signature
                       // Return type is NOT part of the signature
```

### Bẫy 2: Đối Số `double` Mơ Hồ Với Nạp Chồng `int`/`float`

```cpp
void f(int x);
void f(float x);
double d = 3.14;
f(d);  // ERROR — double matches BOTH int and float equally
```

### Bẫy 3: Hàm Tạo Sao Chép (Copy Constructor) vs Toán Tử Gán (Assignment Operator) — KHI NÀO Mỗi Cái Được Gọi

```cpp
MyClass a;
MyClass b = a;  // COPY CONSTRUCTOR — b is NEW (looks like = but it's init)
b = a;          // ASSIGNMENT OPERATOR — b already exists
```

Dấu `=` trong một **khai báo** là cú pháp khởi tạo (hàm tạo sao chép (Copy constructor)), KHÔNG phải toán tử gán (Assignment operator)!

### Bẫy 4: Phải Kiểm Tra Tự Gán (Self-Assignment Check) Nếu Không Bạn Xóa Dữ Liệu Của Chính Mình

```cpp
Transcript& Transcript::operator=(const Transcript& T) {
    if (this != &T) {    // WITHOUT THIS CHECK:
        delete[] courses; // If t = t, this deletes t's own courses!
        // ...
    }
    return *this;
}
```

### Bẫy 5: `operator=` Phải Trả Về `*this` Bằng Tham Chiếu

```cpp
MyClass& MyClass::operator=(const MyClass& other) {  // Return by REFERENCE
    // ...
    return *this;  // Return reference to self
}
```

Trả về `void` sẽ ngăn chuỗi `a = b = c`.
Trả về theo giá trị (`MyClass`) sẽ tạo một bản sao không cần thiết.

### Bẫy 6: Tiền Tố (Prefix) Trả Về `Type&`, Hậu Tố (Postfix) Trả Về `Type`

```cpp
Type& operator++();   // PREFIX  — returns reference (no copy)
Type  operator++(int); // POSTFIX — returns value (must copy old state)
```

Hậu tố (Postfix) trả về bằng tham chiếu sẽ là **tham chiếu treo** — trả về tham chiếu đến biến cục bộ bị hủy khi hàm thoát.

### Bẫy 7: Không Thể Nạp Chồng `.` `.*` `::` `?:`

Chỉ bốn toán tử này bị cấm. Hãy thuộc lòng — đây chắc chắn là câu hỏi thi.

### Bẫy 8: Không Thể Thay Đổi Thứ Tự Ưu Tiên, Tính Kết Hợp, hoặc Ngôi

```cpp
// NONE of this works:
// int operator+(int a, int b, int c);  // ERROR: arity changed (3 operands)
// int operator+(int a);                // ERROR: arity changed (unary + is different operator)
// int operator**(int a, int b);        // ERROR: cannot invent new operators
```

### Bẫy 9: Đối Số Mặc Định Không Thể Dùng Với Toán Tử Nạp Chồng

```cpp
class Bad {
public:
    // int operator+(int x, int y = 5);  // ERROR: default arguments not allowed
};
```

### Bẫy 10: Các Hàm Cùng Tên Nên Làm Những Việc Tương Tự

Sử dụng cùng tên cho getter và setter (ví dụ: `credits()` vs `credits(unsigned)`) là thực hành kém vì ngữ nghĩa khác biệt đáng kể. Thay vào đó hãy dùng `getCredits()` và `setCredits()`.

### Bẫy 11: Hàm Khớp Tốt Nhất: Không Có hoặc Nhiều Hàm Khớp = Lỗi

```cpp
void f(int, double);
void f(double, int);
f(1, 1);  // ERROR — ambiguous! int→int exact vs int→double in first vs second
```

### Bẫy 12: Ép Kiểu Tường Minh Giải Quyết Sự Mơ Hồ

```cpp
void f(int);
void f(float);
double d = 3.14;
f(static_cast<int>(d));    // OK — explicitly calls f(int)
f(static_cast<float>(d));  // OK — explicitly calls f(float)
```

### Bẫy 13: Ép Kiểu (Coercion) vs Nạp Chồng (Overloading) — Các Khái Niệm Khác Nhau

- **Ép kiểu (Coercion)**: Chuyển đổi kiểu tự động (`int` → `long`, `float` → `double`).
- **Nạp chồng (Overloading)**: Nhiều hàm cùng tên, chữ ký (Signature) khác nhau.
- **Chúng tương tác**: ép kiểu (Coercion) làm cho đối số khớp với các ứng viên nạp chồng, điều này có thể gây ra sự mơ hồ.

### Bẫy 14: Thực Hành Kém — Getter/Setter Cùng Tên

```cpp
class Student {
    unsigned credits();          // getter
    unsigned credits(unsigned n); // setter — DIFFERENT semantics, BAD design
};
```

### Bẫy 15: `int` Giả Trong Toán Tử Hậu Tố (Postfix)

```cpp
Time operator++(int);   // postfix — the 'int' is a DUMMY, never used
                        // Its only purpose is to create a different signature
                        // from the prefix version: Time& operator++()
```

### Bẫy Thưởng 16: `=` Trong Khai Báo vs Gán

```cpp
int x = 5;        // Initialization (constructor), NOT operator=
x = 10;           // Assignment (operator=)

MyClass a;
MyClass b = a;    // COPY CONSTRUCTOR — initialization syntax
b = a;            // operator= — assignment
```

### Bẫy Thưởng 17: Tính `const` Của `*this` Trong Nạp Chồng Toán Tử (Operator Overloading)

```cpp
class MyClass {
    int operator+(const MyClass& a) { /* modifies *this? */ }     // non-const
    int operator+(const MyClass& a) const { /* doesn't modify */ } // const — valid overload!
};
// These have DIFFERENT signatures because const on member functions IS part of the signature.
```

---

## 10. BÀI TẬP TỰ VIẾT MÃ

---

### Bài Tập 1: Câu Đố Giải Quyết Nạp Chồng (Overloading Resolution) — `f(int, double)` vs `f(double, int)`

```cpp
#include <iostream>
using namespace std;

void f(int a, double b) { cout << "f(int, double): " << a << ", " << b << endl; }
void f(double a, int b) { cout << "f(double, int): " << a << ", " << b << endl; }

int main() {
    int i = 1;
    double d = 2.0;

    f(i, d);       // line A — which f?
    f(d, i);       // line B — which f?
    f(i, i);       // line C — which f?
    f(d, d);       // line D — which f?
    f(1, 2);       // line E — which f?
    f(1.0, 2.0);   // line F — which f?
    f(1, 2.0);     // line G — which f?
}
```

Với mỗi dòng, hãy cho biết nạp chồng nào được gọi, hoặc giải thích tại sao nó mơ hồ.

> [!success]- Hiển thị Đáp án
> > - **Dòng A**: `f(int, double)` — cả hai đối số khớp chính xác. `f(double, int)` cần int→double và double→int. Khớp chính xác thắng.
> > - **Dòng B**: `f(double, int)` — cả hai đối số khớp chính xác. Đối xứng với A.
> > - **Dòng C**: `f(int→int, double→int)` thắng `f(int→double, int→int)`? Chờ —
> >   - Ứng viên 1: `f(int, double)` — i khớp chính xác, i cần chuyển đổi int→double
> >   - Ứng viên 2: `f(double, int)` — i cần chuyển đổi int→double, i khớp chính xác
> >   - Cả hai đều có một khớp chính xác + một chuyển đổi → **MƠ HỒ → LỖI**
> > - **Dòng D**: `f(double, double)` —
> >   - Ứng viên 1: `f(int, double)` — d cần double→int, d khớp chính xác
> >   - Ứng viên 2: `f(double, int)` — d khớp chính xác, d cần double→int
> >   - Đối xứng → **MƠ HỒ → LỖI**
> > - **Dòng E**: Cả `1` và `2` đều là hằng `int` → tương tự Dòng C → **MƠ HỒ → LỖI**
> > - **Dòng F**: Cả `1.0` và `2.0` đều là hằng `double` → tương tự Dòng D → **MƠ HỒ → LỖI**
> > - **Dòng G**: `1` là int (khớp chính xác cho tham số đầu của f1), `2.0` là double (khớp chính xác cho tham số thứ hai của f1) → `f(int, double)`
> >
> > **Điểm mấu chốt**: Các dòng C-F đều là LỖI vì các nạp chồng hoàn toàn đối xứng — mỗi ứng viên có một khớp chính xác và một yêu cầu chuyển đổi. Trình biên dịch không thể phá vỡ sự hòa.

---

### Bài Tập 2: Nạp Chồng Toán Tử (Operator Overloading) — Lớp Số Phức (Complex)

Implement một lớp `Complex` với `operator+`, `operator-`, `operator*`, và `operator<<`:

```cpp
#include <iostream>
using namespace std;

class Complex {
    double real, imag;
public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}

    // TODO: Implement these
    Complex operator+(const Complex& other) const { /* ... */ }
    Complex operator-(const Complex& other) const { /* ... */ }
    Complex operator*(const Complex& other) const { /* ... */ }
    friend ostream& operator<<(ostream& os, const Complex& c) { /* ... */ }
};

int main() {
    Complex a(3, 2), b(1, 7);
    Complex c = a + b;     // Should be (4, 9)
    Complex d = a - b;     // Should be (2, -5)
    Complex e = a * b;     // Should be (3*1 - 2*7, 3*7 + 2*1) = (-11, 23)
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;
    cout << "a+b = " << c << endl;
    cout << "a-b = " << d << endl;
    cout << "a*b = " << e << endl;
}
```

> [!success]- Hiển thị Đáp án
> > ```cpp
> > #include <iostream>
> > using namespace std;
> > 
> > class Complex {
> >     double real, imag;
> > public:
> >     Complex(double r = 0, double i = 0) : real(r), imag(i) {}
> > 
> >     Complex operator+(const Complex& other) const {
> >         return Complex(real + other.real, imag + other.imag);
> >     }
> > 
> >     Complex operator-(const Complex& other) const {
> >         return Complex(real - other.real, imag - other.imag);
> >     }
> > 
> >     Complex operator*(const Complex& other) const {
> >         // (a+bi)(c+di) = (ac-bd) + (ad+bc)i
> >         return Complex(
> >             real * other.real - imag * other.imag,
> >             real * other.imag + imag * other.real
> >         );
> >     }
> > 
> >     friend ostream& operator<<(ostream& os, const Complex& c) {
> >         os << "(" << c.real;
> >         if (c.imag >= 0) os << " + " << c.imag << "i";
> >         else             os << " - " << -c.imag << "i";
> >         os << ")";
> >         return os;
> >     }
> > };
> > ```
> >
> > **Điểm chính**:
> > - `operator+`, `operator-`, `operator*` là các hàm thành viên `const` — chúng không sửa đổi `*this`.
> > - Chúng trả về **theo giá trị** (một `Complex` mới), không phải tham chiếu — kết quả là một đối tượng tạm thời.
> > - `operator<<` phải là `friend` (hoặc không phải thành viên) vì toán hạng trái là `ostream`, không phải `Complex`. Nó cũng trả về `ostream&` để cho phép chuỗi (`cout << a << b`).

---

### Bài Tập 3: Nạp Chồng Toán Tử (Operator Overloading) — Lớp Money Với `+` và `<`

```cpp
class Money {
    long dollars;
    int  cents;
public:
    Money(long d = 0, int c = 0) : dollars(d), cents(c) { normalize(); }

    void normalize() {
        if (cents >= 100) { dollars += cents / 100; cents %= 100; }
        if (cents < 0)    { dollars -= 1 + (-cents) / 100; cents = 100 - (-cents) % 100; }
    }

    // TODO: Implement operator+, operator<, operator==, operator<<
    Money operator+(const Money& m) const { /* ... */ }
    bool operator<(const Money& m) const { /* ... */ }
    bool operator==(const Money& m) const { /* ... */ }
    friend ostream& operator<<(ostream& os, const Money& m) { /* ... */ }
};

int main() {
    Money m1(10, 50), m2(5, 75), m3(16, 25);
    cout << (m1 + m2) << endl;       // $16.25
    cout << ((m1 + m2) == m3) << endl; // 1 (true)
    cout << (m1 < m2) << endl;       // 0 (false — 10.50 > 5.75)
    cout << (m2 < m1) << endl;       // 1 (true — 5.75 < 10.50)
}
```

> [!success]- Hiển thị Đáp án
> > ```cpp
> > class Money {
> >     long dollars;
> >     int  cents;
> > public:
> >     Money(long d = 0, int c = 0) : dollars(d), cents(c) { normalize(); }
> > 
> >     void normalize() {
> >         if (cents >= 100) { dollars += cents / 100; cents %= 100; }
> >         if (cents < 0)    { dollars -= 1 + (-cents) / 100; cents = 100 - (-cents) % 100; }
> >     }
> > 
> >     Money operator+(const Money& m) const {
> >         return Money(dollars + m.dollars, cents + m.cents);
> >     }
> > 
> >     bool operator<(const Money& m) const {
> >         if (dollars != m.dollars) return dollars < m.dollars;
> >         return cents < m.cents;
> >     }
> > 
> >     bool operator==(const Money& m) const {
> >         return dollars == m.dollars && cents == m.cents;
> >     }
> > 
> >     friend ostream& operator<<(ostream& os, const Money& m) {
> >         os << "$" << m.dollars << ".";
> >         if (m.cents < 10) os << "0";
> >         os << m.cents;
> >         return os;
> >     }
> > };
> > ```
> >
> > **Điểm chính**:
> > - `operator==`, `operator<` trả về `bool`.
> > - `operator+` ủy quyền cho hàm tạo, hàm này tự động chuẩn hóa.
> > - Các toán tử so sánh (`<`, `==`) kiểm tra `dollars` trước, sau đó `cents` — đoản mạch hiệu quả.

---

### Bài Tập 4: Mẫu Toán Tử Gán (Assignment Operator) — Sao Chép Sâu Cho Mảng Động

Hoàn thành lớp `Transcript` với hàm tạo sao chép (Copy constructor) và toán tử gán (Assignment operator) phù hợp:

```cpp
#include <iostream>
#include <string>
using namespace std;

class Transcript {
    const static int MAXCOURSE = 100;
    string* courses;
    unsigned count;
public:
    Transcript() : courses(new string[MAXCOURSE]), count(0) {}
    ~Transcript() { delete[] courses; }

    // TODO: Implement these
    Transcript(const Transcript& T) { /* ... */ }
    Transcript& operator=(const Transcript& T) { /* ... */ }
    void addCourse(const string& name) { if (count < MAXCOURSE) courses[count++] = name; }
    void print() const {
        cout << "Courses (" << count << "): ";
        for (unsigned i = 0; i < count; i++) cout << courses[i] << " ";
        cout << endl;
    }
};

int main() {
    Transcript t1;
    t1.addCourse("CS101"); t1.addCourse("MATH201");

    Transcript t2 = t1;        // copy constructor
    Transcript t3;
    t3.addCourse("PHYS101");
    t3 = t1;                   // assignment operator — overwrites existing PHYS101

    t1.print();  // Courses (2): CS101 MATH201
    t2.print();  // Courses (2): CS101 MATH201
    t3.print();  // Courses (2): CS101 MATH201

    t1 = t1;     // self-assignment — must not crash!
    t1.print();  // Courses (2): CS101 MATH201
}
```

> [!success]- Hiển thị Đáp án
> > ```cpp
> > Transcript::Transcript(const Transcript& T) {
> >     count = T.count;
> >     courses = new string[MAXCOURSE];
> >     for (unsigned i = 0; i < count; i++)
> >         courses[i] = T.courses[i];
> > }
> > 
> > Transcript& Transcript::operator=(const Transcript& T) {
> >     if (this != &T) {                     // Self-assignment check
> >         delete[] courses;                 // Free old memory
> >         courses = new string[MAXCOURSE];  // Allocate new
> >         count = T.count;
> >         for (int i = 0; i < count; i++)
> >             courses[i] = T.courses[i];
> >     }
> >     return *this;
> > }
> > ```
> >
> > **Sự khác biệt chính giữa hàm tạo sao chép (Copy constructor) và toán tử gán (Assignment operator)**:
> > - Hàm tạo sao chép (Copy constructor): KHÔNG có kiểm tra tự gán (Self-assignment check) (đối tượng mới), KHÔNG có `delete[]` (không có gì để giải phóng), KHÔNG có `return *this`.
> > - Toán tử gán (Assignment operator): PHẢI kiểm tra `this != &T`, PHẢI giải phóng tài nguyên cũ trước (`delete[]`), PHẢI trả về `*this` bằng tham chiếu.

---

### Bài Tập 5: Tiền Tố (Prefix) vs Hậu Tố (Postfix) — Lớp Time Tăng Dần

```cpp
#include <iostream>
using namespace std;

class Time {
    int hours, minutes, seconds;
    void normalize() {
        if (seconds >= 60) { minutes += seconds / 60; seconds %= 60; }
        if (minutes >= 60) { hours += minutes / 60; minutes %= 60; }
        hours %= 24;
    }
public:
    Time(int h = 0, int m = 0, int s = 0) : hours(h), minutes(m), seconds(s) { normalize(); }

    // TODO: Implement prefix ++ and postfix ++
    Time& operator++() { /* ... */ }
    Time operator++(int) { /* ... */ }

    void print() const { cout << hours << ":" << minutes << ":" << seconds << endl; }
};

int main() {
    Time t(23, 59, 50);
    Time old = t++;
    old.print();  // 23:59:50 — old value
    t.print();    // 23:59:51

    ++t;
    t.print();    // 23:59:52

    ++(++t);
    t.print();    // 23:59:54 — double prefix works (returns reference)

    Time t2(23, 59, 59);
    t2++;
    t2.print();   // 0:0:0 — wraparound at midnight
}
```

> [!success]- Hiển thị Đáp án
> > ```cpp
> > Time& Time::operator++() {
> >     seconds++;
> >     normalize();
> >     return *this;
> > }
> > 
> > Time Time::operator++(int) {
> >     Time old = *this;
> >     ++(*this);          // reuse prefix operator
> >     return old;
> > }
> > ```
> >
> > **Điểm chính**:
> > - Tiền tố (`++t`): `Time& operator++()` — trả về tham chiếu đến `*this` đã sửa đổi. Cho phép `++(++t)`.
> > - Hậu tố (`t++`): `Time operator++(int)` — trả về theo giá trị (trạng thái cũ). Tham số `int` không bao giờ được dùng — nó tồn tại CHỈ để phân biệt với tiền tố.
> > - Thực hành tốt nhất: implement hậu tố bằng cách gọi tiền tố — tránh trùng lặp logic tăng.

---

### Bài Tập 6: Kịch Bản Ép Kiểu (Coercion) — Nạp Chồng Nào?

```cpp
#include <iostream>
using namespace std;

void display(int x)    { cout << "display(int): "    << x << endl; }
void display(float x)  { cout << "display(float): "  << x << endl; }
void display(double x) { cout << "display(double): " << x << endl; }

void func(long a, float b)  { cout << "func(long, float)" << endl; }
void func(int a, double b)  { cout << "func(int, double)" << endl; }

int main() {
    char c = 'A';
    short s = 10;
    int i = 42;
    float f = 3.14f;
    double d = 2.718;
    long l = 100L;

    display(c);       // line A
    display(s);       // line B
    display(i);       // line C
    display(f);       // line D
    display(d);       // line E
    display(l);       // line F

    func(i, f);       // line G
    func(l, d);       // line H
}
```

Với mỗi dòng, hãy xác định nạp chồng nào được gọi (hoặc nếu mơ hồ), và giải thích tại sao.

> [!success]- Hiển thị Đáp án
> > - **Dòng A** `display(c)`: `char` thăng hạng lên `int` (khớp tốt nhất) → `display(int)`. Cũng có thể chuyển sang `float` hoặc `double`, nhưng thăng hạng lên `int` tốt hơn chuyển đổi sang `float`.
> > - **Dòng B** `display(s)`: `short` thăng hạng lên `int` → `display(int)`. Cùng lý luận.
> > - **Dòng C** `display(i)`: `int` khớp chính xác → `display(int)`.
> > - **Dòng D** `display(f)`: `float` khớp chính xác → `display(float)`.
> > - **Dòng E** `display(d)`: `double` khớp chính xác → `display(double)`.
> > - **Dòng F** `display(l)`: `long` — không có nạp chồng `long` chính xác. `long → int` là chuyển đổi (có thể mất dữ liệu), `long → float` và `long → double` cũng là chuyển đổi. `long → float` và `long → double` là **chuyển đổi dấu phẩy động-số nguyên**, `long → int` là **chuyển đổi số nguyên**. Không có chuyển đổi nào tốt hơn hẳn → **MƠ HỒ → LỖI**.
> > - **Dòng G** `func(i, f)`: `func(int, double)` — i khớp chính xác, f cần thăng hạng float→double. `func(long, float)` — chuyển đổi int→long, f khớp chính xác. Khớp chính xác + thăng hạng thắng chuyển đổi + khớp chính xác → `func(int, double)` thắng.
> > - **Dòng H** `func(l, d)`: `func(long, float)` — l khớp chính xác, d cần chuyển đổi double→float. `func(int, double)` — l cần chuyển đổi long→int, d khớp chính xác. Cả hai đều có một khớp chính xác + một chuyển đổi → **MƠ HỒ → LỖI**.

---

### Bài Tập 7: Nạp Chồng Hàm Tạo (Constructor Overloading) — Hoàn Thiện Lớp Figure/Point

Mở rộng lớp `Figure` với các hàm tạo bổ sung và dấu vết hàm tạo nào được gọi trong mỗi trường hợp:

```cpp
#include <iostream>
#include <string>
using namespace std;

class Point {
public:
    int x, y;
    Point(int xx = 0, int yy = 0) : x(xx), y(yy) {
        cout << "  Point(" << x << ", " << y << ") constructed" << endl;
    }
};

class Figure {
    string name;
    Point* vertices;
    int vertexCount;
public:
    Figure() : name("Empty"), vertices(nullptr), vertexCount(0) {
        cout << "Figure() — default" << endl;
    }
    Figure(const string& n) : name(n), vertices(nullptr), vertexCount(0) {
        cout << "Figure(string) — named: " << name << endl;
    }
    Figure(const Point& center) : name("Centered"), vertices(new Point[1]), vertexCount(1) {
        vertices[0] = center;
        cout << "Figure(Point) — center-based" << endl;
    }
    Figure(const Point verts[], int count) : name("Polygon"), vertices(new Point[count]), vertexCount(count) {
        for (int i = 0; i < count; i++) vertices[i] = verts[i];
        cout << "Figure(Point[], int) — " << count << " vertices" << endl;
    }
    ~Figure() { delete[] vertices; }
};

int main() {
    // TODO: For each line below, write which constructor is called
    // and whether a Figure or Point constructor runs at each step.

    Figure f1;                                           // line 1
    Figure f2("Triangle");                               // line 2
    Point p(10, 20);                                     // line 3
    Figure f3(p);                                        // line 4

    Point verts[3];                                      // line 5
    Figure f4(verts, 3);                                 // line 6

    const int N = 3;
    Point arr[N] = { Point(1,2), Point(3,4), Point(5,6) }; // line 7
    Figure f5(arr, N);                                   // line 8

    Figure f6 = f2;                                      // line 9 — what constructor is this?
}
```

Dấu vết tất cả các lời gọi hàm tạo và xác định điều gì xảy ra ở dòng 9 (là hàm tạo sao chép (Copy constructor) hay toán tử gán (Assignment operator)?).

> [!success]- Hiển thị Đáp án
> > **Dòng 1** `Figure f1;`:
> > - Gọi `Figure()` — hàm tạo mặc định.
> > - Đầu ra: `Figure() — default`
> >
> > **Dòng 2** `Figure f2("Triangle");`:
> > - Gọi `Figure(const string&)` — hàm tạo chuỗi.
> > - Đầu ra: `Figure(string) — named: Triangle`
> >
> > **Dòng 3** `Point p(10, 20);`:
> > - Gọi `Point(int, int)` — hàm tạo hai đối số.
> > - Đầu ra: `Point(10, 20) constructed`
> >
> > **Dòng 4** `Figure f3(p);`:
> > - Gọi `Figure(const Point&)` — hàm tạo dựa trên tâm.
> > - Đầu ra: `Figure(Point) — center-based`
> >
> > **Dòng 5** `Point verts[3];`:
> > - Gọi `Point()` (hàm tạo mặc định) **3 lần** — một lần mỗi phần tử mảng.
> > - Đầu ra: `Point(0, 0) constructed` ba lần
> >
> > **Dòng 6** `Figure f4(verts, 3);`:
> > - Gọi `Figure(const Point[], int)` — hàm tạo mảng + số lượng.
> > - Đầu ra: `Figure(Point[], int) — 3 vertices`
> >
> > **Dòng 7** `Point arr[N] = { Point(1,2), Point(3,4), Point(5,6) };`:
> > - Gọi `Point(int, int)` ba lần (mỗi lần một bộ khởi tạo).
> > - Đầu ra: `Point(1, 2) constructed`, `Point(3, 4) constructed`, `Point(5, 6) constructed`
> >
> > **Dòng 8** `Figure f5(arr, N);`:
> > - Gọi `Figure(const Point[], int)` — hàm tạo mảng + số lượng.
> > - Đầu ra: `Figure(Point[], int) — 3 vertices`
> >
> > **Dòng 9** `Figure f6 = f2;`:
> > - Đây là lời gọi **HÀM TẠO SAO CHÉP (COPY CONSTRUCTOR)**, KHÔNG phải toán tử gán (Assignment operator). `f6` đang được khai báo và khởi tạo trong cùng một dòng. Dấu `=` ở đây là cú pháp khởi tạo.
> > - Vì chúng ta không định nghĩa hàm tạo sao chép (Copy constructor), trình biên dịch tạo ra một **hàm tạo sao chép mặc định** (sao chép nông). Điều này **nguy hiểm** — nó sao chép con trỏ `vertices` thay vì thực hiện sao chép sâu. Khi cả `f2` và `f6` ra khỏi phạm vi, các hàm hủy sẽ cố gắng `delete[]` cùng một con trỏ hai lần → **giải phóng kép / hành vi không xác định**.
> >
> > **Thứ tự đầu ra đầy đủ**:
> > ```
> > Figure() — default
> > Figure(string) — named: Triangle
> >   Point(10, 20) constructed
> > Figure(Point) — center-based
> >   Point(0, 0) constructed
> >   Point(0, 0) constructed
> >   Point(0, 0) constructed
> > Figure(Point[], int) — 3 vertices
> >   Point(1, 2) constructed
> >   Point(3, 4) constructed
> >   Point(5, 6) constructed
> > Figure(Point[], int) — 3 vertices
> > ```
> >
> > **Bẫy dòng 9**: `Figure f6 = f2;` là **xây dựng sao chép**, không phải gán. Nếu không có hàm tạo sao chép do người dùng định nghĩa, hàm tạo do trình biên dịch tạo ra thực hiện **sao chép nông**, chia sẻ con trỏ `vertices` → giải phóng kép khi hủy. Điều này nhấn mạnh lý do tại sao các lớp có bộ nhớ động PHẢI tự định nghĩa hàm tạo sao chép (Copy constructor) của riêng mình (**Quy tắc Ba**).

---

### Bài Tập 8: Giải Quyết Nạp Chồng (Overloading Resolution) Toàn Diện — Nhiều Ứng Viên

```cpp
#include <iostream>
using namespace std;

void foo(int a, int b)          { cout << "foo(int, int)" << endl; }
void foo(int a, double b)       { cout << "foo(int, double)" << endl; }
void foo(double a, int b)       { cout << "foo(double, int)" << endl; }
void foo(double a, double b)    { cout << "foo(double, double)" << endl; }

int main() {
    int    i = 1;
    float  f = 2.5f;
    double d = 3.0;
    char   c = 'A';

    foo(i, i);   // A
    foo(i, d);   // B
    foo(d, i);   // C
    foo(d, d);   // D
    foo(i, c);   // E
    foo(f, f);   // F
    foo(c, c);   // G
    foo(i, f);   // H
    foo(f, d);   // I
}
```

> [!success]- Hiển thị Đáp án
> > - **A**: `foo(int, int)` — cả hai khớp chính xác → `foo(int, int)`
> > - **B**: `foo(int, double)` — i khớp chính xác, d khớp chính xác → `foo(int, double)`
> > - **C**: `foo(double, int)` — d khớp chính xác, i khớp chính xác → `foo(double, int)`
> > - **D**: `foo(double, double)` — cả hai khớp chính xác → `foo(double, double)`
> > - **E**: `foo(i, c)` — i khớp chính xác. c là `char`:
> >   - `foo(int, int)` — c: char→int (thăng hạng)
> >   - `foo(int, double)` — c: char→double (thăng hạng... nhưng thăng hạng int tốt hơn)
> >   - Lưu ý: `char → int` là thăng hạng, `char → double` là chuyển đổi dài hơn. `foo(int, int)` thắng.
> > - **F**: `foo(f, f)` — cả hai `float`:
> >   - `foo(int, int)` — cả hai cần float→int (chuyển đổi)
> >   - `foo(int, double)` — float→int, float→double (chuyển đổi + thăng hạng)
> >   - `foo(double, int)` — float→double, float→int (thăng hạng + chuyển đổi)
> >   - `foo(double, double)` — cả hai float→double (thăng hạng)
> >   - `foo(double, double)` **tốt nhất** (hai thăng hạng) thắng hỗn hợp chuyển đổi+thăng hạng hoặc hai chuyển đổi → `foo(double, double)`
> > - **G**: `foo(c, c)` — cả hai `char`:
> >   - `foo(int, int)` — cả hai char→int (thăng hạng) → tốt nhất: hai thăng hạng
> >   - Các ứng viên khác có chuyển đổi + thăng hạng hoặc chuỗi dài hơn → `foo(int, int)` thắng.
> > - **H**: `foo(i, f)` — i là int khớp chính xác, f là float:
> >   - `foo(int, int)` — f: float→int (chuyển đổi)
> >   - `foo(int, double)` — f: float→double (thăng hạng)
> >   - `foo(int, double)` thắng (thăng hạng thắng chuyển đổi cho đối số float) → `foo(int, double)`
> > - **I**: `foo(f, d)` — f là float, d là double:
> >   - `foo(int, double)` — f: float→int (chuyển đổi), d khớp chính xác
> >   - `foo(double, double)` — f: float→double (thăng hạng), d khớp chính xác
> >   - `foo(double, double)` thắng → `foo(double, double)`

---

> [!NOTE]
> Hướng dẫn ôn tập này bao gồm tất cả nội dung bài giảng cho Lec10: Nạp chồng (Overloading). Nắm vững sự phân biệt giữa nạp chồng (Overloading) (thời gian biên dịch, chữ ký (Signature) khác nhau) và ghi đè (overriding) (thời gian chạy, cùng chữ ký, cần virtual). Ghi nhớ bốn toán tử bị cấm (`.`, `.*`, `::`, `?:`), sự khác biệt chữ ký (Signature) tiền tố (Prefix)/hậu tố (Postfix) `++`, mẫu tự gán (Self-assignment check) của toán tử gán (Assignment operator), và sự phân biệt giữa hàm tạo sao chép (Copy constructor) và toán tử gán (Assignment operator). Luyện tập các bài giải quyết nạp chồng (Overloading resolution) cho đến khi bạn có thể dự đoán lựa chọn của trình biên dịch mà không do dự.
