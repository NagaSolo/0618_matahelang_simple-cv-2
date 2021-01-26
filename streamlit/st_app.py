import streamlit as st

def deskripsi():
    st.title('WMark')
    st.subheader('Me"Water marked"kan gambar peribadi mu')

def aplikasi():
    pass

def informasi():
    with st.beta_expander('Penyedia'):
        st.write('Seramamas')
        st.write('Matahelang')

def main():
    menu = st.sidebar
    menu.title('Menu')
    pilihan_pilihan = ['Deskripsi', 'Aplikasi', 'Informasi']
    memilih = menu.selectbox('Pilihan', pilihan_pilihan)
    if memilih == 'Deskripsi':
        deskripsi()
    elif memilih == 'Aplikasi':
        aplikasi()
    elif memilih == 'Informasi':
        informasi()

if __name__ == '__main__':
    main()