import streamlit as st
from datetime import datetime
from openai import OpenAI

# =========================================================
# CẤU HÌNH
# =========================================================

st.set_page_config(
    page_title="Trà Sữa BaoBao",
    page_icon="🧋",
    layout="wide"
)

# =========================================================
# HÌNH ẢNH
# =========================================================

try:
    st.image("IMG_2995.jpeg", use_container_width=True)
except:
    pass

# =========================================================
# MENU
# =========================================================

TRA_SUA = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa matcha": 35000,
    "Trà sữa socola": 35000,
    "Trà sữa dâu": 35000,
    "Trà sữa khoai môn": 35000,
    "Trà sữa đào": 35000,
    "Trà sữa ô long": 35000,
}

TOPPING = {
    "Không topping": 0,
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Thạch phô mai": 7000,
    "Kem cheese": 10000,
}

SIZE = {
    "Size M": 0,
    "Size L": 5000,
    "Size XL": 10000,
}

MON_THEM = {
    "Không thêm món": 0,
    "Bánh flan": 15000,
    "Bánh tiramisu": 25000,
    "Bánh kem mini": 20000,
    "Khoai tây chiên": 25000,
    "Xúc xích": 15000,
}

# =========================================================
# TIỆN ÍCH
# =========================================================

def vnd(number):
    return f"{number:,.0f} VNĐ"


def tao_menu_text():
    text = "=== TRÀ SỮA ===\n"

    for name, price in TRA_SUA.items():
        text += f"- {name}: {vnd(price)}\n"

    text += "\n=== TOPPING ===\n"

    for name, price in TOPPING.items():
        text += f"- {name}: {vnd(price)}\n"

    text += "\n=== SIZE ===\n"

    for name, price in SIZE.items():
        text += f"- {name}: +{vnd(price)}\n"

    text += "\n=== MÓN THÊM ===\n"

    for name, price in MON_THEM.items():
        text += f"- {name}: {vnd(price)}\n"

    return text


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_order" not in st.session_state:
    st.session_state.chat_order = []

if "last_bill" not in st.session_state:
    st.session_state.last_bill = None


# =========================================================
# TIÊU ĐỀ
# =========================================================

st.title("🧋 Trà Sữa BaoBao")

st.caption(
    "Ứng dụng quản lý đơn hàng, tính tiền và chatbot AI"
)

st.divider()


# =========================================================
# THÔNG TIN KHÁCH
# =========================================================

st.header("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)


# =========================================================
# CHỌN MÓN
# =========================================================

st.header("🧋 Chọn món")

col1, col2 = st.columns(2)

with col1:

    loai_tra_sua = st.selectbox(
        "Loại trà sữa",
        list(TRA_SUA.keys())
    )

    so_luong = st.number_input(
        "Số lượng",
        min_value=1,
        max_value=50,
        value=1,
        step=1
    )

    muc_duong = st.selectbox(
        "Mức độ đường",
        [
            "100% đường",
            "70% đường",
            "50% đường",
            "30% đường",
            "Không đường"
        ]
    )


with col2:

    muc_da = st.selectbox(
        "Mức độ đá",
        [
            "100% đá",
            "70% đá",
            "50% đá",
            "30% đá",
            "Không đá"
        ]
    )

    topping = st.selectbox(
        "Topping",
        list(TOPPING.keys())
    )

    size_ly = st.selectbox(
        "Size ly",
        list(SIZE.keys())
    )


# =========================================================
# MÓN THÊM
# =========================================================

st.subheader("🍰 Món thêm")

them_mon = st.radio(
    "Bạn có muốn thêm món không?",
    ["Không", "Có"],
    horizontal=True
)

mon_them = "Không thêm món"
so_luong_mon_them = 0

if them_mon == "Có":

    col3, col4 = st.columns(2)

    with col3:

        mon_them = st.selectbox(
            "Chọn món thêm",
            [
                x for x in MON_THEM.keys()
                if x != "Không thêm món"
            ]
        )

    with col4:

        so_luong_mon_them = st.number_input(
            "Số lượng món thêm",
            min_value=1,
            max_value=20,
            value=1,
            step=1
        )


# =========================================================
# TÍNH TIỀN
# =========================================================

gia_tra_sua = TRA_SUA[loai_tra_sua]
gia_topping = TOPPING[topping]
gia_size = SIZE[size_ly]

tien_mot_ly = (
    gia_tra_sua
    + gia_topping
    + gia_size
)

tien_tra_sua = tien_mot_ly * so_luong

gia_mon_them = MON_THEM[mon_them]

tien_mon_them = (
    gia_mon_them
    * so_luong_mon_them
)

tong_tien = (
    tien_tra_sua
    + tien_mon_them
)


# =========================================================
# ĐƠN HÀNG
# =========================================================

st.divider()

st.header("📋 Nội dung đơn hàng")

if not ten_khach.strip():
    st.warning("Vui lòng nhập tên khách hàng.")

col_a, col_b = st.columns(2)

with col_a:

    st.write(
        "**👤 Khách hàng:**",
        ten_khach if ten_khach else "Chưa nhập"
    )

    st.write(
        "**🧋 Trà sữa:**",
        loai_tra_sua
    )

    st.write(
        "**📏 Size:**",
        size_ly
    )

    st.write(
        "**🔢 Số lượng:**",
        so_luong
    )


with col_b:

    st.write(
        "**🍬 Đường:**",
        muc_duong
    )

    st.write(
        "**🧊 Đá:**",
        muc_da
    )

    st.write(
        "**🧋 Topping:**",
        topping
    )

    if them_mon == "Có":

        st.write(
            f"**🍰 Món thêm:** "
            f"{mon_them} × {so_luong_mon_them}"
        )

    else:

        st.write(
            "**🍰 Món thêm:** Không"
        )


# =========================================================
# THANH TOÁN
# =========================================================

st.subheader("💰 Chi tiết thanh toán")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Tiền trà sữa",
        vnd(tien_tra_sua)
    )

with col2:

    st.metric(
        "Tiền món thêm",
        vnd(tien_mon_them)
    )

with col3:

    st.metric(
        "TỔNG THANH TOÁN",
        vnd(tong_tien)
    )


# =========================================================
# THANH TOÁN
# =========================================================

st.divider()

st.header("💳 Thanh toán")

phuong_thuc = st.radio(
    "Chọn phương thức thanh toán",
    [
        "💵 Tiền mặt",
        "🏦 Chuyển khoản"
    ],
    horizontal=True
)

xac_nhan = st.button(
    "✅ THANH TOÁN & XUẤT HÓA ĐƠN",
    use_container_width=True,
    type="primary"
)


# =========================================================
# HÓA ĐƠN
# =========================================================

if xac_nhan:

    if not ten_khach.strip():

        st.error(
            "❌ Vui lòng nhập tên khách hàng trước khi thanh toán."
        )

    else:

        thoi_gian = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        if phuong_thuc == "💵 Tiền mặt":
            phuong_thuc_text = "Tiền mặt"
        else:
            phuong_thuc_text = "Chuyển khoản"

        st.session_state.last_bill = {
            "khach": ten_khach,
            "thoi_gian": thoi_gian,
            "phuong_thuc": phuong_thuc_text,
            "tra_sua": loai_tra_sua,
            "size": size_ly,
            "so_luong": so_luong,
            "duong": muc_duong,
            "da": muc_da,
            "topping": topping,
            "mon_them": mon_them,
            "sl_mon_them": so_luong_mon_them,
            "tong": tong_tien
        }

        st.success(
            "✅ Thanh toán thành công!"
        )

        st.divider()

        st.subheader(
            "🧾 HÓA ĐƠN THANH TOÁN"
        )

        st.markdown(
            """
            <div style="
                text-align:center;
                padding:10px;
                border:2px solid #333;
                border-radius:10px;
            ">
                <h2>🧋 TRÀ SỮA BAOBAO</h2>
                <p>HÓA ĐƠN THANH TOÁN</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.write(
            f"**Khách hàng:** {ten_khach}"
        )

        st.write(
            f"**Thời gian:** {thoi_gian}"
        )

        st.write(
            f"**Thanh toán:** {phuong_thuc_text}"
        )

        st.divider()

        st.write("### 🧋 Chi tiết món")

        st.write(
            f"""
            **{loai_tra_sua}**

            - Size: {size_ly}
            - Số lượng: {so_luong}
            - Đường: {muc_duong}
            - Đá: {muc_da}
            - Topping: {topping}
            - Đơn giá: {vnd(tien_mot_ly)}
            - Thành tiền: **{vnd(tien_tra_sua)}**
            """
        )

        if them_mon == "Có":

            st.write(
                f"""
                **🍰 {mon_them}**

                - Số lượng: {so_luong_mon_them}
                - Đơn giá: {vnd(gia_mon_them)}
                - Thành tiền: **{vnd(tien_mon_them)}**
                """
            )

        st.divider()

        st.markdown(
            f"""
            ## 💰 TỔNG THANH TOÁN

            # {vnd(tong_tien)}
            """
        )

        st.success(
            "🎉 Cảm ơn quý khách! Hẹn gặp lại!"
        )

        st.markdown(
            """
            <button onclick="window.print()"
                style="
                    width:100%;
                    padding:12px;
                    background-color:#333;
                    color:white;
                    border:none;
                    border-radius:8px;
                    font-size:16px;
                    cursor:pointer;
                ">
                🖨️ IN HÓA ĐƠN
            </button>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# CHATBOT AI
# =========================================================

st.divider()

st.header("🤖 Trợ lý AI - Trà Sữa BaoBao")

st.caption(
    "Bạn có thể hỏi về menu, giá, tư vấn món, "
    "tính tiền hoặc nhờ chatbot phân tích đơn hàng."
)


# =========================================================
# API OPENAI
# =========================================================

try:

    client = OpenAI(
        api_key=st.secrets["OPENAI_API_KEY"]
    )

except Exception:

    client = None


# =========================================================
# NÚT CHỨC NĂNG CHATBOT
# =========================================================

chat_col1, chat_col2, chat_col3 = st.columns(3)

with chat_col1:

    if st.button(
        "📋 Xem menu",
        use_container_width=True
    ):

        st.session_state.messages.append(
            {
                "role": "user",
                "content": "Cho tôi xem menu và giá."
            }
        )

        st.rerun()


with chat_col2:

    if st.button(
        "💰 Phân tích đơn",
        use_container_width=True
    ):

        cau_hoi = (
            "Hãy phân tích đơn hàng hiện tại "
            "và cho tôi biết tổng tiền."
        )

        st.session_state.messages.append(
            {
                "role": "user",
                "content": cau_hoi
            }
        )

        st.rerun()


with chat_col3:

    if st.button(
        "💡 Gợi ý món",
        use_container_width=True
    ):

        st.session_state.messages.append(
            {
                "role": "user",
                "content": (
                    "Hãy gợi ý một số món phù hợp "
                    "với khách hàng."
                )
            }
        )

        st.rerun()


# =========================================================
# HIỂN THỊ LỊCH SỬ
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# =========================================================
# CHAT INPUT
# =========================================================

cau_hoi = st.chat_input(
    "Ví dụ: Gợi ý cho tôi món dưới 50k..."
)


if cau_hoi:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": cau_hoi
        }
    )

    with st.chat_message("user"):

        st.markdown(cau_hoi)


# =========================================================
# XỬ LÝ CHATBOT
# =========================================================

if (
    st.session_state.messages
    and st.session_state.messages[-1]["role"] == "user"
):

    cau_hoi_hien_tai = (
        st.session_state.messages[-1]["content"]
    )

    # -----------------------------------------------------
    # Không có API
    # -----------------------------------------------------

    if client is None:

        cau_tra_loi = """
⚠️ Chatbot AI chưa được kết nối.

Bạn cần tạo file:

`.streamlit/secrets.toml`

và thêm:

`OPENAI_API_KEY = "API_KEY_CUA_BAN"`

Sau đó chạy lại ứng dụng.
"""

    else:

        # -------------------------------------------------
        # THÔNG TIN ĐƠN HIỆN TẠI
        # -------------------------------------------------

        don_hien_tai = f"""
Khách hàng: {ten_khach if ten_khach else "Chưa nhập"}

Trà sữa: {loai_tra_sua}
Số lượng: {so_luong}
Size: {size_ly}
Đường: {muc_duong}
Đá: {muc_da}
Topping: {topping}

Món thêm: {mon_them}
Số lượng món thêm: {so_luong_mon_them}

Tiền trà sữa: {vnd(tien_tra_sua)}
Tiền món thêm: {vnd(tien_mon_them)}

TỔNG: {vnd(tong_tien)}
"""

        # -------------------------------------------------
        # PROMPT
        # -------------------------------------------------

        system_prompt = f"""
Bạn là trợ lý AI của quán Trà Sữa BaoBao.

Bạn có các nhiệm vụ:

1. Tư vấn menu.
2. Tư vấn giá.
3. Gợi ý món.
4. Gợi ý topping.
5. Tư vấn size.
6. Tư vấn mức đường và đá.
7. Tính tiền.
8. Phân tích đơn hàng.
9. Gợi ý món theo ngân sách.
10. Trả lời câu hỏi thường gặp.
11. Giúp khách hiểu đơn hàng hiện tại.
12. Gợi ý combo dựa trên menu.

QUY TẮC:

- Luôn trả lời bằng tiếng Việt.
- Thân thiện, ngắn gọn.
- Có thể dùng emoji.
- Không tự tạo món.
- Không tự tạo giá.
- Chỉ sử dụng món và giá có trong MENU.
- Khi tính tiền phải tính chính xác.
- Nếu khách hỏi món không có trong menu,
  hãy nói món đó hiện chưa có.
- Nếu khách hỏi giá, phải ghi rõ VNĐ.
- Nếu khách muốn đặt món, hãy tóm tắt đơn.
- Không tự xác nhận thanh toán.
- Không yêu cầu khách cung cấp API key.

========================
MENU
========================

{tao_menu_text()}

========================
ĐƠN HÀNG HIỆN TẠI
========================

{don_hien_tai}

========================
YÊU CẦU KHÁCH
========================

{cau_hoi_hien_tai}
"""

        try:

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    }
                ]
                + st.session_state.messages,
                temperature=0.5
            )

            cau_tra_loi = (
                response.choices[0]
                .message.content
            )

        except Exception as e:

            cau_tra_loi = (
                "❌ Có lỗi khi kết nối AI.\n\n"
                f"Chi tiết: {str(e)}"
            )

    # -----------------------------------------------------
    # HIỂN THỊ
    # -----------------------------------------------------

    with st.chat_message("assistant"):

        st.markdown(cau_tra_loi)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": cau_tra_loi
        }
    )


# =========================================================
# QUẢN LÝ CHAT
# =========================================================

st.divider()

c1, c2 = st.columns(2)

with c1:

    if st.button(
        "🗑️ Xóa lịch sử chatbot",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()


with c2:

    if st.button(
        "🔄 Làm mới chatbot",
        use_container_width=True
    ):

        st.session_state.messages = []
        st.session_state.chat_order = []

        st.rerun()


# =========================================================
# THÔNG TIN CUỐI TRANG
# =========================================================

st.divider()

st.caption(
    "🧋 Trà Sữa BaoBao • Hệ thống tính hóa đơn & trợ lý AI"
)
