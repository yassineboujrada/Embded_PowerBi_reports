from threading import Thread
from .models import Post
import schedule
import time

def mmm():
    print("post")

def main2():
    # post=Post.objects.all()
    schedule.every(10).seconds.do(mmm)
    # .do(send_pdf_file,email,subj,path_pd)

    while True:
        schedule.run_pending()
        time.sleep(1)

t = Thread(target=main2)
t.start()

# class StartSending(threading.Thread):
#     def __init__(self):
#         threading.Thread().__init__(self)
    
#     def run(self):
#         print("hi")