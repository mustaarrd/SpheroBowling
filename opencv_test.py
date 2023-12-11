from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
from threading import Thread, Event 
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.types import Color
from animation import Animaition
from datetime import datetime, timedelta
from time import time

#region 변수
low_bgr = np.array([0, 0, 0])
high_bgr = np.array([255, 255, 255])
min_size = 1000
max_size = 5000
blob = 0
game_pin = 6
angle = 0
start = 200
speed = 0
count = 3
round = 0
turn = 'SB-286E'#'SB-70A1'
score = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
names =['SB-286E', 'SB-C1F1', 'SB-818E', 'SB-286E']
mode = 99
balls = []
window = Tk()
cap = None
rg_thread, mask_thread, blob_thread = None, None, None
stop_capture = Event()
lock = False
#endregion


def Delay(sec):
    wait = datetime.now() + timedelta(seconds=sec)
    while True:
        if wait <= datetime.now():
            break

def on_cls0(api):
    global mode, angle, speed, count, round, lock, turn
    if lock: 
        return
    else:
        if turn != names[0]:
            return
        lock = True
    if mode == 0:
        if blob != game_pin:
            api.set_main_led(Color(255, 51, 51))
            api.set_main_led(Color(0, 0, 0))
            api.set_main_led(Color(255, 51, 51))
            api.set_main_led(Color(0, 0, 0))
            api.set_main_led(Color(255, 51, 51))
            api.set_main_led(Color(0, 0, 0))
            return
        api.set_stabilization(stabilize=False)
        mode = 1
        #angle
        api.play_matrix_animation(animation_id=0, loop=True)
    else:
        if mode == 1:
            #check
            api.play_matrix_animation(animation_id=3)
            api.reset_aim()
            Delay(1.5)
            api.set_heading(heading=0)
            ori = api.get_orientation()['roll']
            angle = (((ori % 4) - 2) * 2)
            #heart
            api.play_matrix_animation(animation_id=4)
            mode = 2
        elif mode == 2:
            #check
            api.play_matrix_animation(animation_id=3)
            Delay(1.5)
            #arrow
            api.play_matrix_animation(animation_id=1, loop=False)
            ori = api.get_orientation()['pitch']
            speed = (((ori % 2) * 70) + 100) 
            mode = 3
        elif mode == 3:
            api.set_main_led(Color(255, 255, 255))
            for i in range(3, 0, -1):
                api.set_matrix_character(character=str(i), color=Color(255,205,154))
                Delay(1)
            #arrow
            api.play_matrix_animation(animation_id=1)
            api.set_heading(heading=int(angle))
            api.set_speed(speed=int(speed))
            move = api.get_distance()
            for i in range(0, 100):
                if start + move <= api.get_distance():
                    break
                else:
                    Delay(0.1)
            api.stop_roll()
            score[round][0] = blob
           #return
            api.play_matrix_animation(animation_id=2)
            move = api.get_distance()
            Delay(3)
            api.set_heading(heading=int(angle + 180))
            api.set_speed(int((speed - 70)))
            for i in range(0, 100):
                if start + move <= api.get_distance():
                    break
                else:
                    Delay(0.1)
            api.stop_roll()
            mode = 4
            if round == 0:
                turn = names[1]
                api.scroll_matrix_text(text="1 Round End", color=Color(203,255,117), fps=15, wait=True)
                balls[1].set_main_led(Color(0,255,0))
            elif round == 1:
                turn = names[1]
                api.scroll_matrix_text(text="2 Round End", color=Color(255,166,35), fps=15, wait=True)
                balls[1].set_main_led(Color(0,255,0))
            elif round == 2:
                turn = names[1]
                api.scroll_matrix_text(text="GameOver", color=Color(255,51,51), fps=15, wait=True)
                balls[1].set_main_led(Color(0,255,0))
            mode = 0 
    lock = False

def on_cls1(api):
    global mode, angle, speed, count, round, lock, turn
    if lock: 
        return
    else:
        if turn != names[1]:
            return
        lock = True
    if mode == 0:
        if blob != game_pin:
            api.set_main_led(Color(255, 51, 51))
            api.set_main_led(Color(0, 0, 0))
            api.set_main_led(Color(255, 51, 51))
            api.set_main_led(Color(0, 0, 0))
            api.set_main_led(Color(255, 51, 51))
            api.set_main_led(Color(0, 0, 0))
            return
        api.set_stabilization(stabilize=False)
        mode = 1
        #angle
        api.play_matrix_animation(animation_id=0, loop=True)
    else:
        if mode == 1:
            #check
            api.play_matrix_animation(animation_id=3)
            api.reset_aim()
            Delay(1.5)
            api.set_heading(heading=0)
            ori = api.get_orientation()['roll']
            angle = (((ori % 4) - 2) * 2)
            #heart
            api.play_matrix_animation(animation_id=4)
            mode = 2
        elif mode == 2:
            #check
            api.play_matrix_animation(animation_id=3)
            Delay(1.5)
            #arrow
            api.play_matrix_animation(animation_id=1, loop=False)
            ori = api.get_orientation()['pitch']
            speed = (((ori % 2) * 70) + 100) 
            mode = 3
        elif mode == 3:
            api.set_main_led(Color(255, 255, 255))
            for i in range(3, 0, -1):
                api.set_matrix_character(character=str(i), color=Color(255,205,154))
                Delay(1)
            #arrow
            api.play_matrix_animation(animation_id=1)
            api.set_heading(heading=int(angle))
            api.set_speed(speed=int(speed))
            move = api.get_distance()
            for i in range(0, 100):
                if start + move <= api.get_distance():
                    break
                else:
                    Delay(0.1)
            api.stop_roll()
            score[round][1] = blob
           #return
            api.play_matrix_animation(animation_id=2)
            move = api.get_distance()
            Delay(3)
            api.set_heading(heading=int(angle + 180))
            api.set_speed(int((speed - 70)))
            for i in range(0, 100):
                if start + move <= api.get_distance():
                    break
                else:
                    Delay(0.1)
            api.stop_roll()
            mode = 4
            if round == 0:
                turn = names[2]
                api.scroll_matrix_text(text="1 Round End", color=Color(203,255,117), fps=15, wait=True)
                balls[2].set_main_led(Color(0,255,0))
            elif round == 1:
                turn = names[2]
                api.scroll_matrix_text(text="2 Round End", color=Color(255,166,35), fps=15, wait=True)
                balls[2].set_main_led(Color(0,255,0))
            elif round == 2:
                turn = names[2]
                api.scroll_matrix_text(text="GameOver", color=Color(255,51,51), fps=15, wait=True)
                balls[21].set_main_led(Color(0,255,0))
            mode = 0 
    lock = False

def on_cls2(api):
    global mode, angle, speed, count, round, lock, turn
    if lock: 
        return
    else:
        if turn != names[2]:
            return
        lock = True
    if mode == 0:
        if blob != game_pin:
            api.set_main_led(Color(255, 51, 51))
            api.set_main_led(Color(0, 0, 0))
            api.set_main_led(Color(255, 51, 51))
            api.set_main_led(Color(0, 0, 0))
            api.set_main_led(Color(255, 51, 51))
            api.set_main_led(Color(0, 0, 0))
            return
        api.set_stabilization(stabilize=False)
        mode = 1
        #angle
        api.play_matrix_animation(animation_id=0, loop=True)
    else:
        if mode == 1:
            #check
            api.play_matrix_animation(animation_id=3)
            api.reset_aim()
            Delay(1.5)
            api.set_heading(heading=0)
            ori = api.get_orientation()['roll']
            angle = (((ori % 4) - 2) * 2)
            #heart
            api.play_matrix_animation(animation_id=4)
            mode = 2
        elif mode == 2:
            #check
            api.play_matrix_animation(animation_id=3)
            Delay(1.5)
            #arrow
            api.play_matrix_animation(animation_id=1, loop=False)
            ori = api.get_orientation()['pitch']
            speed = (((ori % 2) * 70) + 100) 
            mode = 3
        elif mode == 3:
            api.set_main_led(Color(255, 255, 255))
            for i in range(3, 0, -1):
                api.set_matrix_character(character=str(i), color=Color(255,205,154))
                Delay(1)
            #arrow
            api.play_matrix_animation(animation_id=1)
            api.set_heading(heading=int(angle))
            api.set_speed(speed=int(speed))
            move = api.get_distance()
            for i in range(0, 100):
                if start + move <= api.get_distance():
                    break
                else:
                    Delay(0.1)
            api.stop_roll()
            score[round][2] = blob
           #return
            api.play_matrix_animation(animation_id=2)
            move = api.get_distance()
            Delay(3)
            api.set_heading(heading=int(angle + 180))
            api.set_speed(int((speed - 70)))
            for i in range(0, 100):
                if start + move <= api.get_distance():
                    break
                else:
                    Delay(0.1)
            api.stop_roll()
            mode = 4
            if round == 0:
                turn = names[3]
                api.scroll_matrix_text(text="1 Round End", color=Color(203,255,117), fps=15, wait=True)
                balls[3].set_main_led(Color(0,255,0))
            elif round == 1:
                turn = names[3]
                api.scroll_matrix_text(text="2 Round End", color=Color(255,166,35), fps=15, wait=True)
                balls[3].set_main_led(Color(0,255,0))
            elif round == 2:
                turn = names[3]
                api.scroll_matrix_text(text="GameOver", color=Color(255,51,51), fps=15, wait=True)
                balls[3].set_main_led(Color(0,255,0))
            mode = 0 
    lock = False

def on_cls3(api):
    global mode, angle, speed, count, round, lock, turn
    if lock: 
        return
    else:
        if turn != names[3]:
            return
        lock = True
    if mode == 0:
        if blob != game_pin:
            api.set_main_led(Color(255, 51, 51))
            api.set_main_led(Color(0, 0, 0))
            api.set_main_led(Color(255, 51, 51))
            api.set_main_led(Color(0, 0, 0))
            api.set_main_led(Color(255, 51, 51))
            api.set_main_led(Color(0, 0, 0))
            return
        api.set_stabilization(stabilize=False)
        mode = 1
        #angle
        api.play_matrix_animation(animation_id=0, loop=True)
    else:
        if mode == 1:
            #check
            api.play_matrix_animation(animation_id=3)
            api.reset_aim()
            Delay(1.5)
            api.set_heading(heading=0)
            ori = api.get_orientation()['roll']
            angle = (((ori % 4) - 2) * 2)
            #heart
            api.play_matrix_animation(animation_id=4)
            mode = 2
        elif mode == 2:
            #check
            api.play_matrix_animation(animation_id=3)
            Delay(1.5)
            #arrow
            api.play_matrix_animation(animation_id=1, loop=False)
            ori = api.get_orientation()['pitch']
            speed = (((ori % 2) * 70) + 100) 
            mode = 3
        elif mode == 3:
            api.set_main_led(Color(255, 255, 255))
            for i in range(3, 0, -1):
                api.set_matrix_character(character=str(i), color=Color(255,205,154))
                Delay(1)
            #arrow
            api.play_matrix_animation(animation_id=1)
            api.set_heading(heading=int(angle))
            api.set_speed(speed=int(speed))
            move = api.get_distance()
            for i in range(0, 100):
                if start + move <= api.get_distance():
                    break
                else:
                    Delay(0.1)
            api.stop_roll()
            score[round][3] = blob
           #return
            api.play_matrix_animation(animation_id=2)
            move = api.get_distance()
            Delay(3)
            api.set_heading(heading=int(angle + 180))
            api.set_speed(int((speed - 70)))
            for i in range(0, 100):
                if start + move <= api.get_distance():
                    break
                else:
                    Delay(0.1)
            api.stop_roll()
            mode = 4
            if round == 0:
                turn = names[0]
                api.scroll_matrix_text(text="1 Round End", color=Color(203,255,117), fps=15, wait=True)
                balls[0].set_main_led(Color(0,255,0))
                round += 1
            elif round == 1:
                turn = names[0]
                api.scroll_matrix_text(text="2 Round End", color=Color(255,166,35), fps=15, wait=True)
                balls[0].set_main_led(Color(0,255,0))
                round += 1
            elif round == 2:
                turn = names[0]
                api.scroll_matrix_text(text="GameOver", color=Color(255,51,51), fps=15, wait=True)
                balls[0].set_main_led(Color(0,255,0))
                round += 1
            mode = 0 
    lock = False

def game_start():
    global mode, turn
    if blob == game_pin:
        round = 0
        mode = 0
        turn = names[0]
        balls[0].set_main_led(Color(0,255,0))
        while True:
            time.sleep(0.1)
            if round == 3:
                break
        bs1 = score[0][0] + score[1][0] + score[2][0]
        bs2 = score[0][1] + score[1][1] + score[2][1]
        bs3 = score[0][2] + score[1][2] + score[2][2]
        bs4 = score[0][3] + score[1][3] + score[2][3]
        sum = [bs1, bs2, bs3, bs4]
        sum.sort()
        if bs1 == sum[0]:
            balls[0].play_matrix_animation(animation_id=5)
        if bs2 == sum[1]:
            balls[1].play_matrix_animation(animation_id=5)
        if bs3 == sum[2]:
            balls[2].play_matrix_animation(animation_id=5)
        if bs4 == sum[3]:
            balls[3].play_matrix_animation(animation_id=5)
        
    else:
        tkinter.messagebox.showerror("error", "이미지를 점검하세요.")
        return

#region video  
def video_masking(param):
    while True:
        try:
            if stop_capture.is_set():
                return
        
            ret, frame = cap.read()
            if ret:
                global low_bgr, high_bgr
                mask = cv2.inRange(frame, low_bgr, high_bgr)
                cv2image = cv2.cvtColor(mask, cv2.COLOR_BGR2RGBA)
                img = Image.fromarray(cv2image)
                imgtk = ImageTk.PhotoImage(image=img)
                param.create_image(0, 0, image=imgtk, anchor=NW)
                param.image = imgtk
            else:
                pass
        except:
            pass
    
    

def video_get_blob(param):
    global low_bgr, high_bgr, min_size, max_size, valid_contours, blob

    while True:
        try:
            if stop_capture.is_set():
                return
    
            prev_count = 0
            ret, frame = cap.read()
            if not ret or frame is None:
                pass

            mask = cv2.inRange(frame, low_bgr, high_bgr)
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            valid_contours = 0
            for cnt in contours:
                area = cv2.contourArea(cnt)
                if min_size <= area <= max_size:
                    x, y, w, h = cv2.boundingRect(cnt)
                    # 색상 일치 비율 확인
                    if np.sum(mask[y:y+h, x:x+w]) / (w*h) > 0.75: # 75% 이상
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        valid_contours += 1

            # 검출된 덩어리 수 업데이트
            if valid_contours != prev_count:
                count_label.config(text=f"{valid_contours} 덩어리 검출됨")
                prev_count = valid_contours
                blob = valid_contours

            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            param.create_image(0, 0, image=imgtk, anchor=NW)
            param.image = imgtk
        except:
            pass
#endregion
#region TKinter 설정
def update_settings(val):
    global low_bgr, high_bgr, min_size, max_size
    low_bgr = np.array([blue_low.get(), green_low.get(), red_low.get()])
    high_bgr = np.array([blue_high.get(), green_high.get(), red_high.get()])
    min_size = min_size_scale.get()
    max_size = max_size_scale.get()

window.title("OpenCV and Tkinter")
window.geometry("1400x600")

right_frame = Frame(window, border=1, relief="solid", width=220)
right_frame.pack(side=RIGHT, fill=BOTH, anchor="e")

top_frame = Frame(window)
top_frame.pack(side=TOP, fill=BOTH, expand=True, anchor="nw")

lt_frame = Frame(top_frame, border=2, relief="solid")
lt_frame.pack(side=LEFT, fill=BOTH, expand=True)
rt_frame = Frame(top_frame, border=2, relief="solid")
rt_frame.pack(side=RIGHT, fill=BOTH, expand=True)

org_cam = Canvas(lt_frame)
org_cam.pack(fill=BOTH, expand=True)

mask_cam = Canvas(rt_frame)
mask_cam.pack(fill=BOTH, expand=True)


blue_low_label = Label(right_frame, text="blue Low")
blue_low_label.pack()
blue_low = Scale(right_frame, from_=0, to=255, orient=HORIZONTAL, command=update_settings)
blue_low.set(0)
blue_low.pack()

green_low_label = Label(right_frame, text="green Low")
green_low_label.pack()
green_low = Scale(right_frame, from_=0, to=255, orient=HORIZONTAL, command=update_settings)
green_low.set(0)
green_low.pack()

red_low_label = Label(right_frame, text="red Low")
red_low_label.pack()
red_low = Scale(right_frame, from_=0, to=255, orient=HORIZONTAL, command=update_settings)
red_low.set(0)
red_low.pack()

blue_high_label = Label(right_frame, text="blue High")
blue_high_label.pack()
blue_high = Scale(right_frame, from_=0, to=255, orient=HORIZONTAL, command=update_settings)
blue_high.set(255)
blue_high.pack()

green_high_label = Label(right_frame, text="green High")
green_high_label.pack()
green_high = Scale(right_frame, from_=0, to=255, orient=HORIZONTAL, command=update_settings)
green_high.set(255)
green_high.pack()

red_low_label = Label(right_frame, text="red High")
red_low_label.pack()
red_high = Scale(right_frame, from_=0, to=255, orient=HORIZONTAL, command=update_settings)
red_high.set(255)
red_high.pack()

min_size_scale = Scale(right_frame, from_=0, to=10000, orient=HORIZONTAL, label="최소 사이즈", command=update_settings)
min_size_scale.set(1000)
min_size_scale.pack()

max_size_scale = Scale(right_frame, from_=0, to=10000, orient=HORIZONTAL, label="최대 사이즈", command=update_settings)
max_size_scale.set(5000)
max_size_scale.pack()

Button(right_frame, command=game_start, text="게임 시작").pack()

count_label = Label(right_frame, text=f"{blob} 덩어리 검출됨")
count_label.pack()
#endregion
#region camera
try:
    cap = cv2.VideoCapture(0)
    mask_thread = Thread(target=video_masking, args=(mask_cam,), daemon=True)
    mask_thread.start()

    blob_thread = Thread(target=video_get_blob, args=(org_cam,), daemon=True)
    blob_thread.start()
            
except:
    tkinter.messagebox.showerror("error", "카메라를 불러올 수 없습니다.")
    quit()
#endregion
#region sphero
try:
    ani = Animaition()
    for i in range(0,len(names)):
        balls.append(SpheroEduAPI(scanner.find_toy(toy_name=names[i])))
        if balls[i] is not None:
            balls[i].__enter__()
            balls[i].register_matrix_animation(frames= ani.angle_frames, palette= ani.angle_pallete, fps=ani.angle_fps, transition=False)
            balls[i].register_matrix_animation(frames= ani.arrow_frames, palette= ani.arrow_palette, fps=ani.arrow_fps, transition=False)
            balls[i].register_matrix_animation(frames= ani.return_frames, palette= ani.return_palette, fps=ani.return_fps, transition=False)
            balls[i].register_matrix_animation(frames= ani.check_frames, palette= ani.check_palette, fps=ani.check_fps, transition=False)
            balls[i].register_matrix_animation(frames= ani.heart_frames, palette= ani.heart_palette, fps=ani.heart_fps, transition=False)
            balls[i].set_main_led(Color(255,255,255))
    balls[0].register_event(EventType.on_collision, on_cls0)
    balls[1].register_event(EventType.on_collision, on_cls1)
    balls[2].register_event(EventType.on_collision, on_cls2)
    balls[3].register_event(EventType.on_collision, on_cls3)

except:
    tkinter.messagebox.showerror("error", "통신 개체 연결 상태를 확인하세요.")
    quit()
#endregion

if __name__ == '__main__':
    window.mainloop()
    stop_capture.set()
    if cap is not None:
        cap.release()
