import tkinter as tk
from build.Debug import sudoku

window=tk.Tk()
window.title("解数独")

window.geometry("600x450")

width=3
height=1
labels=[]
entrys=[]

for _ in range(81):
    labels.append(tk.Label(window,width=width,height=height,bg='yellow'))
    entrys.append(tk.Entry(window,width=width,justify='center'))

def get_entry_input():
    board=[['.' for p in range(9)] for q in range(9)]
    for i in range(81):
        board[i//9][i%9]=entrys[i].get() if entrys[i].get() else '.'
    board=sudoku.fill_solution(board)
    for idx in range(81):
        labels[idx]['text']=board[idx//9][idx%9]
        labels[idx].place(x=str(idx%9*28+idx//3%3*6+300),y=str(idx//9*24+idx//27*6+70)) 
    answer_title=tk.Label(window,text="完整数独结果")
    answer_title.place(x='400',y='25')

def clear_input():
    for i in range(81):
        entrys[i].delete(0,'end')
        labels[i].place_forget()


title=tk.Label(window,text="输入原始数独")
title.place(x='100',y='25')
button=tk.Button(window,text="开始求解",command=get_entry_input)
button.place(x='230',y='320')
clear_button=tk.Button(window,text="清空",command=clear_input)
clear_button.place(x='50',y='320')

for idx in range(81):
    entrys[idx].place(x=str(idx%9*28+idx//3%3*6+20),y=str(idx//9*24+idx//27*6+70))

window.mainloop()