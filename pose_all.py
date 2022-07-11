import cv2
import numpy as np
import pose_mould as pm
import five_poses as the_poses


cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
pose = ['none', 'barbell_bent_over', 'crunch', 'pull_up', 'deep_keen_bend', 'stretch']
state = pose[0]
pose = ['none', 'barbell_bent_over', 'crunch', 'pull_up', 'deep_keen_bend', 'stretch']
state_store = []
out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (640, 480))  # 保存视频
k=1
score=0
mode=0
deep_keen_score_list=[]



import tkinter as tk
from tkinter import *



def change_to_mode_1():
     global  mode
     mode=1
     pass


def change_to_mode_2():
    global mode
    mode = 2
    pass


def change_to_mode_3():
    global mode
    mode = 3
    pass


def change_to_mode_4():
    global mode
    mode = 4
    pass


def change_to_mode_5():
    global mode
    mode = 5
    pass




def tkImage(frame):
    cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    pilImage = Image.fromarray(cvimage)
    pilImage = pilImage.resize((640, 480), Image.ANTIALIAS)
    tkImage = ImageTk.PhotoImage(image=pilImage)
    return tkImage



##############################################################################################################################################################################
def all_the_task():
    pull_up_state = False
    barbell_bent_over_state = False
    crunch_state = False
    deep_keen_bend_state = False
    stretch_state = False
    global k, output_state
    global root
    barbrll_bent_over_row_count=0
    crunch_count=0
    pull_up_count=0
    deep_keen_count=0
    stretch_count=0
    stretch_left_count=0
    stretch_right_count=0
    push_up_count = 0
    lunge_left_count=0
    lunge_right_count=0

    global  mode


    while True:
        success, img = cap.read()
        img=cv2.resize(img,(640,480))
        img = detector.findPose(img)
        lmlist = detector.getPosition(img, False)

        if cv2.waitKey(1) & 0xFF == ord('6'):
            the_poses.all_poses_count_clear()

        if len(lmlist) != 0:
            # 获得各种的位置参数
            left_side_angle = detector.find_angle(img, 13, 15, 14, False)
            right_side_angle = detector.find_angle(img, 14, 16, 13, False)
            per_side_angle = int((left_side_angle + right_side_angle) / 2)
            two_pinky_distance = detector.find_distance(img, 17, 18, False)
            right_leg_angle = detector.find_angle(img, 24, 26, 28)
            waist_angle = detector.find_angle(img, 12, 24, 26, False)
            id_15, left_wrist_position_x, left_wrist_position_y = lmlist[15]
            id_16, right_wrist_position_x, right_wrist_position_y = lmlist[16]
            id_13, left_elbow_position_x, left_elbow_position_y = lmlist[13]
            id_14, right_elbow_position_x, right_elbow_position_y = lmlist[14]
            left_hip_angle = detector.find_angle(img, 24, 23, 25, False)
            right_hip_angle = detector.find_angle(img, 23, 24, 26, False)
            per_hip_angle = (left_hip_angle + right_hip_angle) / 2
            left_arm_and_knee_angle = detector.find_angle(img, 13, 25, 27, False)
            right_arm_and_knee_angle = detector.find_angle(img, 14, 26, 28, False)
            per_arm_and_knee_angle = (left_arm_and_knee_angle + right_arm_and_knee_angle) / 2
            left_wrist_and_knee_distance = detector.find_distance(img, 15, 25,False)
            right_wrist_and_knee_distance = detector.find_distance(img, 16, 26,False)
            per_wrist_and_knee_diatance = (left_wrist_and_knee_distance + right_wrist_and_knee_distance) / 2
            id_0,nose_position_x,nose_position_y=lmlist[0]
            id_25,left_knee_position_x,left_knee_position_y=lmlist[25]
            id_26,right_knee_position_x,right_knee_position_y=lmlist[26]

            #上肢训练模块
            if mode==1:
                #首先，我们进行引体向上的训练5次
                if pull_up_count <= 5:
                    img, pull_up_count = the_poses.pull_up(img, lmlist)
                    cv2.putText(img, 'pull_up', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                    cv2.putText(img, str(pull_up_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                elif pull_up_count>=5 and push_up_count <=5:
                    img, push_up_count = the_poses.push_up(img, lmlist)
                    cv2.putText(img, 'push_up', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                    cv2.putText(img, str(push_up_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                elif push_up_count >=5:
                    cv2.putText(img, 'training_ok', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                    #之后，我们再进行10次


            #下肢训练模块
            if mode==2:
                if deep_keen_count <=5:
                    img, deep_keen_count = the_poses.deep_keen_dete(img, lmlist)
                    cv2.putText(img, str(deep_keen_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)
                    cv2.putText(img, 'deep_keen_bend', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)
                elif deep_keen_count >=5 and lunge_left_count <=5:
                    img, lunge_left_count = the_poses.Lunge_left(img, lmlist)
                    cv2.putText(img, str(lunge_left_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)
                    cv2.putText(img, 'lunge_left', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)
                elif lunge_left_count>=5 and  lunge_right_count <=5:
                    img, lunge_right_count = the_poses.Lunge_right(img, lmlist)
                    cv2.putText(img, str(lunge_right_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)
                    cv2.putText(img, 'lunge_right', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)
                elif lunge_right_count >=5:
                    cv2.putText(img, 'training_ok', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)



            #腹部背部训练按钮
            if mode==3:
                if crunch_count<=5:
                    img, crunch_count = the_poses.crunch(img, lmlist)
                    cv2.putText(img, 'crunch', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                    cv2.putText(img, str(crunch_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                elif crunch_count>=5 and barbrll_bent_over_row_count<=5:
                    img, barbrll_bent_over_row_count = the_poses.barbrll_bent_over_row(img, lmlist)
                    cv2.putText(img, 'barbell_bent_over', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                    cv2.putText(img, str(barbrll_bent_over_row_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                elif barbrll_bent_over_row_count>=5:
                    cv2.putText(img, 'training_ok', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)


            #训练后的拉伸模块
            if mode==4:
                if stretch_count<=5:
                    img, stretch_count = the_poses.stretch(img, lmlist)
                    cv2.putText(img, 'stretch', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                    cv2.putText(img, str(stretch_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3   , (255, 0, 0), 5)
                elif stretch_count>=5 and stretch_left_count<=5:
                    img, stretch_left_count = the_poses.stretch_left(img, lmlist)
                    cv2.putText(img, 'stretch_left', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                    cv2.putText(img, str(stretch_left_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                elif stretch_left_count>=5 and stretch_right_count <=5:
                    img, stretch_right_count = the_poses.stretch_right(img, lmlist)
                    cv2.putText(img, 'stretch_right', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                    cv2.putText(img, str(stretch_right_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                elif stretch_right_count>=5:
                    cv2.putText(img, 'training_ok', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)

            #多种动作训练模块
            if mode==5:
                # 以下为深蹲时的手臂检测
                if per_side_angle < 110 and per_side_angle > 80 and two_pinky_distance < 50 and per_hip_angle >= 95 :
                    deep_keen_bend_state = True
                else:
                    deep_keen_bend_state = False

                # 以下为卷腹时的腿部检测
                if (right_leg_angle > 50 and right_leg_angle < 80 and
                     (nose_position_y >left_knee_position_y +20 or nose_position_y >right_knee_position_y-20 )):
                    crunch_state = True
                else:
                    crunch_state = False

                # 以下为俯身划船时的腰部检测
                if (85 <= waist_angle <= 140 and
                    (left_wrist_position_y > left_elbow_position_x or
                        right_wrist_position_y > right_elbow_position_y) and
                        per_wrist_and_knee_diatance>100):

                    barbell_bent_over_state = True
                else:
                    barbell_bent_over_state = False

                # 以下为引体向上的检测
                if (left_wrist_position_y < left_elbow_position_x and right_wrist_position_y < right_elbow_position_y and
                        95 >= per_hip_angle >= 85):
                    pull_up_state = True
                else:
                    pull_up_state = False

                # 以下为伸展运动的检测
                if ((120 < per_hip_angle < 150) and (
                        170 > per_arm_and_knee_angle > 150) and per_wrist_and_knee_diatance < 90):
                    stretch_state = True
                else:
                    stretch_state = False


                # 分类为卷腹
                if crunch_state:
                    state = pose[2]

                # 分类为俯身划船
                elif barbell_bent_over_state:
                    state = pose[1]

                # 分类为深蹲
                elif deep_keen_bend_state:
                    state = pose[4]

                # 分类为引体向上
                elif pull_up_state:
                    state = pose[3]

                # 分类为伸展
                elif stretch_state:
                    state = pose[5]

                # 全都不是，没有分类
                else:
                    state = pose[0]

                print('state_now:', state)

                #以下为姿势稳定代码
                none_number = 0
                barbell_bent_over_number = 0
                crunch_number = 0
                pull_up_number = 0
                deep_keen_bend_number = 0
                stretch_number = 0


                state_store.append(state)
                print(state_store)
                for i in state_store:
                    if i == 'none':
                            none_number += 1
                    elif i == 'barbell_bent_over':
                            barbell_bent_over_number += 1
                    elif i == 'crunch':
                            crunch_number += 1
                    elif i == 'pull_up':
                            pull_up_number += 1
                    elif i == 'deep_keen_bend':
                            deep_keen_bend_number += 1
                    elif i == 'stretch':
                            stretch_number += 1
                    if none_number + barbell_bent_over_number + crunch_number + pull_up_number + deep_keen_bend_number + stretch_number == 20:
                            del state_store[0]

                print(none_number, barbell_bent_over_number, crunch_number, pull_up_number, deep_keen_bend_number,
                          stretch_number)
                # pose = ['none', 'barbell_bent_over', 'crunch', 'pull_up', 'deep_keen_bend', 'stretch']

                if (none_number >= barbell_bent_over_number and none_number >= barbell_bent_over_number and none_number >= crunch_number and
                            none_number >= pull_up_number and none_number >= deep_keen_bend_number and none_number >= stretch_number):
                        output_state = pose[0]
                elif ( barbell_bent_over_number >= crunch_number and barbell_bent_over_number >= pull_up_number and barbell_bent_over_number >= deep_keen_bend_number and
                            barbell_bent_over_number >= stretch_number):
                        output_state = pose[1]
                elif crunch_number >= pull_up_number and crunch_number >= deep_keen_bend_number and crunch_number >= stretch_number:
                        output_state = pose[2]
                elif pull_up_number >= deep_keen_bend_number and pull_up_number >= stretch_number:
                        output_state = pose[3]
                elif deep_keen_bend_number >= stretch_number:
                        output_state = pose[4]
                elif stretch_number != 0:
                        output_state = pose[5]

                #print('the out put state:', output_state)
                none_number = 0
                barbell_bent_over_number = 0
                crunch_number = 0
                pull_up_number = 0
                deep_keen_bend_number = 0
                stretch_number = 0

    ###################################################################################################################################################################################
                #以下为各种动作的输出界面
                # pose = ['none', 'barbell_bent_over', 'crunch', 'pull_up', 'deep_keen_bend', 'stretch']

                if output_state=='barbell_bent_over':
                    img,barbrll_bent_over_row_count=the_poses.barbrll_bent_over_row(img,lmlist)
                    cv2.putText(img, 'barbell_bent_over', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                    cv2.putText(img, str(barbrll_bent_over_row_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0),5)

                elif output_state=='crunch':
                    img,crunch_count=the_poses.crunch(img,lmlist)
                    cv2.putText(img, 'crunch', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                    cv2.putText(img, str(crunch_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)

                elif output_state=='pull_up':
                    img,pull_up_count=the_poses.pull_up(img,lmlist)
                    cv2.putText(img, 'pull_up', (0,100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                    cv2.putText(img, str(pull_up_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)

                elif output_state=='deep_keen_bend':
                    img,deep_keen_count,score=the_poses.deep_keen_dete(img,lmlist)
                    cv2.putText(img, str(deep_keen_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)
                    cv2.putText(img, 'deep_keen_bend', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)

                    if score !=0:
                        deep_keen_score_list.append(score)
                    print(deep_keen_score_list)

                    if deep_keen_score_list:
                        cv2.putText(img, str(deep_keen_score_list[-1]), (0, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)
                        print('deep_keen_bend is',deep_keen_score_list)

                elif output_state=='stretch':
                    img,stretch_count=the_poses.stretch(img,lmlist)
                    cv2.putText(img, 'stretch', (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
                    cv2.putText(img, str(stretch_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)

                elif output_state == 'none':
                    cv2.putText(img, str('barbrll_bent_over_row_count'), (0, 25), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)
                    cv2.putText(img, str(barbrll_bent_over_row_count), (0, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)

                    cv2.putText(img, str('crunch_count'), (0,80), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)
                    cv2.putText(img, str(crunch_count), (0, 105), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)

                    cv2.putText(img, str('pull_up_count'), (0, 135), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)
                    cv2.putText(img, str(pull_up_count), (0, 160), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)

                    cv2.putText(img, str('deep_keen_count'), (0, 190), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)
                    cv2.putText(img, str(deep_keen_count), (0, 215), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)

                    cv2.putText(img, str('stretch_count'), (0, 245), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)
                    cv2.putText(img, str(stretch_count), (0, 270), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)

                    cv2.putText(img, str('calorie_calculate'), (0,300), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)
                    cv2.putText(img, str(0.5*(barbrll_bent_over_row_count+crunch_count+pull_up_count+deep_keen_count+stretch_count)), (0, 325), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)

#以下为视频功能的写入




            image_width = 640
            image_height = 480
            canvas = Canvas(root, bg='white', width=image_width, height=image_height)  # 绘制画布
            canvas.place(x=160, y=70)
            pic = tkImage(img)
            canvas.create_image(320, 240, image=pic)

            root.update()
            root.after(1)

    root.mainloop()





#####################################################################################################################################################
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

def next_page():
    global mode
    name = username.get()
    global root

    root.destroy()
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry('800x600')
    root.title("视频窗口")

    background = Canvas(root, bg='white', width=800, height=600)  # 绘制画布
    background.place(x=0, y=0)
    # background_img = PhotoImage(file='D:/new_poses_7_5/6416f6b269cc4f871c1daaf7bd2dd27c.gif')
    # background.create_image(320, 240, image=background_img)

    tk.Label(root, text="基于龙芯教育派的运动姿态识别系统-----动作训练", font="-size 15 -weight bold").place(x=150, y=20)
    tk.Button(root, font="-size 15 -weight bold", text="上肢训练", command=change_to_mode_1).place(x=0, y=90)
    tk.Button(root, font="-size 15 -weight bold", text="下肢训练", command=change_to_mode_2).place(x=0,
                                                                                                     y=170)
    tk.Button(root, font="-size 15 -weight bold", text="腹部背部训练", command=change_to_mode_3).place(x=0, y=260)
    tk.Button(root, font="-size 15 -weight bold", text="拉伸训练", command=change_to_mode_4).place(x=0,
                                                                                                     y=350)
    tk.Button(root, font="-size 15 -weight bold", text="自动识别训练", command=change_to_mode_5).place(x=0,
                                                                                                       y=440)
    tk.Button(root, font="-size 15 -weight bold", text="返回示教模块", command=s_userpage).place(x=0, y=520)

    all_the_task()


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
    tk.Button(root, font="-size 15 -weight bold", text="上肢训练示教", command=action1).place(x=30, y=90)
    tk.Button(root, font="-size 15 -weight bold", text="下肢训练示教", command=action2).place(x=30, y=170)
    tk.Button(root, font="-size 15 -weight bold", text="腹部背部训练示教", command=action3).place(x=30, y=260)
    tk.Button(root, font="-size 15 -weight bold", text="拉伸训练示教", command=action4).place(x=30, y=350)
    tk.Button(root, font="-size 15 -weight bold", text="进入训练模块", command=next_page).place(x=30, y=440)
    movieLabel=tk.Label(root)
    movieLabel.place(x=230, y=90)

    root.mainloop()

# 登录操作
def sign():
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
###############################################################################################################################

# if __name__ == "__main__":
#     main()
