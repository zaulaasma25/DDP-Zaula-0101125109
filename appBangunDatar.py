import streamlit as st

#ini adalah halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu = st.sidebar.selectbox('pilih aplikasi',['luas persegi', 'luas segitiga', 'luas lingkaran'])
 
if menu == 'luas persegi':
    st.write(':blue [ini halaman untuk menghitung luas peregi]')
    st.markdown(':red[luas persegi]:balloon::balloon:')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi.jpg', caption='gambar luas persegi')
    sisi = st.number_input('silahkan masukkan sisi', min_value=0, )
    if st.button('hitung'):
        luas = sisi * sisi
        st.write(f'luas persegi adalah: {luas}')

elif menu == 'luas segitiga':
    st.write('ini halaman untuk menghitung luas segitiga')
    st.subheader('Hitung Luas Segitiga')

    # Menampilkan gambar ilustrasi
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvnU93yw54EG4p3cL7lMuWFeCGlkPv0co7cA&s", caption="Ilustrasi Segitiga", width=300,)

    # Input Data
    input_alas = st.number_input('Masukkan Alas', min_value=0)
    input_tinggi = st.number_input('Masukkan Tinggi', min_value=0)

    if st.button('Hitung Luas Segitiga'):
        if input_alas > 0 and input_tinggi > 0:
            luas = input_alas * input_tinggi / 2
            st.write(f"Luas segitiga adalah: {luas}")
        else:
            st.warning('Masukkan nilai alas dan tinggi yang lebih besar dari 0!')
                                               
elif menu == 'luas lingkaran':
    st.write('ini halaman untuk menghitung luas lingkaran')
    st.subheader('Hitung Luas Lingkaran')

    # Menampilkan gambar ilustrasi
    st.image("https://thumb.viva.co.id/media/frontend/thumbs3/2022/04/11/6253bd91b52f8-rumus-luas-lingkaran_1265_711.jpg", caption= "Ilustrasi Lingkaran", width=300,)

    # Input Data
    input_jari2 = st.number_input('Masukkan Jari-Jari', min_value=0)

    if st.button('Hitung Luas Lingkaran'):
        if input_jari2 > 0:
            luas = 3.14 * input_jari2 ** 2
            st.write(f"Luas lingkaran adalah: {luas}")
        else:
            st.warning('Masukkan nilai jari-jari yang lebih besar dari 0!')