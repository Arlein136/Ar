import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Log Bahan Kimia Organik", layout="centered")

st.title("🧪 Pemantauan Bahan Kimia Organik Berbahaya")

tanggal = st.date_input("Tanggal", value=date.today(), format="YYYY/MM/DD")

data = {
    'Senyawa': [
        'Benzena', 'Formaldehida', 'Aseton', 'Toluena', 'Etil Asetat', 'Metanol', 'Kloroform',
        'Fenol', 'Nitrobenzena', 'Karbon tetraklorida', 'Anilin', 'Asam asetat glasial',
        'Asetonitril', 'Piridina'
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

st.header("🧫 Shift Pagi")
pagi = st.selectbox("Pilih senyawa (pagi)", [""] + df['Senyawa'].tolist(), key="pagi")

st.header("🧪 Shift Siang")
siang = st.selectbox("Pilih senyawa (siang)", [""] + df['Senyawa'].tolist(), key="siang")

st.header("🌙 Shift Malam")
malam = st.selectbox("Pilih senyawa (malam)", [""] + df['Senyawa'].tolist(), key="malam")

st.header("🧴 Cadangan")
cadangan = st.selectbox("Pilih senyawa cadangan", [""] + df['Senyawa'].tolist(), key="cadangan")

dipilih = [s for s in [pagi, siang, malam, cadangan] if s != ""]

if dipilih:
    st.subheader("📋 Detail Senyawa Dipilih")
    hasil = df[df['Senyawa'].isin(dipilih)]

    for _, row in hasil.iterrows():
        st.markdown(f"""
        ### 🧪 {row['Senyawa']}
        - **Bahaya:** {row['Bahaya']}
        - **Tingkat Keparahan:** :red[{row['Keparahan']}]
        - **Penanganan:** {row['Penanganan']}
        """)

    st.success(f"{len(dipilih)} senyawa dicatat untuk tanggal {tanggal.strftime('%Y/%m/%d')}")
else:
    st.info("Pilih senyawa organik untuk melihat informasinya.")

st.markdown("---")
st.caption("Dibuat oleh Kelompok 2 – 2025")
