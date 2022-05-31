from tkinter import *

def soma():
     if entrada1.get().isnumeric() and entrada2.get().isnumeric():
        result['text'] = float(entrada1.get()) + float(entrada2.get())
     else:
         result['text'] = 'Valor Inválido!'


def sub():
    if entrada1.get().isnumeric() and entrada2.get().isnumeric():
        result['text'] = float(entrada1.get()) - float(entrada2.get())
    else:
        result['text'] = 'Valor Inválido!'


def mult():
    if entrada1.get().isnumeric() and entrada2.get().isnumeric():
        result['text'] = float(entrada1.get()) * float(entrada2.get())
    else:
        result['text'] = 'Valor Inválido!'


def div():
    if entrada1.get().isnumeric() and entrada2.get().isnumeric():
        result['text'] = float(entrada1.get()) / float(entrada2.get())
    else:
        result['text'] = 'Valor Inválido!'


janela = Tk()
janela.geometry('400x230+750+300')
janela.maxsize(width=400, height=230)
janela.minsize(width=400, height=230)
janela.config(background='#2F4F4F')

result = Label(janela, text='RESULTADO', foreground='white', bg='#2F4F4F', font='Consolas 27')
entrada1 = Entry(janela, font='Consolas 18')
entrada2 = Entry(janela, font='Consolas 18')

botao = Button(janela, text=' + ', font='Consolas 15', command=soma)
botao1 = Button(janela, text=' - ', font='Consolas 15', command=sub)
botao2 = Button(janela, text=' * ', font='Consolas 15', command=mult)
botao3 = Button(janela, text=' / ', font='Consolas 15', command=div)

espacinho = Label(janela, text=' ', background='#2F4F4F')
espacinho1 = Label(janela, text=' ', background='#2F4F4F')
espacinho2 = Label(janela, text=' ', background='#2F4F4F')

result.pack()
espacinho.pack()
entrada1.pack()
espacinho1.pack()
entrada2.pack()
espacinho1.pack()
botao.pack(side=LEFT)
botao1.pack(side=LEFT)
botao2.pack(side=LEFT)
botao3.pack(side=LEFT)

janela.mainloop()