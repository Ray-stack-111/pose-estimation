import math
import cv2
import numpy as np


deep_keen_count=0
deep_keen_dir=0
deep_keen_state = ['none', 'is_bending', 'bend_ok']
deep_keen_text_state = deep_keen_state[0]

pull_up_count=0
pull_up_dir=0
pull_up_state=['none','is_pull_up','pull_up_ok']
pull_up_text_state=pull_up_state[0]

barbrll_bent_over_row_count=0
barbrll_bent_over_row_dir=1
barbell_state=['none','is_barbell','barbell_ok']
barbell_text_state=barbell_state[0]

crunch_count=0
crunch_dir=0
crunch_state=['none','is_crunch','crunch_ok']
crunch_text_state=crunch_state[0]

stretch_count=0
stretch_dir=0

push_up_count=0
push_up_dir=1

lunge_left_count=0
lunge_left_dir=1

lunge_right_count=0
lunge_right_dir=1

stretch_left_count = 0
stretch_left_dir = 1

stretch_right_count = 0
stretch_right_dir = 1

def find_angle(img,lmlist,p1,p2,p3,draw=True):
        x1,y1  = lmlist[p1][1:]
        x2, y2 = lmlist[p2][1:]
        x3, y3 = lmlist[p3][1:]


        angle = math.degrees((math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2)))
        if angle <0:
            angle=-angle
        if 180<angle :
            angle=360-angle
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 9)
            cv2.line(img, (x2, y2), (x3, y3), (255, 255, 255), 9)
            cv2.circle(img, (x1, y1), 5, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (255, 0, 0), 2)
            cv2.circle(img, (x2, y2), 5, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 0), 2)
            cv2.circle(img, (x3, y3), 5, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (255, 0, 0), 2)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        return angle



def find_distance(img,lmlist,c1,c2,draw=True):
        x1, y1 = lmlist[c1][1:]
        x2, y2 = lmlist[c2][1:]

        distance= math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))

        if draw:
            cv2.line(img,(x1,y1),(x2,y2),(255,255,255),9)
            cv2.circle(img, (x1, y1), 5, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (255, 0, 0), 2)
            cv2.circle(img, (x2, y2), 5, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 0), 2)
            cv2.putText(img, str(int(distance)), (x2-50, y2+50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        return distance


def all_poses_count_clear():
    global  deep_keen_count
    global  pull_up_count
    global  barbrll_bent_over_row_count
    global  stretch_count
    global  crunch_count
    global  lunge_left_count
    global  lunge_right_count
    global  stretch_left_count
    global  stretch_right_count

    deep_keen_count=0
    pull_up_count=0
    barbrll_bent_over_row_count=0
    stretch_count=0
    crunch_count=0
    lunge_left_count = 0
    lunge_right_count = 0
    stretch_left_count = 0
    stretch_right_count = 0


def deep_keen_dete(img,lmlist):
    global deep_keen_dir
    global deep_keen_count
    global deep_keen_text_state

    while True:

        if len(lmlist) !=0:
            left_leg_angle=find_angle(img,lmlist,23,25,27)
            left_leg_per=np.interp(left_leg_angle,(130,160),(0,100))
            right_leg_angle = find_angle(img, lmlist,24, 26, 28)
            right_leg_per = np.interp(right_leg_angle, (130, 160), (0, 100))
            per_leg_angle=(left_leg_angle+right_leg_angle)/2
            shoulder_diatance=find_distance(img,lmlist,11,12)
            feet_distance=find_distance(img,lmlist,27,28)

            if shoulder_diatance > feet_distance:
                cv2.putText(img, 'please split your feet as wide as your shoulder', (0, 250), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)

            left_hip_position=lmlist[23]
            right_hip_position=lmlist[24]
            right_knee_position=lmlist[26]
            left_knee_position=lmlist[25]

            print("left_hip_position:",left_hip_position[2])
            print("left_knee_position:",left_knee_position[2])
            print("left_leg_angle:",left_leg_angle)

            if left_leg_per ==100 or right_leg_per ==100 :
                if deep_keen_dir ==1:
                    deep_keen_count +=0.5
                    deep_keen_dir=0
                    deep_keen_text_state=deep_keen_state[1]


            elif left_leg_per ==0 or right_leg_per ==0 :
                if deep_keen_dir ==0:
                    deep_keen_count+=0.5
                    deep_keen_dir = 1
                    deep_keen_text_state = deep_keen_state[2]

            cv2.putText(img, 'per_leg_angle', (0, 300), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)
            cv2.putText(img, str(per_leg_angle),(0, 400), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)

            if deep_keen_text_state=='is_bending':
                cv2.putText(img, 'please keep down', (0, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)
            elif deep_keen_text_state=='bend_ok':
                cv2.putText(img, 'ok,a deep_keen_bend is done', (0, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)
            return(img,deep_keen_count)


def barbrll_bent_over_row(img,lmlist):
    global  barbrll_bent_over_row_count
    global  barbrll_bent_over_row_dir
    global  barbell_state
    global  barbell_text_state
    while True:


        if len(lmlist) !=0:
            left_leg_angle=find_angle(img,lmlist,13,11,23)
            left_leg_per=np.interp(left_leg_angle,(5,48),(0,100))

            right_leg_angle = find_angle(img,lmlist, 14, 12, 24)
            right_leg_per = np.interp(right_leg_angle, (5, 48), (0, 100))


            if left_leg_per ==100 or right_leg_per ==100:
                if barbrll_bent_over_row_dir ==1:
                    barbrll_bent_over_row_count+=0.25
                    barbrll_bent_over_row_dir=0
                    barbell_text_state=barbell_state[1]

            if left_leg_per ==0 or right_leg_per ==0:
                if barbrll_bent_over_row_dir ==0:
                    barbrll_bent_over_row_count+=0.25
                    barbrll_bent_over_row_dir=1
                    barbell_text_state=barbell_state[2]
            # barbell_state = ['none', 'is_barbell', 'barbell_ok']
            # barbell_text_state = barbell_state[0]

            if barbell_text_state=='is_barbell':
                cv2.putText(img, 'keep on', (0, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)
            elif barbell_text_state=='barbell_ok':
                cv2.putText(img, 'ok a barbell_bent_over is done', (0, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)

            return(img,barbrll_bent_over_row_count)


def crunch(img,lmlist):
    global crunch_count
    global crunch_dir
    global crunch_state
    global crunch_text_state
    while True:

        if len(lmlist) !=0:
            left_haunch_angle=find_angle(img,lmlist,11,23,25)
            left_haunch_per=np.interp(left_haunch_angle,(95,120),(0,100))

            right_haunch_angle = find_angle(img,lmlist, 12, 24, 26)
            right_haunch_per = np.interp(right_haunch_angle, (95, 120), (0, 100))

            if left_haunch_per ==100 or right_haunch_per ==100 :
                if crunch_dir ==0:
                    crunch_count +=0.5
                    crunch_dir=1
                    crunch_text_state=crunch_state[1]

            if left_haunch_per ==0 or left_haunch_per ==0:
                if crunch_dir ==1:
                    crunch_count+=0.5
                    crunch_dir=0
                    crunch_text_state=crunch_state[2]

                #crunch_state=['none','is_crunch','crunch_ok']
            if crunch_text_state == 'is_crunch':
                cv2.putText(img, 'keep on', (0, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)
            elif crunch_text_state == 'crunch_ok':
                cv2.putText(img, 'ok a crunch is done ', (0, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)

            return (img,crunch_count)


def pull_up(img,lmlist):
    global pull_up_count
    global pull_up_dir
    pull_up_all_state=['none','up','down']
    pull_up_now_state=pull_up_all_state[0]
    global pull_up_state
    global pull_up_text_state
    while True:

        if len(lmlist) !=0:
            left_pinky_distance=find_distance(img,lmlist,0,17)
            right_pinky_distance=find_distance(img,lmlist,0,18)
            averge_pinky_distance=(left_pinky_distance+right_pinky_distance)/2

            pull_up_bar = np.interp(averge_pinky_distance, (160, 200), (50, 300))

            id01,left_pinky_position_x,left_pinky_position_y=lmlist[17]
            id02,right_pinky_position_x,right_pinky_position_y=lmlist[18]
            id03,nose_position_x,nose_position_y=lmlist[0]

            if nose_position_y < (left_pinky_position_y+right_pinky_position_y)/2 :
                pull_up_now_state=pull_up_all_state[1]
            elif nose_position_y > (left_pinky_position_y+right_pinky_position_y)/2:
                pull_up_now_state=pull_up_all_state[2]

            if pull_up_now_state=='up' and pull_up_dir==1:
                pull_up_count+=0.5
                pull_up_dir  =0
                pull_up_text_state=pull_up_state[1]

            elif pull_up_now_state=='down' and pull_up_dir==0:
                pull_up_count+=0.5
                pull_up_dir=1
                pull_up_text_state=pull_up_state[2]

            # pull_up_state=['none','is_pull_up','pull_up_ok']
            # pull_up_text_state=pull_up_state[0]
            if pull_up_text_state == 'is_pull_up':
                cv2.putText(img, 'keep on', (0, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)
            elif pull_up_text_state == 'pull_up_ok':
                cv2.putText(img, 'ok a pull_up is done ', (0, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 5)

            return(img,pull_up_count)


def stretch(img,lmlist):
    stretch_mode=['left','right','none']
    global stretch_count
    global stretch_dir
    dir=stretch_mode[2]

    while True:

        if len(lmlist) !=0:
            id_0,nose_position_x,nose_position_y=lmlist[0]
            id_24,right_hip_position_x,right_hip_position_y=lmlist[24]
            id_23,left_hip_position_x,left_hip_position_y=lmlist[23]

            if nose_position_x > left_hip_position_x:
                dir=stretch_mode[0]
            elif nose_position_x < right_hip_position_x:
                dir=stretch_mode[1]
            else:
                dir=stretch_mode[2]


            if dir=='left' and stretch_dir==0 :
                stretch_count+=1
                stretch_dir=1
            if dir=='right' and stretch_dir==1:
                stretch_count+=1
                stretch_dir=0

            return(img,stretch_count)

def stretch_left(img,lmlist):
    global stretch_left_count
    global stretch_left_dir

    while True:

        if len(lmlist) != 0:
            right_leg_angle = find_angle(img,lmlist, 11, 23, 25)
            right_leg_per = np.interp(right_leg_angle, (150, 175), (0, 100))

            if right_leg_per == 100:
                if stretch_left_dir  == 0:
                    stretch_left_count += 0.5
                    stretch_left_dir  = 1

            if right_leg_per == 0:
                if stretch_left_dir  == 1:
                    stretch_left_count += 0.5
                    stretch_left_dir  = 0

        return (img, stretch_left_count)


def stretch_right(img,lmlist):
    global stretch_right_count
    global stretch_right_dir

    while True:

        if len(lmlist) != 0:
            right_leg_angle = find_angle(img,lmlist, 12, 24, 26)
            right_leg_per = np.interp(right_leg_angle, (150, 175), (0, 100))

            if right_leg_per == 100:
                if stretch_right_dir  == 0:
                    stretch_right_count += 0.5
                    stretch_right_dir  = 1

            if right_leg_per == 0:
                if stretch_right_dir  == 1:
                    stretch_right_count += 0.5
                    stretch_right_dir  = 0

        return (img, stretch_right_count)


def push_up(img,lmlist):
    global push_up_count
    global push_up_dir
    down_state = False

    while True:

        if len(lmlist) != 0:
            left_arm_angle = find_angle(img,lmlist, 11, 13, 15)
            left_arm_per = np.interp(left_arm_angle, (60, 160), (0, 100))
            left_arm_bar = np.interp(left_arm_angle, (60, 160), (50, 300))

            right_arm_angle = find_angle(img,lmlist, 12, 14, 16)
            right_arm_per = np.interp(right_arm_angle, (60, 160), (0, 100))
            right_arm_bar = np.interp(right_arm_angle, (60, 160), (50, 300))

            nose_position = lmlist[0]
            left_shoulder_position = lmlist[11]
            right_shoulder_position = lmlist[12]

            print("nose_position:", nose_position[2])
            print("left_shoulder_position:", left_shoulder_position[2])

            if nose_position[2] > left_shoulder_position[2] and nose_position[2] > right_shoulder_position[2]:
                down_state = True
            else:
                down_state = False

            if left_arm_per == 100 or right_arm_per == 100:
                if push_up_dir == 0:
                    push_up_count  += 0.5
                    push_up_dir = 1

            if (left_arm_per == 0 or right_arm_per == 0) and down_state:
                if push_up_dir== 1:
                    push_up_count  += 0.5
                    push_up_dir = 0

            cv2.rectangle(img, (500, 50), (540, 300), (0, 255, 0), 3)
            cv2.rectangle(img, (500, int(left_arm_bar)), (540, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(left_arm_per), (460, 330), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 5)

            cv2.rectangle(img, (560, 50), (600, 300), (0, 255, 0), 3)
            cv2.rectangle(img, (560, int(right_arm_bar)), (600, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(right_arm_per), (560, 330), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 5)


            return (img, push_up_count)

def Lunge_left(img,lmlist):
    global lunge_left_count
    global lunge_left_dir
    down_state=False

    while True:

        if len(lmlist) !=0:

            left_leg_angle=find_angle(img,lmlist,23,25,27)
            left_leg_per=np.interp(left_leg_angle,(90,130),(0,100))

            if left_leg_per ==100:
                if lunge_left_dir ==0:
                    lunge_left_count +=0.5
                    lunge_left_dir=1

            if left_leg_per ==0:
                if lunge_left_dir ==1:
                    lunge_left_count+=0.5
                    lunge_left_dir=0
        return (img,lunge_left_count )


def Lunge_right(img,lmlist):
    global lunge_right_count
    global lunge_right_dir
    down_state=False

    while True:

        if len(lmlist) !=0:

            right_leg_angle=find_angle(img,lmlist,24,26,28)
            right_leg_per=np.interp(right_leg_angle,(90,130),(0,100))

            if right_leg_per ==100:
                if lunge_right_dir ==0:
                    lunge_right_count+=0.5
                    lunge_right_dir=1

            if right_leg_per ==0:
                if lunge_right_dir ==1:
                    lunge_right_count+=0.5
                    lunge_right_dir=0

        return (img, lunge_right_count)

