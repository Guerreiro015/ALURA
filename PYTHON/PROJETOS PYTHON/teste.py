import os
os.system('cls')
import tkinter
from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter.commondialog import Dialog
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
from datetime import timedelta
from datetime import *
from datetime import datetime
from dateutil import relativedelta


import tkinter as t

class JanelaRolavel(t.Frame):
    def __init__(self, parent, *args, **kw):
        t.Frame.__init__(self, parent, *args, **kw)            

        # cria um canvas e uma barra de rolagem para rolá-lo:
        rolagem = t.Scrollbar(self, orient=t.VERTICAL)
        rolagem.pack(fill=t.Y, side=t.RIGHT, expand=t.FALSE)
        self.canvas = t.Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=rolagem.set)
        self.canvas.pack(side=t.LEFT, fill=t.BOTH, expand=t.TRUE)
        rolagem.config(command=self.canvas.yview)

        # reseta a visão:
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # cria um frame dentro do canvas
        # para que seja rolado junto com ele:
        self.conteudo =  t.Frame(self.canvas)
        self.id_conteudo = self.canvas.create_window(
            0, 0, window=self.conteudo, anchor=t.NW)

        # cria eventos para detectar mudanças no canvas
        # e sincronizar com a barra de rolagem:
        self.conteudo.bind('<Configure>', self._configurar_conteudo)
        self.canvas.bind('<Configure>', self._configurar_canvas)

    def _configurar_conteudo(self, evento):
            # atualiza a barra de rolagem para o tamanho do frame de conteudo:
            tamanho = (
                self.conteudo.winfo_reqwidth(),
                self.conteudo.winfo_reqheight()
            )
            self.canvas.config(scrollregion="0 0 %s %s" % tamanho)
            if self.conteudo.winfo_reqwidth() != self.canvas.winfo_width():
                # atualizar tambem a largura do canvas para caber o conteudo:
                self.canvas.config(width=self.conteudo.winfo_reqwidth())

    def _configurar_canvas(self, evento):
        if self.conteudo.winfo_reqwidth() != self.canvas.winfo_width():
            # atualizar tambem a largura do conteudo para preencher o canvas:
            self.canvas.itemconfigure(
                self.id_conteudo, width=self.canvas.winfo_width())
if __name__ == "__main__":
    class Exemplo(t.Tk):
        def __init__(self, *args, **kwargs):
            t.Tk.__init__(self, *args, **kwargs)

            self.frame = JanelaRolavel(self)
            self.frame.pack(fill=t.BOTH)
            for i in range(10): # cria botoes no frame interno
                t.Button(self.frame.conteudo, 
                    text="Botão {}".format(i)).pack(fill=t.BOTH)

    app = Exemplo()
    app.mainloop()            