import streamlit as st
import pandas as pd

# Sidebar navigasi
st.sidebar.title("Navigasi")
halaman = st.sidebar.radio("Pilih Halaman:", ["Home", "Kimia Organik", "Kimia Anorganik"])

# Halaman: Home
if halaman == "Home":
    st.title("🏠 Selamat Datang di Aplikasi Kimia")
    st.write("Aplikasi ini berisi informasi tentang bahan kimia organik dan anorganik.")
    st.info("Kelompok 7 - Kelas 1D")

# Halaman: Kimia Organik
elif halaman == "Kimia Organik":
    st.title("🧪 Bahan Kimia Organik")
    # tampilkan data organik di sini
    st.write("Contoh data kimia organik akan ditampilkan di sini...")

# Halaman: Kimia Anorganik
elif halaman == "Kimia Anorganik":
    st.title("⚗️ Bahan Kimia Anorganik")
    # tampilkan data anorganik di sini
    st.write("Contoh data kimia anorganik akan ditampilkan di sini...")
