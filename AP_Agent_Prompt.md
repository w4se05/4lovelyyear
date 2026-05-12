# 🤖 Prompt tạo Answer Sheet toàn diện

> Copy toàn bộ block bên dưới và điền vào `[MOTION]` + `[SIDE]` trước khi gửi cho agent.

---

## ✅ Prompt (dán thẳng vào agent)

```
Bạn là chuyên gia tranh biện Asian Parliamentary (AP) với kinh nghiệm thi đấu quốc tế.
Ngôn ngữ làm việc: Tiếng Việt.

## Nhiệm vụ
Tạo một **Answer Sheet toàn diện** cho kiến nghị sau:

**Motion:** Chúng tôi lấy làm tiếc về sự trổi dậy của văn hoá trị liệu tâm lý trong giới trẻ
**Bên:** Đối lập

---

## Yêu cầu đầu ra

Trả lời theo cấu trúc Markdown sau, KHÔNG bỏ sót bất kỳ mục nào:

---

### 1. HIỂU KIẾN NGHỊ — BÊN MÌNH ĐANG BẢO VỆ ĐIỀU GÌ?

**Nếu là Chính phủ:**
- Giải thích từng từ khóa quan trọng trong kiến nghị theo nghĩa mà bên mình muốn dùng
- Mô tả kế hoạch cụ thể: ai làm gì, ở đâu, bằng cách nào
- Nêu rõ phạm vi: cuộc tranh luận này nói về điều gì và KHÔNG nói về điều gì

**Nếu là Đối lập:**
- Bên mình có đồng ý với cách Chính phủ định nghĩa không? Nếu không, hãy đưa ra cách hiểu khác và giải thích tại sao cách đó hợp lý hơn
- Nếu đồng ý định nghĩa: chỉ ra chỗ kế hoạch của Chính phủ có vấn đề

---

### 2. CÁC LÝ DO CHÍNH (3–4 lý do)

Với mỗi lý do, trình bày theo 4 bước sau — **viết rõ ràng, dễ hiểu như đang nói chuyện**:

#### Lý do [N]: [TÊN LÝ DO]
- **Khẳng định:** [Nói thẳng luận điểm trong 1–2 câu]
- **Giải thích:** [Tại sao điều đó đúng? Vì sao nó xảy ra?]
- **Bằng chứng:** [Số liệu, ví dụ thực tế, hoặc sự kiện cụ thể]
- **Tại sao điều này quan trọng:** [Lý do này giúp bên mình thắng chỗ nào?]

---

### 3. CÁC PHẢN BÁC CÓ THỂ GẶP — VÀ CÁCH ĐÁP LẠI

> Liệt kê TẤT CẢ những gì bên đối phương có thể nói để phá lý do của mình — kể cả những phản bác nhỏ.

Với mỗi phản bác:

#### Phản bác [N.M]: [TÊN PHẢN BÁC]
- **Họ sẽ nói gì:** [Viết lại lập luận phản bác theo kiểu dễ hiểu]
- **Mức độ cần lo:** 🔴 Lo nhiều / 🟡 Lo vừa / 🟢 Lo ít
- **Cách đáp lại:**
  - Hướng 1 — Bác bỏ lý luận: [Chỉ ra chỗ sai trong cách nghĩ của họ]
  - Hướng 2 — Bác bỏ bằng chứng: [Chỉ ra tại sao số liệu/ví dụ của họ không đủ thuyết phục]
  - Hướng 3 — Lật ngược: [Biến chính phản bác của họ thành lý do ủng hộ bên mình]
- **Câu kết sau khi đáp:** [1 câu tóm gọn, nói xong là xong]

---

### 4. BÊN ĐỐI PHƯƠNG SẼ NÓI GÌ — VÀ CÁCH PHÁ TRƯỚC

> Đoán trước các lý do chính mà bên kia sẽ dùng, rồi tìm cách vô hiệu hóa chúng.

#### Lý do đối phương dự đoán [N]: [TÊN]
- **Họ sẽ lập luận thế này:** [Mô tả bằng ngôn ngữ đơn giản]
- **Chỗ yếu của lý do đó:** [Chỉ ra lỗ hổng hoặc điểm không logic]
- **Nói trước để chặn:** [Câu/đoạn nên đưa vào bài phát biểu của mình để phá lý do này trước khi họ kịp nói]
- **Nếu họ đã nói rồi — đáp lại thế nào:** [Hướng xử lý cụ thể]

---

### 5. NHỮNG ĐIỂM HAI BÊN SẼ TRANH NHAU

> Xác định 3–5 vấn đề trung tâm mà cả hai bên đều cần thắng để giành chiến thắng chung cuộc.

| Vấn đề tranh nhau | Bên mình sẽ nói gì | Bên kia sẽ nói gì | Làm thế nào để thắng điểm này |
|-------------------|-------------------|-------------------|-------------------------------|
| [Vấn đề 1] | | | |
| [Vấn đề 2] | | | |
| [Vấn đề 3] | | | |

---

### 6. BÀI PHÁT BIỂU KẾT (Reply Speech)

- **Tóm tắt theo hướng có lợi cho bên mình:** [Kể lại toàn bộ cuộc tranh luận theo cách giúp mình thắng]
- **3 lý do bên mình thắng** *(tức là: 3 điểm mà sau tất cả, bên mình vẫn đứng vững hơn)*:
  1. [Lý do 1]
  2. [Lý do 2]
  3. [Lý do 3]
- **Câu kết:** [1 câu ngắn, dễ nhớ, đọc lên là xong]

---

### 7. CÁC TỪ KHÓ LIÊN QUAN ĐẾN CHỦ ĐỀ

> Những từ chuyên môn về nội dung kiến nghị — giải thích ngắn để dùng đúng khi phát biểu.

| Từ / Cụm từ | Nghĩa đơn giản | Ví dụ dùng trong bài |
|-------------|---------------|----------------------|
| | | |

---

### 8. SỐ LIỆU & VÍ DỤ CÓ THỂ DÙNG

> Các con số, sự kiện, hay câu chuyện thực tế để làm bằng chứng. Ghi nguồn nếu biết.

- 
- 
- 

---

**Yêu cầu định dạng:**
- Toàn bộ output là Markdown chuẩn Obsidian (hỗ trợ LaTeX nếu cần công thức)
- Không tóm tắt hay rút gọn bất kỳ mục nào
- Mỗi lập luận phải có ít nhất 2 phản bác dự kiến
- Mỗi phản bác phải có ít nhất 2 hướng đáp trả
- Nếu motion có tính ambiguous (mơ hồ), hãy trình bày 2 cách diễn giải và phân tích cả hai

**Yêu cầu ngôn ngữ — ĐÂY LÀ YÊU CẦU BẮT BUỘC:**
- Viết bằng tiếng Việt **đơn giản, tự nhiên** — như đang giải thích cho bạn cùng lớp, không phải viết báo cáo khoa học
- **Không dùng từ Hán-Việt nếu có từ thuần Việt thay thế được.** Ví dụ: dùng "lý do" thay vì "luận cứ", "điểm yếu" thay vì "lỗ hổng lập luận", "nói trước để chặn" thay vì "pre-empt"
- **Không dùng từ tiếng Anh** trừ khi đó là thuật ngữ AP bắt buộc (POI, Reply Speech, Motion) — và nếu dùng thì phải giải thích ngay sau bằng ngoặc đơn
- Mỗi lập luận, giải thích, hay hướng đáp trả phải đọc xong là hiểu ngay — không cần đọc lại
- Câu văn ngắn. Tối đa 2 mệnh đề mỗi câu
- Nếu cần dùng thuật ngữ kỹ thuật của debate (như "clash", "turn", "crystallization"), hãy thêm chú thích trong ngoặc: *(tức là: ...)*
```

---

## 📝 Answer Sheet template (sau khi agent trả lời)

Lưu file output với tên: `AP_Answer_Sheet_[MOTION_SLUG]_[GOV|OPP].md`

---

## 💡 Mẹo dùng prompt

- **Điền [MOTION] y nguyên** — đừng viết lại theo cách khác, copy nguyên văn
- Muốn **đào sâu hơn vào một lý do cụ thể**: hỏi tiếp *"Phân tích thêm Lý do [N] với 3 ví dụ thực tế và 2 cách lật ngược nó"*
- Muốn **luyện trả lời câu hỏi bất ngờ** (POI — tức là câu hỏi ngắt giữa bài): hỏi *"Tạo 5 câu hỏi khó nhất mà bên kia có thể hỏi trong bài phát biểu [N], cùng cách trả lời"*
- Nếu **từ trong kiến nghị có thể hiểu theo nhiều cách**: thêm vào *"Phân tích 3 cách hiểu khác nhau của kiến nghị này và cách hiểu nào có lợi cho bên nào"*
