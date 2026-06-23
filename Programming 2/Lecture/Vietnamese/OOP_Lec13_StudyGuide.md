# Lec13: Thiết kế hướng đối tượng (Object-Oriented Design) — Hướng dẫn học tập

---

## 1. THẺ KHÁI NIỆM: THIẾT KẾ HƯỚNG ĐỐI TƯỢNG (OBJECT-ORIENTED DESIGN)

### 1.1 Định nghĩa

Thiết kế hướng đối tượng (OOD - Object-Oriented Design) là quá trình lập kế hoạch một hệ thống phần mềm dưới dạng tập hợp các **đối tượng (objects)** tương tác với nhau để giải quyết một vấn đề. Nó bao gồm việc xác định các lớp (classes), trách nhiệm của chúng và các mối quan hệ (relationships) giữa chúng. OOD là cầu nối giữa **phân tích yêu cầu (requirements analysis)** (hệ thống nên làm gì) và **cài đặt (implementation)** (viết mã).

### 1.2 Vấn đề Nó Giải Quyết

Nếu không có thiết kế có hệ thống, phần mềm sẽ trở nên:
- **Khó hiểu** — không có kiến trúc rõ ràng.
- **Khó sửa đổi** — các thay đổi lan truyền không thể dự đoán.
- **Khó mở rộng** — tính năng mới đòi hỏi viết lại phần lớn mã nguồn.
- **Khó bảo trì** — lỗi khó cô lập.

OOD tạo ra phần mềm có **cấu trúc nội tại rõ ràng**, dễ kiểm thử, di chuyển, bảo trì, mở rộng và hiểu hơn.

### 1.3 Cách Hoạt Động

Quá trình thiết kế tuân theo các bước có cấu trúc:
1. **Tìm lớp (classes)** — danh từ (nouns) trong mô tả vấn đề.
2. **Xác định thao tác (operations)** — động từ (verbs) — mỗi lớp có thể làm gì.
3. **Xác định phụ thuộc (dependencies)** — kế thừa (inheritance) và mối quan hệ sử dụng (use relationships).
4. **Xác định giao diện (interfaces)** — public so với protected, kiểu dữ liệu chính xác.
5. **Tổ chức lại (reorganize)** hệ thống phân cấp khi cần (thêm lớp cơ sở chung, tách lớp).
6. **Mô hình hóa trực quan** bằng biểu đồ UML (Unified Modeling Language).

### 1.4 Chiến Lược Tổng Thể — Chia để Trị (Divide and Conquer)

Hệ thống được chia thành các **mô-đun (modules)** (các đối tượng và lớp). Thách thức là đảm bảo **giao tiếp hiệu quả** giữa các phần khác nhau của phần mềm **mà không phá vỡ sự phân chia** (tức là duy trì khớp nối lỏng lẻo (loose coupling)).

### 1.5 Nó KHÔNG Phải Là Gì

- OOD **KHÔNG phải** là viết mã — nó là giai đoạn thiết kế trước khi cài đặt.
- OOD **KHÔNG phải** chỉ là vẽ sơ đồ — nó là đưa ra các quyết định có chủ đích về cấu trúc lớp và mối quan hệ.
- OOD **KHÔNG phải** là hoạt động một lần — thiết kế tiến hóa theo vòng lặp.

---

## 2. VÒNG ĐỜI PHÁT TRIỂN PHẦN MỀM (SOFTWARE DEVELOPMENT CYCLE)

### 2.1 Các Giai Đoạn

| Giai đoạn | Mô tả |
|-------|-------------|
| **Phân tích vấn đề (Problem Analysis)** | Hiểu người dùng cần gì |
| **Thiết kế giải pháp (Solution Design)** | Lập kế hoạch kiến trúc (lớp, mối quan hệ) |
| **Viết mã (Coding)** | Cài đặt thiết kế |
| **Tài liệu hóa (Documenting)** | Ghi lại quyết định, giao diện, cách sử dụng |
| **Kiểm thử (Testing)** | Xác minh tính đúng đắn |
| **Bảo trì (Maintenance)** | Sửa lỗi, thích ứng với yêu cầu mới |

### 2.2 Thực hành Tốt nhất (Công nghệ Hướng đối tượng Giúp Như Thế Nào)

1. **Phát triển theo vòng lặp (Develop iteratively)** — chấp nhận yêu cầu thay đổi, tích hợp các phần tử dần dần, tạo điều kiện tái sử dụng.
2. **Sử dụng kiến trúc dựa trên thành phần (Use component-based architectures)** — thiết kế với các thành phần có thể tái sử dụng.
3. **Mô hình hóa trực quan (Model visually)** — sử dụng UML để dễ hiểu và dễ sửa đổi.

---

## 3. TẠI SAO CẤU TRÚC NỘI TẠI RÕ RÀNG LẠI QUAN TRỌNG

Một hệ thống được thiết kế tốt giúp đơn giản hóa:

| Khía cạnh | Cấu trúc Rõ ràng Giúp Như Thế Nào |
|---------|--------------------------|
| **Kiểm thử (Testing)** | Các đơn vị độc lập có thể được kiểm thử riêng rẽ |
| **Di chuyển (Porting)** | Mã phụ thuộc nền tảng được đóng gói |
| **Bảo trì (Maintenance)** | Lỗi được giới hạn trong các lớp cụ thể |
| **Mở rộng (Extension)** | Có thể thêm lớp mới mà không sửa mã hiện có (Nguyên lý đóng-mở - Open-Closed Principle) |
| **Tái tổ chức (Re-organization)** | Các thành phần có thể được sắp xếp lại với tác động tối thiểu |
| **Hiểu (Understanding)** | Ranh giới và trách nhiệm lớp rõ ràng |

### 3.1 Đặc điểm của Phần mềm Thành công

Phần mềm thành công có **vòng đời kéo dài** và có thể:
- Được làm việc bởi **nhiều thế hệ lập trình viên và nhà thiết kế**.
- Được **di chuyển (ported)** sang phần cứng mới.
- Được **thích ứng (adapted)** cho các mục đích sử dụng không lường trước.

---

## 4. CÁC BƯỚC THIẾT KẾ HƯỚNG ĐỐI TƯỢNG (OO DESIGN STEPS)

### 4.1 Bước 1 — Tìm Khái niệm / Lớp (Find the Concepts / Classes)

Nhìn vào **ứng dụng (application)** thay vì các khái niệm trừu tượng. **Danh từ (nouns)** trong mô tả vấn đề thường tương ứng với **lớp (classes)**. **Động từ (verbs)** đại diện cho **hàm (functions)** (thao tác).

### 4.2 Bước 2 — Tinh chỉnh Lớp bằng Cách Xác định Thao tác (Refine Classes by Specifying Operations)

Phân loại thao tác thành các nhóm:
- **Nền tảng (Foundation)**: Hàm tạo (constructors), hàm hủy (destructors), toán tử sao chép (copy operators).
- **Bộ chọn (Selectors)**: Thao tác KHÔNG thay đổi trạng thái của đối tượng (hàm const).
- **Bộ sửa đổi (Modifiers)**: Thao tác CÓ thay đổi trạng thái của đối tượng.
- **Toán tử chuyển đổi (Conversion Operators)**: Tạo ra đối tượng kiểu khác dựa trên trạng thái của đối tượng.
- **Bộ duyệt (Iterators)**: Duyệt qua các bộ sưu tập đối tượng để xử lý thành phần dữ liệu.

Cân nhắc:
- **Tối giản (Minimalism)**: Chỉ bao gồm các thao tác thiết yếu.
- **Đầy đủ (Completeness)**: Cung cấp tất cả thao tác người dùng hợp lý cần.
- **Tiện lợi (Convenience)**: Thêm thao tác cải thiện khả năng sử dụng (nhưng không làm phình to giao diện).
- Thao tác nào nên là **virtual**.

### 4.3 Bước 3 — Xác định Phụ thuộc vào Các Lớp Khác (Specify Dependencies on Other Classes)

Các loại phụ thuộc chính:

| Phụ thuộc (Dependency) | Mô tả |
|------------|-------------|
| **Kế thừa (Inheritance)** | Mối quan hệ "is-a" — lớp dẫn xuất phụ thuộc vào lớp cơ sở |
| **Sử dụng / Hợp thành (Use / Composition)** | Mối quan hệ "has-a" — một lớp sử dụng hoặc chứa một lớp khác |

**Cảnh báo**: Lạm dụng phụ thuộc dẫn đến thiết kế kém hiệu quả và khó hiểu. Giữ khớp nối lỏng lẻo (loose coupling).

### 4.4 Bước 4 — Xác định Giao diện (Specify Interfaces)

- Hàm private **không được xem xét** ở giai đoạn này (chi tiết cài đặt).
- Giao diện nên **có thể cài đặt độc lập** — có thể có nhiều hơn một cách cài đặt.
- Tất cả thao tác trong một lớp nên hỗ trợ **cùng mức độ trừu tượng**.
- Phân tách hàm thành **public** và **protected**:
  - `public` — có sẵn cho tất cả người dùng của lớp.
  - `protected` — chỉ có sẵn cho các lớp dẫn xuất.

### 4.5 Bước 5 — Tổ chức lại Hệ thống Phân cấp Lớp (Reorganize the Class Hierarchy)

Hai cách tổ chức lại phổ biến nhất:

| Tổ chức lại (Reorganization) | Khi nào sử dụng |
|----------------|-------------|
| **Thêm lớp cơ sở chung (Introduce a common base)** | Hai lớp chia sẻ chức năng đáng kể — trích xuất các thành phần dùng chung vào lớp cơ sở mới |
| **Tách một lớp (Split a class)** | Một lớp có quá nhiều trách nhiệm (vi phạm Nguyên lý Đơn trách nhiệm - Single Responsibility Principle) — chia thành hai hay nhiều lớp |

---

## 5. TÌM LỚP — KỸ THUẬT DANH TỪ / ĐỘNG TỪ (NOUN/VERB TECHNIQUE)

### 5.1 Phương pháp

1. Lấy mô tả vấn đề / tài liệu yêu cầu.
2. Gạch chân **danh từ (nouns)** — đây là các **lớp (classes)** ứng viên.
3. Gạch chân **động từ (verbs)** — đây là các **thao tác (operations)** ứng viên (hàm thành viên).

### 5.2 Ví dụ Có Lời Giải — Hàng tồn kho Cửa hàng Băng video (Video Store Inventory)

**Mô tả vấn đề:**

> Khi đặt hàng băng video mới từ nhà cung cấp, quản lý cửa hàng tạo một đơn đặt hàng (purchase order), điền ngày tháng, tên và địa chỉ nhà cung cấp, và nhập danh sách các băng video cần đặt. Đơn đặt hàng được thêm vào danh sách mua hàng vĩnh viễn. Khi một hoặc nhiều băng video được nhận từ nhà cung cấp, nhân viên kho xác định đơn đặt hàng gốc và ghi lại mỗi băng đã nhận. Bản ghi của băng video sau đó được thêm vào hàng tồn kho của cửa hàng. Khi tất cả băng được liệt kê trong một đơn đặt hàng cụ thể đã được nhận, quản lý gửi thanh toán cho nhà cung cấp và đơn đặt hàng được đánh dấu ngày hoàn thành.

**Các lớp ứng viên (danh từ):**
- **Videotape** — đại diện cho một tựa đầu băng / mặt hàng cụ thể
- **Supplier** — tên, địa chỉ
- **PurchaseOrder** — ngày tháng, nhà cung cấp, danh sách băng, ngày hoàn thành
- **List of Purchases** — bộ sưu tập các đơn đặt hàng (danh sách vĩnh viễn)
- **Inventory** — hàng tồn kho hiện tại của cửa hàng
- **Payment** — thanh toán cho nhà cung cấp
- **Store Manager** — tác nhân (có thể là một lớp hoặc chỉ là một cấp quyền)
- **Clerk** — tác nhân

**Các thao tác ứng viên (động từ):**

| Động từ (Verb) | Lớp Khả năng (Likely Class) | Thao tác (Operation) |
|------|-------------|-----------|
| creates | (Manager) | `createPurchaseOrder()` |
| fills in | PurchaseOrder | `setDate()`, `setSupplier()` |
| enters | PurchaseOrder | `addTape()` |
| added to | List of Purchases | `add()` |
| received | Inventory | `receive()` |
| locates | List of Purchases | `find()` |
| makes a record | PurchaseOrder | `recordReceipt()` |
| added to | Inventory | `addTape()` |
| sends a payment | (Manager) | `sendPayment()` |
| given a completion date | PurchaseOrder | `setCompletionDate()` |

---

## 6. VÍ DỤ CÓ LỜI GIẢI — LỊCH HẸN PHÒNG KHÁM BÁC SĨ (DOCTOR'S OFFICE SCHEDULING)

### 6.1 Đặc tả

- Cho phép đặt lịch hẹn cho bệnh nhân.
- Nhiều bác sĩ, mỗi người có lịch hàng ngày chia thành **các khe 15 phút** từ 8:00 sáng đến 6:00 chiều.
- In lịch hàng ngày riêng cho từng bác sĩ (thời gian + tên bệnh nhân).
- Đầu ra ra **màn hình** (ngoại trừ lịch → tệp tin).
- Để đơn giản: mỗi bác sĩ chỉ có **một ngày hẹn duy nhất**.

### 6.2 Tìm Lớp

Từ đặc tả, các lớp ứng viên:
- **Doctor** — có lịch hàng ngày
- **Patient** — có tên, có thể đặt lịch hẹn
- **DailySchedule** — bộ sưu tập các khe thời gian cho một bác sĩ
- **Appointment** — một lượt đặt cụ thể (bác sĩ + bệnh nhân + thời gian)
- **Scheduler** — giao diện với người dùng (điều phối quy trình)

### 6.3 Kịch bản (Use Cases)

1. Scheduler yêu cầu tên bệnh nhân.
2. Bệnh nhân chọn bác sĩ.
3. Scheduler hiển thị lịch của bác sĩ (các khe trống).
4. Bệnh nhân yêu cầu một khe cụ thể.
5. Scheduler thêm cuộc hẹn vào lịch của bác sĩ và vào hồ sơ bệnh nhân.
6. Scheduler xác nhận cuộc hẹn.

### 6.4 Phụ thuộc Lớp (Class Dependencies)

```
Scheduler ────uses────> Patient
    │                      │
    │ uses                 │ uses
    ↓                      ↓
  Doctor ──contains──> DailySchedule ──contains──> Appointment
```

- **Hợp thành (Composition — contains)**: Doctor HAS A DailySchedule. DailySchedule HAS Appointments.
- **Sử dụng/Liên kết (Use/Link)**: Scheduler sử dụng Patient và Doctor. Patient sử dụng Doctor.

### 6.5 Các Thao tác

**Doctor:**

| Thao tác (Operation) | Mô tả |
|-----------|-------------|
| `addToSchedule` | Thêm cuộc hẹn vào lịch của bác sĩ |
| `showAppointment` | Hiển thị lịch |

**Patient:**

| Thao tác (Operation) | Mô tả |
|-----------|-------------|
| `inputName` | Nhập tên bệnh nhân |
| `chooseDoctor` | Chọn bác sĩ |
| `chooseTimeSlot` | Chọn khe thời gian trống |
| `setAppointment` | Đặt lịch hẹn |

**DailySchedule:**

| Thao tác (Operation) | Mô tả |
|-----------|-------------|
| `setAppointment` | Thêm cuộc hẹn vào lịch |
| `isTimeSlotFree` | Kiểm tra xem một khe cụ thể có trống không |
| `showAppointments` | Hiển thị các cuộc hẹn đã lên lịch |

**Appointment:**

| Thao tác (Operation) | Mô tả |
| ------------- | --------------------------------- |
| Hàm tạo (Constructor) | Tạo một cuộc hẹn |
| `isScheduled` | Kiểm tra xem cuộc hẹn đã được đặt chưa |

**Scheduler:**

| Thao tác (Operation) | Mô tả |
| ------------------------ | ------------------------------------------------ |
| `scheduleOneAppointment` | Điều phối quy trình đặt lịch |
| `printAllAppointment` | In tất cả các cuộc hẹn đã lên lịch cho tất cả bác sĩ |

### 6.6 Các Lớp Trợ giúp Bổ sung

- **TimeSlot** — xử lý chuyển đổi và định dạng thời gian hẹn.
- **string** — cho các thành phần dữ liệu dạng chuỗi (tên bệnh nhân, v.v.).

---

## 7. VÒNG LẶP PHÁT TRIỂN (THE DEVELOPMENT CYCLE — ITERATIVE PROCESS)

```
Tạo thiết kế tổng thể
    → Tìm thành phần chuẩn → tùy chỉnh cho thiết kế này
    → Tạo thành phần chuẩn mới → tùy chỉnh cho thiết kế này
    → Lắp ráp thiết kế
    → (lặp lại)
```

**Thiết kế cho sự thay đổi**: Hệ thống phải duy trì đơn giản nhất có thể dưới một chuỗi các thay đổi. Hướng tới:
- **Linh hoạt (Flexibility)** — dễ dàng sửa đổi hành vi.
- **Khả năng mở rộng (Extensibility)** — dễ dàng thêm tính năng mới.
- **Khả năng di chuyển (Portability)** — dễ dàng chuyển sang nền tảng mới.

---

## 8. BIỂU ĐỒ LỚP VÀ UML

### 8.1 UML Là Gì?

**Unified Modeling Language** — một ngôn ngữ trực quan để đặc tả, xây dựng và tài liệu hóa các hệ thống phần mềm. Nó cung cấp nhiều loại biểu đồ để **tất cả các bên liên quan** (nhà phân tích, nhà thiết kế, lập trình viên, kiểm thử, QA, khách hàng, tác giả kỹ thuật) đều có thể hưởng lợi từ ít nhất một biểu đồ UML.

### 8.2 Các Loại Biểu đồ UML

| Biểu đồ (Diagram) | Mục đích |
|---------|---------|
| **Biểu đồ ca sử dụng (Use Case Diagram)** | Mô tả hành vi hệ thống từ góc nhìn người dùng; hỗ trợ phân tích yêu cầu |
| **Biểu đồ lớp (Class Diagram)** | Hiển thị các lớp, thuộc tính, thao tác và mối quan hệ; thiết yếu cho thiết kế OO |
| **Biểu đồ cộng tác (Collaboration Diagram)** | Hiển thị cách các đối tượng cộng tác (tương tác) để đạt được một nhiệm vụ |
| **Biểu đồ tuần tự (Sequence Diagram)** | Tương tự biểu đồ cộng tác nhưng hiển thị **thứ tự thời gian** (đường chấm = dòng thời gian) |

### 8.3 Biểu diễn Đối tượng

Một đối tượng được biểu diễn dưới dạng **hình chữ nhật có tên được gạch chân**:
```
┌──────────────────┐       ┌──────────────────┐
│   Kenji: Professor│       │   : Professor    │
└──────────────────┘       └──────────────────┘
  Đối tượng có tên           Đối tượng không tên
  (Named Object)              (Unnamed Object)
```

### 8.4 Biểu diễn Lớp

Một lớp được biểu diễn dưới dạng **hình chữ nhật có các ngăn**:
```
┌──────────────────┐
│   ClassName      │  ← Tên lớp (Class name)
├──────────────────┤
│   attribute1     │  ← Thuộc tính (Attributes — thành phần dữ liệu)
│   attribute2     │
├──────────────────┤
│   operation1()   │  ← Thao tác (Operations — hàm thành viên)
│   operation2()   │
└──────────────────┘
```

### 8.5 Ký hiệu Mối quan hệ (Biểu đồ Lớp)

| Ký hiệu | Ý nghĩa |
|----------|---------|
| ◇─────── | **Chứa đựng/Hợp thành (Containment/Composition)** — một lớp duy trì các thể hiện của lớp khác (has-a) |
| ─────── | **Liên kết/Kết hợp (Link/Association)** — các đối tượng yêu cầu dịch vụ hoặc gửi thông điệp |
| △─────── | **Kế thừa (Inheritance)** — mối quan hệ "is-a" (tam giác chỉ vào lớp cơ sở) |

### 8.6 Số lượng (Cardinality / Multiplicity)

Xác định có bao nhiêu thể hiện tham gia vào một mối quan hệ:

| Ký hiệu | Ý nghĩa |
|----------|---------|
| `1` | Chính xác một |
| `n` hoặc `*` | Không hoặc nhiều |
| `0..n` hoặc `0..*` | Không hoặc nhiều |
| `1..n` hoặc `1..*` | Một hoặc nhiều |
| `10..30` | Khoảng: 10 đến 30 |
| `2..4, 8` | Khoảng hoặc số cụ thể |

Ví dụ: `Doctor 1 ────contains───> 1 DailySchedule` (mỗi bác sĩ có chính xác một lịch hàng ngày, mỗi lịch hàng ngày thuộc về chính xác một bác sĩ).

---

## 9. TẠO MẪU, THỬ NGHIỆM VÀ PHÂN TÍCH (PROTOTYPING, EXPERIMENTATION, AND ANALYSIS)

- **Tạo mẫu (Prototyping)** thường được sử dụng để thử nghiệm các thiết kế trước khi cam kết.
- Các khía cạnh khác nhau của hệ thống có thể được tạo mẫu độc lập (ví dụ: GUI, lớp dữ liệu).
- **Phân tích (Analysis)** một thiết kế và/hoặc cài đặt cung cấp hiểu biết sâu sắc quan trọng — hãy xem xét thiết kế của bạn trước và trong khi cài đặt.

---

## 10. BẢO TRÌ VÀ TÁI SỬ DỤNG (MAINTENANCE AND RE-USE)

### 10.1 Bảo trì Phần mềm

Bảo trì thường có nghĩa là **thiết kế lại và cài đặt lại**. Khi **tính linh hoạt, khả năng mở rộng và khả năng di chuyển** được nhấn mạnh trong thiết kế, các vấn đề bảo trì được giải quyết dễ dàng hơn.

Mô hình Hướng đối tượng thúc đẩy bảo trì vì:
- Sản phẩm bao gồm các **đơn vị độc lập** (các lớp).
- **Đóng gói (Encapsulation)** cung cấp sự độc lập về mặt khái niệm.
- **Che giấu thông tin (Information hiding)** cung cấp sự độc lập về mặt vật lý.
- **Truyền thông điệp (Message-passing)** là cơ chế giao tiếp duy nhất (các giao diện được kiểm soát).

### 10.2 Tái sử dụng Phần mềm

Tái sử dụng **mã nguồn** và **thiết kế** thường là lý do để chọn OOP.

Phần mềm có thể **tái sử dụng** nếu:
1. Nó **hoạt động** (đúng đắn, đáng tin cậy).
2. Nó **dễ hiểu** (được tài liệu hóa tốt, thiết kế sạch sẽ).
3. Nó có thể **cùng tồn tại** với các phần mềm khác không được viết để cùng tồn tại với nó (giao diện chuẩn).
4. Nó được **hỗ trợ** (được bảo trì, cập nhật).
5. Nó **kinh tế** (chi phí bảo trì thấp hơn xây dựng lại từ đầu).

Hướng đối tượng **hỗ trợ** tái sử dụng nhưng cần **công cụ và tiêu chuẩn** (thư viện, khung làm việc, mẫu thiết kế, UML).

---

## 11. TỔNG KẾT NGUYÊN LÝ THIẾT KẾ

| Nguyên lý | Ý nghĩa |
|-----------|---------|
| **Chia để Trị (Divide and Conquer)** | Chia hệ thống thành các mô-đun (đối tượng/lớp) |
| **Đóng gói (Encapsulation)** | Gói dữ liệu với thao tác; ẩn chi tiết nội tại |
| **Che giấu Thông tin (Information Hiding)** | Dữ liệu private, giao diện public |
| **Khớp nối Lỏng lẻo (Loose Coupling)** | Tối thiểu hóa phụ thuộc giữa các lớp |
| **Kết dính Cao (High Cohesion)** | Mỗi lớp có một trách nhiệm duy nhất, được xác định rõ |
| **Thiết kế cho Sự thay đổi (Design for Change)** | Tiên liệu các sửa đổi trong tương lai |
| **Phát triển Theo vòng lặp (Iterative Development)** | Thiết kế → tạo mẫu → tinh chỉnh → lặp lại |

---

## 12. KHUNG KIẾN THỨC BẮT BUỘC GHI NHỚ

### 12.1 Các Bước Thiết Kế OO (Theo Thứ Tự)

```
1. Tìm LỚP (CLASSES) — danh từ từ mô tả vấn đề
2. Xác định THAO TÁC (OPERATIONS) — động từ → hàm tạo, bộ chọn, bộ sửa đổi, bộ duyệt, chuyển đổi
3. Xác định PHỤ THUỘC (DEPENDENCIES) — kế thừa: is-a; sử dụng/hợp thành: has-a
4. Xác định GIAO DIỆN (INTERFACES) — public so với protected, kiểu chính xác
5. TỔ CHỨC LẠI hệ thống phân cấp (thêm lớp cơ sở chung, tách lớp)
```

### 12.2 Phân loại Thao tác

| Nhóm (Category) | Mô tả | Ví dụ |
|----------|-------------|---------|
| Nền tảng (Foundation) | Hàm tạo, hàm hủy, thao tác sao chép | `Doctor()`, `~Doctor()` |
| Bộ chọn (Selectors) | Không sửa đổi trạng thái (const) | `getSchedule() const` |
| Bộ sửa đổi (Modifiers) | Sửa đổi trạng thái | `addAppointment()` |
| Chuyển đổi (Conversion) | Tạo đối tượng kiểu khác | `toString()`, `toJson()` |
| Bộ duyệt (Iterators) | Duyệt qua bộ sưu tập | `getNextAppointment()` |

### 12.3 Các Loại Mối quan hệ trong Biểu đồ Lớp

| Mối quan hệ (Relationship) | Ký hiệu UML | Cài đặt C++ |
|-------------|-------------|-------------------|
| Kế thừa (is-a) | △─────── | `class D : public B` |
| Hợp thành (has-a) | ◇─────── | Thành phần đối tượng hoặc con trỏ |
| Kết hợp (uses) | ─────── | Tham số phương thức hoặc con trỏ |

### 12.4 Biểu diễn Lớp UML

```
┌──────────────────────────┐
│       ClassName           │
├──────────────────────────┤
│  - privateAttr: type     │   ← dấu trừ = private
│  # protectedAttr: type   │   ← dấu thăng = protected
│  + publicAttr: type      │   ← dấu cộng = public
├──────────────────────────┤
│  + operation(): retType  │
│  - helper(): void        │
└──────────────────────────┘
```

### 12.5 Mẫu Kịch bản Ca sử dụng (Use Case Scenario Template)

```
1. Tác nhân/hệ thống thực hiện X
2. Hệ thống phản hồi bằng Y
3. Tác nhân chọn Z
4. Hệ thống cập nhật W
...
```

---

## 13. BẪY THI CỬ

### Bẫy 1: Nhầm lẫn Phân tích (Cái gì) với Thiết kế (Như thế nào)
Phân tích (Analysis) mô tả **cái gì** hệ thống nên làm (yêu cầu). Thiết kế (Design) mô tả **như thế nào** nó sẽ làm điều đó (lớp, thao tác, mối quan hệ). Hãy giữ chúng tách biệt trong tư duy của bạn — mặc dù trong thực tế chúng có thể chồng lấn.

### Bẫy 2: Tìm Quá Nhiều hoặc Quá Ít Lớp
Không phải mọi danh từ đều là lớp (ví dụ: "date" có thể chỉ là một thuộc tính chuỗi). Không phải mọi lớp đều là danh từ trong phát biểu vấn đề (các lớp trợ giúp như `TimeSlot` có thể là ẩn). Hãy sử dụng phán đoán.

### Bẫy 3: Đặt Thao tác Sai Lớp
Các thao tác nên nằm trong lớp **sở hữu dữ liệu** mà chúng thao tác. `addTape()` thuộc về `PurchaseOrder`, không phải `Supplier`, vì đơn hàng sở hữu danh sách băng.

### Bẫy 4: Quên Các Lớp Trợ giúp/Tiện ích
Các lớp như `string`, `TimeSlot`, `Date` thường cần thiết nhưng không được đề cập dưới dạng danh từ. Chúng xuất hiện trong bước tinh chỉnh thiết kế.

### Bẫy 5: Đặc tả Quá Chi tiết Cài đặt trong Thiết kế
Trong thiết kế, tập trung vào **cái gì** một lớp làm (giao diện của nó), không phải **như thế nào** nó làm điều đó (cài đặt private). Chi tiết cài đặt đến sau.

### Bẫy 6: Nhầm lẫn Số lượng UML (Cardinality)
- `1` KHÔNG giống `0..1` — `0..1` có nghĩa là tùy chọn.
- `*` (hoặc `n`) có nghĩa là không hoặc nhiều, BAO GỒM cả không.
- Nếu một bác sĩ BẮT BUỘC phải có chính xác một lịch: `1 ──── 1`, không phải `1 ──── 0..1`.

### Bẫy 7: Kế thừa so với Hợp thành
- "Is-a" → **Kế thừa (Inheritance)** (một `Car` IS A `Vehicle`).
- "Has-a" → **Hợp thành (Composition)** (một `Car` HAS an `Engine`).
- Lựa chọn sai dẫn đến thiết kế thiếu linh hoạt. Ưu tiên hợp thành khi nghi ngờ.

### Bẫy 8: Thiết kế Là Theo vòng lặp — Lần Thử Đầu Hiếm Khi Là Cuối Cùng
Tổ chức lớp ban đầu có thể cần tổ chức lại (thêm lớp cơ sở chung, tách lớp). Điều này là bình thường và được mong đợi.

### Bẫy 9: Quên Các Thao tác Virtual
Cân nhắc thao tác nào nên là virtual trong giai đoạn thiết kế. Nếu các lớp dẫn xuất có thể cần hành vi khác, hãy đánh dấu nó là virtual trong lớp cơ sở.

### Bẫy 10: Giao diện Nên Hỗ trợ Cùng Mức Trừu tượng
Đừng pha trộn các thao tác cấp thấp và cấp cao trong cùng một giao diện lớp. Tất cả các thao tác public nên hoạt động ở một mức khái niệm nhất quán.

---

## 14. BÀI TẬP THỰC HÀNH VIẾT TAY

### Bài tập 1: Tìm Lớp và Thao tác từ Mô tả Vấn đề

**Vấn đề**: Một hệ thống quản lý thư viện cho phép thành viên mượn và trả sách. Mỗi sách có tiêu đề, tác giả và ISBN. Mỗi thành viên có tên và mã thành viên. Hệ thống phải theo dõi sách nào đang được mượn và bởi ai. Thành viên có thể mượn tối đa 5 sách cùng một lúc. Thủ thư có thể thêm sách mới và đăng ký thành viên mới.

> Xác định các lớp ứng viên, thuộc tính chính và ít nhất hai thao tác cho mỗi lớp.

> [!success]- Xem Đáp án
> **Các lớp:**
>
> **Book**
> - Thuộc tính: title, author, ISBN, isBorrowed
> - Thao tác: `borrow()`, `returnBook()`, `isAvailable()`
>
> **Member**
> - Thuộc tính: name, membershipID, booksBorrowed (bộ sưu tập)
> - Thao tác: `borrowBook(Book*)`, `returnBook(Book*)`, `canBorrow()` (kiểm tra giới hạn)
>
> **Library** (hoặc LibrarySystem)
> - Thuộc tính: books (bộ sưu tập), members (bộ sưu tập)
> - Thao tác: `addBook(Book*)`, `registerMember(Member*)`, `findBook(ISBN)`
>
> **Librarian** (tác nhân — có thể là một lớp hoặc chỉ một người dùng giao diện)
> - Thao tác: `addNewBook()`, `registerNewMember()`

### Bài tập 2: Biểu đồ Lớp — Vẽ Hệ thống Phòng khám Bác sĩ

Vẽ biểu đồ lớp kiểu UML cho hệ thống đặt lịch phòng khám bác sĩ, hiển thị:
- Tất cả năm lớp chính
- Các thuộc tính và thao tác chính
- Các mối quan hệ kèm số lượng (cardinality)

> [!success]- Xem Đáp án
> ```
> ┌──────────────┐         ┌──────────────┐
> │   Scheduler  │────────>│   Patient    │
> ├──────────────┤  uses   ├──────────────┤
> │ +schedule()  │         │ -name        │
> │ +printAll()  │         │ +inputName() │
> └──────┬───────┘         │ +chooseDr()  │
>        │                 │ +chooseSlot()│
>        │ uses            └──────┬───────┘
>        ↓                       │ uses
> ┌──────────────┐ 1     1 ┌─────┴────────┐
> │   Doctor     │◇───────│DailySchedule │
> ├──────────────┤contains ├──────────────┤
> │ -name        │         │ +setAppt()   │
> │ +addToSched()│         │ +isSlotFree()│
> │ +showAppt()  │         │ +showAppts() │
> └──────────────┘         └──────┬───────┘
>                                 │ 1..n contains
>                          ┌──────┴───────┐
>                          │ Appointment  │
>                          ├──────────────┤
>                          │ -timeSlot    │
>                          │ -patientName │
>                          │ +isBooked()  │
>                          └──────────────┘
> ```

### Bài tập 3: Tổ chức lại Hệ thống Phân cấp Lớp

Hai lớp chia sẻ hành vi đáng kể:

```cpp
class Car {
    string make, model;
    int year;
    void drive();
    void park();
    double fuelCapacity;
    void refuel();
};

class Motorcycle {
    string make, model;
    int year;
    void drive();
    void park();
    int engineCC;
    void wheelie();
};
```

> Tổ chức lại: thêm một lớp cơ sở chung. Nó chứa những gì? Những gì ở lại trong các lớp dẫn xuất?

> [!success]- Xem Đáp án
> ```cpp
> class Vehicle {              // Lớp cơ sở chung MỚI
> protected:
>     string make, model;
>     int year;
> public:
>     virtual void drive() = 0;   // pure virtual — có thể có các cài đặt khác nhau
>     virtual void park() = 0;
>     // Các getter cho make, model, year
> };
>
> class Car : public Vehicle {
>     double fuelCapacity;
> public:
>     void drive() override { /* dành riêng cho Car */ }
>     void park() override { /* dành riêng cho Car */ }
>     void refuel() { /* dành riêng cho Car */ }
> };
>
> class Motorcycle : public Vehicle {
>     int engineCC;
> public:
>     void drive() override { /* dành riêng cho Motorcycle */ }
>     void park() override { /* dành riêng cho Motorcycle */ }
>     void wheelie() { /* dành riêng cho Motorcycle */ }
> };
> ```
> Các thuộc tính dùng chung (`make`, `model`, `year`) và chữ ký thao tác (`drive`, `park`) được chuyển lên `Vehicle`. Các thành phần riêng theo kiểu ở lại trong các lớp dẫn xuất.

### Bài tập 4: Xác định Thao tác Theo Nhóm

Cho một lớp `BankAccount` với các thao tác ứng viên sau, hãy phân loại mỗi thao tác là Nền tảng (Foundation), Bộ chọn (Selector), Bộ sửa đổi (Modifier) hoặc Bộ duyệt (Iterator):

```
BankAccount(id, balance)  // constructor
getBalance()              // trả về số dư
deposit(amount)           // thêm vào số dư
withdraw(amount)          // trừ khỏi số dư
getStatement(dates)       // trả về các giao dịch trong khoảng ngày
applyInterest()           // tính và thêm lãi suất
```

> [!success]- Xem Đáp án
> | Thao tác (Operation) | Nhóm (Category) |
> |-----------|----------|
> | `BankAccount(id, balance)` | **Nền tảng (Foundation)** (hàm tạo) |
> | `getBalance()` | **Bộ chọn (Selector)** (không sửa đổi trạng thái) |
> | `deposit(amount)` | **Bộ sửa đổi (Modifier)** (thay đổi số dư) |
> | `withdraw(amount)` | **Bộ sửa đổi (Modifier)** (thay đổi số dư) |
> | `getStatement(dates)` | **Bộ duyệt (Iterator)** (duyệt qua bộ sưu tập giao dịch) |
> | `applyInterest()` | **Bộ sửa đổi (Modifier)** (thay đổi số dư) |

### Bài tập 5: Viết Kịch bản Ca sử dụng

Viết một kịch bản ca sử dụng từng bước cho sinh viên đăng ký một khóa học trong hệ thống đăng ký của trường đại học.

> [!success]- Xem Đáp án
> 1. Sinh viên nhập mã sinh viên của họ.
> 2. Hệ thống xác thực mã và hiển thị tên sinh viên.
> 3. Hệ thống hiển thị các khóa học có sẵn (chưa đầy, không xung đột thời gian).
> 4. Sinh viên chọn một khóa học.
> 5. Hệ thống kiểm tra điều kiện tiên quyết — nếu không đáp ứng, hiển thị lỗi.
> 6. Hệ thống kiểm tra sức chứa — nếu đầy, hiển thị lỗi kèm tùy chọn danh sách chờ.
> 7. Hệ thống thêm sinh viên vào danh sách khóa học.
> 8. Hệ thống cập nhật lịch học của sinh viên.
> 9. Hệ thống xác nhận đăng ký và hiển thị lịch học đã cập nhật.

---

> [!NOTE]
> Hướng dẫn học tập này bao gồm toàn bộ nội dung bài giảng Lec13: Thiết kế hướng đối tượng (Object-Oriented Design). Cần nắm vững năm bước thiết kế OO, kỹ thuật danh từ/động từ để tìm lớp/thao tác, ký hiệu biểu đồ lớp UML (bao gồm số lượng), và các ví dụ có lời giải (cửa hàng băng video, phòng khám bác sĩ). Tập trung vào quy trình thiết kế — xác định lớp, thao tác, phụ thuộc và giao diện — không phải chi tiết cài đặt.
