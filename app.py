import streamlit as st
from PIL import Image

# ---------------- HOME ----------------
def tampilkan_home():
    st.markdown("<h1 style='text-align: center;'>🔬 Aplikasi Informasi Bahan Kimia</h1>", unsafe_allow_html=True)
    st.markdown("### 📚 Edukasi Kimia Organik & Anorganik")
    
    st.image("https://images.unsplash.com/photo-1581090700227-1e8d53e8efef", caption="Ilustrasi Kimia", use_column_width=True)

    st.markdown("""
    Selamat datang di aplikasi **Informasi Bahan Kimia**!  
    Di sini kamu bisa mempelajari:
    - 🧪 **Bahan Kimia Organik** (berbasis karbon seperti alkohol, asam karboksilat)
    - ⚗️ **Bahan Kimia Anorganik** (garam, asam kuat, basa kuat)
    
    Aplikasi ini cocok untuk pelajar, mahasiswa, atau siapa saja yang ingin mengenal bahaya & penanganan bahan kimia dengan cepat dan jelas.
    """)

    st.success("📘 Dibuat oleh: **Kelompok 7 - Kelas 1D**")

    st.info("🔍 Silakan pilih menu di **sidebar** untuk mulai menjelajahi!")
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
