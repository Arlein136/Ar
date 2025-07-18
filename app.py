if menu == "Home":
    st.markdown(
        "<h1 style='text-align: center; color:#4CAF50;'>🧪 Aplikasi Informasi Bahan Kimia</h1>", 
        unsafe_allow_html=True
    )
    st.markdown(
        "<h4 style='text-align: center; color:#2196F3;'>📚 Jelajahi Dunia Kimia Organik & Anorganik</h4>", 
        unsafe_allow_html=True
    )

    st.image("https://images.unsplash.com/photo-1618232991513-06d4f4241b2e?auto=format&fit=crop&w=800&q=80", 
             caption="Eksperimen Laboratorium Kimia", use_column_width=True)

    st.markdown("""
    ---
    ### 🌟 **Selamat Datang!**
    Aplikasi ini dirancang khusus untuk memberikan edukasi seputar **bahan kimia** yang sering kita temui di kehidupan sehari-hari.

    **Apa aja sih isi aplikasinya?**
    - 🔬 Penjelasan senyawa **organik** dan **anorganik**
    - ⚠️ Tingkat bahaya dan cara penanganan bahan kimia
    - 🧪 Rumus kimia dan kegunaannya

    ---
    ### 🧠 **Apa itu Kimia Organik & Anorganik?**

    🧬 **Kimia Organik**: Senyawa yang mengandung karbon, seperti alkohol, asam karboksilat, dan ester.  
    ⚗️ **Kimia Anorganik**: Senyawa tanpa karbon, seperti asam sulfat, natrium klorida, dan logam oksida.

    ---
    ### 🎯 Yuk Jelajahi Menu di Sebelah Kiri!
    Klik menu **Bahan Kimia Organik** atau **Anorganik** buat mulai belajar.
    """)

    st.success("👈 Ayo mulai eksplorasi bahan kimia favoritmu!")
