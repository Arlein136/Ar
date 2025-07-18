import streamlit as st

st.set_page_config(page_title="Info Bahan Kimia", layout="wide")

# Navigasi menu
menu = st.sidebar.selectbox("Pilih Halaman", ["Home", "Kimia Organik", "Kimia Anorganik"])
if menu == "Home":
    st.title("Selamat Datang di Aplikasi Bahan Kimia")
    # dan seterusnya...
    
    st.markdown(
        "<h3 style='text-align: center; color:#2196F3;'>📚 Edukasi Kimia Organik & Anorganik</h3>", 
        unsafe_allow_html=True
    )

    st.image(
        "https://images.unsplash.com/photo-1618232991513-06d4f4241b2e?auto=format&fit=crop&w=800&q=80", 
        caption="Eksperimen Laboratorium Kimia", 
        use_container_width=True
    )

    st.markdown("---")

    st.markdown("""
    ### 🌟 Selamat Datang!
    Aplikasi ini dirancang untuk memberikan informasi lengkap dan edukatif tentang berbagai bahan kimia yang digunakan dalam kehidupan sehari-hari.

    **Apa yang bisa kamu pelajari di sini?**
    - 🔬 Pengetahuan tentang senyawa **organik** dan **anorganik**
    - ⚠️ Informasi bahaya bahan kimia & cara penanganannya
    - 🧪 Rumus kimia dan aplikasinya

    ---

    ### 🧠 Apa Itu Kimia Organik & Anorganik?

    **Kimia Organik**: Mempelajari senyawa karbon seperti alkohol, asam karboksilat, ester, dll.  
    **Kimia Anorganik**: Mempelajari senyawa non-karbon seperti logam, asam mineral, basa kuat, dan garam.

    ---

    📌 Gunakan menu di samping untuk mulai belajar!

    """)
