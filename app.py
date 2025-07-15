import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Informasi Kimia Organik", layout="centered")

st.title("🧪 Informasi Senyawa Kimia Organik Berbahaya")

# Fakta acak
fakta = [
    "Benzena dulunya digunakan sebagai pelarut industri, tapi sekarang dibatasi karena sifat karsinogennya.",
    "Metanol bisa menyebabkan kebutaan jika dikonsumsi secara tidak sengaja.",
    "Formaldehida digunakan untuk mengawetkan spesimen biologis.",
    "Kloroform dulunya digunakan sebagai anestesi, tapi sekarang dilarang.",
    "Beberapa senyawa organik dapat menembus kulit dan langsung masuk ke aliran darah."
]
st.success(f"💡 Fakta Kimia: {random.choice(fakta)}")

# Penjelasan
st.markdown("""
Kimia organik adalah cabang ilmu kimia yang mempelajari senyawa karbon. 
Beberapa senyawa organik bersifat toksik dan berbahaya jika tidak ditangani dengan benar.  
Gunakan aplikasi ini untuk mengenali bahaya dan cara penanganan yang tepat.
""")

# Data senyawa
data = {
    'Senyawa': [
        'Benzena', 'Formaldehida', 'Aseton', 'Toluena', 'Etil Asetat', 'Metanol', 'Kloroform',
        'Fenol', 'Nitrobenzena', 'Karbon tetraklorida', 'Anilin', 'Asam asetat glasial',
        'Asetonitril', 'Piridina'
    ],
    'Rumus': [
        'C₆H₆', 'CH₂O', 'C₃H₆O', 'C₇H₈', 'C₄H₈O₂', 'CH₃OH', 'CHCl₃',
        'C₆H₅OH', 'C₆H₅NO₂', 'CCl₄', 'C₆H₅NH₂', 'CH₃COOH',
        'CH₃CN', 'C₅H₅N'
    ],
    'Bahaya': [
        'Karsinogen, mudah menguap',
        'Iritasi mata dan saluran napas, toksik',
        'Mudah terbakar, iritasi',
        'Kerusakan saraf pusat',
        'Iritasi kulit dan mata, mudah terbakar',
        'Beracun jika tertelan atau terhirup',
        'Karsinogenik, depresi sistem saraf',
        'Korosif, menyebabkan luka bakar',
        'Beracun, memengaruhi sistem darah',
        'Kerusakan hati dan ginjal',
        'Beracun, iritasi kulit dan mata',
        'Korosif kuat, menyebabkan luka bakar',
        'Mudah terbakar dan racun',
        'Iritasi saluran pernapasan, racun sistemik'
    ],
    'Keparahan': [
        'Tinggi', 'Tinggi', 'Sedang', 'Tinggi', 'Sedang', 'Tinggi', 'Tinggi',
        'Tinggi', 'Tinggi', 'Tinggi', 'Sedang', 'Tinggi', 'Tinggi', 'Tinggi'
    ],
    'Penanganan': [
        'Gunakan sarung tangan dan masker, ventilasi baik',
        'Gunakan APD, hindari paparan langsung',
        'Jauhkan dari api, gunakan ventilasi',
        'Hindari inhalasi, gunakan pelindung mata',
        'Simpan dalam wadah tertutup, APD diperlukan',
        'Gunakan di ruang terbuka, APD wajib',
        'Tangani di lemari asam, hindari kontak langsung',
        'Gunakan pelindung lengkap, ventilasi maksimal',
        'Gunakan sarung tangan dan goggles',
        'Tangani dengan hati-hati di ruang berventilasi',
        'Gunakan APD lengkap, hindari kontak kulit',
        'Tangani dalam lemari asam, APD lengkap',
        'Hindari percikan, gunakan masker dan pelindung',
        'Tangani dengan ventilasi baik dan APD'
    ]
}

df = pd.DataFrame(data)

# Fitur pencarian senyawa
search = st.text_input("🔎 Cari senyawa berdasarkan nama...")
filtered_df = df[df['Senyawa'].str.contains(search, case=False)] if search else df

# Dropdown senyawa
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
    st.info("Silakan pilih atau cari senyawa.")

# Tips keamanan
st.markdown("---")
st.subheader("🧯 Tips Keamanan Umum")
st.markdown("""
- Gunakan APD: sarung tangan, jas lab, masker.
- Jangan pipet bahan kimia langsung dengan mulut.
- Simpan bahan sesuai kelas bahayanya.
- Gunakan lemari asam untuk zat mudah menguap.
- Laporkan tumpahan atau kecelakaan ke dosen/lab assistant.
""")

# Footer
st.markdown("---")
st.caption("📘 Dibuat oleh Kelompok 7 - Kelas 1D · 2025")
