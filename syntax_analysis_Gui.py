#coding:utf-8

from Tkinter import *
import syntax_analysis_kernel
import Tkinter

code_entry=None
result_listBox=None
root=None
frame=None
frame2=None
compile_from_file_btn =None
var=None

def on_click():
	global code_entry,result_message
	result_message.delete(0, END)
	tmp_str = code_entry.get()
	result_message.insert(0, tmp_str)
	
def onclick_file():
	global result_listBox
	result_listBox.delete(0, result_listBox.size())
	result_from_file = syntax_analysis_kernel.drive_from_file()
	for each in result_from_file:
		result_listBox.insert(END,each)
		
	

def main():
	global code_entry,result_listBox,frame,frame2,compile_from_file_btn,var
	root = Tk()
	root.title('DaggerStudio LL1 Compiler')

	frame=Frame(root,width=600,height=400)
	frame.pack(side=TOP)
	
	frame2=Frame(root,width=600,height=100)
	frame2.pack(side=BOTTOM)

	code_entry = Entry(frame)
	code_entry.pack(side=LEFT,ipadx=190,ipady=300,anchor='nw')
	
# 	设置右侧的结果界面
	scrollbar = Scrollbar(frame2)
	scrollbar.pack(side=RIGHT, fill=Y)
	
	result_listBox = Tkinter.Listbox(frame2, yscrollcommand=scrollbar.set)
	result_listBox.pack(side=RIGHT,ipadx=300,ipady=300)
	result_listBox.see(10)
	for x in xrange (1,15):
		result_listBox.insert(END,'index')
	scrollbar.config(command=result_listBox.yview)
	

# 	设置下面的按钮
	compile_btn = Button(frame2,text='COMPILE',command=on_click)
	compile_btn.pack(side='left')
	
	compile_from_file_btn = Button(frame2,text='COMPILE FROM FILE',command=onclick_file)
	compile_from_file_btn.pack(side='right')
	
	syntax_analysis_kernel.compiler_init()

	mainloop()

if __name__ == '__main__':
	main()
