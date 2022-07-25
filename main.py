from tkinter import *
from tkinter import filedialog
from moviepy import * 
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil


# from Saving_Path import select_path
def select_path():
    #allows user to select path from the file explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

#for downloading the file and saving it in the desired directory
def download_file():
    #get link path
    get_link = link_field.get()
    #get file save path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    video = VideoFileClip(mp4_video)
    video.close()
    #moveing file to the selected folder
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete!')
    

screen = Tk()

title = screen.title('YouTube Video Downloader')
canvas = Canvas(screen, width=500, height=500, bg='white')
canvas.pack()

#image :
img = PhotoImage(file = 'yt_logo.png')
#resize
img = img.subsample(5,5)
canvas.create_image(250,80, image=img)

#link :
link_field = Entry(screen, width=60, bg='light blue')
link_label = Label(screen, text="Enter Download Link", font=('Arial', 15), bg='white')

#add widgets
canvas.create_window(250,170, window=link_label)
canvas.create_window(250,205, window=link_field, height=30)

#select path for saving the file
path_label = Label(screen, text="Select folder", font=('Arial', 15), bg='white')
select_button = Button(screen, text="Select", bg='orange', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_path)
#add path_label and select_button to canvas
canvas.create_window(250,260, window=path_label)
canvas.create_window(250,305, window=select_button)

#download botton
download_text = Label(screen, text="Click to start downloading", font=('Arial', 15), bg='white')
download_button = Button(screen, text="Download File", bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_file)
#add to canvas
canvas.create_window(250,375, window=download_text)
canvas.create_window(250,420, window=download_button)


screen.mainloop()