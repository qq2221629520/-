# 批量修改照片大小
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def collect_photos():
    photos_path = []
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilenames(title="选择照片", filetypes=[("图片文件", "*.jpg;*.png")])
    photos_path.extend(path)
    #print(photos_path)
    numbers_photo=len(photos_path)
    for photo in photos_path:
        print(os.path.basename(photo))
    #print(numbers_photo)
    print('你一共选择了',numbers_photo,'张图片')
    return photos_path

photos_path= None

def collect_photos2():
    global photos_path
    photos_path =collect_photos()
resized_files_dir=None
def resize_images(file_paths):
    new_width = int(input("你想把照片的宽度设为多少，请输入数字，单位是像素: "))
    new_height = int(input("你想把照片的高度设为多少，: 请输入数字，单位是像素"))
    global resized_files_dir
    resized_files_dir= os.path.split(file_paths[0])[0]
    for file_path in file_paths:
        file_dir, file_name = os.path.split(file_path)
        image = Image.open(file_path)
        new_image = image.resize((new_width, new_height))
        new_file_path = os.path.join(file_dir, "resized_" + file_name)
        new_image.save(new_file_path)
    print("修改完毕")
    print('生成的文件在这个目录：',resized_files_dir,'你可以复制这个目录到资源管理器打开')
    print('___________________________________________________________________')
    print("如果需要继续转换照片，请关闭软件重启使用，谢谢，软件开发者：方中原")

def open_resized_files_dir():
    if resized_files_dir is None:
        print("欢迎使用简易照片大小批量处理软件！本软件由python开发！！！")
        return
    os.startfile(resized_files_dir)


def finish_and_close():
    # 完成操作并关闭窗口
    root.quit()
root = tk.Tk()
root.title("转换窗口")
root.geometry("400x400+630+254")
select_file_button = tk.Button(root, text="选择文件", command=lambda: collect_photos2())
start_convert_button = tk.Button(root, text="开始转换", command=lambda: resize_images(photos_path))
open_resized_files_dir1 = tk.Button(root, text="打开转换后的文件夹", command= open_resized_files_dir())
finish_and_close_button = tk.Button(root, text="完成并关闭窗口", command= finish_and_close)
select_file_button.config(width=20, height=2)
start_convert_button.config(width=20, height=2)
open_resized_files_dir1.config(width=20, height=2)
finish_and_close_button.config(width=20, height=2)


select_file_button.pack()
start_convert_button.pack()
open_resized_files_dir1.pack()
finish_and_close_button.pack()
root.update_idletasks()

select_file_button.place(relx=0.5, rely=0.2, anchor="center")
start_convert_button.place(relx=0.5, rely=0.4, anchor="center")
open_resized_files_dir1.place(relx=0.5, rely=0.6, anchor="center")
finish_and_close_button.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()

#本程序的打包命令 pyinstaller E:\python项目\自动化项目\main9.py --onefile --icon=E:\python项目\自动化项目\图标头像.ico


