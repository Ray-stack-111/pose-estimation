import math

import cv2
import mediapipe as mp
import time



class poseDetector():
    def __init__(self, static_image_mode = False,model_complexity = 1,smooth_landmarks = True,enable_segmentation = False,
        smooth_segmentation = True,min_detection_confidence = 0.5,min_tracking_confidence = 0.5):

        self.static_image_mode=static_image_mode
        self.model_complexity =model_complexity
        self.smooth_landmarks=smooth_landmarks
        self.enable_segmentation =enable_segmentation
        self.smooth_segmentation =smooth_segmentation
        self.min_detection_confidence=min_detection_confidence
        self.min_tracking_confidence=min_tracking_confidence

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.static_image_mode,self.model_complexity,self.smooth_landmarks,self.enable_segmentation,
                                     self.smooth_segmentation,self.min_detection_confidence,self.min_tracking_confidence)

    def findPose(self,img,draw=True,size_change=1):
        x,y,z=img.shape
        x=int(x*size_change)
        y=int(y*size_change)
        img=cv2.resize(img,(y,x))
        self.imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.result=self.pose.process(self.imgRGB)
        if self.result.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,self.result.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
        return img

    def getPosition(self,img,draw=True):
        self.lmlist=[]
        if self.result.pose_landmarks:
            for id, lm in enumerate(self.result.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 1, (255, 0, 0), cv2.FILLED)
        return self.lmlist

    def find_distance(self,img,c1,c2,draw=True):
        x1, y1 = self.lmlist[c1][1:]
        x2, y2 = self.lmlist[c2][1:]

        distance= math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))

        if draw:
            cv2.line(img,(x1,y1),(x2,y2),(255,255,255),9)
            cv2.circle(img, (x1, y1), 5, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (255, 0, 0), 2)
            cv2.circle(img, (x2, y2), 5, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 0), 2)
            cv2.putText(img, str(int(distance)), (x2-50, y2+50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        return distance


    def find_angle(self,img,p1,p2,p3,draw=True):
        x1,y1  = self.lmlist[p1][1:]
        x2, y2 = self.lmlist[p2][1:]
        x3, y3 = self.lmlist[p3][1:]


        angle = math.degrees((math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2)))
        if angle <0:
            angle=-angle
        if 180<angle :
            angle=360-angle


        if draw:
            cv2.line(img,(x1,y1),(x2,y2),(255,255,255),9)
            cv2.line(img,(x2, y2), (x3, y3), (255, 255, 255),9)
            cv2.circle(img, (x1, y1), 5, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (255, 0, 0), 2)
            cv2.circle(img, (x2, y2), 5, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 0), 2)
            cv2.circle(img, (x3, y3), 5, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (255, 0, 0), 2)
            cv2.putText(img, str(int(angle)), (x2-50, y2+50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        return angle



def main():
    ptime = 0
    cap = cv2.VideoCapture(0)
    detector=poseDetector()

    while True:

        success, img = cap.read()
        img=detector.findPose(img)
        lmlist = detector.getPosition(img, False)
        if len(lmlist) != 0:
            lmlist=detector.getPosition(img)
            print(lmlist)
            distance01=detector.find_distance(img,23,25)
            distance02 = detector.find_distance(img, 25, 27)
            print('datui:',distance01)
            print('xiaotui:', distance02)
            cttime = time.time()
            fps = 1 / (cttime - ptime)
            ptime = cttime

            cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            cv2.imshow("Image", img)

            cv2.waitKey(1)


if __name__ =="__main__":
    main()