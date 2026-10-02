import streamlit as st
from datetime import datetime

# =========================================================
# CẤU HÌNH
# =========================================================

st.set_page_config(
    page_title="Trà Sữa BaoBao",
    page_icon="🧋",
    layout="wide"
)

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


# =========================================================
# HÀM TIỀN
# =========================================================

def money(value):
    return f"{value:,.0f} VNĐ"


# =========================================================
# ẢNH
# =========================================================

try:
    st.image("IMG_2995.jpeg", use_container_width=True)
except:
    st.warning("Không tìm thấy ảnh IMG_2995.jpeg")


# =========================================================
# TIÊU ĐỀ
# =========================================================

st.title("🧋 TRÀ SỮA BAOBAO")
st.caption("Tính hóa đơn và trợ lý chatbot")

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
# CHỌN TRÀ SỮA
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
    "Có muốn thêm món không?",
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


# =========================================================
# TÍNH TIỀN
# =========================================================

gia_tra_sua = TRA_SUA[loai_tra_sua]
gia_topping = TOPPING[topping]
gia_size = SIZE[size_ly]

gia_mot_ly = (
    gia_tra_sua
    + gia_topping
    + gia_size
)

tien_tra_sua = (
    gia_mot_ly
    * so_luong
)

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

c1, c2 = st.columns(2)

with c1:

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


with c2:

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
# GIÁ
# =========================================================

st.subheader("💰 Chi tiết thanh toán")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Tiền trà sữa",
        money(tien_tra_sua)
    )

with c2:

    st.metric(
        "Tiền món thêm",
        money(tien_mon_them)
    )

with c3:

    st.metric(
        "TỔNG THANH TOÁN",
        money(tong_tien)
    )


# =========================================================
# THANH TOÁN
# =========================================================

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


# =========================================================
# HÓA ĐƠN
# =========================================================

if xac_nhan:

    if not ten_khach.strip():

        st.error(
            "❌ Vui lòng nhập tên khách hàng."
        )

    else:

        thoi_gian = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        phuong_thuc_text = (
            "Tiền mặt"
            if phuong_thuc == "💵 Tiền mặt"
            else "Chuyển khoản"
        )

        st.success(
            "✅ Thanh toán thành công!"
        )

        st.divider()

        st.subheader("🧾 HÓA ĐƠN")

        st.markdown(
            f"""
            <div style="
                text-align:center;
                padding:15px;
                border:2px solid black;
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

        st.write("### 🧋 Trà sữa")

        st.write(
            f"""
            **{loai_tra_sua}**

            - Size: {size_ly}
            - Số lượng: {so_luong}
            - Đường: {muc_duong}
            - Đá: {muc_da}
            - Topping: {topping}
            - Đơn giá: {money(gia_mot_ly)}
            - Thành tiền: **{money(tien_tra_sua)}**
            """
        )

        if them_mon == "Có":

            st.write(
                f"""
                **🍰 {mon_them}**

                - Số lượng: {so_luong_mon_them}
                - Đơn giá: {money(gia_mon_them)}
                - Thành tiền: **{money(tien_mon_them)}**
                """
            )

        st.divider()

        st.markdown(
            f"# 💰 TỔNG: {money(tong_tien)}"
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


# =========================================================
# CHATBOT
# =========================================================

st.divider()

st.header("🤖 CHATBOT TRÀ SỮA BAOBAO")

st.caption(
    "Chatbot tự động tư vấn menu và tính tiền."
)


# =========================================================
# LỊCH SỬ CHAT
# =========================================================

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []


# =========================================================
# HÀM CHATBOT
# =========================================================

def chatbot(question):

    q = question.lower().strip()

    # -----------------------------------------------------
    # CHÀO HỎI
    # -----------------------------------------------------

    if any(x in q for x in [
        "xin chào",
        "hello",
        "hi",
        "chào"
    ]):

        return (
            "👋 Xin chào! Mình là chatbot của "
            "Trà Sữa BaoBao.\n\n"
            "Bạn có thể hỏi mình:\n"
            "- 📋 Menu và giá\n"
            "- 💰 Tính tiền\n"
            "- 🧋 Gợi ý món\n"
            "- 🍬 Topping\n"
            "- 📏 Size\n"
            "- 🧾 Đơn hàng hiện tại"
        )


    # -----------------------------------------------------
    # MENU
    # -----------------------------------------------------

    if (
        "menu" in q
        or "thực đơn" in q
        or "có món gì" in q
    ):

        text = "📋 **MENU TRÀ SỮA BAOBAO**\n\n"

        for name, price in TRA_SUA.items():

            text += (
                f"🧋 {name}: "
                f"**{money(price)}**\n"
            )

        text += "\n🍬 **TOPPING**\n"

        for name, price in TOPPING.items():

            if price == 0:

                text += f"- {name}\n"

            else:

                text += (
                    f"- {name}: "
                    f"{money(price)}\n"
                )

        text += "\n📏 **SIZE**\n"

        for name, price in SIZE.items():

            if price == 0:

                text += f"- {name}\n"

            else:

                text += (
                    f"- {name}: +"
                    f"{money(price)}\n"
                )

        text += "\n🍰 **MÓN THÊM**\n"

        for name, price in MON_THEM.items():

            if price == 0:

                continue

            text += (
                f"- {name}: "
                f"{money(price)}\n"
            )

        return text


    # -----------------------------------------------------
    # TOPPING
    # -----------------------------------------------------

    if (
        "topping" in q
        or "trân châu" in q
    ):

        text = "🍬 **Topping hiện có:**\n\n"

        for name, price in TOPPING.items():

            text += (
                f"- {name}: "
                f"{money(price)}\n"
            )

        return text


    # -----------------------------------------------------
    # SIZE
    # -----------------------------------------------------

    if "size" in q:

        return (
            "📏 **Size ly:**\n\n"
            "- Size M: Giá gốc\n"
            "- Size L: +5.000 VNĐ\n"
            "- Size XL: +10.000 VNĐ"
        )


    # -----------------------------------------------------
    # MÓN THÊM
    # -----------------------------------------------------

    if (
        "món thêm" in q
        or "món ăn" in q
        or "bánh" in q
    ):

        text = "🍰 **Món thêm:**\n\n"

        for name, price in MON_THEM.items():

            if price == 0:
                continue

            text += (
                f"- {name}: "
                f"{money(price)}\n"
            )

        return text


    # -----------------------------------------------------
    # ĐƠN HIỆN TẠI
    # -----------------------------------------------------

    if (
        "đơn hiện tại" in q
        or "đơn hàng" in q
        or "tổng tiền" in q
        or "bao nhiêu tiền" in q
    ):

        text = (
            "🧾 **ĐƠN HÀNG HIỆN TẠI**\n\n"
            f"👤 Khách: "
            f"{ten_khach or 'Chưa nhập'}\n\n"
            f"🧋 Món: {loai_tra_sua}\n"
            f"🔢 Số lượng: {so_luong}\n"
            f"📏 Size: {size_ly}\n"
            f"🍬 Đường: {muc_duong}\n"
            f"🧊 Đá: {muc_da}\n"
            f"🍬 Topping: {topping}\n"
        )

        if them_mon == "Có":

            text += (
                f"🍰 Món thêm: "
                f"{mon_them} × "
                f"{so_luong_mon_them}\n"
            )

        else:

            text += "🍰 Món thêm: Không\n"

        text += (
            f"\n💰 **TỔNG: "
            f"{money(tong_tien)}**"
        )

        return text


    # -----------------------------------------------------
    # GỢI Ý MÓN
    # -----------------------------------------------------

    if (
        "gợi ý" in q
        or "tư vấn" in q
        or "nên uống" in q
        or "uống gì" in q
    ):

        return (
            "💡 **Một số lựa chọn:**\n\n"
            "🧋 Trà sữa truyền thống – "
            f"{money(30000)}\n"
            "→ Vị truyền thống, dễ uống.\n\n"
            "🍵 Trà sữa matcha – "
            f"{money(35000)}\n"
            "→ Vị matcha đặc trưng.\n\n"
            "🍫 Trà sữa socola – "
            f"{money(35000)}\n"
            "→ Vị socola ngọt, thơm.\n\n"
            "🍓 Trà sữa dâu – "
            f"{money(35000)}\n"
            "→ Vị dâu dễ uống."
        )


    # -----------------------------------------------------
    # GIÁ TỪNG MÓN
    # -----------------------------------------------------

    for name, price in TRA_SUA.items():

        if name.lower() in q:

            return (
                f"🧋 **{name}** có giá "
                f"**{money(price)}** cho Size M.\n\n"
                "Size L cộng 5.000 VNĐ.\n"
                "Size XL cộng 10.000 VNĐ."
            )


    # -----------------------------------------------------
    # NGÂN SÁCH
    # -----------------------------------------------------

    if (
        "50k" in q
        or "50000" in q
        or "50.000" in q
    ):

        return (
            "💰 Nếu ngân sách khoảng 50.000 VNĐ, "
            "bạn có thể chọn:\n\n"
            "🧋 Trà sữa truyền thống + "
            "Trân châu đen = 35.000 VNĐ\n\n"
            "🧋 Trà sữa matcha + "
            "Trân châu đen = 40.000 VNĐ\n\n"
            "🧋 Trà sữa socola + "
            "Pudding trứng = 42.000 VNĐ"
        )


    # -----------------------------------------------------
    # CẢM ƠN
    # -----------------------------------------------------

    if (
        "cảm ơn" in q
        or "thanks" in q
    ):

        return (
            "🥰 Không có gì! "
            "Cảm ơn bạn đã ghé Trà Sữa BaoBao!"
        )


    # -----------------------------------------------------
    # KHÔNG HIỂU
    # -----------------------------------------------------

    return (
        "🤖 Mình chưa hiểu câu hỏi này.\n\n"
        "Bạn có thể thử:\n"
        "• “Cho tôi xem menu”\n"
        "• “Topping có gì?”\n"
        "• “Size L bao nhiêu?”\n"
        "• “Gợi ý món cho tôi”\n"
        "• “Đơn hiện tại bao nhiêu tiền?”"
    )


# =========================================================
# HIỂN THỊ CHAT CŨ
# =========================================================

for item in st.session_state.chat_history:

    with st.chat_message(item["role"]):

        st.markdown(item["content"])


# =========================================================
# Ô CHAT
# =========================================================

question = st.chat_input(
    "Nhập câu hỏi cho chatbot..."
)


# =========================================================
# XỬ LÝ CHAT
# =========================================================

if question:

    # Người dùng
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Chatbot
    answer = chatbot(question)

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()


# =========================================================
# NÚT XÓA CHAT
# =========================================================

if st.session_state.chat_history:

    if st.button(
        "🗑️ Xóa lịch sử chatbot"
    ):

        st.session_state.chat_history = []

        st.rerun()


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🧋 Trà Sữa BaoBao | Hệ thống tính hóa đơn"
)
