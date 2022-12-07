import tkinter as tk
from tkinter import messagebox

def cadastrar_funcionario():
    messagebox.showinfo(title='Sucesso', message=' Funcionário cadastrado com suceso')

janela =  tk.Tk()
janela.title('Tela cadastro funcionários')
frame = tk.Frame(master=janela, width=300, height=200, background='blue')
frame.pack()
# criação do Label Nome e Entry para o nome
label_nome = tk.Label(master=frame, text='Nome: ', width=10)
entry_nome = tk.Entry(master=frame, width=50)
label_nome.grid(row=0,column=0)
entry_nome.grid(row=0,column=1)

label_CPF = tk.Label(master=frame, text = 'CPF: ', width=10)
entry_CPF = tk.Entry(master=frame, width=50)
label_CPF.grid(row=1, column=0)
entry_CPF.grid(row=1, column=1)

label_salario = tk.Label(master=frame, text='Salário', width=10)
entry_salario = tk.Entry(master=frame, width=25)
label_salario.grid(row=2,column=0)
entry_salario.grid(row=2, column=1)

botao_cadastrar = tk.Button(master=frame, text='CADASTRAR', command=cadastrar_funcionario)
botao_cadastrar.grid(row=3, column=1)
janela.mainloop()