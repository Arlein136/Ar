import streamlit as st import pandas as pd import random

st.set_page_config(page_title="Kimia Organik Berbahaya", layout="centered")

st.title("🧪 Informasi Senyawa Kimia Organik Berbahaya")

Info menarik acak

fakta_menarik = [ "🔬 Benzena pernah digunakan sebagai pelarut dalam industri sebelum diketahui karsinogenik.", "⚠️ Metanol bisa menyebabkan kebutaan jika tertelan.", "🔥 Aseton sangat mudah terbakar dan biasa ditemukan dalam penghapus cat kuku.", "☠️ Kloroform dulu dipakai sebagai anestesi, tapi sekarang dilarang karena toksisitasnya.", "🧯 Beberapa senyawa organik bisa menyerap lewat kulit dan masuk ke aliran darah.", "🧪 Banyak senyawa organik ditemukan di rumah, tapi tidak semuanya aman digunakan.", "💡 Etil asetat digunakan sebagai pelarut pada lem dan cat, tapi mudah menguap dan inflamabel.", "🚫 Paparan jangka panjang terhadap formaldehida bisa menyebabkan kanker saluran napas.", "👃 Banyak senyawa organik berbau tajam karena uapnya mudah menguap ke udara.", "📛 Fenol bisa menyebabkan luka bakar serius walau hanya terkena sedikit di kulit." ]

st.success(f"💡 Info Menarik: {random.choice(fakta_menarik)}")

Penjelasan umum

st.markdown(""" Kimia organik mempelajari senyawa karbon. Beberapa di antaranya bersifat beracun, korosif, bahkan karsinogenik. Aplikasi ini menyajikan informasi senyawa organik berbahaya, rumus, bahaya, dan cara penanganannya. """)

Data senyawa kimia organik (50 data)

data = { 'Senyawa': [...],  # <--- Ganti dengan daftar 50 senyawa lengkap (sebelumnya dibuat) 'Rumus': [...], 'Bahaya': [...], 'Keparahan': [...], 'Penanganan': [...] }

Buat DataFrame

df = pd.DataFrame(data)

Fitur pencarian

search = st.text_input("🔍 Cari senyawa organik...") filtered_df = df[df['Senyawa'].str.contains(search, case=False)] if search else df

Dropdown pemilihan

pilih = st.selectbox("📋 Pilih Senyawa:", [""] + filtered_df['Senyawa'].tolist())

Warna keparahan

warna = { "Tinggi": "red", "Sedang": "orange", "Rendah": "green" }

Tampilkan info senyawa

if pilih: row = df[df['Senyawa'] == pilih].iloc[0] st.markdown(f""" ## 🧪 {row['Senyawa']} - Rumus Kimia: {row['Rumus']} - Bahaya: {row['Bahaya']} - Tingkat Keparahan: <span style='color:{warna.get(row['Keparahan'], "black")}'>{row['Keparahan']}</span> - Cara Penanganan: {row['Penanganan']} """, unsafe_allow_html=True) else: st.info("Silakan pilih atau cari senyawa dari daftar di atas.")

Tips tambahan

st.markdown("---") st.subheader("🧯 Tips Keamanan Umum") st.markdown("""

Gunakan APD saat bekerja dengan bahan kimia.

Jangan hirup uap langsung.

Simpan bahan di tempat sesuai klasifikasinya.

Cuci tangan setelah kontak bahan kimia. """)


Footer

st.markdown("---") st.caption("📘 Dibuat oleh Kelompok 7 - Kelas 1D · 2025")

