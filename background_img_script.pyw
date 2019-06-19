from os import listdir
import ctypes,time
dir_path = "C:/Users/Manoj Paladugu/Desktop/background_imgs"
def main():
    while (True):
        images = [dir_path + "/" + file for file in listdir("C:/Users/Manoj Paladugu/Desktop/background_imgs") if file.endswith(('.png', '.jpg', '.jpeg'))]        
        for i,img in enumerate(images):            
            ctypes.windll.user32.SystemParametersInfoW(20, 0, images[i] , 0)
            time.sleep(60)
main()