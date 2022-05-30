from pytube import YouTube
import tkinter as tk
from tkinter import  messagebox

def get_entry_1():
    value_1=link_entry.get()
    value_2=ent2.get()
    if value_1 and value_2:
        youtube(value_1,value_2)
        delete_entry_1()
        clicked()
    else:
        print('Empty entry')

def delete_entry_1():
    link_entry.delete(0,'end')
    ent2.delete(0,'end')

def clicked():
    messagebox.showinfo('Congratulations!', 'Download completed successfully!\nSearch for the file in the specified folder.')

win=tk.Tk()
win.geometry('300x250')

lbl_1=tk.Label(text='Enter the link to the video:').grid(row=0,column=0, sticky='wn', )
frm_1=tk.Frame(win,borderwidth=2 )
frm_1.grid(row=1,column=0, sticky='we')
link_entry=tk.Entry(master=frm_1)
link_entry.grid(row=1,column=0,sticky='nsew')
win.grid_columnconfigure(0,weight=1)

lbl_2=tk.Label(text='Specify the path where to save the video:').grid(row=2,column=0,sticky='w')
frm_2=tk.Frame( borderwidth=2)
frm_2.grid(row=3,column=0, sticky='we')
ent2=tk.Entry(master=frm_2)
ent2.grid(row=3,column=0, sticky='we')

link_btn=tk.Button(text='Enter', command=get_entry_1).grid(row=4,column=0,sticky='w')

def youtube(link,puth):
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4')
    yt.streams.order_by('resolution')
    yt.streams.desc()
    yt.streams.first().download(puth)

win.mainloop()

