from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil
import requests
from tkinter import *
ydl_opts = {}
a=[]

root=Tk()
root.geometry('600x250')
root.title('Tohfa Youtube Video Downloader ')
#root.iconbitmap('download.ico')
label_1=Label(root,text='Paste The Youtube Link Here',font=('blod',20))
label_1.place(x=120,y=20)
url=StringVar()
pastelink=Entry(root,width=60,textvariable=url)
pastelink.place(x=140,y=80)
chunk_size =256

def downloadVideoYoutube():
    x=str(url.get())
    a.append(x)
    
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(a)
    

Button(root,text="Download Video Youtube",width=20,bg='red',fg='white',command=downloadVideoYoutube).place(x=160,y=110)




chunk_size =256

def downloadVideo():
    x=str(url.get())
    
    
    r=requests.get(x,stream=True)

    with open('hacked.mp4','wb') as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            f.write(chunk)
    

Button(root,text="Download Video",width=20,bg='green',fg='white',command=downloadVideo).place(x=330,y=110)

def downloadAudio():
    x=str(url.get())
    
    
    r=requests.get(x,stream=True)

    with open('hacked.mp3','wb') as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            f.write(chunk)
    print('Downloaded')
Button(root,text="Download audio",width=20,bg='blue',fg='white',command=downloadAudio).place(x=250,y=140)
root.mainloop()


