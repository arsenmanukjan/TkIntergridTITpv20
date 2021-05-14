from tkinter import *
list_ = ["HARJUMAA","VILJANDI","VALGAMAA","SAAREMAA","ROBOT-ANDROID"]
foto_list=["HarjumaaKaadrioruMuuseum.png","ViljanduMost.png","PühajarvValga.png","EpiskopZamokSaaremaa.png"]
global can, pc
def list_to_txt(event):
    global can, pc
    txt.delete(0.0,END)
    valik=lbox.curselection()
    txt.insert(END,lbox.get(valik[0]))
    print(lbox.get(valik[0]))
    can.delete(ALL)
    pc = PhotoImage(file=foto_list[valik[0]])
    print(foto_list[valik[0]])
    can.create_image(0,0,image=pc,anchor=NW)
    

def txt_to_list(event):
    text=text.get(0.0,END)
    text=text[-2:-1]
    if text--"/n":
        pass
    else:
        foto_list.append(text)
        lbox.config(height=len(foto_list))
        lbox.insert(END,text)
        txt.delete(0.0,END)
        text-""

def opisanie():
    text = txt.get(0.0, END)
    print(list(text))
    if text=="HarjumaaKaadrioruMuuseum.png\n":
        ttt="(1700–1721) Петр I, уверенный в своих позициях на завоеванных территориях в регионе Бм, начал создавать в окрестностях (Таллинна) новый летний дворец."
    elif text=="PühajarvValga.png\n":
        ttt="Озеро Пюхаярв со своей извилистой береговой линией и пятью островами является крупнейшим и живописнейшим озером в регионе."
    elif text=="ViljanduMost.png\n":
        ttt="Созданный в Риге в 1879-м году фирмой (Felser & Co) мост был установлен на крепостном холме города Вильянди в 1931 г. Мост подарил городу помещик Тарвасту Карл фон Мензенкампф."
    elif text=="EpiskopZamokSaaremaa.png\n":
        ttt="Точная дата начала строительства замка Курессааре(Сааремаа) не установлена. Предполагается, что закладка крепости произошла в 1322-38 годах, во время правления епископа Якоба."
    opis.config(text=ttt)



win=Tk()
lbox=Listbox(win,width=20,height=len(foto_list),selectmode=SINGLE)
for element in foto_list:
    lbox.insert(END,element)

lbox.pack()
lbox.bind("<<ListboxSelect>>",list_to_txt)
txt=Text(win,height=5,width=20,wrap=WORD)
txt.pack()
txt.bind("<Return>",txt_to_list)
can=Canvas(win,width=130,height=130,bg="gold")
pc = PhotoImage(file="")#220px-PelobatesFuscus.png
panel = Label(win, image = pc)
panel.pack(side = "bottom", fill = "both", expand = "yes")
foto=PhotoImage(file="ViljanduMost.png")
bt=Button(text='Info', command=opisanie).pack()#, command=op
opis=Label(win, text="DESCRIPTION", width=150, height=40)
opis.pack()
can.pack()
win.mainloop()
