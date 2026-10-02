import streamlit as st
from datetime import datetime

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính hóa đơn trà sữa",
    page_icon="🧋",
    layout="wide"
)

# =========================
# DỮ LIỆU MENU
# =========================

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

# =========================
# TIÊU ĐỀ
# =========================

st.title("🧋 Trà Sữa BaoBao ")
st.caption("Ứng dụng tính tiền và xuất hóa đơn bằng Streamlit")

st.divider()

# =========================
# THÔNG TIN KHÁCH HÀNG
# =========================

st.header("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)

# =========================
# NHẬP MÓN
# =========================

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

# =========================
# CÓ THÊM MÓN KHÔNG?
# =========================

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
            [x for x in MON_THEM.keys() if x != "Không thêm món"]
        )

    with col4:
        so_luong_mon_them = st.number_input(
            "Số lượng món thêm",
            min_value=1,
            max_value=20,
            value=1,
            step=1
        )

# =========================
# TÍNH TIỀN
# =========================

gia_tra_sua = TRA_SUA[loai_tra_sua]
gia_topping = TOPPING[topping]
gia_size = SIZE[size_ly]

tien_mot_ly = gia_tra_sua + gia_topping + gia_size
tien_tra_sua = tien_mot_ly * so_luong

gia_mon_them = MON_THEM[mon_them]
tien_mon_them = gia_mon_them * so_luong_mon_them

tong_tien = tien_tra_sua + tien_mon_them

# =========================
# HIỂN THỊ ĐƠN HÀNG
# =========================

st.divider()

st.header("📋 Nội dung đơn hàng")

if not ten_khach.strip():
    st.warning("Vui lòng nhập tên khách hàng.")

col_a, col_b = st.columns(2)

with col_a:
    st.write("**👤 Khách hàng:**", ten_khach if ten_khach else "Chưa nhập")
    st.write("**🧋 Trà sữa:**", loai_tra_sua)
    st.write("**📏 Size:**", size_ly)
    st.write("**🔢 Số lượng:**", so_luong)

with col_b:
    st.write("**🍬 Đường:**", muc_duong)
    st.write("**🧊 Đá:**", muc_da)
    st.write("**🧋 Topping:**", topping)

    if them_mon == "Có":
        st.write(
            f"**🍰 Món thêm:** {mon_them} × {so_luong_mon_them}"
        )
    else:
        st.write("**🍰 Món thêm:** Không")

# =========================
# CHI TIẾT GIÁ
# =========================

st.subheader("💰 Chi tiết thanh toán")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Tiền trà sữa",
        f"{tien_tra_sua:,.0f} VNĐ"
    )

with col2:
    st.metric(
        "Tiền món thêm",
        f"{tien_mon_them:,.0f} VNĐ"
    )

with col3:
    st.metric(
        "TỔNG THANH TOÁN",
        f"{tong_tien:,.0f} VNĐ"
    )

# =========================
# THANH TOÁN
# =========================

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

# =========================
# XUẤT HÓA ĐƠN
# =========================

if xac_nhan:

    if not ten_khach.strip():
        st.error("❌ Vui lòng nhập tên khách hàng trước khi thanh toán.")

    else:
        thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if phuong_thuc == "💵 Tiền mặt":
            phuong_thuc_text = "Tiền mặt"
        else:
            phuong_thuc_text = "Chuyển khoản"

        st.success("✅ Thanh toán thành công!")

        st.divider()

        st.subheader("🧾 HÓA ĐƠN THANH TOÁN")

        # Phần thông tin cửa hàng
        st.markdown(
            """
            <div style="
                text-align:center;
                padding:10px;
                border:2px solid #333;
                border-radius:10px;
            ">
                <h2>🧋 TRÀ SỮA MILK TEA</h2>
                <p>HÓA ĐƠN THANH TOÁN</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")
        st.write(f"**Khách hàng:** {ten_khach}")
        st.write(f"**Thời gian:** {thoi_gian}")
        st.write(f"**Thanh toán:** {phuong_thuc_text}")

        st.divider()

        # =========================
        # CHI TIẾT HÓA ĐƠN
        # =========================

        st.write("### 🧋 Chi tiết món")

        st.write(
            f"""
            **{loai_tra_sua}**

            - Size: {size_ly}
            - Số lượng: {so_luong}
            - Đường: {muc_duong}
            - Đá: {muc_da}
            - Topping: {topping}
            - Đơn giá: {tien_mot_ly:,.0f} VNĐ
            - Thành tiền: **{tien_tra_sua:,.0f} VNĐ**
            """
        )

        if them_mon == "Có":
            st.write(
                f"""
                **🍰 {mon_them}**

                - Số lượng: {so_luong_mon_them}
                - Đơn giá: {gia_mon_them:,.0f} VNĐ
                - Thành tiền: **{tien_mon_them:,.0f} VNĐ**
                """
            )

        st.divider()

        st.markdown(
            f"""
            ### 💰 TỔNG THANH TOÁN: {tong_tien:,.0f} VNĐ
            """
        )

        st.success("🎉 Cảm ơn quý khách! Hẹn gặp lại!")

        # =========================
        # NÚT IN HÓA ĐƠN
        # =========================

        st.markdown(
            """
            <script>
            function printBill() {
                window.print();
            }
            </script>

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
