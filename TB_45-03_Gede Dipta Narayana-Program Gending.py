from tkinter import *
from tkinter import filedialog
import pygame
import os

#Registrasi
print('')
print(50*'=')
print('\tSELAMAT DATANG DI PROGRAM GENDING!')
print(50*'=')

print('')
print('Daftar Dulu Yuk!')
print('''
1. Isi Data Diri
0. Keluar
''')
while True:
    try:
        menu = int(input('Pilih Opsi : '))
        break
    except ValueError:
        print('Input Salah')
    except TypeError:
        print('Input Salah')

name = []
gen = []
ask = 'y'

while ask == 'y':
    user = input('\nMasukan Nama Kamu : ')
    genr = input('Masukan Genre Favorit : ')
    name.append(user)
    gen.append(genr)
    with open('Database Pengguna.txt','w') as file:
        file.write(f'Nama : {name}\n')
        file.write(f'Genre : {gen}')
    check = False
    while check == False:
        ask = input('Apakah Kamu Ingin Mengisi Data Diri Lagi? : ')
        check = ask == 'y','ya','yes' or ask == 'n','tidak','no'

print('\nSelamat Datang Di Gending! \nSilahkan Masuk Ke Dalam Aplikasi')


#Main Program
base = Tk()
base.title('Gending')
base.geometry('300x430')
base.config(bg='green')
Label(base, text='Gending', font='Normal 30', bg='green', fg='white').place(x=70, y=0)

pygame.mixer.init()

#Import Song
menubar = Menu(base)
base.config(menu=menubar)

songs = []
songflow = ''
paused = False

def loadsong():
    global songflow
    base.directory = filedialog.askdirectory()
    for song in os.listdir(base.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song) 
    for song in songs:
        listsong.insert('end',song)

    listsong.selection_set(0)
    songflow = songs[listsong.curselection()[0]]

ormenu = Menu(menubar, tearoff=False)
ormenu.add_command(label='Pilih Folder Lagu', command=loadsong)
menubar.add_cascade(label='Masukan Lagu', menu=ormenu)

#Song List Bar
listsong = Listbox(base, bg='green', fg='black', width=100, height=15, selectbackground='white', selectforeground='black')
listsong.pack(pady=50)

#Frame Button
cframe = Frame(base)
cframe.pack()

#Config Button
def conplay():
    global songflow, paused
    if not paused:
        pygame.mixer.music.load(os.path.join(base.directory, songflow))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False
bplay = Button(cframe, text='Play', borderwidth=0, command=conplay)
bplay.grid(row=0, column=1, padx=7, pady=10)

def conpause():
    global paused
    pygame.mixer.music.pause()
    paused = True
bpause = Button(cframe, text='Pause', borderwidth=0, command=conpause)
bpause.grid(row=0, column=2, padx=7, pady=10)

def unpauseco():
    global paused
    pygame.mixer.music.unpause()
    paused = True
bunpause = Button(cframe, text='Resume', borderwidth=0, command=unpauseco)
bunpause.grid(row=0, column=3, padx=7, pady=10)

def costop():
    global paused
    pygame.mixer.music.stop()
    paused = True
bunpause = Button(cframe, text='Stop', borderwidth=0, command=costop)
bunpause.grid(row=0, column=4, padx=7, pady=10)

def conext():
    global songflow, paused
    try:
        listsong.selection_clear(0, END)
        listsong.selection_set(songs.index(songflow)+1)
        songflow = songs[listsong.curselection()[0]]
    except:
        pass
bnext = Button(cframe, text='>>', borderwidth=0, command=conext)
bnext.grid(row=0, column=5, padx=7, pady=10)

def coprev():
    global songflow, paused
    try:
        listsong.selection_clear(0, END)
        listsong.selection_set(songs.index(songflow)-1)
        songflow = songs[listsong.curselection()[0]]
        conplay()
    except:
        pass
bprev = Button(cframe, text='<<', borderwidth=0, command=coprev)
bprev.grid(row=0, column=0, padx=7, pady=10)

base.mainloop()