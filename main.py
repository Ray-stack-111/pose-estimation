import threading
import time
import tkinter as tk

import cv2
from PIL import ImageTk, Image
from ttkbootstrap import Style
from tkinter import messagebox



def action1():
    global movie_path
    global isbreak
    global th
    if th:
        isbreak = True
        messagebox.showwarning("提示", "切换成功！")

    movie_path="1.mp4"
    print("上肢训练模式")
    th = threading.Thread(target=video_loop)
    th.start()


def action2():
    global movie_path
    global isbreak
    global th
    if th:
        isbreak = True
        messagebox.showwarning("提示", "切换成功！")

    movie_path = "2.mp4"
    print("下肢训练模式")
    th = threading.Thread(target=video_loop)
    th.start()

def action3():
    global movie_path
    global isbreak
    global th
    if th:
        isbreak = True
        messagebox.showwarning("提示", "切换成功！")

    movie_path = "3.mp4"
    print("腹部肺部训练模式")
    th = threading.Thread(target=video_loop)
    th.start()

def action4():
    global movie_path
    global isbreak
    global th
    if th:
        isbreak = True
        messagebox.showwarning("提示", "切换成功！")

    movie_path = "4.mp4"
    print("拉伸训练模式")
    th = threading.Thread(target=video_loop)
    th.start()

# 视频显示
def video_loop():
    global isbreak
    global th

    cap = cv2.VideoCapture(movie_path)  # 获取视频
    while True:
        ret, frame = cap.read()
        if ret and not isbreak:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            #print(frame.shape[1])
            #print(frame.shape[0])
            if isbreak:
                break
            current_image = Image.fromarray(img).resize((int(frame.shape[1]/2), int(frame.shape[0]/2)))  # 将图像转换成Image对象
            if isbreak:
                break
            imgtk = ImageTk.PhotoImage(image=current_image)
            if isbreak:
                break
            # movieLabel.imgtk = imgtk
            movieLabel.config(image=imgtk)
            movieLabel.image = imgtk
        else:
            break
    # if not isbreak:
    #     video_loop()
    # else:
    isbreak = False
    th = None



# 登录成功后的界面
def s_userpage():
    name = username.get()
    global root
    global movieLabel
    root.destroy()
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry('900x800')
    root.title("视频窗口")
    tk.Label(root, text="基于龙芯教育派的运动姿态识别系统-----标准动作示范", font="-size 15 -weight bold").place(x=150, y=20)
    tk.Button(root, font="-size 15 -weight bold", text="  上肢训练模式  ", command=action1).place(x=30, y=90)
    tk.Button(root, font="-size 15 -weight bold", text="  下肢训练模式  ", command=action2).place(x=30, y=170)
    tk.Button(root, font="-size 15 -weight bold", text="腹部肺部训练模式", command=action3).place(x=30, y=260)
    tk.Button(root, font="-size 15 -weight bold", text="  拉伸训练模式  ", command=action4).place(x=30, y=350)
    movieLabel=tk.Label(root)
    movieLabel.place(x=230, y=90)

    root.mainloop()

# 登录操作
def sign():
    # name = username.get()
    # pwd = passward.get()
    # if name =="admin" and pwd =="admin":
    #     messagebox.showinfo("提示","登录成功")
    #     s_userpage()
    # else:
    #     messagebox.showerror("提示","账户或密码错误，请检查！")
    s_userpage()


movie_path=""
movieLabel=None
th=None
isbreak = False
#cosmo - flatly - journal  - lumen - minty - pulse - sandstone - united - yeti -cyborg - darkly - solar - superhero
style = Style(theme='superhero')
# 登录界面
root = style.master
root.resizable(False,False)
username = tk.StringVar()
passward = tk.StringVar()
root.geometry('560x380')
root.title("登录界面")

tk.Label(root, text="基于龙芯教育派的运动姿态识别系统",font="-size 15 -weight bold").place(x=120, y=50)
tk.Label(root, text="标准动作示范",font="-size 15 -weight bold").place(x=225, y=80)
tk.Label(root, text="账户：",font="-size 12 -weight bold").place(x=150, y=150)
tk.Entry(root, textvariable=username,width=23,font="-weight bold").place(x=210, y=150)
tk.Label(root, text="密码：",font="-size 12 -weight bold").place(x=150, y=200)
tk.Entry(root, textvariable=passward,width=23,font="-weight bold",show="*").place(x=210, y=200)
sig = tk.Button(root,font="-size 15 -weight bold", text="登录", command=sign).place(x=180, y=260)
eit = tk.Button(root,font="-size 15 -weight bold", text="取消", command=root.destroy).place(x=320, y=260)
root.mainloop()

'''if __name__ == '__main__':
    global root
    root = tk.Tk()
    login()
    conn.close()
    print("数据库已关闭")
    conn = conn('127.0.0.1','1433','sa','123456')
    delete_DB(conn)'''
