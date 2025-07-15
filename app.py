import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Kimia Organik Berbahaya", layout="centered")

st.title("🧪 Informasi Senyawa Kimia Organik Berbahaya")

# Baca file Excel
try:
    df = pd.read_excel("data_kimia(1).xlsx")
except Exception as e:
    st.error(f"Gagal membaca file Excel: {e}")
    st.stop()

# Fakta acak
fakta = [
    "Beberapa senyawa organik dapat diserap lewat kulit dan masuk ke aliran darah.",
    "Benzena bersifat karsinogen dan dilarang untuk penggunaan rumah tangga.",
    "Metanol sangat beracun jika tertelan, bahkan dalam jumlah kecil.",
    "Formaldehida biasa dipakai untuk mengawetkan spesimen, tapi sangat iritatif.",
    "Fenol dapat menyebabkan luka bakar serius di kulit."
]
st.success(f"💡 Fakta Kimia: {random.choice(fakta)}")

# Deskripsi
st.markdown("""
Kimia organik mempelajari senyawa karbon. Beberapa di antaranya bersifat beracun, korosif, bahkan karsinogenik.
Aplikasi ini menyajikan informasi senyawa organik berbahaya, rumus, bahaya, dan cara penanganannya.
""")

# Pencarian senyawa
search = st.text_input("🔍 Cari senyawa organik...")
filtered_df = df[df['Senyawa'].str.contains(search, case=False)] if search else df

# Pilihan dropdown
pilih = st.selectbox("📋 Pilih Senyawa:", [""] + filtered_df['Senyawa'].tolist())

# Tampilkan hasil
if pilih:
    row = df[df['Senyawa'] == pilih].iloc[0]
    warna = {
        "Tinggi": "red",
        "Sedang": "orange",
        "Rendah": "green"
    }
    st.markdown(f"""
    ## 🧪 {row['Senyawa']}
    - **Rumus Kimia:** `{row['Rumus']}`
    - **Bahaya:** {row['Bahaya']}
    - **Tingkat Keparahan:** <span style='color:{warna.get(row['Keparahan'], "black")}'><b>{row['Keparahan']}</b></span>
    - **Cara Penanganan:** {row['Penanganan']}
    """, unsafe_allow_html=True)
else:
    st.info("Silakan pilih atau cari senyawa dari daftar di atas.")

# Tips keamanan
st.markdown("---")
st.subheader("🧯 Tips Keamanan Umum")
st.markdown("""
- Gunakan APD saat bekerja dengan bahan kimia.
- Jangan hirup uap langsung.
- Simpan bahan di tempat sesuai klasifikasinya.
- Cuci tangan setelah kontak bahan kimia.
""")

# Footer
st.markdown("---")
st.caption("📘 Dibuat oleh Kelompok 7 - Kelas 1D · 2025")
