import tkinter as tk
from build.Debug import sudoku

class SudoduTK():
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("解数独")
        self.window.geometry("600x450")
        self.width=3
        self.height=1
        self.labels=[tk.Label(self.window,width=self.width,height=self.height,bg='yellow') for _ in range(81)]
        self.entrys=[tk.Entry(self.window,width=self.width,justify='center') for _ in range(81)]

        title=tk.Label(self.window,text="输入原始数独")
        title.place(x='100',y='25')
        button=tk.Button(self.window,text="开始求解",command=self.get_entry_input)
        button.place(x='230',y='320')
        clear_button=tk.Button(self.window,text="清空",command=self.clear_input)
        clear_button.place(x='50',y='320')

        for idx in range(81):
            self.entrys[idx].place(x=str(idx%9*28+idx//3%3*6+20),y=str(idx//9*24+idx//27*6+70))

    def get_entry_input(self):
        board=[['.' for p in range(9)] for q in range(9)]
        for i in range(81):
            board[i//9][i%9]=self.entrys[i].get() if self.entrys[i].get() else '.'
        board=sudoku.fill_solution(board)
        for idx in range(81):
            self.labels[idx]['text']=board[idx//9][idx%9]
            self.labels[idx].place(x=str(idx%9*28+idx//3%3*6+300),y=str(idx//9*24+idx//27*6+70)) 
        answer_title=tk.Label(self.window,text="完整数独结果")
        answer_title.place(x='400',y='25')
    
    def clear_input(self):
        for i in range(81):
            self.entrys[i].delete(0,'end')
            self.labels[i].place_forget()

    def tk_show(self):
        self.window.mainloop()


sktk=SudoduTK()
sktk.tk_show()