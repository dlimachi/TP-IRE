import pygame
import os
from tkinter import *
from tkinter import filedialog

pygame.init()

root = Tk()
root.title("Reproductor de Música")
root.geometry("400x400")

canciones = [
    "As long as you love me.mp3",
    "Everybody.mp3",
    "I Want It That Way.mp3",
]

current_song_index = 0
musica_pausada = False

def agregar_cancion():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos MP3", "*.mp3")])
    if file_path:
        canciones.append(file_path)
        actualizar_lista_canciones()

def eliminar_cancion():
    global canciones, current_song_index
    if len(canciones) > 0:
        del canciones[current_song_index]
        current_song_index = 0 
        actualizar_lista_canciones()
        reproducir_cancion()

def actualizar_lista_canciones():
    lista_canciones.delete(0, END) 
    for cancion in canciones:
        lista_canciones.insert(END, os.path.basename(cancion)) 

def reproducir_cancion():
    global current_song_index
    if len(canciones) > 0:
        pygame.mixer.music.load(canciones[current_song_index])
        pygame.mixer.music.play()
        actualizar_titulo()

def pausar_cancion():
    global musica_pausada
    if pygame.mixer.music.get_busy():
        if musica_pausada:
            pygame.mixer.music.unpause()
            musica_pausada = False
        else:
            pygame.mixer.music.pause()
            musica_pausada = True

def reproducir_cancion_seleccionada(event):
    global current_song_index
    selected_song_index = lista_canciones.curselection()[0]
    current_song_index = selected_song_index
    reproducir_cancion()

def siguiente_cancion():
    global current_song_index
    if len(canciones) > 0:
        current_song_index = (current_song_index + 1) % len(canciones)
        reproducir_cancion()

def anterior_cancion():
    global current_song_index
    if len(canciones) > 0:
        current_song_index = (current_song_index - 1) % len(canciones)
        reproducir_cancion()

def actualizar_titulo():
    titulo_var.set(os.path.basename(canciones[current_song_index]))

botones_marco1 = Frame(root)
botones_marco1.pack(pady=10)
botones_marco2 = Frame(root)
botones_marco2.pack(pady=10)

# Botones 
btn_agregar = Button(botones_marco1, text="Agregar Canción", command=agregar_cancion)
btn_eliminar = Button(botones_marco1, text="Eliminar Canción", command=eliminar_cancion)
btn_agregar.pack(side=LEFT, padx=10)
btn_eliminar.pack(side=LEFT, padx=10)
btn_anterior = Button(botones_marco2, text="Anterior", command=anterior_cancion)
btn_pausar_reproducir = Button(botones_marco2, text="Pausar", command=pausar_cancion)
btn_reproducir = Button(botones_marco2, text="Reproducir", command=reproducir_cancion)
btn_siguiente = Button(botones_marco2, text="Siguiente", command=siguiente_cancion)
btn_anterior.pack(side=LEFT)
btn_pausar_reproducir.pack(side=LEFT)
btn_reproducir.pack(side=LEFT)
btn_siguiente.pack(side=LEFT)

# Lista de canciones
lista_canciones = Listbox(root)
lista_canciones.pack()
actualizar_lista_canciones()
lista_canciones.bind("<Double-Button-1>", reproducir_cancion_seleccionada)
titulo_var = StringVar()
mostrar_titulo = Label(root, textvariable=titulo_var)
mostrar_titulo.pack()

root.mainloop()
