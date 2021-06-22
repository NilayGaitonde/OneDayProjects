from tkinter import *
from youtube_search import YoutubeSearch
from pytube import YouTube
filled=False

def downloadVid():
    vidName=f"{nameText.get()}"
    print(vidName)
    results=YoutubeSearch(vidName,max_results=10).to_dict()
    ytLink='youtube.com'+results[0]['url_suffix']
    print(ytLink)
    yt=YouTube(ytLink)
    # print(yt.title)
    stream=yt.streams.first()
    print(yt.length,'miuntes')
    stream.download()
    print(yt.description)

def click(*args):
    nameText.delete(0,'end')
    global filled
    filled=True

root=Tk()
root.title('YouTube Downloader')
root.minsize(width=300,height=200)

nameText=Entry(root,width=30)
nameText.insert(0,'Enter video title:')
nameText.bind("<Button-1>",click)
nameText.grid(row=0,column=0)

downloadButton=Button(root,text='DOWNLOAD',command=downloadVid).grid(row=0,column=1)

root.mainloop()