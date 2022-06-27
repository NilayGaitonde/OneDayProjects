import tkinter
from pygame import mixer
import youtube_dl
import shutil
from youtube_search import YoutubeSearch
from tkinter.filedialog import askdirectory
import os

class musicPlayer:
    def __init__(self,root):
        self.root=root
        root.title('Music player')
        root.geometry("500x500")
        self.songName=tkinter.StringVar()
        self.songName.set("Why so silent?")
        name=tkinter.Frame(root)
        self.nameLabel=tkinter.Label(name,textvariable=self.songName,font='Times 20').grid(row=0,column=1)
        name.grid(row=0)

        buttons=tkinter.Frame(root)
        self.queueButton=tkinter.Button(buttons,text='Queue').pack(padx=10,pady=10,side=tkinter.LEFT)
        self.playButton=tkinter.Button(buttons,text='Play',command=self.play).pack(padx=10,pady=15,side=tkinter.LEFT)
        self.pauseButton=tkinter.Button(buttons,text='Pause',command=self.pause).pack(padx=10,pady=20,side=tkinter.LEFT)
        self.increaseButton=tkinter.Button(buttons,text='Increase Vol').pack(padx=10,pady=25,side=tkinter.LEFT)
        buttons.grid(row=1)

        search=tkinter.Frame(root)
        self.searchEntry=tkinter.Entry(search,width=40)
        self.searchIcon=tkinter.Button(search,text='search',command=self.searchSong)
        search.grid(row=2)
        self.searchEntry.grid(row=1,column=0)
        self.searchIcon.grid(row=1,column=2)

        playListFrame=tkinter.Frame(self.root)
        self.playList=tkinter.Listbox(playListFrame,font="helvetica 10",selectmode=tkinter.SINGLE,width=40)
        self.count=0
        for pos,song in enumerate(os.listdir('/Users/nilaygaitonde/Documents/GitHub/OneDayProjects/musicplayer/music')):
            self.playList.insert(pos,song)
            self.count=pos
        self.playList.pack()
        playListFrame.grid(row=3)

    def moveFile(self):
        for files in os.listdir('/Users/nilaygaitonde/Documents/GitHub/OneDayProjects/musicplayer/'):
            if(files.endswith('.mp3')):
                shutil.move('/Users/nilaygaitonde/Documents/GitHub/OneDayProjects/musicplayer/'+files,'/Users/nilaygaitonde/Documents/GitHub/OneDayProjects/musicplayer/music')
    

    def searchSong(self):
        vidname=self.searchEntry.get()+' audio'
        print(vidname)
        results=YoutubeSearch(vidname,max_results=10).to_dict()
        ytLink='youtube.com'+results[0]['url_suffix']
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        audioDownload=youtube_dl.YoutubeDL(ydl_opts)
        try:
            audioDownload.download([ytLink])
        except Exception as e:
            print('Something went wrong',e)
        finally:
            self.moveFile()
            self.playList.delete(0,self.count)
            for pos,song in enumerate(os.listdir('/Users/nilaygaitonde/Documents/GitHub/OneDayProjects/musicplayer/music')):
                self.playList.insert(pos,song)
                self.count=pos

    def play(self):
        mixer.init()
        mixer.music.set_volume(0.7)
        song=self.playList.get(tkinter.ACTIVE)
        self.songName.set(song)
        mixer.music.load('/Users/nilaygaitonde/Documents/GitHub/OneDayProjects/musicplayer/music/'+song)
        mixer.music.play()
    def pause(self):
        mixer.music.pause()
    

root=tkinter.Tk()
music=musicPlayer(root)
root.mainloop()
