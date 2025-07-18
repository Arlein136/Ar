import streamlit as st import pandas as pd import random

st.set_page_config(page_title="Aplikasi Informasi Bahan Kimia", layout="centered")

Navigasi halaman

menu = st.sidebar.selectbox("📂 Menu", ["Home", "Kimia Organik", "Kimia Anorganik"])

Fakta menarik kimia

fakta_menarik = [ "🔬 Benzena pernah digunakan sebagai pelarut dalam industri sebelum diketahui karsinogenik.", "⚠️ Metanol bisa menyebabkan kebutaan jika tertelan.", "🔥 Aseton sangat mudah terbakar dan biasa ditemukan dalam penghapus cat kuku.", "☠️ Kloroform dulu dipakai sebagai anestesi, tapi sekarang dilarang karena toksisitasnya.", "🧯 Beberapa senyawa organik bisa menyerap lewat kulit dan masuk ke aliran darah.", "🧪 Banyak senyawa organik ditemukan di rumah, tapi tidak semuanya aman digunakan.", "💡 Etil asetat digunakan sebagai pelarut pada lem dan cat, tapi mudah menguap dan inflamabel.", "🚫 Paparan jangka panjang terhadap formaldehida bisa menyebabkan kanker saluran napas.", "👃 Banyak senyawa organik berbau tajam karena uapnya mudah menguap ke udara.", "📛 Fenol bisa menyebabkan luka bakar serius walau hanya terkena sedikit di kulit." ]

warna = { "Tinggi": "red", "Sedang": "orange", "Rendah": "green" }

Data bahan kimia organik

organik_data = { 'Senyawa': [...], 'Rumus': [...], 'Bahaya': [...], 'Keparahan': [...], 'Penanganan': [...] }

Data bahan kimia anorganik (contoh sederhana)

anorganik_data = { 'Senyawa': ["Asam Sulfat", "Natrium Klorida", "Amonia", "Asam Nitrat"], 'Rumus': ["H2SO4", "NaCl", "NH3", "HNO3"], 'Bahaya': [ "Korosif, menyebabkan luka bakar", "Iritasi jika konsentrasi tinggi", "Beracun, menyebabkan iritasi saluran napas", "Korosif dan oksidator kuat" ], 'Keparahan': ["Tinggi", "Rendah", "Sedang", "Tinggi"], 'Penanganan': [ "Gunakan pelindung, hindari kontak kulit", "Hindari paparan langsung", "Ventilasi baik, gunakan masker", "Gunakan pelindung lengkap dan penanganan sesuai protokol" ] }

Halaman Home

if menu == "Home": st.title("🔬 Aplikasi Informasi Bahan Kimia") st.success(f"💡 Info Menarik: {random.choice(fakta_menarik)}") st.markdown(""" Selamat datang di aplikasi informasi bahan kimia! Di sini kamu bisa melihat informasi lengkap tentang bahan kimia organik dan anorganik yang berbahaya:

- 🧪 **Kimia Organik**: Senyawa berbasis karbon
- ⚗️ **Kimia Anorganik**: Senyawa selain karbon, seperti asam, basa, dan garam

Pilih dari menu di samping untuk mulai eksplorasi!
""")
st.markdown("---")
st.caption("📘 Dibuat oleh Kelompok 7 - Kelas 1D · 2025")

Halaman Kimia Organik

elif menu == "Kimia Organik": st.title("🧪 Informasi Kimia Organik Berbahaya") df = pd.DataFrame(organik_data) search = st.text_input("🔍 Cari senyawa organik...") filtered_df = df[df['Senyawa'].str.contains(search, case=False)] if search else df pilih = st.selectbox("📋 Pilih Senyawa:", [""] + filtered_df['Senyawa'].tolist()) if pilih: row = df[df['Senyawa'] == pilih].iloc[0] st.markdown(f""" ## 🧪 {row['Senyawa']} - Rumus Kimia: {row['Rumus']} - Bahaya: {row['Bahaya']} - Tingkat Keparahan: <span style='color:{warna.get(row['Keparahan'], "black")}'>{row['Keparahan']}</span> - Cara Penanganan: {row['Penanganan']} """, unsafe_allow_html=True) else: st.info("Silakan pilih atau cari senyawa organik.")

Halaman Kimia Anorganik

elif menu == "Kimia Anorganik": st.title("⚗️ Informasi Kimia Anorganik Berbahaya") df = pd.DataFrame(anorganik_data) search = st.text_input("🔍 Cari senyawa anorganik...") filtered_df = df[df['Senyawa'].str.contains(search, case=False)] if search else df pilih = st.selectbox("📋 Pilih Senyawa:", [""] + filtered_df['Senyawa'].tolist()) if pilih: row = df[df['Senyawa'] == pilih].iloc[0] st.markdown(f""" ## ⚗️ {row['Senyawa']} - Rumus Kimia: {row['Rumus']} - Bahaya: {row['Bahaya']} - Tingkat Keparahan: <span style='color:{warna.get(row['Keparahan'], "black")}'>{row['Keparahan']}</span> - Cara Penanganan: {row['Penanganan']} """, unsafe_allow_html=True) else: st.info("Silakan pilih atau cari senyawa anorganik.")

