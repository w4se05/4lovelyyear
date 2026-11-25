# Lec3: Giới thiệu về OOP — Hướng dẫn học tập

## 1. THẺ KHÁI NIỆM: Lập trình hướng đối tượng
### 1.1 Định nghĩa
Một cách viết chương trình bằng cách nhóm dữ liệu liên quan và các hàm thao tác trên dữ liệu đó vào trong các đơn vị độc lập gọi là các đối tượng (objects).
### 1.2 Vấn đề nó giải quyết
Trước OOP, chương trình được viết theo phong cách có cấu trúc (thủ tục). Dữ liệu được lưu trữ toàn cục, và bất kỳ hàm nào trong chương trình cũng có thể truy cập và sửa đổi nó. Khi yêu cầu thay đổi — điều luôn xảy ra trong phần mềm thực tế — một thay đổi nhỏ có thể âm thầm phá vỡ các phần xa, không liên quan của chương trình vì mọi thứ đều chia sẻ cùng dữ liệu toàn cục. OOP khắc phục điều này bằng cách gói dữ liệu cùng với các hàm (phương thức) được phép chạm vào nó. Mỗi đối tượng bảo vệ dữ liệu của chính nó; các phần khác của chương trình chỉ có thể tương tác thông qua các giao diện (interfaces) được định nghĩa rõ ràng. Thay đổi nội bộ của một đối tượng không còn lan truyền khắp toàn bộ mã nguồn.
### 1.3 Cách hoạt động
1. Xác định các "thứ" trong thế giới thực trong bài toán của bạn (một sinh viên, một khóa học, một điểm GPS).
2. Với mỗi thứ, định nghĩa một **lớp (class)** — một bản thiết kế liệt kê dữ liệu nó lưu trữ và các hành động nó có thể thực hiện.
3. Tạo các **đối tượng (objects)** (thể hiện - instances) từ bản thiết kế lớp. Mỗi đối tượng giữ bản sao dữ liệu riêng của nó.
4. Các đối tượng giao tiếp bằng cách gửi **thông điệp (messages)** (gọi các phương thức của nhau).
5. Một chương trình trở thành một xã hội các đối tượng tương tác, mỗi đối tượng chịu trách nhiệm về hành vi của chính nó.
### 1.4 Ví dụ cụ thể
Một hệ thống định vị GPS:
- Lớp `Waypoint` lưu vĩ độ, kinh độ và độ cao. Các phương thức của nó cho phép bạn tính khoảng cách đến một Waypoint khác.
- Lớp `Route` giữ một danh sách có thứ tự các Waypoint. Các phương thức của nó tính tổng khoảng cách và thời gian di chuyển ước tính.
- Lớp `Navigator` sử dụng một Route và vị trí GPS hiện tại để xác định chỉ dẫn tiếp theo.
- Mỗi lớp sở hữu dữ liệu của nó. `Route` không trực tiếp can thiệp vào lat/lon của `Waypoint` — nó yêu cầu Waypoint tự tính khoảng cách.
### 1.5 Nó KHÔNG phải là gì
OOP KHÔNG chỉ đơn thuần là "đặt mã vào trong các lớp." Nếu bạn viết các lớp chỉ là không gian tên cho một đống hàm không liên quan, không chia sẻ trạng thái kết dính, bạn đang làm lập trình có cấu trúc trong một bộ trang phục hình lớp. OOP thực sự yêu cầu các đối tượng gói **trạng thái (state)** có ý nghĩa cùng với **hành vi (behavior)** tác động lên trạng thái đó.

## 2. CÁC MÔ HÌNH LẬP TRÌNH & PHƯƠNG PHÁP LUẬN
### 2.1 Các bước giải quyết vấn đề lập trình
```
Phân tích → Thiết kế → Mã hóa → Ngôn ngữ lập trình → Quản lý
```
Mọi giải pháp phần mềm đều tuân theo chuỗi này. Đầu tiên bạn phân tích yêu cầu, sau đó thiết kế giải pháp, viết mã bằng ngôn ngữ lập trình, và quản lý dự án qua vòng đời của nó.
### 2.2 Phương pháp tư duy: Quy nạp (Induction)
Quy nạp đi **từ cụ thể đến tổng quát**. Bạn quan sát nhiều ví dụ cụ thể và rút ra khái niệm chung.

Ví dụ: Bạn thấy các xe buýt khác nhau — xe buýt hạng sang, xe buýt trường học, xe buýt thành phố. Bằng cách nhận thấy các đặc điểm chung (xe chở khách lớn, nhiều ghế, dùng cho giao thông công cộng), bạn quy nạp ra khái niệm trừu tượng **"Xe buýt."** Cao hơn nữa: bạn quy nạp ra **"Xe cộ"** từ Ô tô, Xe máy và Xe buýt.

```
        Xe cộ
           |
   ┌───────┼───────┐
 Ô tô    Xe máy  Xe buýt
   |                    |
 Sedan  Xe thể thao  Xe buýt hạng sang  Xe buýt trường học
```

> [!success]- Show Answer
> > Quy nạp đi LÊN hệ thống phân cấp — từ các thể hiện cụ thể đến một lớp trừu tượng. Sơ đồ cho thấy cách các xe cụ thể (dưới cùng) được tổng quát hóa thành Xe cộ (trên cùng).

### 2.3 Phương pháp tư duy: Suy diễn (Deduction)
Suy diễn đi **từ tổng quát đến cụ thể**. Bạn bắt đầu với một khái niệm đã biết và suy luận xem một trường hợp cụ thể có phù hợp hay không.

Ví dụ: Một khi bạn đã học khái niệm **"Xe buýt,"** bạn có thể nhìn vào một phương tiện mới và suy diễn xem nó CÓ hay KHÔNG phải là xe buýt bằng cách kiểm tra nó dựa trên các thuộc tính định nghĩa xe buýt (kích thước lớn, nhiều ghế hành khách, mục đích giao thông công cộng).

> [!success]- Show Answer
> > Suy diễn đi XUỐNG hệ thống phân cấp — từ một lớp trừu tượng đến các thể hiện cụ thể. Bạn sử dụng định nghĩa để phân loại các thứ cụ thể.

### 2.4 Khái niệm và Mối quan hệ
Hiểu cách các khái niệm liên quan với nhau là nền tảng cho thiết kế hướng đối tượng:

| Mối quan hệ | Ví dụ | Ý nghĩa |
|---|---|---|
| **SỬ DỤNG (USES)** | Một hình chữ nhật **sử dụng** các đường thẳng | Một đối tượng gọi hoặc phụ thuộc vào đối tượng khác mà không sở hữu nó. Liên kết tạm thời, lỏng lẻo. |
| **IS-A** (Tính kế thừa - Inheritance) | Một hình tròn **là một** hình elip | Một lớp là phiên bản chuyên biệt hóa của lớp khác. Hình tròn là hình elip có cả hai bán kính bằng nhau. |
| **HAS-A / IS PART OF** (Hợp thành - Composition) | Một bánh xe **là một phần của** ô tô | Một đối tượng chứa đối tượng khác như một thành phần. Vòng đời của bánh xe gắn liền với xe. |
| **TẠO RA (CREATES)** (Factory) | Một tập hợp **tạo ra** các phần tử của nó | Một đối tượng chịu trách nhiệm khởi tạo và quản lý đối tượng khác. |

> [!success]- Show Answer
> > - **USES**: hình chữ nhật → đường thẳng (thao tác vẽ, phụ thuộc lỏng lẻo)
> > - **IS-A**: hình tròn → hình elip (hệ thống phân cấp kế thừa)
> > - **HAS-A**: bánh xe → ô tô (bánh xe là một bộ phận; hợp thành)
> > - **CREATES**: tập hợp → phần tử (mẫu factory; tập hợp quản lý vòng đời phần tử)

### 2.5 Phương pháp Tiếp cận Từ trên xuống (Top-Down) vs Từ dưới lên (Bottom-Up)
#### Từ trên xuống (Top-Down)
- Một module lớn duy nhất được chia thành các module nhỏ dần.
- Dòng chảy **Tổng quát → Cụ thể**.
- Sử dụng khi **yêu cầu rõ ràng ngay từ đầu** và ít có khả năng thay đổi.

#### Từ dưới lên (Bottom-Up)
- Nhiều module nhỏ được nhóm lại với nhau để tạo thành một module lớn duy nhất.
- Dòng chảy **Cụ thể → Tổng quát**.
- Sử dụng khi **yêu cầu liên tục được thêm vào / thay đổi** theo thời gian.

> [!success]- Show Answer
> > **Từ trên xuống** bắt đầu với bức tranh lớn và chia nhỏ nó thành các mảnh. **Từ dưới lên** bắt đầu với các mảnh nhỏ, có thể tái sử dụng và lắp ráp chúng lại. Hầu hết phần mềm thực tế sử dụng phương pháp từ dưới lên (hoặc kết hợp) vì yêu cầu chắc chắn thay đổi.

### 2.6 Lập trình có cấu trúc (Trước OOP)
Lập trình có cấu trúc tổ chức mã bằng các hàm và chia chương trình thành các module. Mỗi module có dữ liệu và hàm riêng có thể được gọi bởi các module khác.

```
        CHƯƠNG TRÌNH CHÍNH
              |
         DỮ LIỆU TOÀN CỤC
              |
   ┌──────────┼──────────┐
 HÀM 1     HÀM 2     HÀM 3
   └──────────┼──────────┘
         HÀM 4     HÀM 5
```

**Vấn đề cơ bản:** Không có tính đóng gói (encapsulation). Dữ liệu toàn cục nằm phơi bày ra ngoài. Bất kỳ hàm nào cũng có thể đọc hoặc sửa đổi bất kỳ phần dữ liệu toàn cục nào vào bất kỳ lúc nào. Khi chương trình phát triển, việc truy tìm hàm nào đã thay đổi cái gì trở thành một cơn ác mộng. Một sửa đổi nhỏ đối với dữ liệu toàn cục trong một module có thể âm thầm làm hỏng hành vi trong một module hoàn toàn không liên quan.

> [!success]- Show Answer
> > Lập trình có cấu trúc = các hàm + module + dữ liệu toàn cục. Nó hoạt động cho các chương trình nhỏ nhưng sụp đổ dưới độ phức tạp vì không có gì bảo vệ dữ liệu khỏi truy cập bừa bãi.

### 2.7 Tại sao OOP? (Tầm quan trọng)
- **Yêu cầu thực tế liên tục thay đổi và tích lũy.** Bản chất từ dưới lên của OOP đáp ứng điều này một cách tự nhiên — bạn có thể thêm các lớp mới mà không làm gián đoạn các lớp hiện có.
- **Biểu diễn dễ dàng các đối tượng thế giới thực, trạng thái và khả năng của chúng.** Bạn ánh xạ miền bài toán trực tiếp vào mã.
- **Tương tác với các đối tượng cùng loại và khác loại.** Các đối tượng cộng tác tự nhiên thông qua các lời gọi phương thức.
- **Hỗ trợ tính đa hình (Polymorphism) và nạp chồng (Overloading).** Một giao diện, nhiều hành vi.
- **Tiết kiệm thời gian phát triển nhờ tái sử dụng mã.** Một khi lớp được tạo và kiểm thử, nó có thể được sử dụng trong các ứng dụng khác mà không cần viết lại.
- **Gỡ lỗi dễ dàng hơn.** Các lớp có thể được kiểm thử độc lập (kiểm thử đơn vị), và các đối tượng được tái sử dụng đã được thử nghiệm trong các dự án trước đó.

> [!success]- Show Answer
> > Lợi ích chính của OOP: nó mô hình hóa thế giới thực, chịu đựng các yêu cầu thay đổi, tái sử dụng mã đã kiểm thử, và cô lập lỗi. Bạn gỡ lỗi một lớp, không phải toàn bộ chương trình cùng một lúc.

## 3. TRIẾT LÝ HƯỚNG ĐỐI TƯỢNG
### 3.1 Nguyên lý cốt lõi
- **Mọi thứ đều là một đối tượng.**
- **Bất kỳ hệ thống nào cũng được cấu thành từ các đối tượng** — và một hệ thống tự nó là một đối tượng có thể là một phần của hệ thống lớn hơn.
- **Sự tiến hóa và phát triển của một hệ thống** được gây ra bởi các tương tác của các đối tượng bên trong và bên ngoài hệ thống đó.

> [!success]- Show Answer
> > Ba trụ cột triết học: (1) mọi thứ là một đối tượng, (2) hệ thống được xây dựng từ các đối tượng, (3) thay đổi xảy ra thông qua các tương tác đối tượng.

### 3.2 Thuộc tính của Đối tượng
- Các đối tượng có **cả dữ liệu VÀ phương thức** (trạng thái + hành vi được gói cùng nhau).
- Các đối tượng **cùng lớp** có cùng các phần tử dữ liệu và phương thức (cùng bản thiết kế, giá trị khác nhau).
- Các đối tượng **gửi và nhận THÔNG ĐIỆP** để gọi các hành động. Một thông điệp là một lời gọi đến một phương thức trên một đối tượng đích.
- **Ý tưởng chính:** *"Thế giới thực có thể được mô tả chính xác như một tập hợp các đối tượng tương tác."*

```
┌──────────┐     Thông điệp     ┌──────────┐
│ Đối tượng A │ ──────────────→ │ Đối tượng B │
│  Dữ liệu    │                 │  Dữ liệu    │
│  Phương thức│ ←────────────── │  Phương thức│
└──────────┘     Thông điệp     └──────────┘
```

> [!success]- Show Answer
> > Các đối tượng chứa dữ liệu + phương thức. Các đối tượng cùng lớp chia sẻ cấu trúc nhưng giữ các giá trị khác nhau. Chúng giao tiếp độc quyền thông qua các thông điệp (lời gọi phương thức). Toàn bộ thế giới chỉ là các đối tượng nói chuyện với các đối tượng.

### 3.3 Ví dụ "Mọi thứ đều là một đối tượng"
Từ nhỏ nhất đến lớn nhất — tất cả đều có thể được mô hình hóa như các đối tượng:
- Một **sinh viên**, một **giáo sư**
- Một **bàn**, một **ghế**, một **phòng học**, một **tòa nhà**
- Một **trường đại học**, một **thành phố**, một **quốc gia**
- **Thế giới**, **vũ trụ**
- Một môn học: **KHMT**, **HTTT**, **Toán**, **Lịch sử**

> [!success]- Show Answer
> > Mọi danh từ trong miền bài toán đều có thể là một đối tượng. Không có gì quá nhỏ (một cái ghế) hoặc quá lớn (vũ trụ) để được biểu diễn như một đối tượng với dữ liệu và hành vi.

### 3.4 Hệ thống được cấu thành từ các Đối tượng
Các hệ thống tự chúng là các đối tượng, được xây dựng từ các đối tượng nhỏ hơn:
- Một **hệ thống giáo dục** (bao gồm trường học, sinh viên, chương trình giảng dạy)
- Một **hệ thống kinh tế** (bao gồm thị trường, tiền tệ, giao dịch)
- Một **hệ thống thông tin** (bao gồm cơ sở dữ liệu, người dùng, truy vấn)
- Một **hệ thống máy tính** (bao gồm CPU, bộ nhớ, lưu trữ, HĐH)

> [!success]- Show Answer
> > Mọi hệ thống là một đối tượng được tạo từ các đối tượng nhỏ hơn. Sự lồng ghép này tiếp tục đệ quy — các thành phần của hệ thống là các đối tượng, và bản thân hệ thống là một đối tượng bên trong một hệ thống lớn hơn.

### 3.5 Phát triển thông qua Tương tác
Một hệ thống tiến hóa thông qua các tương tác giữa các đối tượng bên trong và bên ngoài của nó.

**Ví dụ — VGU (Trường Đại học Việt-Đức):**

Bên trong VGU (tương tác nội bộ):
- **Sinh viên** tương tác với **giáo sư** (học tập, nghiên cứu)
- **Nhân viên** tương tác với **hội đồng quản trị** (hành chính, chính sách)

Bên ngoài VGU (tương tác bên ngoài):
- VGU tương tác với **chính quyền nhà nước** (tuân thủ, tài trợ, quy định)

> [!success]- Show Answer
> > VGU được định nghĩa KHÔNG phải bởi bất kỳ thành phần đơn lẻ nào mà bởi các tương tác đang diễn ra giữa sinh viên, giáo sư, nhân viên, hội đồng quản trị (nội bộ), và chính quyền nhà nước (bên ngoài). Thay đổi bất kỳ tương tác nào và bạn thay đổi hệ thống.

## 4. PHƯƠNG PHÁP LUẬN THIẾT KẾ
### 4.1 Hướng Đối tượng như Thiết kế (OOD)
Thiết kế Hướng Đối tượng sử dụng **các đối tượng làm khối xây dựng** của một chương trình. Mỗi đối tượng đại diện cho một trừu tượng hóa thế giới thực trong miền ứng dụng. Thay vì suy nghĩ theo các hàm và luồng dữ liệu, bạn suy nghĩ theo các đối tượng và sự cộng tác của chúng.

> [!success]- Show Answer
> > OOD = thiết kế phần mềm bằng cách xác định các đối tượng (trừu tượng hóa thế giới thực) và định nghĩa cách chúng tương tác. Các đối tượng là vật liệu xây dựng.

### 4.2 Quy nạp và Suy diễn trong Thiết kế
- **Quy nạp:** đối tượng → một lớp. Bạn nhìn vào một số đối tượng cụ thể, tìm điểm chung của chúng, và tạo định nghĩa lớp. *Các công cụ có thể làm việc này tự động* (kỹ thuật đảo ngược, công cụ tái cấu trúc).
- **Suy diễn:** một lớp → đối tượng. Bạn lấy một bản thiết kế lớp hiện có và tạo các đối tượng cụ thể từ nó. *Thường được thực hiện bởi lập trình viên* khi viết mã.

> [!success]- Show Answer
> > Quy nạp: quan sát các đối tượng để suy ra một lớp (hỗ trợ bởi công cụ). Suy diễn: sử dụng một lớp để tạo các đối tượng (công việc hàng ngày của lập trình viên — `Student s;` tạo một đối tượng từ lớp Student).

### 4.3 Từ trên xuống và Từ dưới lên trong Thiết kế
- **Từ trên xuống:** từ một **siêu lớp (super-class) đến các lớp con (sub-classes)**. Bắt đầu với khái niệm tổng quát nhất và dần dần chuyên biệt hóa. (Xe cộ → Ô tô, Xe máy, Xe buýt)
- **Từ dưới lên:** từ **các lớp con đến một siêu lớp**. Bắt đầu với nhiều lớp cụ thể và trích xuất điểm chung vào một lớp cha. (Sedan, Xe thể thao → Ô tô)

> [!success]- Show Answer
> > Thiết kế Từ trên xuống tạo các lớp con từ một siêu lớp. Thiết kế Từ dưới lên tạo một siêu lớp bằng cách trích xuất các đặc điểm chung từ các lớp con hiện có. Cả hai hướng đều hợp lệ và thường được sử dụng cùng nhau.

## 5. BỐN TRỤ CỘT CỦA OOP
### 5.1 Tính trừu tượng (Abstraction)
Tính trừu tượng có nghĩa là **chỉ tập trung vào các sự kiện quan trọng** về bài toán đang giải quyết và bỏ qua các chi tiết không cần thiết. Bạn thiết kế, tạo ra và mô tả một thứ sao cho nó có thể được sử dụng mà không cần biết nó hoạt động bên trong như thế nào.

**Tương tự:** Khi bạn lái xe, bạn không cần biết xăng và không khí được trộn và đốt cháy trong động cơ như thế nào. Bạn chỉ cần biết cách sử dụng các điều khiển — vô lăng, ga, phanh. Các chi tiết đốt cháy nội bộ phức tạp được **trừu tượng hóa** đằng sau một giao diện đơn giản.

#### Kiểu dữ liệu trừu tượng (ADT)
Một ADT định nghĩa **giao diện (interface)** cho một trừu tượng hóa dữ liệu **mà không chỉ rõ chi tiết cài đặt**.

Thuộc tính ADT:
1. Nó **xuất khẩu một kiểu** (một tên kiểu dữ liệu mới, như `Complex` hoặc `Stack`).
2. Nó **xuất khẩu một tập hợp các thao tác** (các hàm làm việc trên kiểu đó).
3. **Tiên đề và điều kiện tiên quyết** định nghĩa miền ứng dụng — các quy tắc mà mọi cài đặt phải tuân theo.

#### ADT trong C++
- **Các bổ từ truy cập (Access modifiers)** (`private`, `public`, `protected`) cung cấp tính trừu tượng — chúng ẩn những gì người ngoài không nên thấy.
- **Các hàm** cũng cung cấp tính trừu tượng — tên hàm (`sort()`) ẩn thuật toán sắp xếp bên trong.
- **Các biến private** bị ẩn khỏi các lớp khác; chỉ lớp sở hữu mới có thể truy cập chúng.
- **Tên hàm** trong một lời gọi ẩn các chi tiết cài đặt — `computeGPA()` cho thấy phác thảo chức năng mà không tiết lộ thuật toán tính toán.

> [!success]- Show Answer
> > Tính trừu tượng: phơi bày CÁI GÌ đó làm, ẩn LÀM THẾ NÀO nó làm. Bổ từ truy cập ẩn dữ liệu, hàm ẩn thuật toán. Một ADT xuất khẩu một kiểu + các thao tác + quy tắc, không có chi tiết cài đặt nào được phơi bày.

### 5.2 Tính đóng gói (Encapsulation)
Tính đóng gói là quá trình **kết hợp dữ liệu và phương thức** của một đối tượng vào một đơn vị duy nhất. Định nghĩa lớp cung cấp tính năng này.

Tính đóng gói cho phép:
- **Tính mô-đun (Modularity)** — mỗi lớp là một module khép kín.
- **Truy cập có kiểm soát vào dữ liệu** — dữ liệu là private; người ngoài sử dụng các phương thức public.
- **Tách biệt cài đặt khỏi giao diện** — thay đổi nội bộ; người gọi không thấy sự khác biệt.
- **Mở rộng các kiểu dựng sẵn** — bạn tạo các kiểu mới hoạt động như các kiểu dựng sẵn.

#### Ví dụ Số phức
Một số phức có **phần thực** và **phần ảo**, cả hai đều được biểu diễn bằng số thực. Các thao tác bao gồm cộng, trừ, nhân và chia.

Để biểu diễn một số phức, bạn phải định nghĩa cấu trúc dữ liệu của nó. Có ít nhất hai cách:

**Cách tiếp cận 1 — Mảng hai giá trị:**
```cpp
c[0] = phần thực    // x = c[0]
c[1] = phần ảo  // y = c[1]
```

**Cách tiếp cận 2 — Bản ghi hai giá trị (struct):**
```cpp
c.r = phần thực     // x = c.r
c.i = phần ảo  // y = c.i
```

Trong cả hai trường hợp, `x` bằng "phần thực của `c`." **Ngữ nghĩa (semantics)** (ý nghĩa) là giống hệt nhau — nhưng **cấu trúc dữ liệu** khác nhau. Định nghĩa ADT nói rằng mỗi truy cập vào cấu trúc dữ liệu **nên có một thao tác được định nghĩa**. Truy cập mảng trực tiếp (`c[0]`) mâu thuẫn với nguyên tắc này — nó phơi bày các chi tiết lưu trữ thô.

**Giải pháp đóng gói:**
Một khi ADT `Complex` được tạo, bạn sử dụng nó như bất kỳ kiểu dựng sẵn nào:
```cpp
Complex a;
```

Đối với các thao tác như cộng, thao tác `add` **đóng gói** các chi tiết. Người gọi chỉ đơn giản *"cộng hai số phức"* mà không biết cấu trúc dữ liệu nội bộ nào được sử dụng:
```cpp
Complex result = a.add(b);   // người gọi không biết gì về mảng hay bản ghi bên trong
```

> [!success]- Show Answer
> > Tính đóng gói gói dữ liệu + phương thức lại với nhau. Ví dụ Complex chứng minh rằng hai biểu diễn nội bộ khác nhau (mảng vs. struct) có thể có hành vi bên ngoài giống hệt nhau. Tính đóng gói ẩn biểu diễn nào được sử dụng, vì vậy người gọi không bao giờ phụ thuộc vào chi tiết nội bộ. Thay đổi nội bộ không bao giờ làm hỏng mã bên ngoài.

### 5.3 Tính kế thừa (Inheritance)
Tính kế thừa cho phép **tái sử dụng mã**. Một kiểu dữ liệu trừu tượng mới (lớp dẫn xuất - derived class) có thể **kế thừa** dữ liệu và chức năng của một kiểu hiện có (lớp cha - parent class), và được phép **sửa đổi** một số thực thể đó và **thêm các thực thể mới**.

#### Thuật ngữ

| Thuật ngữ | Định nghĩa |
| ---------------------------------------- | ------------------------------------------------------------------------------------ |
| **Lớp (Class)** | Kiểu dữ liệu trừu tượng (ADT) trong các ngôn ngữ hướng đối tượng. |
| **Đối tượng (Object)** | Một thể hiện của một lớp — một thực thể cụ thể với các giá trị dữ liệu thực tế. |
| **Lớp dẫn xuất (Derived class / subclass)** | Một lớp được định nghĩa thông qua kế thừa từ một lớp khác. |
| **Lớp cha (Parent class / superclass)** | Một lớp mà từ đó một lớp mới được dẫn xuất. |
| **Phương thức (Methods)** | Các chương trình con định nghĩa các thao tác trên các đối tượng của một lớp. |
| **Thông điệp (Messages)** | Các lời gọi đến phương thức. Một thông điệp có hai phần: tên phương thức và đối tượng đích. |
| **Giao thức thông điệp (Message Protocol / Message Interface)** | Toàn bộ tập hợp các phương thức của một đối tượng — API công khai của nó. |

#### Hệ thống phân cấp Kế thừa

```
               Siêu lớp
                Xe cộ
                   |
       ┌───────────┼───────────┐
    Ô tô       Xe máy     Xe buýt
       |                        |
   Sedan  Xe thể thao    Luxury Bus  School Bus
```

Mỗi cấp kế thừa các thuộc tính từ tất cả các cấp phía trên nó. Một `School Bus` kế thừa mọi thứ từ `Bus`, mà kế thừa từ `Vehicle`.

#### Ví dụ Sinh viên
```
          Lớp mới
          Students
              |
    ┌─────────┴─────────┐
  Đối tượng           Đối tượng
  Trung (Dữ liệu+Phương thức)   Linh (Dữ liệu+Phương thức)
              |
    Học viên Cao học IS-A Sinh viên
    (Lớp dẫn xuất của lớp Student)
         Master Students
```

Một Học viên Cao học **IS-A** Sinh viên — nó kế thừa tất cả các thuộc tính của Sinh viên và thêm hoặc sửa đổi các thuộc tính riêng.

> [!success]- Show Answer
> > Tính kế thừa = mối quan hệ "is-a". Một lớp dẫn xuất kế thừa dữ liệu + phương thức từ lớp cha, có thể sửa đổi hành vi được kế thừa, và có thể thêm các tính năng mới. Hãy nghĩ Xe cộ → Xe buýt → Xe buýt trường học: mỗi cấp nhận mọi thứ từ cấp trên cộng với các chuyên biệt hóa riêng.

### 5.4 Tính đa hình (Polymorphism)
Tính đa hình là **khả năng của các đối tượng khác nhau để phản hồi khác nhau trước cùng một thông điệp hoặc lời gọi hàm**.

- **Poly** = Nhiều
- **Morph** = Hình thức
- **Polymorphism** = khả năng cùng tồn tại ở nhiều hơn một hình thức

**Trong C++:** Tính đa hình được cài đặt thông qua **nạp chồng hàm (function overloading)** và **nạp chồng toán tử (operator overloading)** — cùng tên hàm hoặc ký hiệu toán tử hoạt động khác nhau tùy thuộc vào kiểu hoặc số lượng đối số.

> [!success]- Show Answer
> > Cùng thông điệp, hành vi khác nhau tùy thuộc vào ai nhận nó. Trong C++, nạp chồng hàm (`add(int, int)` vs `add(double, double)`) và nạp chồng toán tử (`+` cho Complex vs `+` cho int) là các cài đặt cụ thể của tính đa hình.

## 6. MẪU CÚ PHÁP CẦN GHI NHỚ
```cpp
class ClassName {          // Khai báo một lớp (bản thiết kế)
private:                   // Dữ liệu bị ẩn khỏi người ngoài
    int dataMember;        // Mỗi đối tượng có bản sao riêng
public:                    // Giao diện hiển thị cho mọi người
    ClassName(int val);    // Hàm tạo (Constructor): khởi tạo đối tượng mới
    int getData();         // Trình truy cập (Accessor): đọc dữ liệu an toàn
    void setData(int v);   // Trình thay đổi (Mutator): thay đổi dữ liệu với xác thực
};                         // DẤU CHẤM PHẨY LÀ BẮT BUỘC
```

> [!success]- Show Answer
> > Mỗi lớp cần: (1) từ khóa `class` + tên, (2) thành viên dữ liệu `private:`, (3) `public:` hàm tạo + trình truy cập + trình thay đổi, (4) dấu chấm phẩy sau dấu ngoặc nhọn đóng. Thiếu dấu chấm phẩy là lỗi biên dịch phổ biến nhất trong các kỳ thi.

## 7. BẪY THI CỬ
### Bẫy 1: Thiếu Dấu Chấm Phẩy Sau Dấu Ngoặc Nhọn Đóng của Lớp
```cpp
class Foo {
    int x;
}     // ← KHÔNG CÓ DẤU CHẤM PHẨY — lỗi biên dịch!

class Bar {
    int y;
};    // ← Đúng
```
> [!success]- Show Answer
> > Một định nghĩa lớp PHẢI kết thúc bằng `};`. Dấu chấm phẩy là không tùy chọn. Quên nó là một trong những lỗi cú pháp phổ biến nhất trong khai báo lớp C++.

### Bẫy 2: Nhầm lẫn Lớp (Bản thiết kế) với Đối tượng (Thể hiện)
```
"Student" là một lớp — nó mô tả những gì mỗi sinh viên có.
"Trung" là một đối tượng — nó là một sinh viên cụ thể với dữ liệu thực tế.
```
Bạn không thể lưu trữ dữ liệu trong một lớp; bạn lưu trữ dữ liệu trong các đối tượng được tạo từ lớp.
> [!success]- Show Answer
> > Một lớp = bản thiết kế (thiết kế). Một đối tượng = thể hiện (một thứ thực tế được xây dựng từ thiết kế). Bạn viết mã trong lớp; chương trình của bạn tạo và thao tác các đối tượng. Bạn không thể gọi `Student.getName()` — bạn gọi `trung.getName()` trên một đối tượng.

### Bẫy 3: "Private Có Nghĩa là Tuyệt Đối Không Ai Có Thể Thấy Nó" — SAI
```cpp
class X {
private:
    int secret;
public:
    void peek(X& other) {
        int leaked = other.secret;  // HỢP LỆ! Cùng lớp.
    }
};
```
> [!success]- Show Answer
> > Truy cập private là **theo-lớp, không phải theo-đối tượng**. Hai đối tượng của cùng một lớp CÓ THỂ truy cập các thành viên private của nhau. Trình biên dịch kiểm tra lớp, không phải đối tượng cụ thể nào bạn đang chạm vào.

### Bẫy 4: Truy cập Mặc định trong `class` vs `struct`
```cpp
class Foo { int x; };     // x là PRIVATE theo mặc định
struct Bar { int y; };    // y là PUBLIC theo mặc định
```
> [!success]- Show Answer
> > Trong một `class`, các thành viên mặc định là `private`. Trong một `struct`, các thành viên mặc định là `public`. Chúng giống hệt nhau về mọi mặt khác. Thêm các nhãn `private:` và `public:` một cách rõ ràng được coi là thực hành tốt nhất.

### Bẫy 5: Nhầm lẫn Tính trừu tượng với Tính đóng gói
- **Tính trừu tượng (Abstraction)** = ẩn các chi tiết không cần thiết (CÁI GÌ, không phải LÀM THẾ NÀO). Tập trung vào các tính năng thiết yếu.
- **Tính đóng gói (Encapsulation)** = gói dữ liệu cùng với các phương thức thao tác trên dữ liệu đó (Ở ĐÂU, cùng nhau).
> [!success]- Show Answer
> > Tính trừu tượng là về **quan điểm** — người dùng thấy một giao diện đơn giản. Tính đóng gói là về **đóng gói** — dữ liệu và phương thức sống bên trong cùng một hộp. Chúng hoạt động cùng nhau nhưng là các khái niệm riêng biệt. Một lớp có thể được đóng gói mà không được trừu tượng hóa tốt, và ngược lại về mặt lý thuyết (mặc dù OOP kết hợp cả hai).

### Bẫy 6: Nghĩ rằng "Mọi thứ Phải là một Đối tượng"
C++ là một ngôn ngữ **đa mô hình (multi-paradigm)**. Nó có:
- Các hàm tự do (độc lập) không thuộc về lớp nào
- Các kiểu nguyên thủy (`int`, `double`, `char`) không phải là đối tượng của lớp
- Các biến toàn cục (mặc dù bạn nên tránh chúng)
> [!success]- Show Answer
> > "Mọi thứ là một đối tượng" là một **triết lý** cho tư duy thiết kế, không phải là một ràng buộc ngôn ngữ trong C++. Không phải mọi dòng mã C++ đều phải nằm trong một lớp. Các hàm tự do và kiểu nguyên thủy là hợp lệ và thường cần thiết.

### Bẫy 7: Nhầm lẫn các Mối quan hệ "IS-A" vs "HAS-A" vs "USES"
| Mối quan hệ | Tính năng OOP | Ví dụ |
|---|---|---|
| IS-A | Tính kế thừa | Một xe thể thao IS-A xe hơi |
| HAS-A / IS PART OF | Hợp thành | Một động cơ IS PART OF một xe hơi |
| USES | Phụ thuộc | Một tài xế USES một xe hơi |
> [!success]- Show Answer
> > IS-A = kế thừa (phân lớp con). HAS-A = hợp thành (các đối tượng thành viên). USES = phụ thuộc (tham số hoặc biến cục bộ). Chọn sai mối quan hệ dẫn đến hệ thống phân cấp lớp tồi. Nếu bạn kế thừa khi bạn nên hợp thành, bạn có mã mong manh, quá khớp nối.

### Bẫy 8: ADT — Nhầm lẫn Giao diện với Cài đặt
Một ADT định nghĩa các thao tác **CÁI GÌ** tồn tại, KHÔNG phải **LÀM THẾ NÀO** chúng hoạt động. Giao diện là hợp đồng; cài đặt là cơ chế ẩn.
```cpp
// Giao diện (định nghĩa ADT):
//   Kiểu: Stack
//   Các thao tác: push(item), pop() → item, isEmpty() → bool
// (Cài đặt: có thể dùng mảng, danh sách liên kết, hoặc vector — người dùng không quan tâm!)
```
> [!success]- Show Answer
> > ADT là lời hứa (giao diện). Cài đặt là bí mật (nó thực sự hoạt động như thế nào). Các kỳ thi sẽ yêu cầu bạn viết một giao diện ADT — chỉ khai báo các thao tác, đừng cài đặt chúng.

### Bẫy 9: Quy nạp vs Suy diễn — Hướng nào là Hướng nào?
- **Quy nạp (Induction):** Cụ thể → Trừu tượng. Ví dụ: thấy một xe buýt hạng sang, một xe buýt trường học, một xe buýt thành phố → hình thành khái niệm "Xe buýt."
- **Suy diễn (Deduction):** Trừu tượng → Cụ thể. Ví dụ: cho khái niệm "Xe buýt," bạn suy diễn xem một phương tiện cụ thể có phải là xe buýt không.
> [!success]- Show Answer
> > Quy nạp đi LÊN (cụ thể đến ý tưởng chung). Suy diễn đi XUỐNG (ý tưởng chung đến trường hợp cụ thể). Gợi nhớ: **Quy** nạp thu thập các ví dụ **riêng lẻ** để suy **luật**. Suy **diễn** xác định nếu một thứ phù hợp với một **luật** bạn đã biết.

### Bẫy 10: Từ trên xuống vs Từ dưới lên — Biết Khi nào Sử dụng Mỗi Phương pháp
- **Từ trên xuống (Top-Down):** Yêu cầu **RÕ RÀNG và ỔN ĐỊNH** ngay từ đầu. Bạn có thể lập kế hoạch toàn bộ kiến trúc từ trên xuống.
- **Từ dưới lên (Bottom-Up):** Yêu cầu **ĐANG TIẾN HÓA / TÍCH LŨY**. Các tính năng mới liên tục xuất hiện. Bạn xây dựng các mảnh nhỏ, có thể tái sử dụng và kết hợp chúng.

> [!success]- Show Answer
> > Từ trên xuống = yêu cầu cố định, bức tranh rõ ràng. Từ dưới lên = yêu cầu thay đổi, tương lai không chắc chắn. Trong thực tế, hầu hết các dự án thực tế là từ dưới lên (hoặc kết hợp) vì yêu cầu LUÔN thay đổi. Bài giảng nói rõ rằng OOP tuân theo chiến lược từ dưới lên.

### Bẫy 11: Tính đa hình (Polymorphism) vs Nạp chồng (Overloading)
- **Tính đa hình** là khái niệm rộng: các đối tượng phản hồi khác nhau trước cùng một thông điệp.
- **Nạp chồng** (hàm và toán tử) là một **kỹ thuật cài đặt** cụ thể để đạt được tính đa hình trong C++.
> [!success]- Show Answer
> > Tính đa hình là "cái gì" (nhiều hình thức). Nạp chồng là "làm thế nào" (cùng tên, kiểu tham số khác nhau). Nạp chồng là một tập con của tính đa hình. Đừng sử dụng các thuật ngữ thay thế cho nhau — tính đa hình cũng bao gồm các hàm ảo (virtual functions), mẫu (templates), và tính đa hình kiểu con (subtype polymorphism).

### Bẫy 12: OOP Không Chỉ là "Mã trong Các Lớp"
Viết một loạt các lớp chỉ là không gian tên chứa đầy các hàm tiện ích tĩnh KHÔNG phải là OOP. OOP thực sự yêu cầu:
- Các đối tượng giữ **trạng thái** (các thành viên dữ liệu)
- Các đối tượng thể hiện **hành vi** (các phương thức thao tác trên trạng thái đó)
- Các đối tượng **tương tác** bằng cách gửi thông điệp cho nhau

> [!success]- Show Answer
> > Nếu lớp của bạn không có thành viên dữ liệu và chỉ có các phương thức tĩnh, bạn đang làm lập trình thủ tục được mặc trong cú pháp lớp. OOP yêu cầu sự kết hợp của trạng thái + hành vi + đóng gói + tương tác. Một lớp thiếu máu chỉ chứa dữ liệu (chỉ getter/setter) cũng không thực sự là OOP — nó là một cấu trúc dữ liệu.

### Bẫy 13: Module Lập trình Có cấu trúc vs Lớp OOP
Trong lập trình có cấu trúc, mỗi module có dữ liệu và hàm riêng — điều này nghe có vẻ giống một lớp, nhưng có một khác biệt quan trọng: dữ liệu trong lập trình có cấu trúc vẫn **có thể truy cập toàn cục** bởi bất kỳ module nào khác gọi hàm. Không có rào cản đóng gói thực sự.

> [!success]- Show Answer
> > Các module có cấu trúc có thể TRÔNG như được đóng gói, nhưng bất kỳ module nào cũng có thể gọi hàm của module khác và do đó chạm vào dữ liệu của nó. Chỉ các lớp OOP mới thực thi kiểm soát truy cập (`private`) mà trình biên dịch thực thi về mặt vật lý. Sơ đồ lập trình có cấu trúc trong bài giảng cho thấy DỮ LIỆU TOÀN CỤC ở trung tâm, phơi bày cho tất cả các hàm — đó là sai lầm chết người.

## 8. BÀI TẬP VIẾT MÃ
### Bài tập 1: Xác định Bốn Trụ cột từ một Kịch bản
**Kịch bản:** Một ứng dụng ngân hàng có `Account` (lưu số dư một cách private, cung cấp `deposit()` và `withdraw()` với xác thực). `SavingsAccount` kế thừa từ `Account` (ghi đè `withdraw()` để ngăn thấu chi, thêm `addInterest()`). Nhiều kiểu `Account` tồn tại — `deposit()` hoạt động khác nhau cho checking vs savings. Khách hàng không bao giờ thấy các truy vấn cơ sở dữ liệu được sử dụng để lưu dữ liệu tài khoản vào đĩa.

Xác định cả bốn trụ cột trong kịch bản này.

> [!success]- Show Answer
> > - **Tính trừu tượng (Abstraction):** Khách hàng thấy `deposit()` và `withdraw()` — họ không bao giờ thấy các truy vấn cơ sở dữ liệu lưu dữ liệu vào đĩa. Cơ chế lưu trữ nội bộ bị ẩn.
> > - **Tính đóng gói (Encapsulation):** Số dư là `private` bên trong `Account`. Chỉ `deposit()` và `withdraw()` mới có thể sửa đổi nó. Dữ liệu và phương thức được gói cùng nhau.
> > - **Tính kế thừa (Inheritance):** `SavingsAccount` kế thừa từ `Account` — nó nhận tất cả dữ liệu và phương thức của Account, sau đó ghi đè `withdraw()` và thêm `addInterest()`.
> > - **Tính đa hình (Polymorphism):** `deposit()` hoạt động khác nhau cho checking vs savings. Cùng tên phương thức tạo ra các kết quả khác nhau tùy thuộc vào loại tài khoản.

### Bài tập 2: Phát hiện OOP Bị Hỏng (Vi phạm Truy cập Thành viên Private)
Đoạn mã nào sau đây chứa vi phạm truy cập thành viên private?

```cpp
class Player {
private:
    int hp;
public:
    int getHP() { return hp; }
    void attack(Player& other) {
        other.hp -= 10;    // (A)
    }
};

void gameLoop() {
    Player p1, p2;
    p1.hp = 100;          // (B)
    int x = p2.getHP();   // (C)
    int y = p1.hp;        // (D)
}
```

> [!success]- Show Answer
> > (B) và (D) là vi phạm. `hp` là private, và `gameLoop()` không phải là hàm thành viên của `Player`.
> > (A) là HỢP LỆ — `attack()` là thành viên của `Player`, và hai đối tượng cùng lớp CÓ THỂ truy cập các thành viên private của nhau.
> > (C) là HỢP LỆ — `getHP()` là một trình truy cập public.

### Bài tập 3: Lựa chọn Thiết kế Từ dưới lên vs Từ trên xuống kèm Biện minh
**Kịch bản A:** Bạn được thuê để xây dựng một hệ thống tính lương cho một công ty với các quy tắc tính lương được ghi chép đầy đủ, không thay đổi trong 15 năm. Tất cả các yêu cầu được đặc tả đầy đủ trong một tài liệu 200 trang.

**Kịch bản B:** Bạn đang xây dựng MVP (sản phẩm khả thi tối thiểu) cho một công ty khởi nghiệp. Người sáng lập nói "Chúng ta cần tài khoản người dùng và xử lý thanh toán ngay bây giờ, nhưng chúng ta sẽ tìm ra phần còn lại khi tiến hành."

Phương pháp nào (Từ trên xuống hay Từ dưới lên) cho mỗi kịch bản? Biện minh.

> [!success]- Show Answer
> > **Kịch bản A → Từ trên xuống.** Yêu cầu rõ ràng, ổn định và được ghi chép đầy đủ. Bạn có thể thiết kế toàn bộ kiến trúc hệ thống (Main → Payroll Engine → Tax Calculator, Salary Calculator, v.v.) từ trên xuống mà không sợ thay đổi lớn.
> > **Kịch bản B → Từ dưới lên.** Yêu cầu mơ hồ và chắc chắn sẽ thay đổi. Xây dựng các module nhỏ, độc lập (module User, module Payment) làm các khối xây dựng có thể tái sử dụng. Khi người sáng lập thay đổi hướng đi vào tuần tới, bạn sắp xếp lại các khối thay vì phá hủy một cấu trúc nguyên khối.

### Bài tập 4: Thiết kế ADT — Viết Giao diện cho Số phức
Chỉ viết giao diện (không cài đặt) cho một ADT `Complex`. Bao gồm:
- Một kiểu cho số phức
- Các thao tác: tạo (với phần thực và phần ảo), cộng, trừ, lấy phần thực, lấy phần ảo
- Điều kiện tiên quyết: đơn vị ảo `i` thỏa mãn `i² = -1`

> [!success]- Show Answer
> > ```cpp
> > // ADT Complex: biểu diễn số phức a + bi với i² = -1
> > // Xuất khẩu kiểu: Complex
> > // Xuất khẩu thao tác:
> > class Complex {
> > private:
> >     double real;
> >     double imag;
> > public:
> >     Complex(double r, double im);           // tạo: r + im*i
> >     Complex add(Complex other);             // trả về this + other
> >     Complex subtract(Complex other);        // trả về this - other
> >     double getReal();                       // trả về phần thực
> >     double getImag();                       // trả về phần ảo
> > };
> > // Tiên đề:
> > //   add có tính giao hoán: a.add(b) == b.add(a)
> > //   add có tính kết hợp: (a.add(b)).add(c) == a.add(b.add(c))
> > ```

### Bài tập 5: Lớp vs Đối tượng — Xác định Cái nào Là Cái nào
**Kịch bản:** Một hệ thống đăng ký đại học có: `Course`, `Student`, khóa học cụ thể "Programming 2" học vào Thứ Ba lúc 8 giờ sáng, sinh viên "Nguyen Van A" với mã số 20240001, `Professor`, và Giáo sư "Dr. Tran" dạy ba khóa học.

Xác định mỗi mục là một LỚP hay một ĐỐI TƯỢNG.

> [!success]- Show Answer
> > | Mục | Lớp hay Đối tượng? |
> > |---|---|
> > | `Course` | Lớp (bản thiết kế cho tất cả các khóa học) |
> > | `Student` | Lớp (bản thiết kế cho tất cả sinh viên) |
> > | "Programming 2" (Thứ Ba 8 AM) | Đối tượng (một thể hiện khóa học cụ thể) |
> > | "Nguyen Van A" (ID 20240001) | Đối tượng (một thể hiện sinh viên cụ thể) |
> > | `Professor` | Lớp (bản thiết kế cho tất cả giáo sư) |
> > | "Dr. Tran" (dạy 3 khóa học) | Đối tượng (một thể hiện giáo sư cụ thể) |
> > 
> > Quy tắc: Nếu nó mô tả một danh mục các thứ có cấu trúc chung, nó là một lớp. Nếu nó là một thứ cụ thể với các giá trị thực tế, nó là một đối tượng.

### Bài tập 6: Xác định Mối quan hệ — IS-A, HAS-A, USES
Xác định mối quan hệ cho mỗi cặp:
1. Một chiếc xe hơi và vô lăng của nó
2. Một tài khoản checking và một tài khoản ngân hàng
3. Một hàm in và một đối tượng tài liệu
4. Một ngôi nhà và các phòng của nó
5. Một sinh viên và một thẻ thư viện

> [!success]- Show Answer
> > | Cặp | Mối quan hệ | Kiểu |
> > |---|---|---|
> > | Xe hơi ↔ Vô lăng | Một vô lăng IS PART OF một chiếc xe hơi | HAS-A (Hợp thành) |
> > | Checking Account ↔ Bank Account | Một checking account IS-A bank account | IS-A (Kế thừa) |
> > | Hàm in ↔ Tài liệu | Một hàm in USES một tài liệu | USES (Phụ thuộc) |
> > | Nhà ↔ Phòng | Một phòng IS PART OF một ngôi nhà | HAS-A (Hợp thành) |
> > | Sinh viên ↔ Thẻ thư viện | Một sinh viên HAS-A thẻ thư viện | HAS-A (Tập hợp — thẻ có thể tồn tại độc lập) |
> > 
> > Phân biệt chính: Hợp thành (HAS-A nơi bộ phận không thể tồn tại độc lập — các phòng không tồn tại sau khi phá hủy) vs Tập hợp (HAS-A nơi bộ phận có thể tồn tại độc lập — một thẻ thư viện tồn tại ngay cả khi sinh viên tốt nghiệp).

### Bài tập 7: Thiết kế từ Đầu — Hệ thống Thư viện
**Kịch bản:** Thiết kế một hệ thống quản lý thư viện. Thư viện có sách (mỗi sách có tiêu đề, tác giả, ISBN và trạng thái sẵn có). Thành viên có thể mượn và trả sách. Một số thành viên là sinh viên (có mã sinh viên và khóa học) và một số là giảng viên (có khoa và mã nhân viên). Một thủ thư quản lý danh mục. Thư viện tính tiền phạt cho việc trả muộn.

Xác định TẤT CẢ các lớp ứng viên và mối quan hệ của chúng. Chỉ rõ các mối quan hệ IS-A, HAS-A và USES. Với mỗi lớp, liệt kê 2-3 thành viên dữ liệu chính và 2-3 phương thức chính.

> [!success]- Show Answer
> > **Các lớp ứng viên và Mối quan hệ:**
> > 
> > | Lớp | Dữ liệu chính | Phương thức chính | Mối quan hệ |
> > |---|---|---|---|
> > | `Book` | title, author, ISBN, isAvailable | `checkOut()`, `returnBook()`, `isOverdue()` | USES `Date` cho ngày đến hạn |
> > | `Member` (trừu tượng) | name, memberID, borrowedBooks[] | `borrow(Book)`, `returnBook(Book)` | HAS-A danh sách `Book` |
> > | `Student` | studentID, course | (kế thừa từ Member) | IS-A `Member` |
> > | `Faculty` | department, employeeID | (kế thừa từ Member) | IS-A `Member` |
> > | `Librarian` | staffID, shift | `addBook(Book)`, `removeBook(ISBN)`, `collectFine(Member, amount)` | USES `Book`, USES `Member` |
> > | `Catalog` | books[] | `searchByTitle(string)`, `searchByAuthor(string)` | HAS-A tập hợp `Book` |
> > | `Loan` | book, member, dueDate, returnDate | `calculateFine()`, `isLate()` | USES `Book`, USES `Member`, USES `Date` |
> > | `Fine` | member, amount, reason, isPaid | `pay()`, `waive()` | USES `Member` |
> > 
> > **Hệ thống phân cấp Kế thừa:** `Member` (siêu lớp) → `Student` và `Faculty` (lớp con). Mối quan hệ IS-A này có nghĩa là sinh viên và giảng viên chia sẻ tất cả các tính năng thành viên nhưng thêm các chuyên biệt hóa riêng.
> > 
> > **Hợp thành:** `Catalog` HAS-A tập hợp `Book`. Các cuốn sách tồn tại bên trong catalog.
> > 
> > **Phụ thuộc:** `Loan` USES `Book` và `Member` — chúng được truyền vào nhưng không được sở hữu bởi Loan.
> > 
> > **Luồng thao tác chính:** `Student.borrow(book)` → kiểm tra sẵn có → tạo `Loan` → cập nhật `book.isAvailable` → nếu quá hạn, tạo `Fine`. Mỗi bước là một đối tượng gửi một thông điệp đến đối tượng khác.
