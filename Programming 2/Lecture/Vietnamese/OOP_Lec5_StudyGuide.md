# Lec5: Đối tượng và Lớp (Khái niệm) — Hướng dẫn Ôn tập

---

## 1. THẺ KHÁI NIỆM (CONCEPT CARD)

### 1.1 Định nghĩa

**Lớp (Class)** là một khuôn mẫu (blueprint) định nghĩa hai thứ cho một nhóm các đối tượng:
- **Cấu trúc dữ liệu (Data structure)** — các bộ mô tả trạng thái (thuộc tính, thành phần dữ liệu) mà mỗi đối tượng sẽ mang theo
- **Phương thức (Methods)** — các thao tác (hành vi, hàm thành viên) mà mỗi đối tượng có thể thực hiện

**Đối tượng (Object)** là một thể hiện (Instance) cụ thể được tạo ra từ khuôn mẫu đó. Nó có:
- **Định danh (Identity)** — một tên hoặc tham chiếu duy nhất phân biệt nó với mọi đối tượng khác
- **Trạng thái (State)** — các giá trị hiện tại của các thuộc tính tại một thời điểm cụ thể
- **Hành vi (Behavior)** — những gì nó có thể làm, được định nghĩa bởi các phương thức của lớp

> [!success]- Show Answer — Định nghĩa Ba Phần (Booch)
> > "Thứ gì đó có trạng thái, hành vi và định danh."

> [!success]- Show Answer — Định nghĩa Martin/Odell
> > "Bất cứ thứ gì, thực tế hoặc trừu tượng, mà chúng ta lưu trữ dữ liệu và các phương thức thao tác trên dữ liệu đó."

> [!success]- Show Answer — Định nghĩa Peter Müller
> > "Một đối tượng là một thể hiện của một lớp. Nó có thể được xác định duy nhất bằng tên của nó và nó định nghĩa một trạng thái được biểu diễn bởi các giá trị của các thuộc tính tại một thời điểm cụ thể."

### 1.2 Vấn Đề Nó Giải Quyết

Trước khi có lớp (class), dữ liệu và hàm sống tách biệt. Nếu bạn cần ba tài khoản ngân hàng, bạn khai báo ba biến số dư riêng biệt, ba hàm nạp tiền riêng biệt, v.v. Không có cách nào để nói "các số dư này và các quy tắc nạp tiền này thuộc về nhau như một đơn vị logic duy nhất."

Lớp (Class) giải quyết điều này bằng cách:
- **Gói gọn (Bundling)** — dữ liệu và các hàm thao tác trên nó vào một đơn vị có tên duy nhất
- **Đóng gói (Encapsulating)** — ẩn các chi tiết nội bộ đằng sau một giao diện công khai để người gọi không thể làm hỏng đối tượng
- **Tái sử dụng (Reusing)** — định nghĩa khuôn mẫu một lần, sau đó tạo ra bao nhiêu thể hiện độc lập tùy ý
- **Mô hình hóa (Modeling)** — cho phép bạn ánh xạ trực tiếp các thực thể trong thế giới thực vào cấu trúc chương trình (một `Student` trong code tương ứng với một sinh viên ngoài đời)

### 1.3 Cách Nó Hoạt Động

1. Bạn viết một **định nghĩa lớp (class definition)** liệt kê các thành phần dữ liệu (trạng thái) và các hàm thành viên (hành vi).
2. Lớp đóng vai trò như một **nhà máy (factory)**: bạn gọi hàm tạo (constructor) của nó để tạo ra các đối tượng.
3. Lớp đóng vai trò như một **bộ phân loại (classifier)**: tất cả các đối tượng của lớp đó chia sẻ cùng một cấu trúc.
4. Mỗi đối tượng có một **bản sao độc lập** riêng của các thành phần dữ liệu.
5. Tất cả các đối tượng của cùng một lớp **chia sẻ** cùng một mã hàm (một bản sao trong bộ nhớ).
6. Các đối tượng giao tiếp bằng cách **gửi thông điệp (sending messages)** — gọi các phương thức công khai của nhau.
7. **Giao diện (Interface)** (tập hợp các phương thức công khai) xác định những gì bên ngoài có thể yêu cầu đối tượng làm.

> [!success]- Show Answer — Mô hình Tinh thần 7 Bước
> > ```
> > Định nghĩa Lớp → Nhà máy (hàm tạo) → Đối tượng (các thể hiện)
> >                                          ↕
> >                          mỗi cái có dữ liệu riêng, code chung
> >                                          ↕
> >                    giao tiếp qua thông điệp (lời gọi phương thức)
> >                                          ↕
> >              chỉ các phương thức công khai tạo thành giao diện
> > ```

### 1.4 Ví dụ Cụ thể

Một hệ thống đặt phòng khách sạn. Lớp `Room` định nghĩa rằng mỗi phòng có số phòng, loại phòng, giá và trạng thái (trống/có khách). Bạn tạo ra đối tượng `room_301` và đối tượng `room_302`. Cả hai đều tuân theo cùng một khuôn mẫu nhưng chứa dữ liệu thực tế khác nhau (số phòng khác nhau, có thể giá khác nhau). Phương thức `book()` tồn tại một lần trong code của lớp, nhưng khi bạn gọi `room_301.book("Alice")`, nó chỉ sửa đổi dữ liệu của `room_301`.

### 1.5 Nó KHÔNG Phải Là Gì

- **KHÔNG phải là struct trong C.** Một struct trong C là một túi dữ liệu thụ động không có hành vi tích hợp sẵn. Một lớp (class) gói gọn dữ liệu CÙNG VỚI các hàm và kiểm soát quyền truy cập.
- **KHÔNG giống với thể hiện (instance).** Lớp là bản thiết kế; đối tượng là ngôi nhà được xây từ bản thiết kế đó. Nhầm lẫn hai thứ này giống như nhầm lẫn công thức nấu ăn với cái bánh.
- **KHÔNG phải là một namespace.** Một lớp cung cấp tính đóng gói (encapsulation) và khả năng tạo thể hiện (instantiation); một namespace chỉ nhóm các tên lại.
- **KHÔNG nhất thiết là một vật thể vật lý.** Đối tượng có thể đại diện cho các khái niệm trừu tượng: một `Transaction`, một `Reservation`, một `Set`, một `Payment`.

---

## 2. HIỂU VỀ ĐỐI TƯỢNG (OBJECTS)

### 2.1 Lập Trình Dựa Trên Đối Tượng

Lập trình dựa trên đối tượng (Object-based programming) nhìn thế giới như một **tập hợp các đối tượng tự trị, tương tác với nhau**. Thay vì một luồng thủ tục duy nhất, hệ thống được cấu thành từ các thực thể mà mỗi thực thể biết cách làm công việc của riêng mình và giao tiếp với các thực thể khác.

Ý tưởng chính: bạn không nói cho một đối tượng biết *cách* làm điều gì đó từng bước; bạn gửi cho nó một thông điệp yêu cầu nó làm điều gì đó, và nó tự tìm ra cách.

Ví dụ về các đối tượng trong thế giới thực có thể nhìn nhận theo cách này:
- **Con người** (tự trị, có khả năng giao tiếp, có tên, được sinh ra/chết đi)
- **Động vật, thực vật** (các thực thể sống có hành vi)
- **Tòa nhà, phòng ốc, cầu thang** (các thực thể cấu trúc có thuộc tính)
- **Máy tính, điện thoại** (các thiết bị xử lý và giao tiếp)

> [!success]- Show Answer — Điều gì làm cho một chương trình trở thành "dựa trên đối tượng"?
> > Một chương trình được gọi là dựa trên đối tượng khi nguyên tắc tổ chức chính của nó là các đối tượng — không phải hàm, không phải thủ tục, không phải luồng dữ liệu. Các đối tượng giữ trạng thái riêng của chúng và phản hồi các thông điệp. Ngay cả khi không có tính kế thừa (inheritance) hay tính đa hình (polymorphism), nếu bạn tổ chức code xoay quanh các đối tượng với trạng thái được đóng gói và giao diện truyền thông điệp, bạn đang làm lập trình dựa trên đối tượng.

### 2.2 Các Thuộc Tính Của Đối Tượng Trong Thế Giới Thực

Các đối tượng trong thế giới thực thể hiện năm thuộc tính chính. Hiểu được những điều này giúp bạn thiết kế các đối tượng ảo (virtual objects) tốt hơn:

| Thuộc tính | Ý nghĩa | Ví dụ Thực tế |
|---|---|---|
| **Chủ động / Tự trị (Active / Autonomous)** | Mỗi đối tượng có hành vi riêng; không bị điều khiển trực tiếp từ bên ngoài | Một người suy nghĩ độc lập; một con chó tự sủa |
| **Có khả năng giao tiếp (Communicative)** | Các đối tượng có thể gửi và nhận thông điệp đến/từ các đối tượng khác | Một người nói chuyện với người khác; một chiếc điện thoại gửi tín hiệu đến trạm phát sóng |
| **Hợp tác (Collaborative)** | Các mối quan hệ lâu dài giữa các đối tượng phát sinh thông qua tương tác lặp lại | Một giáo viên và học sinh hợp tác trong suốt một học kỳ |
| **Lồng ghép (Nested)** | Các đối tượng phức tạp chứa các đối tượng khác như các thành phần | Một chiếc xe hơi chứa động cơ, bánh xe, ghế ngồi |
| **Được đặt tên duy nhất / có định danh (Uniquely named / identifiable)** | Mọi đối tượng đều có một định danh phân biệt nó | Một người có CMND; một máy tính có số serial |
| **Được tạo ra / Bị hủy bỏ (Created / Destroyed)** | Các đối tượng đi vào và ra khỏi sự tồn tại | Một người được sinh ra và chết đi; một tòa nhà được xây dựng và phá dỡ |

> [!success]- Show Answer — Tại sao sáu thuộc tính này quan trọng đối với thiết kế?
> > Khi bạn thiết kế một lớp, hãy tự hỏi: Đối tượng của tôi có tự trị không (hay nó chỉ là một vật chứa dữ liệu thụ động)? Nó có giao tiếp với các đối tượng khác thông qua một giao diện được định nghĩa rõ ràng không? Nó có hợp tác (duy trì tham chiếu đến các đối tượng khác) không? Nó có được cấu thành từ các đối tượng con (composition) không? Nó có một định danh duy nhất không? Vòng đời (tạo/hủy) của nó có được quản lý đúng cách không? Những kiểm tra này tạo ra các thiết kế hướng đối tượng (OO) mạnh mẽ.

### 2.3 Ví dụ Cụ thể Về Các Đối Tượng Trong Thế Giới Thực

**Một Người:**
- Tự trị: suy nghĩ, quyết định, hành động
- Có khả năng giao tiếp: nói, viết, cử chỉ
- Hợp tác: có bạn bè, đồng nghiệp, mối quan hệ gia đình
- Có định danh: có tên, CMND, số hộ chiếu
- Vòng đời: sinh ra (được tạo), chết đi (bị hủy)

**Một Máy Tính:**
- Tự trị: xử lý chỉ thị, chạy chương trình
- Có khả năng giao tiếp: card mạng, USB, Bluetooth
- Hợp tác: là một phần của mạng, tương tác với các thiết bị ngoại vi
- Có định danh: số serial, địa chỉ MAC, hostname
- Vòng đời: được sản xuất (tạo ra), ngừng hoạt động (bị hủy)

### 2.4 Đối Tượng Ảo (Virtual Objects)

Đối tượng ảo là các đối tượng tồn tại **chỉ trong chương trình** (không phải trong thế giới vật lý). Chúng chia sẻ sáu thuộc tính giống nhau nhưng:

- **Chính xác hơn** về tên gọi, ranh giới và tương tác (không có sự mơ hồ)
- **Được định nghĩa đầy đủ** — mọi trạng thái và hành vi có thể có đều được lập trình viên chỉ định
- Là các **khối xây dựng cơ bản** của các chương trình hướng đối tượng

Ví dụ từ bài giảng:

| Đối tượng Ảo | Trạng thái (Dữ liệu) | Hành vi (Phương thức) |
|---|---|---|
| **Tài khoản Ngân hàng (Bank Account)** | balance, accountNumber | deposit(amt), withdraw(amt), getBalance() |
| **Tập hợp (Set)** | collection of elements | add(e), remove(e), contains(e), size() |
| **Vé Điện tử (E-Ticket)** | eventName, seatNumber, paymentStatus | confirmPayment(), isPaid(), getSeat() |
| **Thanh toán (Payment)** | amount, payer, payee, timestamp | process(), refund(), getStatus() |

> [!success]- Show Answer — Điều gì làm cho đối tượng ảo khác với đối tượng thế giới thực?
> > Các đối tượng ảo được lập trình viên chỉ định đầy đủ — mọi ranh giới, hành vi và tương tác đều chính xác. Các đối tượng thế giới thực có ranh giới mờ nhạt (một "dòng sông" kết thúc ở đâu?), hành vi mơ hồ ("suy nghĩ" có nghĩa chính xác là gì?), và các tương tác không được kiểm soát. Đối tượng ảo là các mô hình lý tưởng hóa, đơn giản hóa của bất cứ thứ gì chúng đại diện.

### 2.5 Ví dụ Đối tượng Ảo: Một Tập hợp (Set)

Một `Set` là một trong những ví dụ sạch nhất từ bài giảng. Nó hiểu bốn thông điệp:

| Thông điệp | Hiệu ứng (thay đổi nội bộ) | Giá trị trả về |
|---|---|---|
| `add(anElement)` | Chèn phần tử nếu chưa có | none (void) |
| `remove(anElement)` | Xóa phần tử nếu có | none (void) |
| `contains(anElement)` | Không thay đổi nội bộ | true/false |
| `size()` | Không thay đổi nội bộ | số nguyên đếm |

Mỗi thông điệp có **cả** hiệu ứng (effect) (những gì thay đổi bên trong đối tượng hoặc những thông điệp nó kích hoạt) **và** giá trị trả về (return value) (những gì nó gửi lại cho người gọi). Người dùng chỉ cần biết **góc nhìn bên ngoài (external view)** (giao diện) để sử dụng Set — họ không bao giờ thấy cấu trúc dữ liệu nội bộ.

### 2.6 Tập hợp (Set) Trong Các Ngôn Ngữ Không Phải OOP

Đây là một sự tương phản quan trọng mà bài giảng đưa ra. Trong một ngôn ngữ thủ tục (non-OOP):

- Một `Set` là một **cấu trúc thụ động (passive structure)** (chỉ dữ liệu, giống như struct trong C)
- Các thao tác là các **hàm chủ động nhưng không trạng thái (active but stateless functions)** — chúng không nhớ bất cứ điều gì giữa các lần gọi
- Bạn viết: `procedure add(s: Set, e: Element)` — tập hợp được truyền vào như một **tham số (parameter)**, không dùng ký hiệu dấu chấm (dot notation)
- **Không có tính đóng gói (No encapsulation)**: lập trình viên có thể trực tiếp thao tác dữ liệu nội bộ, có khả năng đưa nó vào trạng thái bị tổn hại (không nhất quán)
- Hàm `add` không "thuộc về" Set — nó chỉ là một thủ tục độc lập tình cờ nhận một Set làm đối số

> [!success]- Show Answer — OOP vs. Thủ tục Set, so sánh song song
> >
> > **Phong cách OOP:**
> > ```
> > mySet.add(42);        // thông điệp đến đối tượng
> > mySet.contains(42);   // đối tượng phản hồi
> > ```
> >
> > **Phong cách Thủ tục:**
> > ```
> > add(mySet, 42);       // hàm với set là tham số
> > contains(mySet, 42);  // set không có quyền chủ động
> > ```
> >
> > Sự khác biệt chính: trong OOP, đối tượng là **người nhận (receiver)** của thông điệp. Trong thủ tục, đối tượng chỉ là một đối số khác. Phiên bản OOP cũng đảm bảo tính đóng gói — bạn không thể bỏ qua `add()` và trực tiếp can thiệp vào mảng nội bộ.

### 2.7 Định nghĩa về "Đối tượng (Object)" (từ các tác giả khác nhau)

Bài giảng trình bày ba định nghĩa chính thức. Các bài kiểm tra có thể yêu cầu bạn so sánh hoặc ghép chúng:

| Tác giả | Định nghĩa | Nhấn mạnh |
|---|---|---|
| **Booch** | "Thứ gì đó có trạng thái, hành vi và định danh." | Ba thuộc tính thiết yếu |
| **Martin / Odell** | "Bất cứ thứ gì, thực tế hoặc trừu tượng, mà chúng ta lưu trữ dữ liệu và các phương thức thao tác trên dữ liệu đó." | Sự kết hợp dữ liệu + phương thức |
| **Peter Müller** | "Một đối tượng là một thể hiện của một lớp. Nó có thể được xác định duy nhất bằng tên của nó và nó định nghĩa một trạng thái được biểu diễn bởi các giá trị của các thuộc tính tại một thời điểm cụ thể." | Mối quan hệ lớp-thể hiện và trạng thái theo thời gian |

> [!success]- Show Answer — Định nghĩa nào mang tính thao tác nhất (hướng code)?
> > Định nghĩa của Müller, vì nó ràng buộc rõ ràng đối tượng với lớp của nó và định nghĩa trạng thái một cách cụ thể như các giá trị thuộc tính tại một thời điểm — điều này ánh xạ trực tiếp vào cách bạn viết và gỡ lỗi code.

> [!success]- Show Answer — Định nghĩa nào trừu tượng nhất?
> > Định nghĩa của Booch, vì "trạng thái, hành vi, định danh" áp dụng cho bất cứ thứ gì theo nghĩa đen — một người, một tài khoản ngân hàng, một tiến trình, một file handle. Nó là một định nghĩa triết học hơn là một định nghĩa cài đặt.

---

## 3. THÔNG ĐIỆP VÀ GIAO DIỆN (MESSAGES AND INTERFACES)

### 3.1 Định nghĩa: Thông điệp (Message)

Một **thông điệp (message)** là một yêu cầu được gửi đến một đối tượng để gọi một trong các phương thức của nó. Nó chứa hai phần:

1. **Tên** của phương thức cần gọi
2. **Các đối số (arguments)** (tham số thực tế) mà phương thức yêu cầu

Các điểm chính:
- **Việc gọi một phương thức là một phản ứng (reaction)** do việc nhận được thông điệp gây ra
- Một thông điệp chỉ thành công nếu phương thức **thực sự được biết đến** bởi đối tượng (tức là được định nghĩa trong lớp của nó và có thể truy cập được)
- Trong C++, gửi thông điệp đến một phương thức private bị từ chối tại **thời điểm biên dịch (compile time)**
- Thông điệp có cả **hiệu ứng (effect)** (những gì đối tượng làm nội bộ) và **giá trị trả về (return value)** (những gì nó gửi lại)

> [!success]- Show Answer — Thông điệp vs. Lời gọi Phương thức: chúng có giống nhau không?
> > Trong C++, "gửi một thông điệp" LÀ gọi một phương thức — chúng đồng nghĩa trong cài đặt. Nhưng về mặt khái niệm, "thông điệp" nhấn mạnh mô hình **yêu cầu-người nhận (request-receiver)**: bạn yêu cầu đối tượng làm điều gì đó, và nó quyết định cách làm. "Lời gọi phương thức" nhấn mạnh **sự gọi cơ học (mechanical invocation)**. Sự khác biệt này quan trọng trong các cuộc thảo luận thiết kế và trong các ngôn ngữ (như Smalltalk) nơi runtime có thể xử lý các thông điệp không xác định một cách động.

> [!success]- Show Answer — Một thông điệp có thể có hiệu ứng nhưng không có giá trị trả về không?
> > Có. `void add(Element e)` trong một Set thay đổi nội dung của Set nhưng không trả về gì. Ngược lại, `contains(e)` trả về một boolean nhưng không có hiệu ứng nào trên Set. Mọi thông điệp đều có CẢ hai ô — một hoặc cả hai có thể trống.

### 3.2 Giao diện (The Interface)

**Giao diện (interface)** là danh sách các tên thao tác (chữ ký phương thức) **mở cho các đối tượng khác** — những gì bên ngoài được phép gọi.

Các phân biệt quan trọng:
- Nếu một đối tượng có một hàm nhưng không công khai nó, thì nó **vô dụng với công chúng** (nó là **private**)
- Trong C++, chỉ các hàm **public** thuộc về giao diện và có thể được gọi từ bên ngoài
- Giao diện định nghĩa **hợp đồng (contract)**: "nếu bạn gửi cho tôi thông điệp này với các đối số này, tôi đảm bảo hành vi này"
- Các thành viên private là **chi tiết cài đặt (implementation details)** — tác giả lớp có thể thay đổi chúng một cách tự do mà không làm hỏng bất kỳ người gọi nào

> [!success]- Show Answer — Cái gì thuộc về giao diện so với cái gì được ẩn nội bộ?
> >
> > | Giao diện (public) | Ẩn (private) |
> > |---|---|
> > | Các phương thức định nghĩa những gì đối tượng CÓ THỂ LÀM | Các phương thức trợ giúp hỗ trợ các phương thức public |
> > | Các accessor (bộ truy cập) tiết lộ trạng thái một cách an toàn | Các thành phần dữ liệu thô |
> > | Các mutator (bộ thay đổi) thay đổi trạng thái có kiểm tra hợp lệ | Bộ đếm nội bộ, bộ nhớ đệm, cờ |
> >
> > Nguyên tắc chung: công khai càng ít càng tốt. Mỗi phương thức public là một cam kết bạn phải duy trì.

> [!success]- Show Answer — "Một phương thức tồn tại nhưng không nằm trong giao diện." Khi nào điều này đúng?
> > Khi phương thức được khai báo `private`. Đối tượng biết cách thực hiện nó và có thể gọi nó nội bộ, nhưng không có đối tượng bên ngoài nào có thể gửi thông điệp đó. Trong C++, cố gắng gọi một phương thức private từ bên ngoài lớp là một lỗi biên dịch (compile-time error).

---

## 4. THUỘC TÍNH VÀ LỢI ÍCH CỦA ĐỐI TƯỢNG

### 4.1 Thuộc tính của Đối tượng

| Thuộc tính | Ý nghĩa |
|---|---|
| **Tính đóng gói (Encapsulation)** | Dữ liệu và các thao tác thao tác trên nó được gói gọn cùng nhau thành một đơn vị (đối tượng). Bạn không có dữ liệu ở đây và hàm ở kia — chúng sống bên trong cùng một ranh giới. |
| **Tính che giấu thông tin (Information Hiding)** | Các chi tiết cài đặt nội bộ được ẩn đằng sau một giao diện công khai. Người gọi chỉ biết đối tượng LÀM gì, không biết NÓ LÀM ĐIỀU ĐÓ NHƯ THẾ NÀO. Biểu diễn dữ liệu nội bộ có thể thay đổi mà không ảnh hưởng đến người gọi. |
| **Tính trừu tượng dữ liệu (Data Abstraction)** (với các lớp) | Lớp định nghĩa một góc nhìn trừu tượng về dữ liệu. Người dùng làm việc với `deposit(amount)` chứ không phải `balance += amount`. Sự trừu tượng hóa ẩn đi biểu diễn cụ thể. |
| **Kiểu dữ liệu trừu tượng (Abstract Data Type - ADT)** (với các lớp) | Một lớp, cùng với tính đóng gói và che giấu thông tin của nó, tạo ra một ADT — một kiểu do người dùng định nghĩa hoạt động như một kiểu tích hợp sẵn. Bạn khai báo `Set s;` và sử dụng `s.add(5)` một cách tự nhiên như `int x; x = 5;`. |

> [!success]- Show Answer — Tính đóng gói (Encapsulation) vs. Che giấu thông tin (Information Hiding): chúng không giống nhau sao?
> > **Tính đóng gói (Encapsulation)** là CƠ CHẾ — gói gọn dữ liệu và phương thức lại với nhau. **Che giấu thông tin (Information Hiding)** là NGUYÊN TẮC THIẾT KẾ — cố tình hạn chế quyền truy cập vào các chi tiết nội bộ. Bạn có thể có tính đóng gói mà không có che giấu thông tin (ví dụ: mọi thứ đều public trong một lớp — được gói gọn, nhưng không bị che giấu). Thiết kế OO tốt yêu cầu cả hai.

### 4.2 Lợi Ích của Đối tượng

| Lợi ích | Giải thích |
|---|---|
| **Các lợi ích giống như ADT** | Che giấu thông tin, trừu tượng dữ liệu và trừu tượng thủ tục đều được áp dụng |
| **Tính kế thừa (Inheritance) cung cấp trừu tượng hóa sâu hơn** | Các lớp con (subclasses) tinh chỉnh và chuyên biệt hóa hành vi mà không cần viết lại chức năng cơ bản (được đề cập trong Lec7 và Lec8) |
| **Phát triển dễ dàng hơn và ít lỗi hơn** | Các đối tượng ánh xạ trực tiếp vào các khái niệm thế giới thực; mỗi đối tượng có trách nhiệm giới hạn, được định nghĩa rõ ràng; ít tác dụng phụ không mong muốn |
| **Bảo trì dễ dàng hơn** | Các thay đổi bên trong một lớp không lan truyền qua toàn bộ chương trình; giao diện vẫn ổn định; lỗi được khoanh vùng |
| **Tính mô-đun (Modularity)** | Các đối tượng là các mô-đun tự nhiên — khép kín, có thể kiểm thử độc lập, có thể hiểu độc lập |
| **Tính tái sử dụng (Reusability)** | Các lớp được thiết kế tốt có thể được tái sử dụng qua nhiều dự án (ví dụ: một `Set`, một `Date`, một `BankAccount`) |

> [!success]- Show Answer — Lợi ích nào phù hợp nhất cho một nhóm lớn làm việc trên một sản phẩm lâu dài?
> > Bảo trì dễ dàng hơn. Trong một nhóm lớn qua nhiều năm, các tác giả ban đầu rời đi, yêu cầu thay đổi và lỗi được phát hiện. Che giấu thông tin có nghĩa là một nhà phát triển mới có thể sửa hoặc thay đổi nội bộ của một lớp mà không cần hiểu toàn bộ hệ thống — miễn là giao diện công khai vẫn giữ nguyên.

---

## 5. PHÂN LOẠI VÀ LỚP (CLASSIFICATION AND CLASSES)

### 5.1 Phân loại (Classification)

Phân loại là quá trình nhóm các thứ dựa trên các đặc điểm chung. Nó **không phải là duy nhất cho OOP** — nó được áp dụng trong sinh học, khoa học thư viện, hóa học và nhiều lĩnh vực khác.

Bài giảng sử dụng một sơ đồ phân cấp:

```
Animal
├── Mammal
│   ├── People
│   │   ├── man
│   │   │   ├── John
│   │   │   └── ...
│   │   └── woman
│   │       ├── Jane
│   │       └── ...
│   └── Dog
│       ├── Fido
│       └── ...
└── Bird
    ├── Sparrow
    └── ...
```

Phân loại là **ý tưởng cơ bản để hiểu về tính kế thừa (inheritance)**: một lớp con (subclass) IS-A (LÀ MỘT) loại cụ thể hơn của lớp cha (superclass) của nó. Nền tảng khái niệm này là những gì Lec7 xây dựng dựa trên.

> [!success]- Show Answer — Tại sao bài giảng giới thiệu phân loại trước khi nói về lớp?
> > Bởi vì một lớp (class) LÀ một cơ chế phân loại. Khi bạn viết `class Dog { ... }`, bạn đang phân loại tất cả các con chó là chia sẻ các thuộc tính và hành vi nhất định. Nhìn nhận phân loại như một công cụ nhận thức tổng quát (không chỉ là một cấu trúc lập trình) giúp bạn hiểu tại sao các lớp là một cách tự nhiên để mô hình hóa thế giới.

### 5.2 Lớp (Class) Là Gì?

Từ bài giảng, một lớp phục vụ hai vai trò riêng biệt:

**Vai trò 1 — Phân loại (chỉ đặc tả):**
Một lớp là một định nghĩa về ý nghĩa của việc là một thành viên của thể loại đó. Nó chỉ rõ cấu trúc (dữ liệu gì) và hành vi (phương thức gì). Đây là vai trò **trừu tượng, khái niệm**.

**Vai trò 2 — Cài đặt (code + đặc tả):**
Một lớp là một cơ chế lập trình thực tế — một khuôn mẫu (template) mà trình biên dịch sử dụng để cấp phát bộ nhớ và sinh mã. Đây là vai trò **cụ thể, cơ học**.

Hai định nghĩa chính thức từ bài giảng:
- "Lớp (Class) — một định nghĩa về một cài đặt (các phương thức và cấu trúc dữ liệu) được chia sẻ bởi một nhóm các đối tượng."
- "Lớp (Class) — một khuôn mẫu (template) từ đó các đối tượng có thể được tạo ra. Chứa định nghĩa về các bộ mô tả trạng thái và phương thức cho các đối tượng."

> [!success]- Show Answer — OOP là "lập trình với các lớp." Tại sao không phải là "lập trình với các đối tượng"?
> > Bởi vì lớp là cơ chế tổ chức trung tâm. Các đối tượng được tạo ra từ các lớp, cấu trúc của chúng được định nghĩa bởi các lớp, và hành vi của chúng được cài đặt trong các lớp. Nếu không có lớp, bạn sẽ có các đối tượng ad-hoc không có cấu trúc chia sẻ — đó chỉ là lập trình thủ tục với các struct. Lớp cung cấp cho bạn phân loại (classification), tạo thể hiện (instantiation), đóng gói (encapsulation) và (sau này) kế thừa (inheritance), tất cả trong một cấu trúc.

### 5.3 Khái niệm Chủ Ý của Lớp (Intentional Notion of Class)

**Khái niệm chủ ý (intentional notion)** là lớp được xem như một **khuôn mẫu hoặc bản thiết kế (template or blueprint)**:

- Các đối tượng mới là các **thể hiện (instances)** của một lớp
- **Trạng thái (state)** (các thành phần dữ liệu) và **hành vi (behavior)** (các phương thức) của mọi thể hiện được xác định bởi định nghĩa lớp
- Khái niệm chủ ý xác định **cấu trúc (structure)** của các thể hiện — những ô (thuộc tính) nào mọi thể hiện sẽ có và những thao tác nào nó có thể thực hiện
- Hãy nghĩ về nó như: "Đây là một X trông như thế nào" — định nghĩa, không phải tập hợp

> [!success]- Show Answer — Khái niệm chủ ý trong một câu
> > Khái niệm chủ ý là lớp như một định nghĩa về cấu trúc — nó nói mọi thể hiện sẽ trông như thế nào trước khi bất kỳ thể hiện nào tồn tại.

### 5.4 Khái niệm Mở rộng của Lớp (Extensional Notion of Class)

**Khái niệm mở rộng (extensional notion)** là lớp được xem như một **nhà kho và nhà máy (warehouse and factory)**:

- **Nhà kho đối tượng (Object warehouse)**: lớp ngầm duy trì một **phạm vi lớp (class extent)** — tập hợp tất cả các thể hiện hiện đang tồn tại
- **Nhà máy đối tượng (Object factory)**: mỗi lớp có một **hàm tạo (constructor)** — một cơ chế để tạo ra các thể hiện mới
- Khái niệm mở rộng theo dõi **có bao nhiêu** đối tượng tồn tại và **đối tượng nào** đang tồn tại
- Hãy nghĩ về nó như: "Đây là tất cả các X hiện đang tồn tại" — tập hợp, không phải định nghĩa

> [!success]- Show Answer — Khái niệm mở rộng trong một câu
> > Khái niệm mở rộng là lớp như một vật chứa/người tạo — nó theo dõi và tạo ra các thể hiện thực tế.

> [!success]- Show Answer — Chủ ý (Intentional) vs. Mở rộng (Extensional) — câu hỏi kiểm tra chính
> >
> > | Khía cạnh | Chủ ý (Intentional) | Mở rộng (Extensional) |
> > |---|---|---|
> > | Mô tả cái gì | Cấu trúc/bản thiết kế | Tập hợp các thể hiện |
> > | Trả lời câu hỏi | "X LÀ gì?" | "Những X nào tồn tại?" |
> > | Biểu hiện trong C++ | Bản thân định nghĩa lớp | Thành viên `static` theo dõi thể hiện, các hàm tạo |
> > | Tồn tại trước khi có đối tượng? | Có | Không (phạm vi rỗng) |

### 5.5 Hiểu Về Lớp — Tổng kết

Một lớp cung cấp:
1. Một định nghĩa về **cấu trúc (structure)** của các thể hiện của lớp đó (chủ ý)
2. **Tên** và kiểu của các thuộc tính (trạng thái) mà các đối tượng thuộc về lớp sẽ giữ
3. **Tên** và chữ ký của các phương thức (hành vi) mà các đối tượng thuộc về lớp có thể thực thi

Cùng nhau: lớp → định nghĩa cấu trúc → các thể hiện với cấu trúc đó → các đối tượng chia sẻ định nghĩa nhưng giữ trạng thái độc lập.

### 5.6 Ví dụ về Lớp (từ bài giảng)

**Ví dụ 1 — Integer:**

```
class Integer {
    Ds: int I;                          // dữ liệu: giá trị integer
    Ops: setValue(int n);               // thao tác: gán một giá trị
         Integer addValue(Integer j);   // thao tác: cộng một Integer khác
};
```

Điều này cho thấy ký hiệu "Ds + Ops" được sử dụng trong bài giảng. Các thành phần dữ liệu (Ds) định nghĩa trạng thái; các thao tác (Ops) định nghĩa hành vi.

**Ví dụ 2 — Horse:**

```
class Horse {
    Ds: Age, Weight, Color;    // thuộc tính mọi con ngựa đều có
    Ops: Drag, Run, Ride;      // hành vi mọi con ngựa đều có thể làm
};
```

> [!success]- Show Answer — Các ví dụ Ds/Ops dạy chúng ta điều gì?
> > Rằng một lớp luôn được định nghĩa bởi HAI thứ: dữ liệu và thao tác. Nếu bạn chỉ có dữ liệu (giống struct trong C), nó không phải là một lớp. Nếu bạn chỉ có các hàm (giống namespace), nó không phải là một lớp. Một lớp luôn gói gọn cả hai.

### 5.7 Các Mối Quan Hệ Giữa Các Lớp

Các lớp không tồn tại một cách cô lập. Bài giảng xác định hai mối quan hệ cơ bản (cộng với một mối quan hệ được xem trước cho phần sau):

| Mối quan hệ | Còn được gọi là | Ý nghĩa | Ví dụ |
|---|---|---|---|
| **Liên kết (Link)** | "use-a" | Một thể hiện của lớp này gửi thông điệp đến một thể hiện của lớp khác. Hai lớp cần giao tiếp với nhau. | Một `Driver` sử dụng một `Car` — gọi `car.start()`, `car.accelerate()` |
| **Hợp thành (Composition)** | "has-a" | Một lớp chứa các thành phần dữ liệu mà bản thân chúng là các đối tượng của một lớp khác. Bộ phận thuộc về toàn thể. | Một `Car` có một `Engine` — `Engine` là một thành phần dữ liệu của `Car` |
| **Kế thừa (Inheritance)** | "is-a" | Một lớp là một loại chuyên biệt hóa của một lớp khác. Được xem trước ở đây, sẽ được đề cập trong Lec7/8. | Một `Dog` là một `Animal` |

UML (Unified Modeling Language - Ngôn ngữ Mô hình hóa Hợp nhất) được giới thiệu như ký hiệu trực quan tiêu chuẩn để biểu diễn các lớp và mối quan hệ của chúng.

> [!success]- Show Answer — "use-a" vs. "has-a": cách phân biệt chúng
> >
> > | Câu hỏi | "use-a" (Liên kết) | "has-a" (Hợp thành) |
> > |---|---|---|
> > | Đối tượng kia có phải là **thành phần dữ liệu** không? | Không — nó được truyền vào hoặc truy cập thông qua một lời gọi phương thức | Có — nó được khai báo như một thuộc tính |
> > | Đối tượng có **sở hữu** đối tượng kia không? | Không — mối quan hệ tạm thời | Có — vòng đời gắn kết |
> > | Nếu đối tượng này chết, đối tượng kia có chết không? | Không | Thường là có |
> >
> > Hãy nghĩ theo cách này: nếu bạn có thể vẽ một mũi tên ghi "gửi thông điệp đến" giữa chúng, đó là use-a. Nếu bạn có thể nói "là một phần của," đó là has-a.

---

## 6. TẠO THỂ HIỆN (INSTANTIATION)

### 6.1 Tạo thể hiện (Instantiation) Là Gì?

**Tạo thể hiện (Instantiation)** là cơ chế tạo ra các đối tượng mới từ một định nghĩa lớp. Mọi lớp đều có một cơ chế như vậy — điển hình là một **hàm tạo (constructor)**. Lớp là khuôn cắt bánh; tạo thể hiện là hành động ấn nó vào bột để tạo ra một cái bánh.

### 6.2 Tạo thể hiện Tĩnh (Static) vs. Động (Dynamic)

| Khía cạnh | Tĩnh (Static) | Động (Dynamic) |
|---|---|---|
| **Khi nào?** | Thời điểm biên dịch (Compile time) | Thời điểm chạy (Run time) |
| **Ai cấp phát?** | Trình biên dịch (trên stack) | Lập trình viên yêu cầu (trên heap) thông qua `new` |
| **Vòng đời** | Tự động — bị hủy khi ra khỏi phạm vi | Thủ công — phải gọi `delete` để hủy |
| **Cú pháp** | `ClassName obj(args);` | `ClassName* obj = new ClassName(args);` |
| **Vị trí bộ nhớ** | Stack | Heap |
| **Chi phí** | Không có (nhanh) | Chi phí cấp phát runtime |

Tạo thể hiện động (Dynamic instantiation) yêu cầu **hỗ trợ thời điểm chạy (run-time support)** để cấp phát (`new`) và giải phóng (`delete`) bộ nhớ.

> [!success]- Show Answer — Khi nào bạn dùng động hơn là tĩnh?
> > Dùng động khi: (1) bạn không biết cần bao nhiêu đối tượng tại thời điểm biên dịch, (2) đối tượng cần tồn tại lâu hơn phạm vi nơi nó được tạo ra, (3) đối tượng rất lớn (không gian stack bị hạn chế). Dùng tĩnh cho các đối tượng nhỏ, tồn tại ngắn với số lượng đã biết.

### 6.3 Tạo Đối tượng từ Khuôn mẫu Lớp

```java
aSet = new Set();        // Set là lớp; new Set() tạo ra một đối tượng
anotherSet = new Set();  // Cùng nhà máy (lớp), đối tượng khác (nội dung)
```

- Cả `aSet` và `anotherSet` đều chia sẻ cùng một định nghĩa lớp (cùng cấu trúc)
- Chúng là **các đối tượng khác nhau** — mỗi cái có dữ liệu độc lập riêng
- `aSet.add(5)` không ảnh hưởng đến `anotherSet` dưới bất kỳ hình thức nào
- Mỗi lần gọi `new` tạo ra một đối tượng **mới và duy nhất**

### 6.4 Cấu trúc Đối tượng

Bài giảng đưa ra một sự phân tích chính thức của một đối tượng:

```
Object ::= <Oid, Cid, Body>
```

| Thành phần | Ý nghĩa |
|---|---|
| **Oid** | Định danh Đối tượng (Object Identifier) — định danh duy nhất của đối tượng cụ thể này |
| **Cid** | Định danh Lớp (Class Identifier) — tên (hoặc định danh) của lớp mà đối tượng này thuộc về |
| **Body** | Không gian bộ nhớ thực tế chứa dữ liệu của đối tượng (các giá trị thuộc tính) |

Lưu ý quan trọng: các **thao tác (operations)** (phương thức) của đối tượng được cài đặt trong **LỚP (CLASS)**, không được sao chép trong mọi đối tượng. Mỗi đối tượng chỉ lưu trữ dữ liệu riêng của nó; tất cả các đối tượng của cùng một lớp chia sẻ một bản sao của code.

> [!success]- Show Answer — Tại sao các phương thức không được lưu trữ trong Body?
> > Vì hiệu quả. Nếu bạn có 10.000 đối tượng `Student`, bạn không muốn 10.000 bản sao của `attendLecture()` trong bộ nhớ. Các phương thức sống trong lớp; mỗi đối tượng chỉ lưu trữ một con trỏ (Cid) trở về lớp của nó để code đúng được thực thi. Body chỉ chứa dữ liệu riêng của từng thể hiện.

### 6.5 Ví dụ về Lớp trong C++ (lớp Student từ bài giảng)

```cpp
class Student {
private:
    unsigned numCoursesRequired;
    unsigned age;
public:
    Student(unsigned nCourses);      // hàm tạo (constructor)
    void attendLecture();            // hành vi
    void selfStudy();                // hành vi
    void play();                     // hành vi
};
```

Điều này minh họa:
- Dữ liệu `private` (được đóng gói — người ngoài không thể chạm trực tiếp vào `age`)
- Giao diện `public` (ba phương thức + hàm tạo có thể gọi từ bên ngoài)
- Hàm tạo (constructor) với tham số (khởi tạo tại thời điểm tạo)
- Mỗi đối tượng `Student` có `numCoursesRequired` và `age` riêng

> [!success]- Show Answer — Dò tìm: điều gì xảy ra khi chúng ta viết `Student s(5); s.attendLecture();`?
> > 1. Hàm tạo `Student(5)` cấp phát bộ nhớ (Body) với Oid, Cid=Student.
> > 2. `numCoursesRequired` được đặt thành 5, `age` chưa được khởi tạo (hoặc được gán giá trị mặc định).
> > 3. `s.attendLecture()` gửi một thông điệp đến đối tượng `s`.
> > 4. Phương thức được tìm thấy thông qua Cid → `Student::attendLecture()` được thực thi.
> > 5. Phương thức chỉ sửa đổi Body của `s` — các đối tượng Student khác không bị ảnh hưởng.

---

## 7. SIÊU LỚP (META-CLASSES)

### 7.1 Siêu lớp (Meta-class) Là Gì?

Một **siêu lớp (meta-class)** là lớp của một lớp. Nếu bạn coi bản thân một lớp như một đối tượng, thì: đối tượng đó thuộc về lớp nào? Câu trả lời là một **siêu lớp (meta-class)**.

```
Cấp thông thường:   đối tượng → thể hiện của →  lớp
Cấp siêu:           lớp      → thể hiện của →  siêu lớp
```

- Một siêu lớp định nghĩa **cấu trúc và hành vi của các lớp**
- Cũng giống như một lớp định nghĩa các thể hiện của nó trông như thế nào, một siêu lớp định nghĩa các lớp trông như thế nào

### 7.2 Mục đích và Thuộc tính

| Mục đích / Thuộc tính | Giải thích |
|---|---|
| **Thuộc tính cấp lớp (Class-level attributes)** | Các thuộc tính của siêu lớp có thể mô tả bản thân lớp (ví dụ: số lượng thể hiện của một lớp, tác giả, phiên bản, ngày tạo) |
| **Xử lý đồng nhất (Uniform treatment)** | Trong các ngôn ngữ có hỗ trợ siêu lớp rõ ràng, các đối tượng, lớp VÀ siêu lớp đều được xử lý đồng nhất — tất cả đều là đối tượng |
| **Tạo lớp tại thời điểm chạy (Run-time class creation)** | Các lớp có thể được tạo ra tại thời điểm chạy bằng cách gửi thông điệp đến một siêu lớp đặc biệt (ví dụ: `MetaClass.new("MyNewClass")`) |
| **Phản chiếu (Reflection)** | Siêu lớp cho phép phản chiếu — một chương trình có thể kiểm tra và sửa đổi cấu trúc của chính nó tại thời điểm chạy |

> [!success]- Show Answer — C++ có siêu lớp (meta-classes) không?
> > **Không.** C++ không có siêu lớp như một tính năng ngôn ngữ. Không có cách tích hợp sẵn để coi một lớp như một đối tượng runtime, không có thuộc tính cấp lớp (ngoài các thành viên `static`, là dữ liệu trên mỗi lớp, không phải một siêu đối tượng bên ngoài), và không có cách tạo lớp mới tại thời điểm chạy. Tài liệu bài giảng này mang tính lý thuyết — nó sẽ không xuất hiện dưới dạng cú pháp C++ trong bài kiểm tra, nhưng hiểu được khái niệm giúp bạn nắm bắt được những gì các ngôn ngữ như Smalltalk, Python (với metaclasses) và Ruby cung cấp.

> [!success]- Show Answer — Nếu C++ không có siêu lớp, tại sao lại học về chúng?
> > Bởi vì khái niệm này hoàn thiện bậc thang trừu tượng hóa: đối tượng → lớp → siêu lớp. Nó cho thấy các lớp không phải là từ cuối cùng trong lý thuyết OOP. Nó cũng giải thích tại sao, trong một số ngôn ngữ, bạn CÓ THỂ hỏi một lớp "bạn có bao nhiêu thể hiện?" hoặc tạo ra các lớp mới bằng lập trình. Hiểu được trần của sự trừu tượng hóa giúp bạn hiểu được nền của nó.

---

## 8. KHUÔN MẪU CÚ PHÁP PHẢI HỌC THUỘC

```cpp
class ClassName {                    // Định nghĩa khuôn mẫu/bản thiết kế
private:                             // Trạng thái: các thành phần dữ liệu (mỗi đối tượng)
    int attribute1;                  // Mỗi ĐỐI TƯỢNG có bản sao riêng
    double attribute2;
public:                              // Hành vi: các hàm thành viên (được chia sẻ)
    ClassName(int a, double b);      // Constructor: tạo đối tượng mới
    void method1();                  // Người nhận thông điệp (mutator)
    int method2() const;             // const = sẽ không sửa đổi đối tượng (accessor)
};                                   // DẤU CHẤM PHẨY BẮT BUỘC — QUÊN CÁI NÀY = -2 điểm

// Tạo đối tượng (tạo thể hiện):
ClassName obj1(5, 3.14);                      // Tĩnh: trên stack, tự động hủy
ClassName *obj2 = new ClassName(10, 2.71);    // Động: trên heap, phải dùng delete

// Dọn dẹp:
delete obj2;    // xóa một đối tượng đơn
// obj1 tự động hủy khi ra khỏi phạm vi — không cần delete thủ công
```

> [!success]- Show Answer — Dấu chấm phẩy sau dấu ngoặc nhọn đóng của lớp
> > `class Foo { ... };` ← Dấu chấm phẩy đó KHÔNG phải là tùy chọn. Trong C++, một định nghĩa lớp là một khai báo (declaration), và các khai báo kết thúc bằng dấu chấm phẩy. Quên nó là một trong những lỗi biên dịch phổ biến nhất và là một khoản trừ điểm chắc chắn trên code viết tay.

> [!success]- Show Answer — Tĩnh vs. Động: tham chiếu cú pháp đầy đủ
> >
> > ```cpp
> > // TĨNH (stack)
> > ClassName obj;                 // hàm tạo mặc định
> > ClassName obj(args);           // hàm tạo có tham số
> > ClassName arr[10];             // mảng 10 phần tử, mỗi phần tử dùng hàm tạo mặc định
> >
> > // ĐỘNG (heap)
> > ClassName* p = new ClassName;          // một phần tử, hàm tạo mặc định
> > ClassName* p = new ClassName(args);    // một phần tử, hàm tạo có tham số
> > ClassName* arr = new ClassName[10];    // mảng 10 phần tử, mỗi phần tử hàm tạo mặc định
> >
> > // DỌN DẸP (chỉ heap — stack tự động hủy)
> > delete p;        // một đối tượng đơn
> > delete[] arr;    // mảng — GHÉP CẶP SAI = hành vi không xác định
> > ```

---

## 9. BẪY THI CỬ (EXAM TRAPS)

### 9.1 Tạo thể hiện Tĩnh vs. Động

- **Sai:** `ClassName obj = new ClassName();` (pha trộn khai báo stack với cấp phát heap)
- **Đúng:** `ClassName obj(args);` (tĩnh) hoặc `ClassName* obj = new ClassName(args);` (động)
- **Bẫy:** Tĩnh = trình biên dịch cấp phát trên stack, tự động hủy khi ra khỏi phạm vi. Động = heap, bạn phải tự `delete`.
- **Bẫy:** Quên `delete[]` cho mảng. `new ClassName[5]` phải đi cặp với `delete[] arr;` — KHÔNG phải `delete arr;`

### 9.2 Thành phần Dữ liệu Là Trên Mỗi Đối tượng, Hàm Là Được Chia Sẻ

- **Sai:** Tin rằng tất cả các đối tượng chia sẻ các thành phần dữ liệu. Chúng không. Mỗi đối tượng có `age`, `balance`, v.v. riêng.
- **Đúng:** Chỉ các hàm thành viên mới được chia sẻ (một bản sao trong bộ nhớ code). Các thành phần dữ liệu được sao chép riêng cho mỗi đối tượng.
- **Bẫy:** Một thành phần dữ liệu `static` THỰC SỰ được chia sẻ — nhưng đó là ngoại lệ, không phải quy tắc.

### 9.3 Các Mối Quan Hệ Lớp — KHÔNG THỂ Thay Thế Cho Nhau

- **"use-a" (Liên kết):** Một đối tượng gọi phương thức của đối tượng khác. `Driver` sử dụng `Car`. Không có quyền sở hữu, mối quan hệ tạm thời.
- **"has-a" (Hợp thành):** Một lớp chứa một lớp khác như một thành phần dữ liệu. `Car` có `Engine`. Có quyền sở hữu, vòng đời gắn kết.
- **"is-a" (Kế thừa):** Được đề cập trong Lec7/8. `Dog` là một `Animal`. KHÔNG giống use-a hay has-a.
- **Bẫy:** Các bài kiểm tra sẽ yêu cầu bạn phân loại một mối quan hệ. Nếu `Car` có một phương thức `void setEngine(Engine e)`, đó là use-a, không phải has-a — Engine được truyền vào, không được lưu trữ như một thành viên.

### 9.4 Thông điệp (Messages) = Lời gọi Phương thức (Method Calls)

- Trong lý thuyết OOP, "gửi một thông điệp" có nghĩa là gọi một phương thức. Nếu phương thức là private, thông điệp bị từ chối tại **thời điểm biên dịch (compile time)** trong C++.
- **Bẫy:** Viết `obj.privateMethod()` trong code mà đáng lẽ phải chạy được. Nếu nó là private, nó sẽ không biên dịch.

### 9.5 Định nghĩa Lớp CHÍNH LÀ Giao diện

- Chỉ các thành viên `public` mới tạo thành giao diện. Các thành viên private là chi tiết cài đặt — người ngoài không thể gọi chúng ngay cả khi họ biết tên.
- **Bẫy:** Liệt kê một phương thức private như một phần của "giao diện" trong một câu hỏi lý thuyết. Giao diện = chỉ các phương thức public.

### 9.6 Siêu lớp (Meta-class) Là Một Khái niệm Lý thuyết

- **Bẫy:** Cố gắng viết `class ClassName : public meta_class` — C++ không có siêu lớp như một tính năng ngôn ngữ. Bài giảng này mang tính khái niệm/lý thuyết.
- Các câu hỏi về siêu lớp trong bài kiểm tra sẽ mang tính định nghĩa: "Siêu lớp là gì?" "Tại sao một ngôn ngữ lại hỗ trợ chúng?" — không phải "Viết code C++ sử dụng siêu lớp."

### 9.7 Khái niệm Chủ Ý (Intentional) vs. Mở rộng (Extensional)

- **Bẫy:** Nhầm lẫn "các thể hiện có cấu trúc gì" (chủ ý) với "những thể hiện nào đang tồn tại ngay bây giờ" (mở rộng).
- **Bẫy:** Nghĩ rằng khái niệm mở rộng là không cần thiết. Nó là khái niệm đằng sau việc theo dõi thành viên `static` (đếm thể hiện), các nhà máy (factories) và bể đối tượng (object pools).

### 9.8 Tính đóng gói (Encapsulation) vs. Che giấu thông tin (Information Hiding)

- **Bẫy:** Sử dụng chúng như từ đồng nghĩa trong một bài kiểm tra. Tính đóng gói là cơ chế (gói gọn). Che giấu thông tin là nguyên tắc thiết kế (hạn chế truy cập). Bạn có thể có tính đóng gói mà không có che giấu thông tin.

### 9.9 Đối tượng (Objects) vs. ADT

- **Bẫy:** Nghĩ rằng Kiểu dữ liệu trừu tượng (Abstract Data Types) và đối tượng là các khái niệm khác nhau. Một lớp được thiết kế tốt LÀ một ADT — nó tạo ra một kiểu do người dùng định nghĩa hoạt động như một kiểu tích hợp sẵn. Các thuật ngữ có liên quan chặt chẽ trong OOP.

### 9.10 Phân loại (Classification) vs. Tạo thể hiện (Instantiation)

- **Bẫy:** Nói "Dog là một thể hiện của Animal." Điều này SAI. `Dog` IS-A (LÀ MỘT) `Animal` (phân loại/kế thừa). `Fido` IS-AN-INSTANCE-OF (LÀ MỘT THỂ HIỆN CỦA) `Dog` (tạo thể hiện). Phân loại liên quan các lớp với các siêu lớp; tạo thể hiện liên quan các đối tượng với các lớp.

---

## 10. BÀI TẬP VIẾT CODE (HAND-CODING DRILLS)

### Bài tập 1: Lớp từ Mô tả

Một máy nghe nhạc kỹ thuật số theo dõi các bài hát. Mỗi bài hát có tiêu đề, tên nghệ sĩ và thời lượng tính bằng giây. Người dùng có thể phát một bài hát (in ra "Playing [title] by [artist]"), lấy tiêu đề và lấy thời lượng. Viết định nghĩa lớp đầy đủ với dữ liệu private và giao diện public.

> [!success]- Show Answer
> > ```cpp
> > class Song {
> > private:
> >     char title[100];
> >     char artist[100];
> >     int duration; // in seconds
> > public:
> >     Song(const char t[], const char a[], int d) {
> >         int i = 0;
> >         while (t[i]) { title[i] = t[i]; i++; }
> >         title[i] = '\0';
> >         i = 0;
> >         while (a[i]) { artist[i] = a[i]; i++; }
> >         artist[i] = '\0';
> >         duration = d;
> >     }
> >     void play() {
> >         cout << "Playing " << title << " by " << artist << endl;
> >     }
> >     const char* getTitle() const { return title; }
> >     int getDuration() const { return duration; }
> > };
> > ```

> [!success]- Show Answer — Kiểm tra Khái niệm Bài tập 1
> > - Những thành viên nào tạo thành **giao diện (interface)**? `Song()`, `play()`, `getTitle()`, `getDuration()` — tất cả các thành viên public.
> > - Những thành viên nào tạo thành **trạng thái (state)**? `title`, `artist`, `duration` — tất cả dữ liệu private.
> > - Lớp này có thể hiện **tính đóng gói (encapsulation)** không? Có — dữ liệu và phương thức được gói gọn cùng nhau.
> > - Nó có thể hiện **che giấu thông tin (information hiding)** không? Có — người gọi không thể truy cập trực tiếp `title`/`artist`/`duration`; họ phải sử dụng các accessor.
> > - Đây có phải là một đối tượng ảo không? Có — một Song trong máy nghe nhạc là một cấu trúc chương trình, không phải một vật thể vật lý.
> > - `Song` có sáu thuộc tính đối tượng (Mục 2.2) không? Tự trị (có hành vi riêng), Giao tiếp (phản hồi thông điệp), Lồng ghép (có thể chứa các đối tượng khác), Có định danh (mỗi đối tượng Song là riêng biệt), Được tạo/Bị hủy (hàm tạo/hàm hủy), Hợp tác (có thể tương tác với các đối tượng Playlist).

### Bài tập 2: Các Phong cách Tạo thể hiện

Cho `class Widget { public: Widget(); Widget(int x); };`, viết code tạo ra:
(a) Một Widget đơn với hàm tạo mặc định trên stack
(b) Một mảng 5 Widget mặc định trên heap
(c) Một Widget đơn với tham số 42 trên heap
Sau đó, viết các câu lệnh `delete` cần thiết để dọn dẹp (b) và (c).

> [!success]- Show Answer
> > ```cpp
> > Widget w1;                        // (a) stack, hàm tạo mặc định
> > Widget* arr = new Widget[5];      // (b) heap array, 5x hàm tạo mặc định
> > Widget* w2 = new Widget(42);      // (c) heap, hàm tạo có tham số
> >
> > delete[] arr;  // xóa mảng cho (b)
> > delete w2;     // xóa đơn cho (c)
> > // w1 tự động hủy khi ra khỏi phạm vi
> > ```

> [!success]- Show Answer — Kiểm tra Khái niệm Bài tập 2
> > - Cái nào là tạo thể hiện tĩnh (static instantiation)? (a). Trình biên dịch cấp phát trên stack tại thời điểm biên dịch.
> > - Cái nào là tạo thể hiện động (dynamic instantiation)? (b) và (c). `new` cấp phát trên heap tại thời điểm chạy.
> > - Điều gì xảy ra nếu bạn viết `delete arr;` thay vì `delete[] arr;`? Hành vi không xác định — chỉ có hàm hủy của phần tử đầu tiên được chạy. Luôn ghép `new[]` với `delete[]`.
> > - Tại sao (a) không cần `delete`? Nó ở trên stack — tự động bị hủy khi khối chứa nó kết thúc (thoát khỏi phạm vi - scope exit).

### Bài tập 3: Phân loại (Classification) vs. Tạo thể hiện (Instantiation)

Giải thích sự khác biệt giữa "khái niệm chủ ý (intentional notion)" và "khái niệm mở rộng (extensional notion)" của một lớp từ bài giảng. Sau đó, minh họa cả hai bằng cách viết một lớp `Library`:
- Chủ ý: định nghĩa một thư viện là gì (kệ sách, sách, tên)
- Mở rộng: duy trì một bộ đếm có bao nhiêu đối tượng Library tồn tại

> [!success]- Show Answer
> > **Khái niệm chủ ý (Intentional notion)** = lớp như một khuôn mẫu định nghĩa CẤU TRÚC (các thể hiện sẽ có dữ liệu và phương thức gì). Nó là bản thiết kế.
> > **Khái niệm mở rộng (Extensional notion)** = lớp như một nhà kho/nhà máy THEO DÕI tất cả các thể hiện của nó. Nó biết những đối tượng nào đã được tạo ra.
> >
> > ```cpp
> > class Library {
> > private:
> >     int numShelves;
> >     int numBooks;
> >     char name[50];
> >     static int totalLibraries;  // mở rộng: theo dõi tất cả các thể hiện
> > public:
> >     Library(const char n[], int shelves, int books) {
> >         int i = 0;
> >         while (n[i]) { name[i] = n[i]; i++; }
> >         name[i] = '\0';
> >         numShelves = shelves;
> >         numBooks = books;
> >         totalLibraries++;        // mỗi đối tượng mới tăng bộ đếm
> >     }
> >     ~Library() { totalLibraries--; }
> >     static int getTotalLibraries() { return totalLibraries; }
> > };
> > int Library::totalLibraries = 0;
> > ```

> [!success]- Show Answer — Kiểm tra Khái niệm Bài tập 3
> > - Phần nào là chủ ý (intentional)? Các thành phần dữ liệu private (`numShelves`, `numBooks`, `name`) và các phương thức public — chúng định nghĩa mọi Library trông như thế nào.
> > - Phần nào là mở rộng (extensional)? `totalLibraries` và `getTotalLibraries()` — chúng theo dõi tập hợp tất cả các thể hiện Library.
> > - `static int totalLibraries` có thuộc về bất kỳ đối tượng cụ thể nào không? Không — nó thuộc về bản thân lớp (khái niệm mở rộng). Nó là một biến được chia sẻ, không phải trên mỗi thể hiện.
> > - Điều này liên quan thế nào đến siêu lớp (meta-classes) (Mục 7)? Một siêu lớp thực sự sẽ làm cho `totalLibraries` trở thành một thuộc tính của lớp-như-đối-tượng. Trong C++, các thành viên `static` là một giải pháp thay thế một phần — chúng cung cấp dữ liệu cấp lớp nhưng không có hỗ trợ siêu lớp thực sự.

### Bài tập 4: Xác định Giao diện

Cho lớp `Student` từ Mục 6.5, hãy xác định:
(a) Trạng thái (các thành phần dữ liệu)
(b) Giao diện (những gì người ngoài có thể gọi)
(c) Đối tượng `Student` phản hồi những thông điệp nào

> [!success]- Show Answer
> > (a) **Trạng thái (State):** `numCoursesRequired` và `age` (cả hai đều `private unsigned`).
> > (b) **Giao diện (Interface):** `Student(unsigned nCourses)`, `attendLecture()`, `selfStudy()`, `play()`.
> > (c) **Thông điệp (Messages):** `attendLecture`, `selfStudy`, `play` — cộng với thông điệp hàm tạo tại thời điểm tạo.
> >
> > Lưu ý: `age` và `numCoursesRequired` KHÔNG phải là một phần của giao diện — chúng là private. Người ngoài không thể gửi thông điệp "đọc age" hay "ghi age" trừ khi một getter/setter public được thêm vào.

### Bài tập 5: Phân loại Mối quan hệ

Với mỗi cặp dưới đây, hãy xác định mối quan hệ là "use-a" (liên kết), "has-a" (hợp thành) hay "is-a" (kế thừa — xem trước):
(a) Một `Student` đăng ký một `Course`. Đối tượng `Student` gọi `course.enroll(this)`.
(b) Một lớp `Car` có một thành phần dữ liệu kiểu `Engine`.
(c) Một lớp `Library` lưu trữ một mảng các đối tượng `Book` như một thành viên.
(d) Một lớp `Person` có một phương thức nhận tham số `Phone` và gọi `phone.dial(number)`.

> [!success]- Show Answer
> > (a) **use-a** — Student gửi thông điệp đến Course, không có quyền sở hữu, tương tác tạm thời.
> > (b) **has-a** — Engine là thành phần dữ liệu của Car (hợp thành). Nó là một phần của Car.
> > (c) **has-a** — Mảng Book là một thành phần dữ liệu. Library chứa các Book.
> > (d) **use-a** — Phone được truyền vào như một tham số, không được lưu trữ như một thành viên. Person sử dụng Phone tạm thời.

### Bài tập 6: Xác định Đối tượng Thế giới Thực

Với mỗi mục sau, hãy xác định thuộc tính nào trong sáu thuộc tính của đối tượng thế giới thực (Mục 2.2) được áp dụng:
(a) Một hệ thống đăng ký khóa học của trường đại học
(b) Một máy ATM ngân hàng
(c) Một đối tượng `Payment` trong hệ thống thương mại điện tử

> [!success]- Show Answer
> > (a) **Hệ thống Đăng ký Khóa học:**
> > - Chủ động/tự trị: xử lý đăng ký một cách độc lập
> > - Giao tiếp: tương tác với các đối tượng Student, Course
> > - Hợp tác: duy trì mối quan hệ giữa sinh viên và khóa học
> > - Lồng ghép: chứa các đối tượng Student, Course, Registration
> > - Có định danh: có ID học kỳ duy nhất
> > - Được tạo/Bị hủy: được tạo thể hiện cho mỗi học kỳ
> >
> > (b) **Máy ATM:**
> > - Chủ động/tự trị: xác thực thẻ, phân phát tiền mặt một cách độc lập
> > - Giao tiếp: nói chuyện với máy chủ ngân hàng, tương tác với khách hàng
> > - Hợp tác: một phần của mạng lưới ngân hàng
> > - Lồng ghép: chứa đầu đọc thẻ, máy phân phát tiền, các thành phần màn hình
> > - Có định danh: có ID thiết bị đầu cuối duy nhất
> > - Được tạo/Bị hủy: được lắp đặt và ngừng hoạt động
> >
> > (c) **Thanh toán (Payment):**
> > - Chủ động/tự trị: xác thực số tiền, xử lý giao dịch
> > - Giao tiếp: tương tác với các đối tượng Account, Order
> > - Hợp tác: một phần của giao dịch giữa người mua và người bán
> > - Lồng ghép: chứa chi tiết giao dịch, dấu thời gian
> > - Có định danh: có ID giao dịch duy nhất
> > - Được tạo/Bị hủy: được tạo ra khi thanh toán xảy ra, không thể "hoàn tác" (hoàn tiền tạo ra một Payment mới)

### Bài tập 7: OOP vs. Thủ tục Set

Viết lại các thao tác Set theo phong cách thủ tục sau đây theo phong cách OOP. Xác định điều gì thay đổi về việc ai là chủ động so với thụ động:

```
// Procedural (Thủ tục)
Set mySet;
add(mySet, 5);
add(mySet, 10);
int count = size(mySet);
bool found = contains(mySet, 5);
remove(mySet, 10);
```

> [!success]- Show Answer
> > ```cpp
> > // OOP Style
> > Set mySet;
> > mySet.add(5);
> > mySet.add(10);
> > int count = mySet.size();
> > bool found = mySet.contains(5);
> > mySet.remove(10);
> > ```
> >
> > **Điều gì đã thay đổi:** Trong phong cách thủ tục, Set là một cấu trúc dữ liệu thụ động — các hàm thao tác TRÊN nó. Trong phong cách OOP, Set là một đối tượng chủ động — nó nhận các thông điệp và phản hồi. Set bây giờ là tác nhân; các hàm bây giờ là các phương thức thuộc sở hữu của Set. Đây là sự chuyển đổi cơ bản từ tư duy thủ tục sang hướng đối tượng: **đối tượng là chủ động, không phải thụ động.**
