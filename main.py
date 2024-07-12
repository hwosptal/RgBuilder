from tkinter import *
from tkinter.ttk import Combobox 
from tkinter import filedialog
import random
from PIL import Image, ImageDraw, ImageFont, ImageTk 

imagem = Image.open("E:/programacao/Python/projetos/RgBuilder/rg.png") 
caminho_img = None
img_3x4 = None 
assinatura = None
digital = None

def carregar():
    global img_3x4
    img_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if img_path:
        img_3x4 = Image.open(img_path).convert("RGBA")
        e_info.config(text="Status: 3X4 Carregada!")

def carregar_assinatura():
    global assinatura
    img_assinatura_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if img_assinatura_path:
        assinatura = Image.open(img_assinatura_path).convert("RGBA")  
        e_info.config(text="Status: Assinatura Carregada!")

def carregar_digital():
    global digital
    digital_path = filedialog.askopenfilename(filetypes=[("Imagens","*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if digital_path:
        digital = Image.open(digital_path).convert("RGBA")
        e_info.config(text="Status: Digital Carregada!")

def gerar(): 
    global imagem
    imagem = Image.open("E:/programacao/Python/projetos/RgBuilder/rg.png") #faz uma copia da imagem original

    nome = e_nome.get()
    rg = e_rg.get()
    nomePai = e_nomeDoPai.get()
    nomeMae = e_nomeDaMae.get()
    naturalidade = e_naturalidade.get()
    estado = e_estado.get()
    docOrigem = e_docOrigem.get()
    cpf = e_cpf.get()
    data_expedicao = e_dataEx.get() 
    nascimento = e_dataNascimento.get()
  
    desenho = ImageDraw.Draw(imagem) #para adicionar os textos
    fonte = ImageFont.truetype("E:/programacao/Python/projetos/RgBuilder/consolas.ttf",20) #fonte


    #coordenadas onde vai ficar o texto
    rgCoordenadas = (787, 50)
    nomeCoordenadas = (782,80)
    nomePaiCoordenadas = (782,140)
    nomeMaeCoordenadas = (782,180)
    naturalidadeCoordenadas = (795,225) 
    docOrigemCoordenadas = (800,285)
    cpfCoordenadas = (761,327)
    expedicaoCoordenadas = (1140,38)
    nascimentoCoordenadas = (1170,225)
    
    cor = (0,0,0) 

    cidade_estado = f"{naturalidade} - {estado}" #para imprimir naturalidade - estado
    desenho.text(nomeCoordenadas,           nome,                  font=fonte, fill=cor)
    desenho.text(rgCoordenadas,             rg,                    font=fonte, fill=cor)
    desenho.text(nomePaiCoordenadas,        nomePai,               font=fonte, fill=cor)
    desenho.text(nomeMaeCoordenadas,        nomeMae,               font=fonte, fill=cor)
    desenho.text(naturalidadeCoordenadas,   cidade_estado,         font=fonte, fill=cor) 
    desenho.text(docOrigemCoordenadas,      docOrigem,             font=fonte, fill=cor)
    desenho.text(cpfCoordenadas,            cpf,                   font=fonte, fill=cor)
    desenho.text(expedicaoCoordenadas,      data_expedicao,        font=fonte, fill=cor)
    desenho.text(nascimentoCoordenadas,     nascimento,            font=fonte, fill=cor)

    #foto 3x4
    #verifica se a foto foi carregada antes de sobrepor
    if img_3x4: 
        tam_img = (185,267)
        tam_img_3x4 = img_3x4.resize(tam_img, resample=Image.BICUBIC)
        tam_img_3x4 = tam_img_3x4.rotate(angle=270, expand=True)
        tam_img_3x4 = tam_img_3x4.convert("RGBA")  
        x_pos = 326
        y_pos = 113
        imagem.paste(tam_img_3x4, (x_pos, y_pos), tam_img_3x4)

    #assinatura
    if assinatura:
        tam_img_a = (100, 100)
        tam_img_assinatura = assinatura.resize(tam_img_a, resample=Image.BICUBIC)
        tam_img_assinatura = tam_img_assinatura.convert("RGBA")   
        x_pos = 275
        y_pos = 290
        imagem.paste(tam_img_assinatura, (x_pos, y_pos), tam_img_assinatura)

    #digital
    if digital:
        tam_digital = (170,250)
        tam_img_digital = digital.resize(tam_digital, resample=Image.BICUBIC)
        tam_img_digital = tam_img_digital.rotate(angle=271, expand=True)
        tam_img_digital = tam_img_digital.convert("RGBA")
        x_pos = 27
        y_pos = 114
        imagem.paste(tam_img_digital, (x_pos, y_pos), tam_img_digital)

    e_info.config(text="Status: RG GERADO!")
    Btnsalvar = Button(frameMeio, text="Salvar", width=23, bd=5, relief=RAISED, borderwidth=1, font=("Roboto 10"), command=salvar)
    Btnsalvar.place(x=218, y=370) 

def salvar():
    n = random.randint(1,100)

    global caminho_img
    diretorio = filedialog.askdirectory()
    if diretorio: 
        caminho_img = f"{diretorio}/RgGerado{n}.png"
        imagem.save(caminho_img, format="PNG")

    abrir = Button(frameMeio, text="Visualizar", width=23, bd=5, relief=RAISED, borderwidth=1, font=("Roboto 10"), command=abrirImg)
    abrir.place(x=401, y=370)

def abrirImg():
    global caminho_img, img_tk, l_img

    if caminho_img:
        imgC = Image.open(caminho_img)
        imgC.thumbnail((900, 900))
        img_tk = ImageTk.PhotoImage(imgC)

        janelaImg = Toplevel() 
        l_img = Label(janelaImg, image=img_tk, width=900, height=900)
        l_img.pack()

        janelaImg.resizable(width=FALSE, height=FALSE)
        janelaImg.geometry("890x300")
        janelaImg.mainloop()

janela = Tk() 
frameTitulo = Frame(janela, width=1200, height=58)
frameTitulo.grid(row=0, column=0)

frameMeio = Frame(janela, width=1200, height=500, relief=FLAT)
frameMeio.grid(row=1, column=0)

#titulo
Titulo = Label(frameTitulo, text="RG BUILDER v2.0.0", width=500, fg="black", compound=CENTER, anchor=NW, font=("Roboto", 20, "bold"))
Titulo.place(x=200, y=20)

#formulario 

#Topo
l_rg = Label(frameMeio, text="Numero do RG: ", font=("Roboto",10,"bold"), height=1, fg="Black")
l_rg.place(x=15, y=20)
e_rg = Entry(frameMeio, justify="left", relief=SOLID, width=15)
e_rg.place(x=128, y=23)

l_cpf = Label(frameMeio, text="Numero do CPF: ", font=("Roboto",10,"bold"), height=1, fg="Black")
l_cpf.place(x=300, y=21)
e_cpf = Entry(frameMeio, justify="left", relief=SOLID, width=25)
e_cpf.place(x=445, y=24)


#parte esquerda
l_nome = Label(frameMeio, text="Seu Nome: ", font=("Roboto",10,"bold"), height=1, fg="Black")
l_nome.place(x=15, y=70)
e_nome = Entry(frameMeio, justify="left", relief=SOLID, width=25)
e_nome.place(x=110, y=74)

l_nomeDoPai = Label(frameMeio, text="Nome do Pai: ", font=("Roboto",10,"bold"), height=1, fg="Black")
l_nomeDoPai.place(x=15, y=110)
e_nomeDoPai = Entry(frameMeio, justify="left", relief=SOLID, width=25)
e_nomeDoPai.place(x=110, y=110) 

l_Naturalidade = Label(frameMeio, text="Naturalidade: ", font=("Roboto",10,"bold"), height=1, fg="Black")
l_Naturalidade.place(x=15, y=149)
e_naturalidade = Entry(frameMeio, justify="left", relief=SOLID, width=25)
e_naturalidade.place(x=110, y=149)

l_docOrigem = Label(frameMeio, text="DOC. Origem: ", font=("Roboto",10,"bold"), height=1, fg="Black")
l_docOrigem.place(x=15, y=190)
e_docOrigem = Entry(frameMeio, justify="left", relief=SOLID, width=25)
e_docOrigem.place(x=110, y=190)

#parte direita
l_dataEx = Label(frameMeio, text="Data de Expedição: ", font=("Roboto",10,"bold"), height=1, fg="Black")
l_dataEx.place(x=300, y=60)
e_dataEx = Entry(frameMeio, justify="left", relief=SOLID, width=25)
e_dataEx.place(x=445, y=60)

l_dataNascimento = Label(frameMeio, text="Data de Nascimento: ", font=("Roboto",10,"bold"), height=1, fg="Black")
l_dataNascimento.place(x=300, y=100)
e_dataNascimento = Entry(frameMeio, justify="left", relief=SOLID, width=25)
e_dataNascimento.place(x=445, y=100) 

l_nomeDaMae = Label(frameMeio, text="Nome da Mãe: ", font=("Roboto",10,"bold"), height=1, fg="Black")
l_nomeDaMae.place(x=300, y=138)
e_nomeDaMae = Entry(frameMeio, justify="left", relief=SOLID, width=31)
e_nomeDaMae.place(x=400, y=138)

l_estado = Label(frameMeio, text="Estado:", font=("Roboto",10,"bold"))
l_estado.place(x=300, y=180) 
e_estado = Combobox(frameMeio, width=6, font=("Roboto 10"), values=["AC","AL","AP","AM","BA","CE","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO","DF"]) 
e_estado.set("")
e_estado.place(x=400, y=180) 

btn = Button(frameMeio, text="Foto", width=13, bd=5, borderwidth=1, relief=RAISED, font=("Roboto 10"), command=carregar)
btn.place(x=300, y=210)   
btnDigital = Button(frameMeio, text="Digital", width=13, bd=5, borderwidth=1, relief=RAISED, font=("Roboto 10"), command=carregar_digital)
btnDigital.place(x=410, y=210)
btnAssinatura = Button(frameMeio, text="Assinatura", width=13, bd=5, borderwidth=1, relief=RAISED, font=("Roboto 10"), command=carregar_assinatura)
btnAssinatura.place(x=518, y=210)

e_info = Label(frameMeio, text="Status: RG NÃO GERADO!", font=("Roboto 10")) 
e_info.place(x=32,y=260)
e_aviso = Label(frameMeio,  text="*Usar sempre imagem png e a assinatura e digital serem", font=("Roboto 9")) 
e_aviso2 = Label(frameMeio, text="com fundo transparente para melhor ajuste", font=("Roboto 9")) 
e_aviso.place(x=32,y=290)
e_aviso2.place(x=32,y=310)

corBtns = '#c2c1be' 

gerar = Button(frameMeio, text="Gerar",      width=23, bd=5, relief=RAISED, borderwidth=1, font=("Roboto 10"), command=gerar)
gerar.place(x=32, y=370)
Btnsalvar = Button(frameMeio, text="Salvar", width=23, bd=5, bg=corBtns, relief=RAISED, borderwidth=1, font=("Roboto 10"))
Btnsalvar.place(x=218, y=370)   
abrir = Button(frameMeio, text="Visualizar", width=23, bd=5, bg=corBtns, relief=RAISED, borderwidth=1, font=("Roboto 10"))
abrir.place(x=401, y=370) 

janela.resizable(width=FALSE, height=FALSE)
janela.geometry("620x480")
janela.mainloop() 