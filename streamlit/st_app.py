import streamlit as st

from PIL import Image, ImageDraw, ImageFont
import os

proc_dir = r'wmarked_imgs'
unproc_dir = r'input_imgs'

proc_dir_list = os.listdir(proc_dir)
unproc_dir_list = os.listdir(unproc_dir)

# List objects in specified dir
def check_wmarked(proc_dir_list, unproc_dir_list):
    return unproc_dir_list == proc_dir_list

def batch_processing(proc_dir, unproc_dir, proc_dir_list, unproc_dir_list):
    
    #Creating text and font object
    text = "MataHelang"
    font = ImageFont.truetype('arial.ttf', 82)
    
    if check_wmarked(proc_dir_list, unproc_dir_list):
        for img in unproc_dir_list:
            #Opening Image
            img_proc = Image.open(unproc_dir+'/'+img)
            
            #Creating draw object
            draw = ImageDraw.Draw(img_proc)
    
            #Positioning Text
            textwidth, textheight = draw.textsize(text, font)
            width, height = img_proc.size 
            x=width/2-textwidth/2
            y=height-textheight-300

            #Applying text on image via draw object
            draw.text((x, y), text, font=font)

            #Saving the new image
            return f'\nWatermarked image {img}\n'
            img_proc.save(proc_dir+'/'+f'{img}'+'.png')
    else:
        return f'\nImage {img} already been watermarked\n'

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