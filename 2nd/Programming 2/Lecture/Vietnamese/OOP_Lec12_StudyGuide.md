# Lec12: Lớp chứa (Container Classes) — Hướng dẫn học tập (Study Guide)

---

## 1. THẺ KHÁI NIỆM: LỚP CHỨA (CONTAINER CLASSES)

### 1.1 Định nghĩa

**Lớp chứa (Container class)** là một lớp mà các đối tượng (instance) của nó chứa các tập hợp những đối tượng khác. Bài giảng này tập trung vào **danh sách liên kết (linked lists)** — bao gồm **danh sách liên kết đơn dùng mẫu (template-based singly linked lists)** và **danh sách liên kết đôi hướng đối tượng (object-based doubly linked lists)**. Một danh sách gồm một tập hợp các phần tử được tổ chức tuần tự (nút), trong đó mỗi nút (trừ nút đầu tiên) có một nút đứng trước, và mỗi nút (trừ nút cuối cùng) có một nút đứng sau.

### 1.2 Vấn đề chúng giải quyết

Mảng có kích thước cố định hoặc yêu cầu thay đổi kích thước thủ công, và việc chèn/xóa phần tử ở giữa tốn O(n) do phải dịch chuyển. Danh sách liên kết giải quyết điều này:
- **Kích thước động (Dynamic sizing)** — phình ra và co lại khi cần (cấp phát bộ nhớ động).
- **Chèn/xóa hiệu quả** tại bất kỳ vị trí nào mà không cần dịch chuyển phần tử (chỉ thay đổi liên kết con trỏ).
- **Tiết kiệm bộ nhớ (Memory efficiency)** — chỉ cấp phát những gì bạn cần, khi bạn cần.

Đánh đổi: các nút được truy cập **tuần tự** (không có truy cập ngẫu nhiên như mảng).

### 1.3 Cách chúng hoạt động

1. Mỗi phần tử (nút) lưu trữ **dữ liệu** và một **con trỏ** tới nút tiếp theo (và tùy chọn là nút trước đó).
2. Danh sách duy trì các con trỏ tới **đầu (head)** (phần tử đầu tiên) và **đuôi (tail)** (phần tử cuối cùng), và tùy chọn là con trỏ vị trí **hiện tại (current)**.
3. Các thao tác như chèn/xóa hoạt động bằng cách thao tác trên các con trỏ nút — không cần dịch chuyển dữ liệu.

### 1.4 Hai cách tiếp cận được trình bày

| Cách tiếp cận | Cơ sở | Ưu điểm |
|----------|-------|-----------|
| **Dùng mẫu (Template-based)** danh sách liên kết đơn (`TList<T>`) | Tham số hóa kiểu (Type-parameterized) | Kiểu mạnh (Strongly typed); một mẫu danh sách dùng được cho mọi kiểu |
| **Hướng đối tượng (Object-based)** danh sách liên kết đôi (`DblList` với `DblNode`) | Dựa trên đa hình (Polymorphism-based) (lớp cơ sở trừu tượng) | Các nút thuộc nhiều kiểu khác nhau có thể cùng tồn tại trong một danh sách (thông qua con trỏ cơ sở) |

### 1.5 Nó KHÔNG phải là gì

- Danh sách liên kết **KHÔNG** phải là mảng — không có truy cập ngẫu nhiên O(1) theo chỉ số.
- Danh sách hướng đối tượng **KHÔNG** phải là dùng mẫu — nó sử dụng kế thừa và đa hình thay vì tổng quát hóa (generics).
- Một mẫu (template) **KHÔNG** phải là một lớp — `TList` là một mẫu, `TList<int>` là một lớp.

---

## 2. DANH SÁCH (LISTS) — CÁC KHÁI NIỆM CƠ BẢN

### 2.1 Định nghĩa

Một danh sách chứa **0 đến n nút (nodes)**. Mỗi phần tử được gọi là một **nút (node)**, và kết nối giữa hai nút bất kỳ được gọi là một **liên kết (link)**. Đây là một dạng cụ thể của đồ thị, trong đó mỗi nút trừ nút đầu tiên có một nút đứng trước, và mỗi nút trừ nút cuối cùng có một nút đứng sau.

### 2.2 Các thao tác trên danh sách

| Thao tác | Mô tả |
|-----------|-------------|
| `append` | Thêm một nút vào cuối |
| `prepend` | Thêm một nút vào đầu |
| `insert` | Chèn một nút vào vị trí cụ thể |
| `find` | Tìm một nút cụ thể |
| `get` | Lấy dữ liệu tại vị trí hiện tại |
| `replace` | Thay thế nội dung của một nút |
| `isEmpty` | Kiểm tra danh sách có rỗng không |
| `remove` | Xóa một nút |
| `clear` | Xóa tất cả các nút |

---

## 3. DANH SÁCH LIÊN KẾT ĐƠN DÙNG MẪU — `TList<T>`

### 3.1 Nút (Node) — `TNode<T>`

```cpp
template <class T>
class TNode {
    friend class TList<T>;            // TList có thể truy cập thành viên private
    T value;                          // dữ liệu được lưu trong nút
    TNode *next;                      // trỏ tới nút tiếp theo
public:
    TNode() : next(NULL) {}           // con trỏ next mặc định là NULL
    TNode(const T &val);
    TNode<T> *getNext() const;
    template <class X>
    friend ostream & operator<<(ostream &, const TNode<X> &);
};
```

// Hàm tạo với giá trị
template <class T>
TNode<T>::TNode(const T &val) {
    value = val;
    next = NULL;
}

template <class T>
TNode<T> *TNode<T>::getNext() const { return next; }

// Nạp chồng << để in một nút
template <class T>
ostream & operator<<(ostream &os, const TNode<T> &node) {
    os << node.value << "->";
    return os;
}
```

**Các quyết định thiết kế chính:**
- `TList<T>` được khai báo là **lớp bạn (friend class)** — cho phép TList truy cập trực tiếp vào `value` và `next`.
- Nút sử dụng **con trỏ thô (raw pointer)** `TNode *next` — KHÔNG phải tham chiếu, KHÔNG phải con trỏ thông minh.
- `operator<<` là một **hàm bạn khuôn mẫu (friend function template)** với tham số mẫu riêng `<class X>` để tránh che khuất (shadowing).

### 3.2 Danh sách (List) — `TList<T>`

```cpp
template <class T>
class TList {
    TNode<T> *head;       // nút đầu giả (dummy head node / sentinel)
    TNode<T> *tail;       // nút cuối giả (dummy tail node / sentinel)
    TNode<T> *current;    // con trỏ vị trí hiện tại
public:
    TList();
    ~TList();
    int advance();                     // di chuyển current tới nút tiếp theo
    void append(const T &nodeVal);     // thêm nút vào cuối
    void clear();                      // xóa tất cả các nút
    T get() const;                     // lấy dữ liệu tại vị trí hiện tại
    void goLast();                     // đặt current tới nút cuối
    void goTop();                      // đặt current tới nút đầu
    void insertAfter(const T &nodeVal);// chèn nút mới sau current
    int isEmpty() const;               // 1 nếu rỗng, 0 nếu không
    void prepend(const T &nodeVal);    // chèn vào đầu
    void replace(const T &newVal);     // thay thế dữ liệu trong nút hiện tại
    template <class X>
    friend ostream & operator<<(ostream &, const TList<X> &);
};
```

**Nút giả (Sentinel nodes / Dummy nodes)**: `head` và `tail` là các **nút giả** không chứa dữ liệu thực. Chúng đơn giản hóa logic xử lý các trường hợp đặc biệt:
- Danh sách rỗng: `head->next == tail` (và `tail->next == head`).
- Nút thực đầu tiên là `head->next`.
- Nút thực cuối cùng là nút có `next == tail`.

### 3.3 Hàm tạo (Constructor) và Hàm hủy (Destructor)

```cpp
template <class T>
TList<T>::TList() {
    head = new TNode<T>;
    tail = new TNode<T>;
    head->next = tail;       // head trỏ tới tail (vòng tròn)?
    tail->next = head;       // tail trỏ ngược lại head
    current = head;
}

template <class T>
TList<T>::~TList() {
    clear();
    delete head;
    delete tail;
}
```

**Trạng thái ban đầu**: `head` và `tail` được liên kết với nhau. Danh sách rỗng (`head->next == tail`). `current` bắt đầu tại `head`.

### 3.4 Các thao tác cốt lõi (Core Operations)

**isEmpty:**
```cpp
template <class T>
int TList<T>::isEmpty() const {
    return head->next == tail;   // nếu next của head là tail → không có nút thực
}
```

**clear — xóa tất cả các nút thực:**
```cpp
template <class T>
void TList<T>::clear() {
    current = head->next;
    while (current != tail) {
        head->next = current->next;
        delete current;
        current = head->next;
    }
    current = head;
    head->next = tail;          // đặt lại trạng thái rỗng
}
```

**advance — di chuyển current về phía trước:**
```cpp
template <class T>
int TList<T>::advance() {
    if (!current) abort();
    if (current->next != tail) {
        current = current->next;
        return 1;                // di chuyển thành công
    }
    return 0;                    // đã ở nút thực cuối cùng
}
```

**goLast / goTop:**
```cpp
template <class T>
void TList<T>::goLast() {
    if (!current) abort();
    while (current->next != tail)
        current = current->next;
}

template <class T>
void TList<T>::goTop() {
    current = head;
}
```

**get / replace:**
```cpp
template <class T>
T TList<T>::get() const {
    if (!current) abort();
    return current->value;
}

template <class T>
void TList<T>::replace(const T &newVal) {
    if (!current) abort();
    current->value = newVal;
}
```

### 3.5 Các thao tác chèn (Insert Operations)

**insertAfter — chèn một nút mới sau current:**
```cpp
template <class T>
void TList<T>::insertAfter(const T &nodeVal) {
    if (!current) abort();
    TNode<T> *p = new TNode<T>(nodeVal);   // tạo nút mới
    p->next = current->next;                // nút mới trỏ tới nút kế của current
    current->next = p;                      // current trỏ tới nút mới
    current = p;                            // di chuyển current tới nút mới
}
```

Minh họa:
```
Trước:  current → A → B
Sau:    current → A → [MỚI] → B
                        ↑ current giờ ở đây
```

**append và prepend — các wrapper tiện lợi:**
```cpp
template <class T>
void TList<T>::append(const T &nodeVal) {
    goLast();                // di chuyển current tới trước tail
    insertAfter(nodeVal);    // chèn sau nút thực cuối cùng
}

template <class T>
void TList<T>::prepend(const T &nodeVal) {
    goTop();                 // current = head (giả)
    insertAfter(nodeVal);    // chèn sau head → nút thực đầu tiên
}
```

### 3.6 Vấn đề "Chèn trước" (The "Insert Before" Problem)

**Chèn trước current rất khó** trong danh sách liên kết đơn — bạn phải tìm kiếm từ `head` để tìm nút có `next == current`, sau đó chèn sau nút đó. Đây là O(n).

Danh sách liên kết đôi giải quyết vấn đề này bằng cách duy trì các con trỏ `prev`.

### 3.7 In danh sách — `operator<<`

```cpp
template <class T>
ostream & operator<<(ostream &os, const TList<T> &list) {
    if (list.isEmpty()) return os;
    TNode<T> *p = list.head->getNext();   // bỏ qua head giả
    while (p != list.tail) {              // dừng trước tail giả
        os << *p;                         // sử dụng operator<< của TNode
        p = p->getNext();
    }
    os << endl;
    return os;
}
```

**Lưu ý**: Chúng ta dùng `getNext()` (public) thay vì `p->next` (private) vì hàm này không phải là thành viên và truy cập danh sách qua tham chiếu `const` — mặc dù nó là bạn (friend), việc dùng bộ truy cập public sẽ sạch sẽ hơn.

---

## 4. DANH SÁCH LIÊN KẾT ĐÔI HƯỚNG ĐỐI TƯỢNG — `DblList` với `DblNode`

### 4.1 Động lực (Motivation) — Danh sách với nhiều kiểu không đồng nhất (Heterogeneous Types)

Danh sách dùng mẫu (`TList<T>`) lưu các nút thuộc **một kiểu cụ thể**. Điều gì xảy ra nếu bạn muốn một danh sách chứa cả `Student`, `Faculty` và `Administrator` cùng nhau?

Giải pháp: Danh sách hướng đối tượng với **kế thừa và đa hình (inheritance and polymorphism)**. Tất cả các nút đều dẫn xuất từ một lớp cơ sở trừu tượng chung (`DblNode`), và danh sách lưu trữ các con trỏ tới lớp cơ sở. Mỗi kiểu nút dẫn xuất có thể có dữ liệu khác nhau trong khi vẫn là một phần của cùng một danh sách.

### 4.2 Nút (Node) — `DblNode` (Lớp cơ sở trừu tượng - Abstract Base)

```cpp
class DblNode {
    friend class DblList;                    // DblList có thể truy cập thành viên private
    virtual void printOn(ostream &os) const = 0;  // thuần ảo — lớp dẫn xuất BẮT BUỘC phải cài đặt
    virtual void readFrom(istream &is) = 0;       // thuần ảo — lớp dẫn xuất BẮT BUỘC phải cài đặt
    DblNode *next;     // con trỏ tới nút tiếp theo
    DblNode *prev;     // con trỏ tới nút trước đó
public:
    DblNode();
    virtual ~DblNode() { }
    DblNode *getNext() const;
    DblNode *getPrev() const;
    DblNode *detach();                       // tách nút khỏi các nút lân cận
    virtual int operator==(const DblNode &N) const = 0;  // so sánh thuần ảo
    friend ostream & operator<<(ostream &os, const DblNode &N);
    friend istream & operator>>(istream &inp, DblNode &N);
};
```

**Các hàm thuần ảo (Pure virtual functions)**: `printOn`, `readFrom` và `operator==` đều là `= 0` — khiến `DblNode` trở thành **lớp trừu tượng (abstract class)**. Bạn không thể tạo đối tượng (instantiate) một `DblNode` trần.

**Liên kết đôi (Doubly linked)**: Mỗi nút có cả hai con trỏ `next` và `prev`.

### 4.3 Cài đặt (Implementation) DblNode

```cpp
DblNode::DblNode() { next = prev = NULL; }

DblNode *DblNode::getNext() const { return next; }
DblNode *DblNode::getPrev() const { return prev; }

DblNode *DblNode::detach() {
    if (next)                    // nếu có nút kế tiếp? cho nó trỏ tới prev
        next->prev = prev;
    if (prev)                    // nếu có nút trước đó? cho nó trỏ tới next
        prev->next = next;
    prev = NULL;                 // tách nút hiện tại khỏi chuỗi
    next = NULL;
    return this;
}

ostream & operator<<(ostream &os, const DblNode &n) {
    n.printOn(os);               // gọi đa hình tới printOn() của lớp dẫn xuất
    return os;
}

istream & operator>>(istream &is, DblNode &n) {
    n.readFrom(is);              // gọi đa hình tới readFrom() của lớp dẫn xuất
    return is;
}
```

**`detach()`** rất quan trọng cho việc xóa — nó loại bỏ nút khỏi chuỗi bằng cách nối tắt (kết nối `prev` với `next`), sau đó đặt các con trỏ của chính nó về NULL.

### 4.4 Danh sách (List) — `DblList`

```cpp
class DblList {
    virtual void printOn(ostream &os) const;
    DblNode *first;    // nút đầu tiên trong danh sách
    DblNode *last;     // nút cuối cùng trong danh sách
    long size;         // số lượng phần tử
public:
    DblList();
    ~DblList();
    void append(DblNode *n);                   // thêm nút vào cuối
    void deleteAll();                          // xóa tất cả các nút
    DblNode *find(const DblNode &n) const;     // tìm nút khớp
    DblNode *remove(DblNode *n);               // xóa và trả về một nút
    int isEmpty() const;
    DblNode *getFirst() const;
    DblNode *getLast() const;
    long getSize() const;
    friend ostream & operator<<(ostream &os, const DblList &);
};
```

**Không có nút giả (No dummy nodes)** — `first` và `last` trỏ trực tiếp tới các nút thực (hoặc là NULL khi rỗng). Đây là một lựa chọn thiết kế khác với cách tiếp cận dùng sentinel của `TList`.

### 4.5 Cài đặt (Implementation) DblList

**Hàm tạo (Constructor) / Hàm hủy (Destructor) / Bộ truy cập cơ bản (Basic Accessors):**
```cpp
DblList::DblList() { first = NULL; last = NULL; size = 0; }
DblList::~DblList() { deleteAll(); }
int DblList::isEmpty() const { return first == NULL; }
long DblList::getSize() const { return size; }
DblNode *DblList::getFirst() const { return first; }
DblNode *DblList::getLast() const { return last; }
```

**append:**
```cpp
void DblList::append(DblNode *p) {
    if (!p) return;
    if (last) {              // có nút cuối không?
        last->next = p;      // có: gắn nút mới sau nó
        p->prev = last;
    } else {
        first = p;           // không: đây là nút đầu tiên
    }
    last = p;                // nút mới trở thành nút cuối
    size++;
}
```

Minh họa cho việc thêm vào cuối danh sách không rỗng:
```
Trước:  A ⇄ B (last=B)
Sau:    A ⇄ B ⇄ [MỚI] (last=MỚI)
```

**remove:**
```cpp
DblNode *DblList::remove(DblNode *p) {
    if (!p) return NULL;
    if (p == first)              // đang xóa nút đầu tiên?
        first = first->next;     // di chuyển first về phía trước
    if (p == last)               // đang xóa nút cuối cùng?
        last = last->prev;       // di chuyển last về phía sau
    p->detach();                 // tách khỏi các nút lân cận
    size--;
    return p;
}
```

**find:**
```cpp
DblNode *DblList::find(const DblNode &n) const {
    DblNode *p = first;
    while (p) {
        if (n == *p) return p;  // sử dụng operator== đa hình (virtual)
        p = p->next;
    }
    return 0;                    // không tìm thấy
}
```

> **Ghi chú**: `n == *p` gọi `operator==`, là **thuần ảo (pure virtual)** trong `DblNode`. Lớp dẫn xuất (ví dụ: `Student`) phải cung cấp logic so sánh thực tế. Cũng lưu ý: `n == *p` so sánh `(const DblNode &n)` với `*p`. Vì chữ ký hàm nhận `const DblNode &n`, nó phải được ép kiểu bên trong `operator==` của lớp dẫn xuất.

**printOn:**
```cpp
void DblList::printOn(ostream &os) const {
    DblNode *n = first;
    while (n) {
        os << (*n);         // in đa hình — gọi operator<< của Node → printOn()
        n = n->next;
    }
}

ostream & operator<<(ostream &os, const DblList &aList) {
    aList.printOn(os);
    return os;
}
```

### 4.6 Con trỏ `current`

Chúng ta có thể thêm một con trỏ `current` làm thành viên dữ liệu vào `DblList` (giống như `TList` có). Điều này không nằm trong thiết kế cơ sở nhưng là một mở rộng tự nhiên.

---

## 5. VÍ DỤ: DANH SÁCH ĐA HÌNH (POLYMORPHIC LIST) — SINH VIÊN TRONG TRƯỜNG ĐẠI HỌC

### 5.1 Student dưới dạng DblNode

```cpp
class Student : public DblNode {
    long id;
public:
    Student() { id = 0; }
    Student(long idNum) { id = idNum; }
    void setId(long idNum) { id = idNum; }

    int operator==(const DblNode &p) const {
        return id == ((Student &)p).id;     // cần ép kiểu: p là tham chiếu DblNode
    }

    void printOn(ostream &os) const {       // ghi đè (override) hàm thuần ảo
        os << id;
    }

    void readFrom(istream &is) {            // ghi đè (override) hàm thuần ảo
        is >> id;
    }
};
```

### 5.2 Sử dụng hai danh sách cùng nhau

```cpp
int registerStudents(TList<Student *> &classRoll, const DblList &college) {
    Student student;
    long id;
    cout << "Enter student id: ";
    cin >> id;
    if (id == -1) return 0;

    student.setId(id);
    Student *p = (Student *) college.find(student); // tìm trong CSDL trường
    if (p) {
        cout << "Adding student to the class roll.\n";
        classRoll.append(p);                 // thêm con trỏ vào danh sách lớp
    } else
        cout << "Student not found in college list!!!\n";
    return 1;
}

int main() {
    Student *sp;
    DblList college;                         // hướng đối tượng: có thể chứa nhiều kiểu

    for (long i = 10000; i < 10050; i++) {
        sp = new Student(i);
        college.append(sp);                  // nạp danh sách trường
    }

    TList<Student *> classRoll;              // dùng mẫu: lưu Student*

    cout << "Register students for a class.\n" << "(enter -1 to quit)\n\n";
    while (registerStudents(classRoll, college))
        continue;

    cout << "Finished.\n" << classRoll << endl;
    return 0;
}
```

**Nhận xét thiết kế**: `DblList` lưu trữ các đối tượng không đồng nhất (tất cả đều dẫn xuất từ `DblNode`). `TList<Student*>` là một **danh sách dùng mẫu chứa các con trỏ** — nó lưu các giá trị `Student*`. Hai kiểu danh sách phục vụ các mục đích khác nhau và có thể tương tác với nhau.

---

## 6. TList vs DblList — SO SÁNH

| Khía cạnh | `TList<T>` | `DblList` |
|--------|-----------|-----------|
| Kiểu nút | Tham số mẫu `T` | Lớp cơ sở trừu tượng `DblNode` |
| Hướng liên kết | Liên kết đơn (chỉ `next`) | Liên kết đôi (`next` + `prev`) |
| Nút giả (Sentinel nodes) | Có (head + tail giả) | Không (kết thúc NULL) |
| Đồng nhất / Không đồng nhất | Đồng nhất (mọi nút cùng kiểu) | Không đồng nhất (nhiều kiểu dẫn xuất) |
| Đa hình (Polymorphism) | Không — thời gian biên dịch qua template | Có — thời gian chạy qua hàm virtual |
| Chèn trước current | Khó (O(n)) — phải tìm từ head | Dễ (O(1)) — theo con trỏ `prev` |
| Con trỏ `current` | Có | Tùy chọn (không có trong thiết kế cơ sở) |
| So sánh nút | Dùng `operator==` trên kiểu `T` | Dùng `operator==` thuần ảo |

---

## 7. CÚ PHÁP MẪU (SYNTAX TEMPLATES) CẦN HỌC THUỘC

### 7.1 Khai báo TNode

```cpp
template <class T>
class TNode {
    friend class TList<T>;
    T value;
    TNode *next;
public:
    TNode() : next(NULL) {}
    TNode(const T &val);
    TNode<T> *getNext() const;
};
```

### 7.2 Cấu trúc cốt lõi của TList

```cpp
template <class T>
class TList {
    TNode<T> *head;      // giả
    TNode<T> *tail;      // giả
    TNode<T> *current;   // vị trí
public:
    TList();
    ~TList();
    void append(const T &val);
    void prepend(const T &val);
    void insertAfter(const T &val);
    void clear();
    int isEmpty() const;
    int advance();
    T get() const;
    void replace(const T &val);
    void goLast();
    void goTop();
};
```

### 7.3 Hàm tạo TList (Sentinel Pattern)

```cpp
template <class T>
TList<T>::TList() {
    head = new TNode<T>;
    tail = new TNode<T>;
    head->next = tail;
    tail->next = head;
    current = head;
}
```

### 7.4 TList::insertAfter

```cpp
template <class T>
void TList<T>::insertAfter(const T &nodeVal) {
    TNode<T> *p = new TNode<T>(nodeVal);
    p->next = current->next;
    current->next = p;
    current = p;
}
```

### 7.5 Lớp cơ sở trừu tượng DblNode

```cpp
class DblNode {
    friend class DblList;
    virtual void printOn(ostream &os) const = 0;
    virtual void readFrom(istream &is) = 0;
    DblNode *next;
    DblNode *prev;
public:
    DblNode();
    virtual ~DblNode() {}
    DblNode *getNext() const;
    DblNode *getPrev() const;
    DblNode *detach();
    virtual int operator==(const DblNode &N) const = 0;
};
```

### 7.6 Cấu trúc cốt lõi của DblList

```cpp
class DblList {
    DblNode *first;
    DblNode *last;
    long size;
public:
    DblList();
    ~DblList();
    void append(DblNode *n);
    DblNode *remove(DblNode *n);
    DblNode *find(const DblNode &n) const;
    void deleteAll();
    int isEmpty() const;
    long getSize() const;
};
```

### 7.7 DblList::append

```cpp
void DblList::append(DblNode *p) {
    if (!p) return;
    if (last) {
        last->next = p;
        p->prev = last;
    } else {
        first = p;
    }
    last = p;
    size++;
}
```

### 7.8 DblList::remove

```cpp
DblNode *DblList::remove(DblNode *p) {
    if (!p) return NULL;
    if (p == first) first = first->next;
    if (p == last) last = last->prev;
    p->detach();
    size--;
    return p;
}
```

### 7.9 DblNode::detach

```cpp
DblNode *DblNode::detach() {
    if (next) next->prev = prev;
    if (prev) prev->next = next;
    prev = NULL;
    next = NULL;
    return this;
}
```

---

## 8. BẪY THI (EXAM TRAPS)

### Bẫy 1: `head->next == tail` Nghĩa là Danh sách Rỗng (trong TList)
Trong `TList`, cả `head` và `tail` đều là nút giả. Một danh sách rỗng có `head->next == tail`. Đừng nhầm lẫn điều này với các nút chứa giá trị.

### Bẫy 2: `insertBefore` Rất Khó trong Danh sách Liên kết Đơn
Để chèn trước `current` trong `TList`, bạn phải duyệt từ `head` để tìm nút đứng trước (O(n)). Không có con trỏ `prev`. Hãy dùng danh sách liên kết đôi nếu bạn cần chèn trước thường xuyên.

### Bẫy 3: Quên Tiền tố Mẫu (Template Prefix) trên Định nghĩa Thành viên
```cpp
// LỖI — cần tiền tố template và <T>
// TList::TList() { ... }

// ĐÚNG:
template <class T>
TList<T>::TList() { ... }
```
Mọi định nghĩa thành viên bên ngoài lớp PHẢI được đặt trước bởi `template <class T>` và sử dụng `ClassName<T>::`.

### Bẫy 4: `DblNode` Là Trừu tượng (Abstract) — Không thể Tạo Đối tượng Trực tiếp
```cpp
DblNode n;               // LỖI — các hàm thuần ảo (printOn, readFrom, operator==)
DblNode *p = new Student(12345);  // OK — Student là lớp cụ thể (concrete)
```

### Bẫy 5: `operator==` trong `DblNode` Yêu cầu Ép kiểu (Casting)
Bên trong `Student::operator==`, tham số là `const DblNode &p`. Để truy cập `id`, bạn phải ép kiểu: `((Student &)p).id`. Không ép kiểu → lỗi biên dịch.

### Bẫy 6: `detach()` KHÔNG `delete` Nút — Chỉ Ngắt Liên kết
`detach()` loại bỏ nút khỏi chuỗi nhưng KHÔNG giải phóng bộ nhớ. Người gọi (`DblList::remove`, `deleteAll`) chịu trách nhiệm gọi `delete`.

### Bẫy 7: Hủy Danh sách có Nút Giả — Xóa Nút Giả Sau khi Clear
```cpp
~TList() {
    clear();         // xóa tất cả nút thực trước
    delete head;     // sau đó xóa các nút giả
    delete tail;
}
```
Xóa nút giả trước nút thực sẽ tạo ra các con trỏ lơ lửng (dangling pointers).

### Bẫy 8: Đa hình (Polymorphism) trong `DblList` — `operator<<` Gọi `printOn()` Ảo
`os << (*n)` với `n` là `DblNode*` gọi `operator<<(ostream&, const DblNode&)`, hàm này gọi `n.printOn(os)`. Vì `printOn` là virtual, phiên bản dẫn xuất đúng sẽ được chạy. Đây là cách danh sách không đồng nhất in ra đúng nội dung.

### Bẫy 9: Mẫu (Template) Sinh Mã Riêng cho Mỗi Kiểu
`TList<int>` và `TList<float>` là các lớp hoàn toàn riêng biệt — mã riêng, thành viên static riêng, vtable riêng. Chúng chỉ chia sẻ mã nguồn mẫu.

---

## 9. BÀI TẬP THỰC HÀNH VIẾT TAY (HAND-CODING DRILLS)

### Bài tập 1: Truy vết Thao tác Chèn trong TList

```cpp
TList<int> list;
list.append(10);
list.append(20);
list.prepend(5);
```

Truy vết nội dung danh sách sau mỗi thao tác. Vẽ chuỗi nút.

> [!success]- Xem đáp án (Show Answer)
> Sau `append(10)`: head → 10 → tail (current tại 10)
> Sau `append(20)`: head → 10 → 20 → tail (current di chuyển tới cuối rồi chèn sau)
> Sau `prepend(5)`: head → 5 → 10 → 20 → tail (chèn sau head)
>
> Kết quả cuối: head(giả) → 5 → 10 → 20 → tail(giả)

### Bài tập 2: Viết DblList::deleteAll

```cpp
// TODO: Cài đặt deleteAll — xóa và giải phóng TẤT CẢ các nút khỏi danh sách
void DblList::deleteAll() {
    // ...
}
```

> [!success]- Xem đáp án (Show Answer)
> ```cpp
> void DblList::deleteAll() {
>     DblNode *p = first;
>     while (p) {
>         DblNode *next = p->getNext();
>         delete p;
>         p = next;
>     }
>     first = NULL;
>     last = NULL;
>     size = 0;
> }
> ```

### Bài tập 3: Dẫn xuất Faculty từ DblNode

Cài đặt một lớp `Faculty` kế thừa từ `DblNode` với các thành viên `string name` và `string department`. Ghi đè (override) `printOn`, `readFrom` và `operator==`.

> [!success]- Xem đáp án (Show Answer)
> ```cpp
> class Faculty : public DblNode {
>     string name;
>     string department;
> public:
>     Faculty() {}
>     Faculty(string n, string d) : name(n), department(d) {}
>
>     int operator==(const DblNode &n) const {
>         const Faculty &f = (const Faculty &)n;
>         return name == f.name && department == f.department;
>     }
>
>     void printOn(ostream &os) const {
>         os << name << " (" << department << ")";
>     }
>
>     void readFrom(istream &is) {
>         is >> name >> department;
>     }
> };
> ```

### Bài tập 4: Truy vết Xóa trong DblList

```cpp
DblList list;
list.append(new Student(100));
list.append(new Student(200));
list.append(new Student(300));

Student s(200);
DblNode *found = list.find(s);
list.remove(found);   // Lưu ý: remove KHÔNG delete — chỉ ngắt liên kết
```

Danh sách trông như thế nào sau khi xóa? `first` là gì? `last` là gì? `size` là gì?

> [!success]- Xem đáp án (Show Answer)
> Danh sách: Student(100) ⇄ Student(300). `first` trỏ tới 100, `last` trỏ tới 300, `size` = 2.
>
> `found` (trỏ tới Student(200)) giờ đã được tách (prev=NULL, next=NULL) nhưng KHÔNG bị xóa — rò rỉ bộ nhớ nếu người gọi không gọi `delete` một cách tường minh.
>
> **Lưu ý**: Thao tác `remove` trả về nút đã được tách nhưng KHÔNG `delete` nó. Người gọi phải tự quản lý bộ nhớ.

### Bài tập 5: Append và Prepend trong TList — Liệu có Hiệu quả?

Giải thích tại sao `append` trong `TList` (gọi `goLast()` rồi `insertAfter`) là O(n) trong khi `prepend` (gọi `goTop()` rồi `insertAfter`) là O(1).

> [!success]- Xem đáp án (Show Answer)
> `goLast()` duyệt toàn bộ danh sách từ `head` để tìm nút có `next == tail` — O(n). `goTop()` chỉ đơn giản gán `current = head` — O(1). Do đó, trong cách cài đặt này, `append` là O(n) và `prepend` là O(1).
>
> Để làm cho `append` thành O(1), bạn có thể duy trì một con trỏ `last` trực tiếp xác định nút thực cuối cùng (giống như `DblList` làm). Vì `tail` là nút giả trong `TList`, bạn cần theo dõi nút đứng trước `tail`.

---

> [!NOTE]
> Hướng dẫn học tập này bao quát toàn bộ nội dung bài giảng cho Lec12: Lớp chứa (Container Classes). Hãy nắm vững cả danh sách liên kết đơn dùng mẫu (`TList<T>` với các nút sentinel) và danh sách liên kết đôi hướng đối tượng (`DblList` / `DblNode` với đa hình). Có khả năng truy vết các thao tác chèn/xóa và hiểu được sự đánh đổi giữa hai cách tiếp cận.
