from PIL import Image, ImageDraw, ImageFont
import os

proc_dir = r'test_imgs_wmarked'
unproc_dir = r'test_imgs'

proc_dir_list = os.listdir(proc_dir)
unproc_dir_list = os.listdir(unproc_dir)

# List objects in specified dir
def check_wmarked(proc_dir_list, unproc_dir_list):
    return False if unproc_dir_list == proc_dir_list else True

def batch_processing(proc_dir, unproc_dir, proc_dir_list, unproc_dir_list):
    
    #Creating text and font object
    text = "MataHelang"
    font = ImageFont.truetype('arial.ttf', 82)
    
    if check_wmarked(proc_dir_list, unproc_dir_list) == True:
        for img in unproc_dir_list:
            #Opening Image
            img = Image.open(unproc_dir+'/'+img)
            
            #Creating draw object
            draw = ImageDraw.Draw(img)
    
            #Positioning Text
            textwidth, textheight = draw.textsize(text, font)
            width, height = img.size 
            x=width/2-textwidth/2
            y=height-textheight-300

            #Applying text on image via draw object
            draw.text((x, y), text, font=font)

            #Saving the new image
            print(f'\nWatermarked image\n')
            img.save(proc_dir+'/'+img)
    else:
        print(f'\nImage already been watermarked\n')

if __name__ == "__main__":
    batch_processing(proc_dir, unproc_dir, proc_dir_list, unproc_dir_list)