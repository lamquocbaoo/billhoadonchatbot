import streamlit as st
from datetime import datetime
from openai import OpenAI

# =====================================================
# CẤU HÌNH
# =====================================================

st.set_page_config(
    page_title="Trà Sữa BaoBao",
    page_icon="🧋",
    layout="wide"
)

# =====================================================
# MENU
# =====================================================

TRA_SUA = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa matcha": 35000,
    "Trà sữa socola": 35000,
    "Trà sữa dâu": 35000,
    "Trà sữa khoai môn": 35000,
    "Trà sữa đào": 35000,
    "Trà sữa ô long": 35000
}

TOPPING = {
    "Không topping": 0,
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Thạch phô mai": 7000,
    "Kem cheese": 10000
}

SIZE = {
    "Size M": 0,
    "Size L": 5000,
    "Size XL": 10000
}

MON_THEM = {
    "Không thêm món": 0,
    "Bánh flan": 15000,
    "Bánh tiramisu": 25000,
    "Bánh kem mini": 20000,
    "Khoai tây chiên": 25000,
    "Xúc xích": 15000
}

# =====================================================
# HÀM ĐỊNH DẠNG TIỀN
# =====================================================

def tien(v):
    return f"{v:,.0f} VNĐ"


# =====================================================
# HÌNH ẢNH
# =====================================================

try:
    st.image("IMG_2995.jpeg", use_container_width=True)
except:
    st.info("Không tìm thấy IMG_2995.jpeg")


# =====================================================
# TIÊU ĐỀ
# =====================================================

st.title("🧋 Trà Sữa BaoBao")
st.caption("Ứng dụng tính hóa đơn và chatbot AI")

st.divider()


# =====================================================
# THÔNG TIN KHÁCH
# =====================================================

st.header("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)


# =====================================================
# CHỌN TRÀ SỮA
# =====================================================

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


# =====================================================
# MÓN THÊM
# =====================================================

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
                x for x in MON_THEM
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


# =====================================================
# TÍNH TIỀN
# =====================================================

gia_tra_sua = TRA_SUA[loai_tra_sua]
gia_topping = TOPPING[topping]
gia_size = SIZE[size_ly]

gia_mot_ly = (
    gia_tra_sua
    + gia_topping
    + gia_size
)

tien_tra_sua = gia_mot_ly * so_luong

gia_mon_them = MON_THEM[mon_them]

tien_mon_them = (
    gia_mon_them
    * so_luong_mon_them
)

tong_tien = (
    tien_tra_sua
    + tien_mon_them
)


# =====================================================
# HIỂN THỊ ĐƠN
# =====================================================

st.divider()

st.header("📋 Nội dung đơn hàng")

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


# =====================================================
# CHI TIẾT GIÁ
# =====================================================

st.subheader("💰 Chi tiết thanh toán")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Tiền trà sữa",
        tien(tien_tra_sua)
    )

with c2:

    st.metric(
        "Tiền món thêm",
        tien(tien_mon_them)
    )

with c3:

    st.metric(
        "TỔNG THANH TOÁN",
        tien(tong_tien)
    )


# =====================================================
# THANH TOÁN
# =====================================================

st.divider()

st.header("💳 Thanh toán")

phuong_thuc = st.radio(
    "Phương thức thanh toán",
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


# =====================================================
# HÓA ĐƠN
# =====================================================

if xac_nhan:

    if not ten_khach.strip():

        st.error(
            "❌ Vui lòng nhập tên khách hàng."
        )

    else:

        thoi_gian = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        if phuong_thuc == "💵 Tiền mặt":
            phuong_thuc_text = "Tiền mặt"
        else:
            phuong_thuc_text = "Chuyển khoản"

        st.success(
            "✅ Thanh toán thành công!"
        )

        st.divider()

        st.subheader(
            "🧾 HÓA ĐƠN THANH TOÁN"
        )

        st.markdown(
            f"""
            <div style="
                text-align:center;
                padding:15px;
                border:2px solid #333;
                border-radius:10px;
            ">
                <h2>🧋 TRÀ SỮA BAOBAO</h2>
                <p>HÓA ĐƠN THANH TOÁN</p>
            </div>
            """,
            unsafe_allow_html=True
        )

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
- Đơn giá: {tien(gia_mot_ly)}
- Thành tiền: **{tien(tien_tra_sua)}**
"""
        )

        if them_mon == "Có":

            st.write(
                f"""
**🍰 {mon_them}**

- Số lượng: {so_luong_mon_them}
- Đơn giá: {tien(gia_mon_them)}
- Thành tiền: **{tien(tien_mon_them)}**
"""
            )

        st.divider()

        st.markdown(
            f"## 💰 TỔNG: {tien(tong_tien)}"
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
                background:#333;
                color:white;
                border:none;
                border-radius:8px;
                font-size:16px;
            ">
            🖨️ IN HÓA ĐƠN
            </button>
            """,
            unsafe_allow_html=True
        )


# =====================================================
# CHATBOT
# =====================================================

st.divider()

st.header("🤖 Chatbot Trà Sữa BaoBao")

st.caption(
    "Hỏi về menu, giá, topping, size, "
    "gợi ý món hoặc tính tiền."
)


# =====================================================
# KHỞI TẠO LỊCH SỬ
# =====================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# =====================================================
# HIỂN THỊ LỊCH SỬ
# =====================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# =====================================================
# NÚT NHANH
# =====================================================

q1, q2, q3, q4 = st.columns(4)

with q1:

    menu_button = st.button(
        "📋 Xem menu",
        use_container_width=True
    )

with q2:

    order_button = st.button(
        "🧾 Xem đơn",
        use_container_width=True
    )

with q3:

    suggest_button = st.button(
        "💡 Gợi ý món",
        use_container_width=True
    )

with q4:

    clear_button = st.button(
        "🗑️ Xóa chat",
        use_container_width=True
    )


# =====================================================
# XỬ LÝ NÚT NHANH
# =====================================================

if clear_button:

    st.session_state.messages = []

    st.rerun()


if menu_button:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": "Cho tôi xem menu và giá."
        }
    )

    st.session_state.quick_question = True


if order_button:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": "Hãy xem và phân tích đơn hàng hiện tại."
        }
    )

    st.session_state.quick_question = True


if suggest_button:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": "Hãy gợi ý cho tôi một món phù hợp."
        }
    )

    st.session_state.quick_question = True


# =====================================================
# NHẬP CHAT
# =====================================================

user_question = st.chat_input(
    "Nhập câu hỏi..."
)


if user_question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    st.session_state.quick_question = True


# =====================================================
# GỌI AI
# =====================================================

if st.session_state.get("quick_question", False):

    st.session_state.quick_question = False

    # ---------------------------------------------
    # API KEY
    # ---------------------------------------------

    try:

        api_key = st.secrets["OPENAI_API_KEY"]

        client = OpenAI(
            api_key=api_key
        )

    except Exception:

        client = None


    # ---------------------------------------------
    # Nếu chưa có API
    # ---------------------------------------------

    if client is None:

        answer = """
⚠️ **Chatbot chưa được kết nối AI.**

Bạn hãy tạo:

`.streamlit/secrets.toml`

với nội dung:

```toml
OPENAI_API_KEY = "API_KEY_CUA_BAN"
