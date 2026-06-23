# Lec11: Mẫu và Bạn (Templates and Friends) — Hướng dẫn Ôn tập

---

## 1. THẺ KHÁI NIỆM: MẪU (TEMPLATES)

### 1.1 Bản chất — Khuôn mẫu để sinh ra một họ các hàm hoặc lớp có cùng chức năng nhưng khác kiểu dữ liệu

Mẫu (Template) cung cấp cho chúng ta phương tiện để định nghĩa một **họ** (family) các hàm hoặc lớp có cùng chức năng nhưng có thể khác nhau về **kiểu dữ liệu** (data type) sử dụng bên trong.

- **Mẫu hàm (Function template)** là khuôn mẫu để sinh ra các hàm có liên quan.
- **Mẫu lớp (Class template)** là khuôn mẫu để sinh ra mã nguồn cho bất kỳ số lượng lớp có liên quan nào.

Mẫu (Template) triển khai **đa hình tham số (parametric polymorphism)** — cùng một đoạn mã hoạt động cho mọi kiểu, và kiểu được cung cấp như một tham số. Trình biên dịch tạo ra một **bản sao riêng** (separate copy) của hàm/lớp cho mỗi kiểu được sử dụng, tất cả đều tại **thời điểm biên dịch** (compile time).

### 1.2 Vấn đề chúng giải quyết — Viết một lần, hoạt động với mọi kiểu (Không trùng lặp mã)

Nếu không có mẫu (Template), bạn sẽ phải viết các hàm/lớp riêng cho từng kiểu:

```cpp
void swap(int &x, int &y)      { int temp = x; x = y; y = temp; }
void swap(float &x, float &y)  { float temp = x; x = y; y = temp; }
void swap(string &x, string &y){ string temp = x; x = y; y = temp; }
// ... và cứ thế cho mọi kiểu
```

Với mẫu (Template):

```cpp
template <class T>
void swap(T &x, T &y) { T temp = x; x = y; y = temp; }
// Một định nghĩa hoạt động cho int, float, string, Student, v.v.
```

### 1.3 Cách hoạt động

1. Bạn viết mẫu (template) với một **kiểu giữ chỗ** (placeholder type) (thường là `T`).
2. Khi bạn gọi/sử dụng nó với một kiểu cụ thể, trình biên dịch **tạo thể hiện (instantiates)** cho mẫu — sinh ra một phiên bản với `T` được thay thế bằng kiểu thực tế.
3. Việc này xảy ra tại **thời điểm biên dịch (compile time)** — không có chi phí runtime so với mã viết tay cho từng kiểu cụ thể.
4. Mỗi tổ hợp đối số mẫu (template arguments) duy nhất tạo ra một **thể hiện riêng biệt (distinct instantiation)**.

```
swap<int>(a, b)     → trình biên dịch sinh ra void swap(int &x, int &y) { ... }
swap<float>(a, b)   → trình biên dịch sinh ra void swap(float &x, float &y) { ... }
swap<string>(a, b)  → trình biên dịch sinh ra void swap(string &x, string &y) { ... }
```

### 1.4 Ví dụ cụ thể — Lớp mảng tổng quát

```cpp
template <class T>
class Array {
public:
    Array(unsigned sz);
    ~Array();
    T & operator[](unsigned i);
private:
    T * values;
    unsigned size;
};

int main() {
    Array<int>    ages(5);    // mảng 5 số int
    Array<float>  gpas(5);    // mảng 5 số float
    Array<string> names(5);   // mảng 5 chuỗi string
    // Một mẫu lớp → ba lớp cụ thể, được sinh tự động
}
```

### 1.5 Nó KHÔNG phải là gì

- **Mẫu (Template) KHÔNG phải là một lớp** — nó là bản thiết kế để sinh ra các lớp. Bạn không thể kế thừa trực tiếp từ một mẫu (`class D : public Array` là lỗi). Bạn chỉ có thể kế thừa từ một **thể hiện** (instantiation) (`class D : public Array<int>`).
- Mẫu (Template) **KHÔNG phải là đa hình lúc chạy (runtime polymorphism)** — chúng được giải quyết tại thời điểm biên dịch thông qua sinh mã. Không có bảng ảo (vtables), không có phân giải động (dynamic dispatch).
- Mẫu (Template) **KHÔNG được kế thừa** — lớp dẫn xuất không kế thừa bản thân mẫu, mà chỉ kế thừa lớp cụ thể đã được tạo thể hiện.

---

## 2. MẪU HÀM (FUNCTION TEMPLATES)

### 2.1 Định nghĩa — Hàm được định nghĩa với một kiểu chưa xác định; Trình biên dịch sinh ra các phiên bản riêng dựa trên kiểu đối số

Một hàm có thể được định nghĩa với một kiểu **chưa xác định** (unspecified). Trình biên dịch sinh ra các phiên bản riêng của hàm dựa trên kiểu của các đối số được truyền vào trong lời gọi hàm.

### 2.2 Cú pháp

```cpp
template <class T>
return-type function-name(T param)
```

- `T` được gọi là **tham số mẫu (template parameter)**.
- Từ khóa `class` có thể được thay thế bằng `typename` (tương đương trong ngữ cảnh này): `template <typename T>`.

### 2.3 Mẫu hàm một tham số

**Dạng cơ bản:**
```cpp
template <class T>
void display(const T &val) { cout << val; }
```

**Với một tham số không phải mẫu bổ sung:**
```cpp
template <class T>
void display(const T &val, ostream &os) { os << val; }
```

**Cùng tham số mẫu xuất hiện nhiều lần:**
```cpp
template <class T>
void swap(T &x, T &y) { T temp = x; x = y; y = temp; }
// T xuất hiện ba lần — đảm bảo cả hai đối số VÀ biến tạm đều có CÙNG KIỂU
```

### 2.4 Swap dưới dạng mẫu hàm

```cpp
#include <iostream>
using namespace std;

template <class T>
void swap(T &x, T &y) {
    T temp;
    temp = x;
    x = y;
    y = temp;
}

int main() {
    int a = 1, b = 2;
    swap(a, b);        // T = int

    float c = 1.5, d = 2.5;
    swap(c, d);        // T = float

    string e = "Hello", f = "World";
    swap(e, f);        // T = string
}
```

### 2.5 Mẫu hàm nhiều tham số

```cpp
template <class T1, class T2>
void arrayInput(T1 array, T2 &count) {
    for (T2 j = 0; j < count; j++) {
        cout << "value: ";
        cin >> array[j];
    }
}

// Sử dụng:
const unsigned tempCount = 3;
float temperature[tempCount];
const unsigned stationCount = 4;
int station[stationCount];

arrayInput(temperature, tempCount);  // T1=float[], T2=const unsigned
arrayInput(station, stationCount);   // T1=int[],    T2=const unsigned
```

### 2.6 Tra bảng — Tìm kiếm tổng quát

```cpp
template <class T>
long indexOf(T searchVal, const T *table, unsigned size) {
    for (unsigned i = 0; i < size; i++)
        if (searchVal == table[i])
            return i;
    return -1;
}

int main() {
    const unsigned iCount = 10, fCount = 5, sCount = 5;
    int iTable[iCount] = { 0, 10, 20, 30, 40, 50, 60, 70, 80, 90 };
    float fTable[fCount] = { 1.1, 2.2, 3.3, 4.4, 5.5 };

    cout << indexOf(20, iTable, iCount) << endl;        // in ra 2
    cout << indexOf(2.2f, fTable, fCount) << endl;      // in ra 1

    string names[sCount] = { "John", "Mary", "Sue", "Dan", "Bob" };
    cout << indexOf((string)"Dan", names, sCount) << endl; // in ra 3
}
```

### 2.7 Làm cho kiểu tự định nghĩa hoạt động với mẫu — Cần nạp chồng toán tử

Nếu một mẫu (template) sử dụng một toán tử (ví dụ: `==`), mọi kiểu sử dụng với mẫu đó **phải hỗ trợ** toán tử đó. Sử dụng nạp chồng toán tử (operator overloading) để đảm bảo tương thích:

```cpp
class Student {
public:
    Student(long idVal) { id = idVal; }
    int operator==(const Student &s2) const {
        return id == s2.id;
    }
private:
    long id;
};

int main() {
    const unsigned sc = 5;
    Student sTable[sc] = { 10000, 11111, 20000, 22222, 30000 };
    Student s(22222);
    cout << indexOf(s, sTable, sc) << endl;  // in ra 3
    // Hoạt động vì Student định nghĩa operator==
}
```

### 2.8 Ghi đè (Chuyên biệt hóa) một mẫu hàm

Khi một mẫu hàm không áp dụng được cho một kiểu cụ thể, bạn có thể cần:
- **Ghi đè (Override)** mẫu hàm (cung cấp một phiên bản không phải mẫu tường minh), hoặc
- Làm cho kiểu đó **tuân thủ** (conform) mẫu hàm (bằng cách thêm toán tử).

```cpp
// Mẫu tổng quát hoạt động cho hầu hết kiểu thông qua operator==
template <class T>
long indexOf(T searchVal, const T *table, unsigned size) { /* sử dụng == */ }

// Nhưng chuỗi char* cần strcmp — operator== so sánh con trỏ, không so sánh nội dung!
// Vì vậy chúng ta cung cấp một phiên bản ghi đè TƯỜNG MINH:
long indexOf(const char *searchVal, const char *table[], unsigned size) {
    for (unsigned i = 0; i < size; i++)
        if (strcmp(searchVal, table[i]) == 0)
            return i;
    return -1;
}

int main() {
    int iTable[] = { 0, 10, 20, 30, 40, 50, 60, 70, 80, 90 };
    cout << indexOf(20, iTable, 10) << endl;  // gọi phiên bản mẫu → 2

    const char *names[] = { "John", "Mary", "Sue", "Dan", "Bob" };
    cout << indexOf("Dan", names, 5) << endl; // gọi phiên bản tường minh → 3
    // Phiên bản tường minh được ưu tiên hơn mẫu cho const char*
}
```

**Quy tắc**: Một **hàm tường minh (không phải mẫu)** được ưu tiên hơn thể hiện mẫu (template instantiation) khi cả hai đều là kết quả khớp tốt như nhau. Điều này cho phép bạn tự viết tay các chuyên biệt hóa cho những kiểu có vấn đề.

---

## 3. MẪU LỚP (CLASS TEMPLATES)

### 3.1 Định nghĩa — Khuôn mẫu để sinh ra các lớp có liên quan; Kiểu được tham số hóa tại khai báo

```cpp
template <class T>
class MyClass {
    // sử dụng T bên trong (như tham số)
};

MyClass<int> x;         // tạo thể hiện với int
MyClass<Student> a;     // tạo thể hiện với Student
```

### 3.2 Ví dụ đơn giản — Hình tròn với tọa độ tổng quát

```cpp
template <class T1, class T2>
class Circle {
private:
    T1 x, y;         // tọa độ — bất kỳ kiểu số nào
    T2 radius;       // bán kính — có thể khác kiểu
};

Circle<int, long>        c1;     // x,y=int, radius=long
Circle<unsigned, float>  c2;     // x,y=unsigned, radius=float
```

### 3.3 Mẫu lớp mảng — Triển khai đầy đủ

```cpp
template <class T>
class Array {
public:
    Array(unsigned sz);
    ~Array();
    T & operator[](unsigned i);
private:
    T * values;
    unsigned size;
};

// Định nghĩa phương thức BÊN NGOÀI lớp — lưu ý tiền tố template trên MỖI phương thức:
template <class T>
Array<T>::Array(unsigned sz) {
    values = new T[sz];
    size = sz;
}

template <class T>
T & Array<T>::operator[](unsigned i) {
    if (i >= size) {
        cout << "ERROR: array index out of bound!!!\n";
        abort();
    }
    return values[i];
}

template <class T>
Array<T>::~Array() {
    delete[] values;
}

// Sử dụng:
int main() {
    const unsigned numStudents = 2;
    Array<int>    ages(numStudents);
    Array<float>  gpas(numStudents);
    Array<string> names(numStudents);

    for (int j = 0; j < numStudents; j++) {
        ages[j] = 20 + j;
        gpas[j] = 3.5 + j * 0.1;
        names[j] = "Student" + to_string(j);
    }
}
```

**Quy tắc cú pháp quan trọng**: Khi định nghĩa các thành viên mẫu lớp **bên ngoài** thân lớp, MỌI hàm thành viên phải được đặt trước bởi `template <class T>` và tên lớp phải bao gồm `<T>` (ví dụ: `Array<T>::Array` chứ không phải `Array::Array`).

---

## 4. MẪU VÀ KẾ THỪA (TEMPLATES AND INHERITANCE)

### 4.1 Mẫu (Template) KHÔNG phải là một lớp

- **Mẫu không phải là một lớp** — nó là khuôn mẫu để sinh ra các lớp.
- **Không thể kế thừa trực tiếp từ một mẫu**.

```cpp
// LỖI — mẫu không phải là lớp:
// class D : public Array { };   // T nào? Bất hợp pháp!

// ĐÚNG — kế thừa từ một thể hiện:
class D : public Array<int> { }; // đúng: Array<int> LÀ một lớp cụ thể

// ĐÚNG — một mẫu lớp có thể kế thừa từ một lớp thông thường:
template <class T>
class MyClass : public aClass { }; // kế thừa từ một lớp thông thường
```

### 4.2 Mẫu và thành viên tĩnh (Static members)

- Các thành viên tĩnh (Static members) được định nghĩa trong một mẫu là **thành viên tĩnh của các lớp liên kết với một mẫu** — KHÔNG phải của bản thân mẫu.
- Mỗi **thể hiện (instantiation)** của mẫu có **bản sao riêng** của thành viên tĩnh:

```cpp
template <class T>
class Counter {
    static int count;
public:
    Counter() { count++; }
    static int getCount() { return count; }
};

template <class T> int Counter<T>::count = 0;

int main() {
    Counter<int> c1, c2;
    Counter<float> c3;

    cout << Counter<int>::getCount() << endl;    // 2 (c1, c2)
    cout << Counter<float>::getCount() << endl;  // 1 (chỉ c3)
    // Counter<int> và Counter<float> có biến static count RIÊNG BIỆT!
}
```

---

## 5. BẠN (FRIENDS)

### 5.1 Lớp bạn (Friend class)

**Lớp bạn (Friend class)** là một lớp trong đó **tất cả các hàm thành viên** được cấp **quyền truy cập đầy đủ** vào tất cả các thành viên (`private`, `protected`, và `public`) của lớp định nghĩa nó làm bạn.

**Khai báo:** Lớp bạn được khai báo bên trong lớp cấp quyền kết bạn.

```cpp
class C1 {
    friend class C2;    // C2 có thể truy cập MỌI thành viên của C1
    int privateData;
};

class C2 {
    friend class C3;    // C3 có thể truy cập MỌI thành viên của C2
    void accessC1(C1 &obj) {
        obj.privateData = 5;  // OK — C2 là bạn của C1
    }
};

class C3 {
    void accessC1(C1 &obj) {
        // obj.privateData = 5;  // LỖI — C3 KHÔNG phải là bạn của C1
    }
};
```

### 5.2 Hàm bạn (Friend function)

**Hàm bạn (Friend function)** là một hàm được cấp **quyền truy cập đầy đủ** vào các thành viên `private` và `protected` của một thể hiện của lớp. Hàm bạn được khai báo bên trong lớp cấp quyền kết bạn.

```cpp
class Employee {
    int id;
    double salary;
public:
    Employee(int i, double s) : id(i), salary(s) {}
    friend float calcPay(Employee &e);  // calcPay có thể truy cập thành viên private
};

float calcPay(Employee &e) {
    return e.salary * 0.85f;  // OK — calcPay là bạn, có thể truy cập salary
}

// Cũng phổ biến: nạp chồng << như một friend
class Point {
    int x, y;
public:
    friend ostream & operator<<(ostream &os, const Point &p) {
        os << "(" << p.x << ", " << p.y << ")";  // Truy cập vào x, y private
        return os;
    }
};
```

### 5.3 Tính chất của bạn (Friends) — Ba "KHÔNG"

| Tính chất | Ý nghĩa | Ví dụ |
|-----------|---------|-------|
| **Không đối xứng (Non-symmetrical)** | Nếu C2 là bạn của C1, C1 KHÔNG nhất thiết là bạn của C2 | C2 có thể truy cập private của C1, nhưng C1 không thể truy cập private của C2 (trừ khi C2 cũng khai báo C1 là bạn) |
| **Không bắc cầu (Non-transitive)** | Nếu C2 là bạn của C1 và C3 là bạn của C2, C3 KHÔNG nhất thiết là bạn của C1 | Quan hệ bạn bè KHÔNG lan truyền qua chuỗi |
| **Không kế thừa được (Not inheritable)** | Bạn của lớp cơ sở KHÔNG được kế thừa bởi lớp dẫn xuất | Một hàm là bạn của `Employee` KHÔNG thể truy cập thành viên private của `SalariedEmployee` |

**Ví dụ về không kế thừa được:**
```cpp
class Employee {
    int empID;
public:
    friend float calcPay(Employee &e);
};

class SalariedEmployee : public Employee {
    double annualSalary;
    // calcPay() KHÔNG phải là bạn ở đây!
};

float calcPay(Employee &e) {
    // CÓ THỂ truy cập e.empID (bạn của Employee)
    // KHÔNG THỂ truy cập bất kỳ thành viên private nào riêng của SalariedEmployee
}
```

### 5.4 Những điều cần cân nhắc khi sử dụng bạn (Friends)

- Bạn (Friends) làm cho các lớp liên kết lỏng lẻo trở nên **liên kết chặt chẽ** (tightly coupled) — gây vấn đề về tính mô-đun và tìm kiếm lỗi.
- Bạn (Friends) **làm giảm tính đóng gói và che giấu thông tin** (encapsulation and information hiding).
- **Hạn chế sử dụng "bạn"** — chỉ dùng khi thực sự cần thiết (ví dụ: nạp chồng toán tử cho luồng nhập/xuất).

---

## 6. CÚ PHÁP MẪU CẦN HỌC THUỘC

### 6.1 Mẫu hàm (Function template)

```cpp
template <class T>
returnType functionName(T param) {
    // sử dụng T
}
```

### 6.2 Mẫu hàm với nhiều tham số

```cpp
template <class T1, class T2>
returnType functionName(T1 p1, T2 p2) {
    // sử dụng T1 và T2
}
```

### 6.3 Khai báo mẫu lớp (Class template)

```cpp
template <class T>
class MyClass {
    T data;
public:
    MyClass(T val);
    T getValue() const;
};
```

### 6.4 Định nghĩa thành viên mẫu lớp (Bên ngoài lớp)

```cpp
template <class T>
MyClass<T>::MyClass(T val) {
    data = val;
}

template <class T>
T MyClass<T>::getValue() const {
    return data;
}
```

### 6.5 Ghi đè tường minh (Không phải mẫu) của hàm mẫu

```cpp
// Phiên bản mẫu cho kiểu tổng quát
template <class T>
long indexOf(T searchVal, const T *table, unsigned size) { /* cài đặt tổng quát */ }

// Ghi đè tường minh cho const char*
long indexOf(const char *searchVal, const char *table[], unsigned size) {
    // cài đặt chuyên biệt dùng strcmp
}
```

### 6.6 Khai báo lớp bạn (Friend class)

```cpp
class A {
    friend class B;   // B có toàn quyền truy cập A
    int secret;
};

class B {
    void peek(A &a) { a.secret = 42; }  // OK
};
```

### 6.7 Khai báo hàm bạn (Friend function)

```cpp
class MyClass {
    int data;
public:
    friend void accessor(MyClass &m);
    friend ostream & operator<<(ostream &, const MyClass &);
};
```

### 6.8 Mẫu + Kế thừa (Cách dùng đúng)

```cpp
// Kế thừa từ một thể hiện mẫu cụ thể
class IntArray : public Array<int> { };

// Lớp mẫu kế thừa từ một lớp thông thường
template <class T>
class SmartPtr : public RefCounter { };
```

---

## 7. BẪY THI CỬ

### Bẫy 1: Mẫu (Template) KHÔNG phải là Lớp — Không thể Kế thừa Trực tiếp từ Mẫu

```cpp
template <class T> class Array { ... };

// LỖI: T nào? Array không phải là kiểu cụ thể
// class D : public Array { };

// ĐÚNG: chỉ rõ kiểu
class D : public Array<int> { };
```

### Bẫy 2: Quên `template <class T>` và `<T>` trên Định nghĩa Thành viên Bên ngoài Lớp

```cpp
// LỖI — thiếu tiền tố template và <T>
// Array::Array(unsigned sz) { ... }

// ĐÚNG:
template <class T>
Array<T>::Array(unsigned sz) { values = new T[sz]; size = sz; }
```

### Bẫy 3: Mẫu (Template) Yêu cầu Các Toán tử Được Sử dụng Phải Được Định nghĩa cho Kiểu

Nếu một mẫu hàm sử dụng `==`, mọi kiểu bạn tạo thể hiện với nó **phải** định nghĩa `operator==`. Nếu không → lỗi biên dịch.

```cpp
class MyType { };  // Không có operator==
// indexOf(MyType(), myArray, 5);  // LỖI BIÊN DỊCH — MyType không có ==
```

### Bẫy 4: Mỗi Thể hiện Mẫu (Template Instantiation) Có Thành viên Tĩnh (Static) RIÊNG

```cpp
template <class T> class C { static int count; };
// C<int>::count và C<float>::count là các biến KHÁC NHAU
```

### Bẫy 5: Ghi đè Hàm Tường minh (Explicit Function Override) Được Ưu tiên Hơn Kết quả Khớp Mẫu

Khi cả một hàm tường minh và một thể hiện mẫu đều khả dụng, phiên bản **không phải mẫu** sẽ thắng.

### Bẫy 6: Quan hệ Bạn (Friendship) KHÔNG Đối xứng

```cpp
class A { friend class B; };
// B có thể truy cập private của A, nhưng A KHÔNG THỂ truy cập private của B (trừ khi B cũng khai báo friend class A)
```

### Bẫy 7: Quan hệ Bạn (Friendship) KHÔNG Bắc cầu

```cpp
class A { friend class B; };
class B { friend class C; };
// C KHÔNG phải là bạn của A — quan hệ bạn không lan truyền
```

### Bẫy 8: Quan hệ Bạn (Friendship) KHÔNG được Kế thừa

```cpp
class Base { friend class F; };
class Derived : public Base { int derivedData; };
// F có thể truy cập thành viên của Base thông qua Derived, nhưng KHÔNG thể truy cập thành viên riêng của Derived
```

### Bẫy 9: Từ khóa `class` trong `template <class T>` — Đừng Nhầm với Kế thừa

`template <class T>` đang khai báo một **tham số kiểu** (type parameter), không phải định nghĩa một lớp. Từ khóa `typename` có thể được dùng thay thế: `template <typename T>`.

### Bẫy 10: Mã Mẫu (Template) Phải Được Đặt trong Tệp Tiêu Đề (Header Files) (Thông thường)

Vì trình biên dịch cần định nghĩa đầy đủ của mẫu để tạo thể hiện, các định nghĩa mẫu thường được đặt trong tệp tiêu đề (không được biên dịch riêng trong các tệp .cpp).

---

## 8. BÀI TẬP VIẾT TAY

### Bài tập 1: Viết Mẫu Hàm — Giá trị Lớn nhất của Hai Số

Viết một mẫu hàm `maximum` nhận hai tham số cùng kiểu và trả về giá trị lớn hơn.

```cpp
// TODO: Viết template

int main() {
    cout << maximum(3, 7) << endl;        // 7
    cout << maximum(3.5, 2.1) << endl;    // 3.5
    cout << maximum('a', 'z') << endl;    // z
}
```

> [!success]- Show Answer
> ```cpp
> template <class T>
> T maximum(T a, T b) {
>     return (a > b) ? a : b;
> }
> ```

### Bài tập 2: Mẫu Lớp — Cặp (Pair)

Triển khai một mẫu lớp `Pair` lưu trữ hai giá trị (có thể) khác kiểu.

```cpp
// TODO: Viết Pair template với constructor, getFirst(), getSecond()

int main() {
    Pair<int, string> p1(42, "hello");
    cout << p1.getFirst() << " " << p1.getSecond() << endl;  // 42 hello

    Pair<string, double> p2("pi", 3.14159);
    cout << p2.getFirst() << " " << p2.getSecond() << endl;  // pi 3.14159
}
```

> [!success]- Show Answer
> ```cpp
> template <class T1, class T2>
> class Pair {
>     T1 first;
>     T2 second;
> public:
>     Pair(T1 f, T2 s) : first(f), second(s) {}
>     T1 getFirst() const { return first; }
>     T2 getSecond() const { return second; }
> };
> ```

### Bài tập 3: Truy cập Lớp bạn (Friend class)

```cpp
class Vault {
    int secretCode;
public:
    Vault(int code) : secretCode(code) {}
    friend class KeyMaster;
};

class KeyMaster {
public:
    void reveal(Vault &v) { cout << "Secret: " << v.secretCode << endl; }
};

class Apprentice {
public:
    // Apprentice có thể truy cập Vault::secretCode không? Viết câu trả lời.
};
```

> [!success]- Show Answer
> `Apprentice` **không thể** truy cập `Vault::secretCode`. Quan hệ bạn (friendship) là không đối xứng và không bắc cầu. Chỉ `KeyMaster` (được khai báo tường minh là bạn) mới có quyền truy cập. `Apprentice` không có mối quan hệ đặc biệt nào với `Vault`.

### Bài tập 4: Ghi đè Hàm Tường minh của Mẫu

Mẫu `indexOf` sử dụng `==` để so sánh. Viết một phiên bản ghi đè tường minh cho chuỗi kiểu C (`const char*`).

```cpp
template <class T>
long indexOf(T searchVal, const T *table, unsigned size) {
    for (unsigned i = 0; i < size; i++)
        if (searchVal == table[i]) return i;
    return -1;
}

// TODO: Viết phiên bản ghi đè tường minh cho const char*

int main() {
    const char *names[] = { "Alice", "Bob", "Charlie" };
    cout << indexOf("Bob", names, 3) << endl;  // nên in ra 1
}
```

> [!success]- Show Answer
> ```cpp
> long indexOf(const char *searchVal, const char *table[], unsigned size) {
>     for (unsigned i = 0; i < size; i++)
>         if (strcmp(searchVal, table[i]) == 0)
>             return i;
>     return -1;
> }
> ```

### Bài tập 5: Mẫu với Thành viên Tĩnh (Static member)

```cpp
template <class T>
class Tracker {
    static int instances;
public:
    Tracker() { instances++; }
    ~Tracker() { instances--; }
    static int count() { return instances; }
};
template <class T> int Tracker<T>::instances = 0;

int main() {
    Tracker<int> a, b, c;
    Tracker<float> x, y;
    cout << Tracker<int>::count() << endl;     // ?
    cout << Tracker<float>::count() << endl;   // ?
}
```

> [!success]- Show Answer
> ```
> 3
> 2
> ```
> `Tracker<int>` và `Tracker<float>` có biến tĩnh (static) `instances` **riêng biệt**. `a, b, c` là 3 tracker kiểu int → `Tracker<int>::count()` = 3. `x, y` là 2 tracker kiểu float → `Tracker<float>::count()` = 2.

---

> [!NOTE]
> Hướng dẫn ôn tập này bao gồm toàn bộ nội dung bài giảng Lec11: Mẫu và Bạn (Templates and Friends). Nắm vững cú pháp cho mẫu hàm (function templates), mẫu lớp (class templates) (bao gồm định nghĩa thành viên bên ngoài lớp), và khai báo bạn (friend declarations). Ghi nhớ ba tính chất của quan hệ bạn (friendship): không đối xứng, không bắc cầu, và không kế thừa được.
