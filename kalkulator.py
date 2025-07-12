import streamlit as st

st.title("Kalkulator Sederhana")

# Input angka
num1 = st.number_input("Masukkan angka pertama:", value=0.0, format="%.2f")
num2 = st.number_input("Masukkan angka kedua:", value=0.0, format="%.2f")

# Pilih operasi
operation = st.selectbox("Pilih operasi:", ("Tambah (+)", "Kurang (-)", "Kali (*)", "Bagi (/)"))

# Tombol hitung
if st.button("Hitung"):
    if operation == "Tambah (+)":
        result = num1 + num2
        st.success(f"Hasil: {result}")
    elif operation == "Kurang (-)":
        result = num1 - num2
        st.success(f"Hasil: {result}")
    elif operation == "Kali (*)":
        result = num1 * num2
        st.success(f"Hasil: {result}")
    elif operation == "Bagi (/)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Hasil: {result}")
        else:
            st.error("Pembagian dengan nol tidak diperbolehkan.")