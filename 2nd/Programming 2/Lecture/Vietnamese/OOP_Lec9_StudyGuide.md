# Lec9: Tính đa hình (Polymorphism) — Hướng dẫn học tập

---

## 1. THẺ KHÁI NIỆM

### 1.1 Định nghĩa

Tính đa hình (Polymorphism) (trong OOP, cụ thể là **Đa hình bao hàm / Ghi đè — Inclusion Polymorphism / Overriding**) là khả năng các đối tượng thuộc các kiểu khác nhau phản hồi khác nhau với **cùng một lời gọi hàm** với **cùng kiểu tham số**. Phiên bản đúng của hàm được chọn tại **thời gian chạy (runtime)** dựa trên kiểu thực tế của đối tượng, chứ không phải kiểu của con trỏ hay tham chiếu.

### 1.2 Vấn đề nó giải quyết

Không có tính đa hình, mã làm việc với các tập hợp đối tượng không đồng nhất (heterogeneous) phải kiểm tra tường minh kiểu của từng đối tượng và rẽ nhánh tương ứng:

```cpp
if (type == CIRCLE)      drawCircle();
else if (type == RECTANGLE) drawRectangle();
else if (type == TRIANGLE)  drawTriangle();
```

Thêm một kiểu mới (`Hexagon`) yêu cầu sửa đổi **mọi** chuỗi if-else như vậy trong toàn bộ mã nguồn. Với tính đa hình, bạn gọi `shape->draw()` và mỗi đối tượng tự biết cách vẽ chính nó. Thêm một lớp hình dạng mới yêu cầu **không thay đổi gì** trong mã hiện có.

### 1.3 Cách hoạt động

1. Khai báo một hàm là `virtual` trong lớp cơ sở (base class).
2. Ghi đè (Override) nó trong mỗi lớp dẫn xuất (cùng chữ ký — cùng tên, cùng kiểu tham số).
3. Tạo đối tượng và lưu trữ qua con trỏ hoặc tham chiếu của lớp cơ sở: `Base* p = new Derived();`.
4. Gọi `p->virtualFunction()` — trình biên dịch tạo mã tra cứu hàm đúng trong **bảng ảo (vtable)** của đối tượng tại thời gian chạy.
5. Các hàm không phải ảo (non-virtual) sử dụng **ràng buộc tĩnh (static binding)** (được giải quyết tại thời gian biên dịch — nhanh hơn).
6. Các hàm ảo (virtual) sử dụng **ràng buộc động (dynamic binding)** (được giải quyết tại thời gian chạy qua tra cứu vtable — chậm hơn một chút).
7. Mỗi lớp có hàm ảo có một **bảng ảo (vtable)** ẩn — một mảng các con trỏ hàm.
8. Mỗi đối tượng của lớp như vậy có một **con trỏ ảo (vptr)** ẩn trỏ đến vtable của lớp của nó.

### 1.4 Ví dụ cụ thể

Một hệ thống xử lý thanh toán:

- `PaymentMethod` khai báo `virtual void processPayment(double amount)`.
- `CreditCard`, `PayPal`, `BankTransfer` mỗi lớp ghi đè nó với logic riêng (giao tiếp với các API thanh toán khác nhau).
- Hệ thống thanh toán giữ một `PaymentMethod*` được người dùng chọn tại thời gian chạy.
- `method->processPayment(total)` — cách triển khai đúng được chạy mà mã thanh toán không cần biết nó đang xử lý kiểu thanh toán cụ thể nào.
- Thêm `CryptoCurrency` sau này yêu cầu tạo **một lớp mới**. Mã thanh toán **không bao giờ thay đổi**.

### 1.5 Nó KHÔNG phải là gì

Tính đa hình (ghi đè) **KHÔNG phải** là nạp chồng (overloading):

| Khía cạnh | Nạp chồng (Overloading) | Ghi đè / Đa hình (Overriding / Polymorphism) |
|-----------|------------------------|----------------------------------------------|
| Tham số | Kiểu, số lượng hoặc thứ tự **Khác nhau** | Kiểu và số lượng **Giống nhau** |
| Thời điểm giải quyết | Thời gian biên dịch (ràng buộc tĩnh) | Thời gian chạy (ràng buộc động) |
| Từ khóa `virtual` | Không bắt buộc | Bắt buộc trong lớp cơ sở |
| Kế thừa (Inheritance) | Không bắt buộc | Bắt buộc (quan hệ cơ sở-dẫn xuất) |
| Tên gọi khác | Đa hình tùy biến (Ad-hoc polymorphism) | Đa hình bao hàm (Inclusion polymorphism) |

Tính đa hình cũng **KHÔNG phải** là ép kiểu (coercion) — nơi trình biên dịch tự động chuyển đổi một kiểu này sang kiểu khác để khớp với chữ ký hàm.

---

## 2. Ý NGHĨA TỪ NGỮ VÀ ĐỊNH NGHĨA

### 2.1 Nguồn gốc từ

- **poly** (πολύς, tiếng Hy Lạp) — nhiều, đa dạng, khác nhau
- **morph** (μορφή, tiếng Hy Lạp) — dạng, hình thái, cấu trúc

Kết hợp: **"nhiều dạng" (many forms)** — một thực thể mang nhiều hình thái hoặc hành vi khác nhau.

### 2.2 Định nghĩa chính thức

Khả năng gán một **ý nghĩa hoặc cách sử dụng khác** cho một thứ gì đó trong các **ngữ cảnh khác nhau**. Trong lập trình, nó có nghĩa là một giao diện đơn lẻ (tên hàm) có thể đại diện cho nhiều hành vi nền tảng, với hành vi phù hợp được xác định bởi ngữ cảnh (kiểu tham số, hoặc kiểu thời gian chạy của đối tượng).

---

## 3. CÁC LOẠI ĐA HÌNH

### 3.1 Tổng quan bốn loại

Tính đa hình trong lập trình rộng hơn việc chỉ ghi đè trong OOP. Có **bốn loại được công nhận**:

| # | Loại | Thời điểm giải quyết | Cơ chế trong C++ |
|---|------|--------------------|-----------------|
| 1 | Nạp chồng (Overloading) | Thời gian biên dịch | Nhiều hàm, cùng tên, chữ ký khác nhau |
| 2 | Ép kiểu (Coercion) | Thời gian biên dịch | Ép kiểu ngầm định bởi trình biên dịch |
| 3 | Đa hình tham số (Parametric) | Thời gian biên dịch | Template (lập trình tổng quát — generic programming) |
| 4 | Bao hàm / Ghi đè (Inclusion / Overriding) | Thời gian chạy | Hàm ảo (virtual functions) + kế thừa |

**Loại đa hình mà mô hình OOP đề cập đến là #4 — Đa hình bao hàm (Ghi đè).** Ba loại còn lại là các cơ chế thời gian biên dịch (tùy biến hoặc tham số).

### 3.2 Nạp chồng (Overloading)

Nạp chồng có nghĩa là có **cùng tên hàm** hoạt động trên **các kiểu tham số khác nhau**. Chúng ta nạp chồng khi muốn làm "về cơ bản là **cùng một việc**" nhưng với **các tham số khác nhau**.

```cpp
int  add(int a, int b)   { return a + b; }
float add(float a, float b) { return a + b; }
```

- Trình biên dịch quyết định gọi phiên bản nào tại **thời gian biên dịch** bằng cách khớp kiểu đối số.
- Đây là một dạng của **đa hình tùy biến (ad-hoc polymorphism)** — được giải quyết cú pháp tại thời gian biên dịch, không phải động.

### 3.3 Ép kiểu (Coercion)

Ép kiểu là khi một đối tượng hoặc kiểu nguyên thủy được **tự động ép** sang kiểu đối tượng/nguyên thủy khác bởi trình biên dịch để khớp với chữ ký hàm. Nó vượt xa việc nạp chồng đơn giản — trình biên dịch chủ động chuyển đổi kiểu.

```cpp
int  add(int a, int b)   { return a + b; }
float add(float a, float b) { return a + b; }

int main() {
    add(1, 1.0);   // 1.0 (double) bị ÉP KIỂU thành int 1
                   // Trình biên dịch chọn add(int, int)
    add(1.0, 1);   // 1.0 (double) bị ÉP KIỂU thành int 1
                   // Trình biên dịch chọn add(int, int)
}
```

- Trình biên dịch thấy `add(1, 1.0)`. Nó tìm kiếm sự khớp: `add(int, float)` — không tồn tại. Nó tìm thấy `add(int, int)` và `add(float, float)`. Nó chuyển đổi (ép kiểu) `1.0` double thành `int` để khớp.
- Ép kiểu là một cơ chế **thời gian biên dịch** — không liên quan đến tra cứu thời gian chạy.
- Đừng **nhầm lẫn** ép kiểu với ghi đè. Ép kiểu chuyển đổi **đối số**; ghi đè chọn một **thân hàm** khác tại thời gian chạy.

### 3.4 Đa hình tham số (Parametric Polymorphism)

Đa hình tham số cung cấp một cách để thực thi **cùng một mã** cho **bất kỳ kiểu nào**. Mã được viết một lần, và kiểu được cung cấp như một tham số.

- Trong C++, được triển khai qua **template**:

```cpp
template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    add<int>(1, 2);       // T = int
    add<float>(1.5, 2.3); // T = float
    add<string>("Hello ", "World"); // T = string
}
```

- Trình biên dịch tạo ra một **bản sao riêng** của hàm cho mỗi kiểu được sử dụng — việc này được giải quyết tại **thời gian biên dịch**.
- Bắt nguồn từ các ngôn ngữ **lập trình hàm** (functional programming) (ví dụ: ML, Haskell).
- Ngày nay phổ biến trong Java dưới tên **lập trình tổng quát (generic programming)**.
- Lưu ý: trong C++, template được giải quyết tại thời gian biên dịch, trong khi trong Java, generic sử dụng xóa kiểu (type erasure).

### 3.5 Đa hình bao hàm / Ghi đè (Inclusion Polymorphism / Overriding)

**Đây CHÍNH LÀ "tính đa hình" trong ngữ cảnh OOP.** Các đối tượng thuộc các kiểu khác nhau phản hồi khác nhau với **cùng một lời gọi hàm** với **cùng kiểu tham số**.

- Đạt được bằng cách **ghi đè (overriding)** các hàm ảo được kế thừa.
- Chúng ta ghi đè một hàm được kế thừa khi muốn làm điều gì đó **hơi khác** so với những gì lớp cơ sở làm.
- Liên quan chặt chẽ đến khái niệm **kế thừa (inheritance)** — bạn không thể có ghi đè mà không có quan hệ lớp cơ sở-dẫn xuất.

Minh họa với mèo:

```cpp
class Cat {
public:
    virtual void makeSound() { cout << "meow" << endl; }
};

class Lion : public Cat {
public:
    void makeSound() { cout << "MREOWWW" << endl; }
};

class Kitten : public Cat {
public:
    void makeSound() { cout << "mews" << endl; }
};
```

- Cùng thông điệp: `makeSound()`
- Cùng kiểu tham số: `void`
- Phản hồi khác nhau: `meow`, `MREOWWW`, `mews`
- Âm thanh nào được phát ra được xác định bởi **kiểu thời gian chạy** của đối tượng, không phải kiểu con trỏ.

---

## 4. KẾT NỐI CÁC TRỤ CỘT OOP (ÔN TẬP)

### 4.1 Tính đa hình nằm ở đâu

Bốn trụ cột của OOP:

| Trụ cột | Mô tả | Vai trò |
|---------|-------|---------|
| **Đóng gói (Encapsulation)** | Gói gọn dữ liệu và các chức năng liên quan vào một đơn vị duy nhất; ẩn chi tiết nội bộ khỏi thế giới bên ngoài. | Bảo vệ tính toàn vẹn dữ liệu; cung cấp giao diện công khai sạch sẽ. |
| **Kế thừa (Inheritance)** | Dẫn xuất một lớp từ lớp khác, thu nhận các thuộc tính và hành vi của nó. | Cho phép tái sử dụng mã và thiết lập quan hệ "là một" (is-a). |
| **Trừu tượng hóa (Abstraction)** | Ẩn sự phức tạp của việc triển khai; chỉ phơi bày các đặc tả thiết yếu qua giao diện hoặc lớp trừu tượng. | Đơn giản hóa việc sử dụng; tập trung vào *cái gì* chứ không phải *như thế nào*. |
| **Đa hình / Ghi đè (Polymorphism / Overriding)** | Các kiểu khác nhau phản hồi khác nhau với cùng một lời gọi hàm. | Cho phép khả năng mở rộng — các kiểu mới có thể được thêm vào mà không cần thay đổi mã hiện có. |

Tính đa hình phụ thuộc vào **kế thừa** (để thiết lập quan hệ cơ sở-dẫn xuất) và **trừu tượng hóa** (để định nghĩa giao diện chung qua các hàm ảo hoặc hàm ảo thuần túy). Nó hoạt động cùng với **đóng gói** (mỗi lớp đóng gói phiên bản hành vi riêng của nó).

---

## 5. RÀNG BUỘC (BINDING)

### 5.1 Ràng buộc là gì?

Ràng buộc (Binding) là quá trình **kết nối một lời gọi phương thức với một thân phương thức** — xác định cách triển khai hàm cụ thể nào sẽ được thực thi khi một lời gọi được thực hiện.

### 5.2 Ràng buộc tĩnh / Ràng buộc sớm (Static / Early Binding)

- Ràng buộc được thực hiện **trước khi** chương trình chạy (tại **thời gian biên dịch**).
- Trình biên dịch xác định hàm nào sẽ gọi dựa trên **kiểu của con trỏ hoặc tham chiếu**, không phải đối tượng thực tế.
- Được sử dụng mặc định trong trình biên dịch C.
- **Hành vi mặc định trong C++** cho các hàm không phải ảo (non-virtual).
- **Nhanh hơn** — không có chi phí tra cứu thời gian chạy.
- Cho phép tối ưu hóa của trình biên dịch (ví dụ: nội tuyến — inlining).

### 5.3 Ràng buộc động / Ràng buộc muộn (Dynamic / Late Binding)

- Ràng buộc xảy ra tại **thời gian chạy**, dựa trên **kiểu thực tế của đối tượng** được trỏ tới (không phải kiểu con trỏ).
- Hệ thống thời gian chạy theo vptr của đối tượng → vtable để tìm địa chỉ hàm đúng.
- **Chậm hơn một chút** so với ràng buộc tĩnh do gián tiếp qua vtable.
- **Đa hình là một KHÁI NIỆM; ràng buộc động là CƠ CHẾ triển khai nó.**
- Trong C++, các hàm phải được khai báo `virtual` để cho phép ràng buộc động.

### 5.4 Ràng buộc tĩnh trong C++ (Hình dung trong đầu)

```
Base* ptr = new Derived();
ptr->nonVirtualFunction();   // Gọi Base::nonVirtualFunction()
                             // Vì ptr được khai báo là Base*
                             // Trình biên dịch giải quyết tại thời gian biên dịch
```

Khi một hàm **không phải ảo (non-virtual)**, trình biên dịch giải quyết toàn bộ lời gọi tại thời gian biên dịch bằng cách sử dụng **kiểu con trỏ/tham chiếu** (`Base*`), bất kể đối tượng mà con trỏ thực sự trỏ tới là gì. Một `Base*` gọi một hàm non-virtual **luôn luôn** gọi phiên bản của `Base`.

### 5.5 Ràng buộc động trong C++ (Hình dung trong đầu)

```
Base* ptr = new Derived();
ptr->virtualFunction();      // Gọi Derived::virtualFunction()
                             // Vì đối tượng thực tế là Derived
                             // Được giải quyết tại thời gian chạy qua vptr → vtable
```

Các điểm chính:

- Các phương thức **MẶC ĐỊNH LÀ NON-VIRTUAL** trong C++.
- Sử dụng từ khóa `virtual` để làm cho một hàm được ràng buộc động.
- **Quyết định thiết kế**: C++ được thiết kế để "gần như hiệu quả bằng C."
  - Ràng buộc động đắt hơn ràng buộc tĩnh (gián tiếp thêm một bước).
  - "Nếu bạn không dùng nó, bạn không trả tiền cho nó."
- Nếu một phương thức không thể bị ghi đè (non-virtual), trình biên dịch có thể:
  - Ràng buộc tĩnh (không có chi phí thời gian chạy).
  - Có thể nội tuyến (inline) nó để tối ưu thêm.
- Nhiều kỹ thuật tối ưu hóa trình biên dịch hơn có thể được áp dụng cho các phương thức non-virtual.

---

## 6. HÀM ẢO (VIRTUAL FUNCTIONS)

### 6.1 Định nghĩa

Một **hàm thành viên không tĩnh (non-static member function)** có từ khóa `virtual` đứng trước. Nó báo cho trình biên dịch tạo mã **chọn phiên bản phù hợp** của hàm này tại **thời gian chạy** dựa trên kiểu đối tượng thực tế.

```cpp
class Base {
public:
    virtual void draw();     // Hàm ảo (Virtual function)
    void print();            // Hàm không ảo (ràng buộc tĩnh)
};
```

### 6.2 Tầm quan trọng của tính đa hình (Tại sao hàm ảo quan trọng)

Sức mạnh thực sự của tính đa hình xuất hiện trong kịch bản này:

1. Bạn có một **tập hợp** các biến tham chiếu tổng quát (ví dụ: một mảng các con trỏ `Base*`).
2. Mỗi phần tử trỏ đến một đối tượng **thuộc kiểu khác nhau** (ví dụ: `Circle`, `Rectangle`, `Triangle` — tất cả đều dẫn xuất từ `Shape`).
3. Bạn duyệt qua tập hợp và gọi một **hàm đa hình** trên mỗi phần tử.
4. **Hệ thống thời gian chạy** tự động chọn thân hàm đúng cho kiểu của mỗi đối tượng.

```cpp
Shape* shapes[3];
shapes[0] = new Circle(5);
shapes[1] = new Rectangle(4, 6);
shapes[2] = new Triangle(3, 4, 5);

for (int i = 0; i < 3; i++) {
    shapes[i]->draw();   // Mỗi cái gọi phiên bản riêng của nó
}
```

**Hiểu biết quan trọng**: Khi một **lớp dẫn xuất mới** được thêm vào (ví dụ: `Cheetah` vào hệ phân cấp `Cat`), bạn **KHÔNG** cần thay đổi bất kỳ mã hiện có nào. Vòng lặp `doMeowing()` hiện có gọi `cat->makeSound()` trên một mảng các con trỏ `Cat*` hoạt động tự động với `Cheetah` — cơ chế vtable xử lý việc điều phối.

---

## 7. HỦY ẢO (VIRTUAL DESTRUCTORS)

### 7.1 Vấn đề

Gọi **sai hàm hủy (destructor)** có thể gây thảm họa, đặc biệt khi hàm hủy chứa câu lệnh `delete`:

```cpp
class Base {
    int* data;
public:
    Base()  { data = new int[100]; }
    ~Base() { delete[] data; }        // Hàm hủy KHÔNG phải ảo
};

class Derived : public Base {
    char* buffer;
public:
    Derived()  { buffer = new char[1024]; }
    ~Derived() { delete[] buffer; }   // Hàm này KHÔNG BAO GIỜ chạy nếu ~Base không phải virtual!
};

int main() {
    Base* ptr = new Derived();
    delete ptr;   // Chỉ gọi Base::~Base() — Derived::~Derived() bị bỏ qua!
                  // buffer bị rò rỉ (rò rỉ 1024 byte)
}
```

- Các hàm hủy **KHÔNG được kế thừa** theo nghĩa truyền thống (mỗi lớp có hàm hủy riêng).
- Nếu hàm hủy của lớp cơ sở không phải virtual, `delete ptr` sử dụng ràng buộc tĩnh và chỉ gọi **duy nhất** hàm hủy của lớp cơ sở.
- Hàm hủy của lớp dẫn xuất không bao giờ chạy → rò rỉ tài nguyên, thành viên treo (dangling members), hành vi không xác định.

### 7.2 Quy tắc

**LUÔN LUÔN làm cho hàm hủy của lớp cơ sở là virtual khi lớp được thiết kế để thao tác đa hình** (tức là bạn có ý định xóa các đối tượng dẫn xuất qua con trỏ lớp cơ sở).

```cpp
class Base {
public:
    virtual ~Base() { delete[] data; }  // Hàm hủy ảo — luôn làm điều này
};
```

Bây giờ khi `delete ptr` được gọi:
1. Ràng buộc động gọi `Derived::~Derived()` trước (dọn dẹp `buffer`).
2. Sau đó tự động gọi `Base::~Base()` (dọn dẹp `data`).

Cả hai tài nguyên đều được giải phóng đúng cách. Chi phí của hàm hủy ảo là không đáng kể so với rủi ro rò rỉ tài nguyên.

> Ví dụ file: `Lec9_ex1-VirtualDes.cpp` từ bài giảng.

---

## 8. LỚP TRỪU TƯỢNG (ABSTRACT CLASSES) (TRONG C++)

### 8.1 Giao diện (Interface) so với Lớp trừu tượng (Abstract Class)

- Trong C++, một **giao diện (interface)** mô tả hành vi hoặc khả năng của một lớp **mà không cam kết** với một cách triển khai cụ thể.
- Giao diện trong C++ được triển khai bằng cách sử dụng **lớp trừu tượng (abstract class)**.
- Không nên nhầm lẫn với **trừu tượng hóa dữ liệu (data abstraction)** (giữ chi tiết triển khai tách biệt khỏi dữ liệu liên quan — đó là một khái niệm khác).

### 8.2 Làm cho một lớp trở nên trừu tượng

Một lớp trở nên **trừu tượng** bằng cách khai báo **ít nhất một** trong các hàm của nó là **hàm ảo thuần túy (pure virtual function)**. Một hàm ảo thuần túy được xác định bằng cách đặt `= 0` trong khai báo của nó:

```cpp
class Box {
public:
    virtual double getVolume() = 0;   // Hàm ảo thuần túy
                                      // Làm Box trở thành lớp trừu tượng
private:
    double length, breadth, height;
};
```

### 8.3 Cú pháp hàm ảo thuần túy

```cpp
virtual returnType functionName(parameters) = 0;
```

- `= 0` là **bộ xác định thuần túy (pure specifier)** — nó làm cho hàm ảo trở nên "thuần túy."
- Một hàm ảo thuần túy KHÔNG có thân trong lớp cơ sở (mặc dù C++ cho phép cung cấp một thân mà các lớp dẫn xuất có thể gọi tường minh qua `Base::functionName()`).
- Bất kỳ lớp nào kế thừa từ một lớp trừu tượng **phải ghi đè tất cả các hàm ảo thuần túy** để trở thành một lớp cụ thể (concrete class).

### 8.4 Thuộc tính của các lớp trừu tượng

| Thuộc tính | Giải thích |
|------------|-----------|
| **Mục đích** | Cung cấp một **lớp cơ sở** phù hợp để các lớp khác có thể kế thừa; định nghĩa một giao diện chung. |
| **Vai trò khái niệm** | Thường đại diện cho các **khái niệm** mà các đối tượng không thể tồn tại một cách có ý nghĩa (ví dụ: `Shape` — bạn có thể vẽ một hình tròn hoặc hình chữ nhật, nhưng một "hình dạng" chung chung trông như thế nào?). |
| **Khởi tạo (Instantiation)** | **KHÔNG THỂ** được sử dụng để khởi tạo đối tượng. `Shape s;` hoặc `new Shape()` là **lỗi biên dịch**. |
| **Vai trò giao diện** | Chỉ phục vụ như một **giao diện** — một hợp đồng mà các lớp dẫn xuất phải thực hiện. |
| **Lớp cụ thể (Concrete classes)** | Các lớp CÓ THỂ được khởi tạo được gọi là **lớp cụ thể**. |
| **Con trỏ và tham chiếu** | Có thể khai báo các biến **con trỏ** và **tham chiếu** đến các lớp trừu tượng: `Shape* s;` là hợp lệ. Bạn chỉ không thể tạo một đối tượng `Shape` trần. |

> Ví dụ file: `Lec9_ex2-Shapes.cpp` — Lớp trừu tượng `Shape` với các lớp dẫn xuất `Circle` và `Polygon`.

### 8.5 Các lớp dẫn xuất trừu tượng

- Nếu một hàm ảo thuần túy **KHÔNG được định nghĩa** (ghi đè) trong một lớp dẫn xuất, thì lớp dẫn xuất đó **cũng là trừu tượng**.
- Nếu một lớp dẫn xuất KHÔNG cung cấp cách triển khai cho một hàm ảo thuần túy, nó kế thừa `= 0` và vẫn là trừu tượng.

```cpp
class Shape {
public:
    virtual void draw() = 0;
    virtual double area() = 0;
};

class Circle : public Shape {
public:
    void draw() { /* ... */ }       // Đã ghi đè
    // area() KHÔNG được ghi đè → Circle VẪN là trừu tượng!
};

class FilledCircle : public Circle {
public:
    double area() { return 3.14159 * r * r; }  // Bây giờ hoàn toàn cụ thể
};
```

- Đối với các hàm ảo **không thuần túy** (non-pure), nếu một lớp dẫn xuất KHÔNG cung cấp override, **cách triển khai của lớp cơ sở được sử dụng** (hành vi được kế thừa).
- Có thể khai báo **biến con trỏ** đến các lớp trừu tượng, cho phép các tập hợp đa hình.

---

## 9. TỪ KHÓA "this"

### 9.1 Định nghĩa

Trong một hàm thành viên, `this` là tên của một **con trỏ ngầm định (implicit pointer)** đến **đối tượng hiện tại** — đối tượng đã nhận thông điệp (lời gọi hàm) liên kết với hàm này.

```cpp
class Point {
    int x, y;
public:
    void setX(int x) {
        this->x = x;   // this->x = biến thành viên; x = tham số
    }
};
```

- `this` được tự động truyền như một tham số ẩn cho mọi hàm thành viên không tĩnh.
- Kiểu của nó là `ClassName* const` (một con trỏ hằng đến kiểu lớp).

### 9.2 Bản chất đa hình

`this` thực sự là một **từ đa hình** — nó có thể chỉ **bất kỳ đối tượng nào** trong ngôn ngữ C++:

```cpp
class Animal {
public:
    virtual void identify() {
        cout << "I am an Animal at " << this << endl;
    }
};

class Dog : public Animal {
public:
    void identify() {
        cout << "I am a Dog at " << this << endl;
    }
};

int main() {
    Animal* a = new Dog();
    a->identify();  // Bên trong identify(), "this" trỏ đến đối tượng Dog
                    // Mặc dù kiểu con trỏ là Animal*
}
```

- Khi một hàm ảo được gọi qua một con trỏ cơ sở, `this` bên trong hàm đó trỏ đến **đối tượng dẫn xuất thực tế**, không phải kiểu cơ sở.
- Điều này rất cần thiết cho việc điều phối hàm ảo: `this` cho phép hàm truy cập vào dữ liệu và vtable của đối tượng đúng.

---

## 10. BẢNG ẢO (VIRTUAL TABLES — VTABLES)

### 10.1 Cơ chế

C++ (và Java) sử dụng cơ chế **bảng ảo (virtual table — vtable)** để triển khai ràng buộc động:

- Một lớp có **các hàm thành viên ảo** có một **bảng ảo** ẩn — một mảng tĩnh chứa **địa chỉ** của các hàm ảo của nó.
- Một đối tượng của lớp như vậy có một con trỏ ẩn gọi là **vptr** (virtual pointer) trỏ đến bảng ảo của lớp của nó.
- vptr thường được lưu trữ như thành viên ẩn đầu tiên của đối tượng.

```
Object of Derived:               Class Derived's vtable:
┌──────────────┐                ┌──────────────────────┐
│    vptr      │──────────────> │ &Derived::action()   │
│  data members│                │ &Derived::draw()     │
│  ...         │                │ &Derived::~Derived() │
└──────────────┘                └──────────────────────┘
```

### 10.2 Ràng buộc động hoạt động như thế nào (Từng bước)

Khi `ptr->virtualFunction()` được gọi:

1. **Theo vptr** — trình biên dịch tạo mã để truy cập vptr của đối tượng và đến bảng ảo của **lớp thực tế** của đối tượng.
2. **Tra cứu vtable** — tại **thời gian chạy**, tra cứu mục nhập trong bảng ảo để tìm địa chỉ của hàm phù hợp.
3. **Gọi hàm** — nhảy đến địa chỉ được tìm thấy trong vtable.

```
ptr -> [object]
      ├── vptr ──────> [vtable]
      │                ├── entry[0]: &Derived::func1()
      │                ├── entry[1]: &Derived::func2()
      │                └── entry[2]: &Derived::func3()
      └── data members
```

- Mỗi hàm ảo chiếm một vị trí cố định (offset) trong vtable.
- Đối với một hệ phân cấp lớp nhất định, bố cục vtable là nhất quán — trình biên dịch biết vị trí cho mỗi hàm ảo.
- Ghi đè một hàm ảo chỉ đơn giản là thay đổi địa chỉ được lưu trữ tại ô vtable đó cho lớp dẫn xuất.

---

## 11. TÓM TẮT (từ bài giảng)

### Bốn loại đa hình

| Loại | Thời điểm ràng buộc | Cơ chế C++ |
|------|--------------------|------------|
| Thời gian chạy / Bao hàm / Ghi đè | Thời gian chạy | Hàm `virtual` + kế thừa |
| Tham số (Parametric) | Thời gian biên dịch | Template |
| Tùy biến (Ad-hoc) — Nạp chồng | Thời gian biên dịch | Nhiều hàm, cùng tên, chữ ký khác nhau |
| Ép kiểu (Coercion / Casting) | Thời gian biên dịch | Chuyển đổi kiểu ngầm định bởi trình biên dịch |

### Đa hình bao hàm (Ghi đè) — Những điểm chính

- **Tại sao nó quan trọng?** → Thêm các lớp dẫn xuất mới **mà không cần thay đổi mã hiện có**. Hệ thống có thể mở rộng.
- **Đừng nhầm lẫn** ghi đè với nạp chồng:
  - Ghi đè = cùng tên VÀ tham số, điều phối thời gian chạy, cần `virtual` + kế thừa.
  - Nạp chồng = cùng tên, tham số KHÁC NHAU, giải quyết tại thời gian biên dịch.
- Tính đa hình **yêu cầu ràng buộc động (dynamic binding)**.
- C++ mặc định là **ràng buộc tĩnh (static binding)** vì hiệu quả; sử dụng từ khóa `virtual` để cho phép ràng buộc động.
- "Nếu bạn không dùng nó, bạn không trả tiền cho nó" — triết lý thiết kế C++.

---

## 12. CÁC MẪU CÚ PHÁP CẦN GHI NHỚ

### Khai báo hàm ảo

```cpp
class Base {
public:
    virtual void action();              // Virtual — có thể ghi đè; ràng buộc động
    virtual void mustImplement() = 0;   // Thuần túy ảo — làm Base trở thành trừu tượng
    virtual ~Base();                    // Hàm hủy ảo — LUÔN làm điều này cho lớp cơ sở
    void nonVirtualFunc();              // Non-virtual — ràng buộc tĩnh; không thể ghi đè đúng cách
};
```

### Ghi đè trong lớp dẫn xuất

```cpp
class Derived : public Base {
public:
    void action() override;            // Ghi đè (virtual là tùy chọn trong lớp dẫn xuất; từ khóa override C++11)
    void mustImplement() override;     // PHẢI triển khai tất cả pure virtual để trở thành cụ thể
    ~Derived();                        // Hàm hủy — tự động virtual nếu hàm hủy của base là virtual
};
```

### Mẫu điều phối động (Tập hợp đa hình)

```cpp
// Lớp cơ sở trừu tượng
class Animal {
public:
    virtual void speak() = 0;           // Thuần túy ảo → trừu tượng
    virtual ~Animal() { }              // Hàm hủy ảo
};

// Các lớp dẫn xuất cụ thể
class Dog : public Animal {
public:
    void speak() { cout << "Woof!" << endl; }
};

class Cat : public Animal {
public:
    void speak() { cout << "Meow!" << endl; }
};

// Sử dụng — tập hợp đa hình
int main() {
    Animal* animals[] = { new Dog(), new Cat() };
    for (Animal* a : animals) {
        a->speak();                    // Điều phối động qua vtable
    }
    for (Animal* a : animals) {
        delete a;                      // Hàm hủy đúng được gọi (virtual)
    }
}
```

### Mẫu lớp trừu tượng

```cpp
class AbstractShape {
public:
    virtual double area() = 0;         // Ít nhất một pure virtual
    virtual void draw() = 0;
    virtual ~AbstractShape() { }       // Hàm hủy ảo
    double getLabel() { return label; } // Non-virtual: triển khai dùng chung
private:
    double label;
};
// AbstractShape s;                    // LỖI: không thể khởi tạo lớp trừu tượng
// AbstractShape* p;                   // OK: con trỏ đến lớp trừu tượng
```

### Mẫu hàm hủy ảo

```cpp
class BaseWithResources {
    int* data;
public:
    BaseWithResources() : data(new int[100]) { }
    virtual ~BaseWithResources() { delete[] data; }  // VIRTUAL — quan trọng!
};
```

---

## 13. BẪY THI CỬ (EXAM TRAPS)

**1. Các phương thức non-virtual sử dụng ràng buộc TĨNH.** Nếu `Base* p = new Derived();` và bạn gọi `p->nonVirtualFunc()`, nó gọi phiên bản của `Base` — ngay cả khi `Derived` có một hàm cùng tên. **Kiểu con trỏ** (`Base*`), không phải kiểu đối tượng, quyết định hàm nào được gọi.

> [!success]- Hiển thị đáp án
> Ràng buộc tĩnh có nghĩa là trình biên dịch giải quyết lời gọi tại thời gian biên dịch bằng kiểu được khai báo của con trỏ. Vì `p` được khai báo là `Base*`, trình biên dịch phát ra lời gọi đến `Base::nonVirtualFunc()`. Phiên bản Derived, dù có tồn tại, cũng không bao giờ được gọi qua một con trỏ cơ sở.

---

**2. Quên `virtual` trên hàm hủy của lớp cơ sở.** `Base* p = new Derived; delete p;` — nếu `~Base()` không phải virtual, chỉ hàm hủy của `Base` chạy. Hàm hủy của Derived không bao giờ kích hoạt, gây rò rỉ tài nguyên và các thành viên treo.

> [!success]- Hiển thị đáp án
> Không có `virtual`, `delete p` sử dụng ràng buộc tĩnh → chỉ gọi `Base::~Base()`. Các tài nguyên riêng của Derived (được cấp phát động trong Derived) không bao giờ được giải phóng. Sửa: `virtual ~Base() { }` trong lớp cơ sở. Bây giờ ràng buộc động gọi `Derived::~Derived()` trước, sau đó tự động dây chuyền đến `Base::~Base()`.

---

**3. Hàm ảo thuần túy được khai báo nhưng không được triển khai trong lớp dẫn xuất.** Lớp dẫn xuất vẫn là trừu tượng và không thể được khởi tạo. Cố gắng `new Derived` tạo ra lỗi biên dịch.

> [!success]- Hiển thị đáp án
> Một lớp kế thừa một hàm ảo thuần túy cũng kế thừa luôn `= 0`. Cho đến khi TẤT CẢ các pure virtual được ghi đè, lớp vẫn là trừu tượng. Việc khởi tạo cụ thể yêu cầu tất cả các pure virtual của lớp cơ sở phải được triển khai.

---

**4. Các lớp trừu tượng CÓ THỂ có con trỏ và tham chiếu.** `Base* p;` hoàn toàn hợp lệ. `Base& r = someDerived;` hoàn toàn hợp lệ. Chỉ việc khởi tạo trực tiếp bị cấm: `Base b;` hoặc `new Base()` là lỗi.

> [!success]- Hiển thị đáp án
> Các lớp trừu tượng định nghĩa một giao diện nhưng thiếu triển khai đầy đủ. Con trỏ và tham chiếu không tạo ra đối tượng — chúng chỉ tham chiếu đến chúng. Bạn có thể trỏ đến một đối tượng dẫn xuất cụ thể qua một con trỏ cơ sở trừu tượng. Đây chính xác là cách các tập hợp đa hình hoạt động.

---

**5. Gọi một hàm ảo trong constructor/destructor KHÔNG thực hiện điều phối động.** Bên trong `Base::Base()`, gọi `virtualFunc()` sẽ gọi phiên bản của `Base` ngay cả khi đối tượng đang được xây dựng là `Derived` — phần dẫn xuất chưa được xây dựng xong.

> [!success]- Hiển thị đáp án
> Trong quá trình xây dựng, đối tượng được xây dựng từ cơ sở đến dẫn xuất. Khi constructor của `Base` chạy, vptr vẫn trỏ đến vtable của `Base` (phần dẫn xuất chưa tồn tại). Tương tự, trong quá trình hủy, một khi `~Derived()` kết thúc, vptr quay trở lại vtable của `Base` trước khi `~Base()` chạy. Không bao giờ gọi các hàm ảo trong constructor/destructor với kỳ vọng hành vi dẫn xuất.

---

**6. Ghi đè hàm ảo phải khớp CHÍNH XÁC chữ ký.** Kiểu trả về khác (trừ khi đồng biến — covariant), const khác, hoặc kiểu tham số khác có nghĩa là bạn đã tạo một **hàm mới** (ẩn giấu/nạp chồng), không phải ghi đè base virtual.

> [!success]- Hiển thị đáp án
> Trình biên dịch khớp các override bằng chữ ký chính xác. Nếu base có `virtual void foo(int)` và derived định nghĩa `void foo(double)`, đó là một hàm hoàn toàn khác — `foo(int)` của base vẫn được kế thừa và có thể gọi được. Sử dụng từ khóa `override` trong C++11+: `void foo(int) override` — trình biên dịch sẽ báo lỗi nếu không có base virtual khớp.

---

**7. `this` là một con trỏ ngầm định đến đối tượng HIỆN TẠI.** Bên trong một hàm thành viên, `*this` là đối tượng đã nhận lời gọi. Trong một hàm ảo được gọi qua con trỏ cơ sở, `this` trỏ đến **đối tượng dẫn xuất thực tế**.

> [!success]- Hiển thị đáp án
> `this` luôn là đối tượng thực tế, bất kể kiểu con trỏ/tham chiếu được sử dụng để gọi hàm. Nếu bạn có `Base* p = new Derived(); p->virtualFunc();`, thì bên trong `virtualFunc()`, `this` trỏ đến đối tượng `Derived`. Đây là cách các hàm ảo truy cập vào dữ liệu thành viên đúng.

---

**8. Ép kiểu (Coercion) KHÔNG giống như ghi đè (Overriding).** `int add(int a, int b)` và `float add(float a, float b)` với lời gọi `add(1, 1.0)` — trình biên dịch chuyển đổi (ép kiểu) `1.0` double thành `int` để khớp chữ ký. Đây là phép thuật thời gian biên dịch, không phải đa hình thời gian chạy.

> [!success]- Hiển thị đáp án
> Ép kiểu xảy ra tại thời gian biên dịch: trình biên dịch ngầm chuyển đổi kiểu đối số để khớp với các chữ ký hàm có sẵn. Không có bảng ảo, không có điều phối thời gian chạy, không yêu cầu kế thừa. Đó là một chuyển đổi kiểu tiện lợi, không phải lựa chọn hành vi động dựa trên kiểu đối tượng.

---

**9. Nhầm lẫn giữa Nạp chồng (Overloading) và Ghi đè (Overriding).** Nếu bạn có `virtual void draw(int)` trong base và viết `void draw(double)` trong derived, bạn đã NẠP CHỒNG, không phải ghi đè. `draw(int)` của base vẫn còn nguyên và có thể gọi được, trong khi một `draw(double)` mới tồn tại trong phạm vi derived.

> [!success]- Hiển thị đáp án
> Kiểu tham số khác nhau = hàm khác nhau. Lớp dẫn xuất bây giờ có HAI hàm `draw`: `draw(int)` được kế thừa và `draw(double)` mới. Qua con trỏ cơ sở, chỉ `draw(int)` có thể truy cập được (vì base không biết về `draw(double)`). Luôn khớp chính xác chữ ký khi ghi đè.

---

**10. Vấn đề cắt xén (Slicing) khi truyền theo giá trị (pass by value).** Truyền một đối tượng dẫn xuất cho một hàm mong đợi một đối tượng cơ sở theo GIÁ TRỊ sẽ cắt bỏ phần dẫn xuất. Hàm chỉ nhận được phần cơ sở — việc điều phối ảo vẫn hoạt động (sử dụng vtable của base), nhưng dữ liệu dẫn xuất bị mất.

> [!success]- Hiển thị đáp án
> Truyền theo giá trị tạo một bản sao. Vì tham số có kiểu `Shape` (không phải `Shape&` hoặc `Shape*`), chỉ đủ bộ nhớ cho một `Shape` được cấp phát. Các thành viên dữ liệu riêng của dẫn xuất bị cắt bỏ. Luôn truyền các đối tượng đa hình bằng con trỏ hoặc tham chiếu để bảo toàn toàn bộ đối tượng.

```cpp
void drawShape(Shape s) { s.draw(); }   // CẮT XÉN — chỉ phần Shape được sao chép
void drawShape(Shape& s) { s.draw(); }  // ĐÚNG — toàn bộ đối tượng được bảo toàn
```

---

**11. Một lớp trở nên trừu tượng nếu nó kế thừa một hàm ảo thuần túy và không ghi đè nó.** Ngay cả khi lớp ghi đè HẦU HẾT các pure virtual, một pure virtual còn lại vẫn giữ lớp ở trạng thái trừu tượng.

> [!success]- Hiển thị đáp án
> Tính trừu tượng "lây nhiễm" xuống hệ phân cấp. Một lớp dẫn xuất phải ghi đè TẤT CẢ các hàm ảo thuần túy được kế thừa để trở thành cụ thể. Nếu `AbstractBase` có 5 pure virtual, một `Derived` ghi đè 4 trong số đó vẫn là trừu tượng và không thể được khởi tạo.

---

**12. Bạn CÓ THỂ cung cấp một thân (body) cho một hàm ảo thuần túy.** `virtual void draw() = 0 { /* body */ }` là hợp lệ trong C++. Các lớp dẫn xuất có thể gọi nó tường minh qua `Base::draw()`. Nhưng lớp vẫn là trừu tượng vì có `= 0`.

> [!success]- Hiển thị đáp án
> Một hàm ảo thuần túy CÓ THỂ có một cách triển khai. Điều này hữu ích khi bạn muốn buộc các lớp dẫn xuất phải ghi đè nhưng cũng cung cấp một cách triển khai mặc định mà chúng có thể gọi. Lớp vẫn là trừu tượng mặc dù có thân cho pure virtual — `= 0` là thứ làm cho nó trừu tượng, không phải việc thiếu thân.

---

**13. Các hàm ảo hoạt động qua THAM CHIẾU (references), không chỉ con trỏ.** `Base& ref = someDerived; ref.virtualFunc();` thực hiện điều phối động giống hệt như qua con trỏ.

> [!success]- Hiển thị đáp án
> Ràng buộc động áp dụng cho cả con trỏ và tham chiếu. Cơ chế vptr/vtable là như nhau — trình biên dịch tạo ra tra cứu vtable cho bất kỳ truy cập nào qua tham chiếu lớp cơ sở. Đây là lý do tại sao truyền theo tham chiếu tránh được cắt xén và bảo toàn tính đa hình.

---

**14. Đa kế thừa (Multiple inheritance) và các hàm ảo.** Nếu một lớp kế thừa từ hai lớp cơ sở mà cả hai đều có hàm ảo, lớp dẫn xuất có thể có nhiều vtable (một cho mỗi cơ sở). Hãy biết rằng sự phức tạp này tồn tại nhưng tập trung vào đơn kế thừa cho các kỳ thi.

> [!success]- Hiển thị đáp án
> Với đa kế thừa, đối tượng dẫn xuất có thể chứa nhiều vptr — một cho mỗi đường dẫn lớp cơ sở. Trình biên dịch tạo ra các điều chỉnh phù hợp. Đây là lý do tại sao mô hình đối tượng của C++ phức tạp hơn các ngôn ngữ đơn kế thừa. Hãy biết rằng nhiều vtable tồn tại trong những trường hợp như vậy.

---

**15. Các hàm thành viên tĩnh (Static member functions) KHÔNG THỂ là virtual.** Một hàm tĩnh thuộc về lớp, không thuộc về bất kỳ đối tượng nào. Vì không có con trỏ `this` và không có đối tượng, không có vptr để theo — việc điều phối ảo là không thể.

> [!success]- Hiển thị đáp án
> Điều phối ảo yêu cầu một vptr, được lưu trữ trên mỗi đối tượng. Các hàm tĩnh không có ngữ cảnh đối tượng — chúng thuộc về chính lớp đó. Do đó chúng không thể là virtual. Ngoài ra, các constructor cũng không thể là virtual (vptr chưa được thiết lập cho đến khi constructor chạy).

---

**16. Từ khóa `virtual` trong các lớp dẫn xuất là TÙY CHỌN nhưng từ khóa `override` (C++11) được khuyến nghị.** Nếu bạn bỏ qua `virtual` trong lớp dẫn xuất, hàm vẫn là virtual nếu base đã khai báo nó như vậy. Tuy nhiên, `override` bắt được các lỗi không khớp chữ ký.

> [!success]- Hiển thị đáp án
> Một khi đã là virtual, luôn là virtual xuống suốt hệ phân cấp. Viết `virtual void draw() override` trong lớp dẫn xuất là dư thừa nhưng tường minh. Chỉ sử dụng `void draw() override` là cách viết chuẩn của C++11 — trình biên dịch xác nhận có một base virtual khớp và báo lỗi nếu không có.

---

**17. Chi phí vtable: một vptr trên mỗi đối tượng + một vtable trên mỗi lớp có hàm ảo.** Chi phí bộ nhớ nhỏ (một con trỏ trên mỗi đối tượng, một vtable trên mỗi lớp), nhưng sự gián tiếp thêm một chi phí thời gian chạy nhỏ cho mỗi lần gọi ảo.

> [!success]- Hiển thị đáp án
> Mỗi đối tượng của một lớp có hàm ảo có một vptr (thường là 4 hoặc 8 byte). Mỗi lớp có hàm ảo có một vtable (được chia sẻ bởi tất cả các đối tượng của lớp đó). Chi phí thời gian chạy là: theo vptr → chỉ mục vào vtable → gọi hàm. Đây là một bước gián tiếp thêm so với lời gọi trực tiếp. Trong thực tế, chi phí là không đáng kể đối với hầu hết các ứng dụng.

---

## 14. BÀI TẬP VIẾT TAY (HAND-CODING DRILLS)

### Bài tập 1: Ràng buộc tĩnh vs Ràng buộc động

```cpp
#include <iostream>
using namespace std;

class Parent {
public:
    void hello() { cout << "Parent hello "; }
    virtual void bye() { cout << "Parent bye "; }
};

class Child : public Parent {
public:
    void hello() { cout << "Child hello "; }
    void bye() { cout << "Child bye "; }
};

int main() {
    Parent* p = new Child();
    p->hello();  // dòng A
    p->bye();    // dòng B
    Child c;
    c.hello();   // dòng C
    c.bye();     // dòng D
    delete p;
}
```

Đầu ra CHÍNH XÁC là gì? Giải thích từng dòng.

> [!success]- Hiển thị đáp án
> Đầu ra: `Parent hello Child bye Child hello Child bye`
>
> - **Dòng A**: `hello()` KHÔNG phải ảo. Ràng buộc tĩnh sử dụng kiểu con trỏ `Parent*` → gọi `Parent::hello`.
> - **Dòng B**: `bye()` là ảo. Ràng buộc động theo vptr đến vtable của `Child` → gọi `Child::bye`.
> - **Dòng C**: `c` là một đối tượng `Child` trên stack. `hello()` phân giải thành `Child::hello` (ẩn phiên bản cha qua cơ chế ẩn tên — name hiding).
> - **Dòng D**: `bye()` là ảo, và `c` là `Child` → điều phối động gọi `Child::bye`.

---

### Bài tập 2: Thiếu hàm hủy ảo

```cpp
class FileHandler {
    char* buffer;
public:
    FileHandler() { buffer = new char[1024]; }
    ~FileHandler() { delete[] buffer; }
};

class EncryptedFileHandler : public FileHandler {
    char* key;
public:
    EncryptedFileHandler() { key = new char[32]; }
    ~EncryptedFileHandler() { delete[] key; }
};

int main() {
    FileHandler* f = new EncryptedFileHandler();
    delete f;
}
```

Lỗi là gì? Thứ gì bị rò rỉ chính xác? Sửa nó với thay đổi tối thiểu.

> [!success]- Hiển thị đáp án
> `~FileHandler()` KHÔNG phải ảo. Khi `delete f` được gọi qua `FileHandler*`, ràng buộc tĩnh chỉ gọi `~FileHandler()`. Hàm hủy của `EncryptedFileHandler` không bao giờ chạy → `key` (32 byte) bị rò rỉ. `buffer` ĐƯỢC xóa đúng cách (qua hàm hủy của `FileHandler`).
>
> **Sửa**: `virtual ~FileHandler() { delete[] buffer; }`
>
> Bây giờ ràng buộc động gọi `~EncryptedFileHandler()` trước (xóa `key`), sau đó tự động gọi `~FileHandler()` (xóa `buffer`). Cả hai tài nguyên đều được giải phóng.

---

### Bài tập 3: Hệ thống thanh toán trừu tượng

Thiết kế một hệ thống thanh toán nơi `PaymentProcessor` là một lớp cơ sở trừu tượng với:

- Một pure virtual `bool charge(double amount)` trả về true nếu thành công
- Một virtual `void refund(double amount)` in `"Refunding [amount] via generic processor"`
- Một concrete `double getFee(double amount)` trả về `amount * 0.03`

Sau đó viết `StripeProcessor`:

- Ghi đè `charge` để in `"Stripe: charging [amount]"` và trả về true
- KHÔNG ghi đè `refund`
- Không thể được khởi tạo nếu nó không ghi đè một hàm nhất định

Cuối cùng viết `PayPalProcessor` ghi đè cả `charge` và `refund`, và hoàn toàn cụ thể.

> [!success]- Hiển thị đáp án
> ```cpp
> class PaymentProcessor {
> public:
>     virtual bool charge(double amount) = 0;  // pure virtual → trừu tượng
>     virtual void refund(double amount) {
>         cout << "Refunding " << amount << " via generic processor" << endl;
>     }
>     double getFee(double amount) {           // non-virtual: chia sẻ cho tất cả
>         return amount * 0.03;
>     }
>     virtual ~PaymentProcessor() { }          // hàm hủy ảo
> };
>
> class StripeProcessor : public PaymentProcessor {
> public:
>     bool charge(double amount) {
>         cout << "Stripe: charging " << amount << endl;
>         return true;
>     }
>     // refund() KHÔNG được ghi đè — sử dụng phiên bản base (thông báo chung)
> };
>
> class PayPalProcessor : public PaymentProcessor {
> public:
>     bool charge(double amount) {
>         cout << "PayPal: charging " << amount << endl;
>         return true;
>     }
>     void refund(double amount) {
>         cout << "PayPal: refunding " << amount << endl;
>     }
> };
> ```

---

### Bài tập 4: Ép kiểu (Coercion) vs Ghi đè (Overriding)

```cpp
class Calculator {
public:
    int add(int a, int b) {
        cout << "Calculator::add(int,int) ";
        return a + b;
    }
    float add(float a, float b) {
        cout << "Calculator::add(float,float) ";
        return a + b;
    }
};

class Scientific : public Calculator {
public:
    int add(int a, int b) {
        cout << "Scientific::add(int,int) ";
        return a + b;
    }
};

int main() {
    Calculator* c1 = new Calculator();
    Calculator* c2 = new Scientific();

    c1->add(1, 2);        // dòng A
    c1->add(1.0f, 2.0f);  // dòng B
    c1->add(1, 2.0f);     // dòng C

    c2->add(3, 4);        // dòng D
    c2->add(3.0f, 4.0f);  // dòng E

    delete c1; delete c2;
}
```

Đầu ra CHÍNH XÁC là gì? Giải thích mỗi dòng sử dụng ép kiểu, nạp chồng, ghi đè hay ràng buộc tĩnh.

> [!success]- Hiển thị đáp án
> ```
> Calculator::add(int,int) Calculator::add(float,float) Calculator::add(int,int) Calculator::add(int,int) Calculator::add(float,float)
> ```
>
> - **Dòng A**: `add(int, int)` khớp chính xác → phân giải nạp chồng chọn `Calculator::add(int,int)`.
> - **Dòng B**: `add(float, float)` khớp chính xác → phân giải nạp chồng chọn `Calculator::add(float,float)`.
> - **Dòng C**: `add(int, double)` — không có khớp chính xác. `2.0f` sẽ là float nhưng `2.0` là double. Phiên bản `int` là khớp tốt nhất sau ép kiểu (double→int) → gọi `Calculator::add(int,int)`. Đây là **ép kiểu + nạp chồng**.
> - **Dòng D**: `c2` là `Calculator*` trỏ đến `Scientific`. `add()` KHÔNG phải ảo (không có từ khóa `virtual` trong base). Ràng buộc tĩnh → gọi `Calculator::add(int,int)`. Việc ghi đè của `Scientific` **KHÔNG ĐƯỢC GỌI** vì không có điều phối động!
> - **Dòng E**: Lý do tương tự — non-virtual, ràng buộc tĩnh → `Calculator::add(float,float)`.
>
> **Bài học chính**: Không có `virtual`, ngay cả khi lớp dẫn xuất ghi đè một hàm, các lời gọi qua con trỏ cơ sở sử dụng ràng buộc tĩnh và gọi phiên bản cơ sở. Ép kiểu là một chuyển đổi đối số thời gian biên dịch, tách biệt với ghi đè.

---

### Bài tập 5: Truy vết khái niệm Bảng ảo

Cho hệ phân cấp lớp sau:

```cpp
class A {
public:
    virtual void f1() { cout << "A::f1 "; }
    virtual void f2() { cout << "A::f2 "; }
    void f3() { cout << "A::f3 "; }
};

class B : public A {
public:
    void f1() { cout << "B::f1 "; }
    virtual void f4() { cout << "B::f4 "; }
};

class C : public B {
public:
    void f2() { cout << "C::f2 "; }
    void f4() { cout << "C::f4 "; }
};
```

Trả lời các câu hỏi:
1. Mỗi lớp có bao nhiêu hàm ảo trong vtable của nó?
2. Mỗi lời gọi xuất ra gì?

```cpp
A* p1 = new A();   p1->f1(); p1->f2(); p1->f3();
A* p2 = new B();   p2->f1(); p2->f2(); p2->f3();
A* p3 = new C();   p3->f1(); p3->f2(); p3->f3();
```

> [!success]- Hiển thị đáp án
> **Vtable**:
> - Vtable của `A`: 2 mục → `f1`, `f2`
> - Vtable của `B`: 3 mục → `f1` (đã ghi đè), `f2` (kế thừa từ A), `f4` (virtual mới trong B)
> - Vtable của `C`: 3 mục → `f1` (kế thừa từ B's override), `f2` (đã ghi đè), `f4` (đã ghi đè)
>
> **Đầu ra**: `A::f1 A::f2 A::f3 B::f1 A::f2 A::f3 B::f1 C::f2 A::f3`
>
> - `p1->f1()`: Đối tượng A, virtual → `A::f1`
> - `p1->f2()`: Đối tượng A, virtual → `A::f2`
> - `p1->f3()`: NON-virtual → ràng buộc tĩnh → `A::f3`
> - `p2->f1()`: Đối tượng B, virtual → tra vtable → `B::f1`
> - `p2->f2()`: Đối tượng B, virtual → mục vtable của B vẫn trỏ đến `A::f2` (B không ghi đè nó) → `A::f2`
> - `p2->f3()`: NON-virtual → ràng buộc tĩnh → `A::f3`
> - `p3->f1()`: Đối tượng C, virtual → tra vtable (kế thừa từ B) → `B::f1`
> - `p3->f2()`: Đối tượng C, virtual → vtable của C có override của C → `C::f2`
> - `p3->f3()`: NON-virtual → ràng buộc tĩnh → `A::f3`

---

### Bài tập 6: Các lớp dẫn xuất trừu tượng

```cpp
class Shape {
public:
    virtual void draw() = 0;
    virtual double area() = 0;
    virtual void rotate(double angle) { cout << "Rotating by " << angle; }
    virtual ~Shape() { }
};

class Circle : public Shape {
    double r;
public:
    Circle(double radius) : r(radius) { }
    void draw() { cout << "Drawing Circle"; }
    double area() { return 3.14159 * r * r; }
    // rotate() KHÔNG được ghi đè — kế thừa triển khai base
};

class Square : public Shape {
    double side;
public:
    Square(double s) : side(s) { }
    void draw() { cout << "Drawing Square"; }
    // area() KHÔNG được ghi đè
    // rotate() KHÔNG được ghi đè
};

class FilledSquare : public Square {
    string color;
public:
    FilledSquare(double s, string c) : Square(s), color(c) { }
    double area() { /* ... */ }
};

int main() {
    Shape s;              // dòng 1 — LỖI hay OK?
    Circle c(5.0);        // dòng 2 — LỖI hay OK?
    Square sq(4.0);       // dòng 3 — LỖI hay OK?
    FilledSquare fs(3.0, "red"); // dòng 4 — LỖI hay OK?
    Shape* shapes[2];
    shapes[0] = new Circle(2.0);
    shapes[1] = new FilledSquare(5.0, "blue");
    for (int i = 0; i < 2; i++) {
        shapes[i]->rotate(90);   // dòng 5 — rotate nào chạy?
    }
}
```

Những dòng nào biên dịch được? Những dòng nào là lỗi? Giải thích. Đối với dòng 5, `rotate()` nào chạy cho mỗi hình?

> [!success]- Hiển thị đáp án
> - **Dòng 1 — LỖI**: `Shape` là trừu tượng (`draw` và `area` là pure virtual) — không thể khởi tạo.
> - **Dòng 2 — OK**: `Circle` ghi đè cả hai pure virtual → hoàn toàn cụ thể.
> - **Dòng 3 — LỖI**: `Square` kế thừa `area() = 0` từ `Shape` mà không ghi đè nó → `Square` vẫn là trừu tượng → không thể khởi tạo.
> - **Dòng 4 — OK**: `FilledSquare` ghi đè `area()` — giải quyết pure virtual còn lại duy nhất từ `Square`/`Shape`. Nó cũng kế thừa `draw()` từ `Square`. Bây giờ là cụ thể.
> - **Dòng 5**: Cả hai đều gọi `Shape::rotate(90)` — triển khai của base. Cả `Circle` và `FilledSquare` đều không ghi đè `rotate`. Vì `rotate` là virtual nhưng KHÔNG được ghi đè, mục vtable trỏ đến `Shape::rotate` cho cả hai. Đầu ra: `Rotating by 90Rotating by 90`.

---

### Bài tập 7: Truy vết toàn bộ Ràng buộc tĩnh vs Ràng buộc động

```cpp
#include <iostream>
using namespace std;

class Vehicle {
public:
    void start() { cout << "Vehicle::start "; }
    virtual void drive() { cout << "Vehicle::drive "; start(); }
    virtual void stop() { cout << "Vehicle::stop "; }
    virtual ~Vehicle() { cout << "~Vehicle "; }
};

class Car : public Vehicle {
public:
    void start() { cout << "Car::start "; }
    void drive() { cout << "Car::drive "; start(); }
    void stop() { cout << "Car::stop "; }
    ~Car() { cout << "~Car "; }
};

class SportsCar : public Car {
public:
    void drive() { cout << "SportsCar::drive "; start(); }
    ~SportsCar() { cout << "~SportsCar "; }
};

int main() {
    Vehicle* v1 = new Car();
    v1->start();           // dòng A
    v1->drive();           // dòng B
    Vehicle* v2 = new SportsCar();
    v2->drive();           // dòng C
    v2->stop();            // dòng D
    delete v1;             // dòng E
    delete v2;             // dòng F
}
```

Viết đầu ra CHÍNH XÁC, phân biệt giữa ràng buộc tĩnh và ràng buộc động tại mỗi dòng.

> [!success]- Hiển thị đáp án
> ```
> Vehicle::start Car::drive Car::start SportsCar::drive Car::start Car::stop ~Car ~Vehicle ~SportsCar ~Car ~Vehicle
> ```
>
> - **Dòng A**: `start()` KHÔNG phải ảo → ràng buộc tĩnh sử dụng `Vehicle*` → `Vehicle::start`
> - **Dòng B**: `drive()` là ảo → ràng buộc động. Đối tượng là `Car` → `Car::drive` → in `Car::drive `, sau đó gọi `start()`. `start()` KHÔNG phải ảo → ràng buộc tĩnh sử dụng `this` (là `Car*` bên trong `Car::drive`) → `Car::start`
> - **Dòng C**: `drive()` là ảo → ràng buộc động. Đối tượng là `SportsCar` → `SportsCar::drive` → in `SportsCar::drive `, sau đó gọi `start()`. `start()` KHÔNG phải ảo → ràng buộc tĩnh sử dụng `this` (là `SportsCar*` nhưng `start` không được định nghĩa trong `SportsCar`) → kế thừa `Car::start` (giải quyết tên đi lên hệ phân cấp) → `Car::start`
> - **Dòng D**: `stop()` là ảo → ràng buộc động. `SportsCar` kế thừa `Car::stop` → `Car::stop`
> - **Dòng E**: `~Vehicle()` là ảo → ràng buộc động gọi `~Car()` trước → in `~Car `, sau đó dây chuyền đến `~Vehicle()` → in `~Vehicle `
> - **Dòng F**: `~Vehicle()` là ảo → ràng buộc động gọi `~SportsCar()` trước → in `~SportsCar `, sau đó `~Car()` → in `~Car `, sau đó `~Vehicle()` → in `~Vehicle `

---

> [!NOTE]
> Hướng dẫn học tập này bao gồm tất cả nội dung bài giảng cho Lec9: Tính đa hình (Polymorphism). Hãy ôn tập bốn loại đa hình, hiểu sự khác biệt giữa ràng buộc tĩnh và ràng buộc động, ghi nhớ cú pháp cho hàm ảo / hàm ảo thuần túy / hàm hủy ảo / lớp trừu tượng, và thực hành các bài tập cho đến khi bạn có thể truy vết bất kỳ đoạn mã nào liên quan đến con trỏ lớp cơ sở và lời gọi hàm ảo mà không do dự.
