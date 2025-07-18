import streamlit as st

# --- Konfigurasi halaman utama ---
st.set_page_config(page_title="Informasi Bahan Kimia", page_icon="🧪", layout="wide")

# --- Navigasi ---
menu = st.sidebar.radio("Navigasi", ["Home", "Bahan Kimia Organik", "Bahan Kimia Anorganik", "Tentang Aplikasi"])

# --- Halaman Home ---
if menu == "Home":
    st.markdown("<h1 style='text-align: center;'>🧪 Aplikasi Informasi Bahan Kimia</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>📘 Edukasi Kimia Organik & Anorganik</h3>", unsafe_allow_html=True)

    st.image("https://cdn-icons-png.flaticon.com/512/3004/3004669.png", width=200, caption="Ilustrasi Kimia")

    st.markdown("### Selamat datang!")
    st.write("Aplikasi ini memberikan informasi menarik tentang berbagai **senyawa kimia organik** dan **anorganik**.")
    st.markdown("> Yuk, eksplorasi dunia kimia bersama kami! 💡")

# --- Halaman Kimia Organik ---
elif menu == "Bahan Kimia Organik":
    st.header("🧬 Bahan Kimia Organik")
    st.info("Berikut beberapa contoh senyawa kimia organik beserta rumus dan kegunaannya:")

    data_organik = [
        {"Nama": "Etil Asetat", "Rumus": "CH3COOC2H5", "Kegunaan": "Pelarut cat & perekat"},
        {"Nama": "Asam Asetat", "Rumus": "CH3COOH", "Kegunaan": "Bahan dasar cuka"},
        {"Nama": "Etanol", "Rumus": "C2H5OH", "Kegunaan": "Disinfektan, pelarut"},
        {"Nama": "Metanol", "Rumus": "CH3OH", "Kegunaan": "Pelarut & bahan bakar"},
        {"Nama": "Asam Benzoat", "Rumus": "C6H5COOH", "Kegunaan": "Pengawet makanan"},
        {"Nama": "Glukosa", "Rumus": "C6H12O6", "Kegunaan": "Sumber energi"},
        {"Nama": "Fruktosa", "Rumus": "C6H12O6", "Kegunaan": "Pemanis alami"},
        {"Nama": "Aspirin", "Rumus": "C9H8O4", "Kegunaan": "Obat pereda nyeri"},
        {"Nama": "Benzena", "Rumus": "C6H6", "Kegunaan": "Bahan dasar industri kimia"},
        {"Nama": "Toluena", "Rumus": "C6H5CH3", "Kegunaan": "Pelarut dan bahan bakar"},
    ]

    for senyawa in data_organik:
        st.subheader(senyawa["Nama"])
        st.markdown(f"**Rumus:** `{senyawa['Rumus']}`  \n**Kegunaan:** {senyawa['Kegunaan']}")

# --- Halaman Kimia Anorganik ---
elif menu == "Bahan Kimia Anorganik":
    st.header("🧪 Bahan Kimia Anorganik")
    st.info("Berikut beberapa senyawa anorganik yang umum digunakan:")

    data_anorganik = [
        {"Nama": "Natrium Klorida", "Rumus": "NaCl", "Kegunaan": "Garam dapur"},
        {"Nama": "Asam Sulfat", "Rumus": "H2SO4", "Kegunaan": "Bahan baterai & pupuk"},
        {"Nama": "Amonia", "Rumus": "NH3", "Kegunaan": "Pembersih dan pupuk"},
        {"Nama": "Kalsium Karbonat", "Rumus": "CaCO3", "Kegunaan": "Kapur, antasida"},
        {"Nama": "Natrium Hidroksida", "Rumus": "NaOH", "Kegunaan": "Sabun dan deterjen"},
        {"Nama": "Asam Nitrat", "Rumus": "HNO3", "Kegunaan": "Pembuatan pupuk"},
        {"Nama": "Magnesium Sulfat", "Rumus": "MgSO4", "Kegunaan": "Laksatif dan pertanian"},
        {"Nama": "Zinc Oksida", "Rumus": "ZnO", "Kegunaan": "Salep kulit, kosmetik"},
        {"Nama": "Ferum(III) Klorida", "Rumus": "FeCl3","Kegunaan": "Mesiu dan pupuk"},
    ]

    for senyawa in data_anorganik:
        st.subheader(senyawa["Nama"])
        st.markdown(f"**Rumus:** `{senyawa['Rumus']}`  \n**Kegunaan:** {senyawa['Kegunaan']}")

# --- Halaman Tentang ---
elif menu == "Tentang Aplikasi":
    st.header("📘 Tentang Aplikasi")
    st.markdown("""
Aplikasi ini dibuat dengan tujuan edukasi untuk mengenalkan berbagai **senyawa kimia organik dan anorganik** 
beserta rumus molekul dan kegunaannya.

**Fitur:**
- Navigasi antar halaman
- Ilustrasi dan penjelasan bahan kimia
- Ramah pengguna dan interaktif

**Dibuat menggunakan:** Streamlit + Python  
**Dikembangkan oleh:** Mahasiswa Kimia 👩‍🔬👨‍🔬
    """)
