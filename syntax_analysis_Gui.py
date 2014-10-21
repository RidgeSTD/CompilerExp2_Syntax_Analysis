#coding:utf-8

from Tkinter import *
import syntax_analysis_kernel
import Tkinter

code_text=None
result_listBox=None
root=None
frame=None
frame2=None
compile_from_file_btn =None
var=None

def on_click():
	global code_text,result_listBox
# 	print('hahaha')
# 	print(result_listBox.size())
	tmp_str = code_text.get('0.0', END)
	print(tmp_str)
	result_listBox.delete(0, result_listBox.size())
	result = syntax_analysis_kernel.driver(tmp_str)
	for each in result:
		result_listBox.insert(END,each)
	
	
	
def onclick_file():
	global result_listBox
	result_listBox.delete(0, result_listBox.size())
	result_from_file = syntax_analysis_kernel.drive_from_file()
	for each in result_from_file:
		result_listBox.insert(END,each)
		
	

def main():
	global code_text,result_listBox,frame,frame2,compile_from_file_btn
	root = Tk()
	root.geometry('800x600')
	root.title('DaggerStudio LL1 Compiler')

	frame=Frame(root)
	frame.pack(side=TOP)
	
	frameleftup=Frame(frame)
	frameleftup.pack(side=LEFT,fill=BOTH)
	
	framerightup=Frame(frame)
	framerightup.pack(side=LEFT)
	
	frame2=Frame(root)
	frame2.pack(side=BOTTOM)

	scrollbary_text = Scrollbar(frameleftup)
	scrollbary_text.pack(side=RIGHT,fill=Y)
	
	scrollbarx_text = Scrollbar(frameleftup,orient = HORIZONTAL)
	scrollbarx_text.pack(side=BOTTOM,fill=X)
	code_text = Text(frameleftup,yscrollcommand=scrollbary_text.set,xscrollcommand=scrollbarx_text.set)
	code_text.pack(side=LEFT,fill=BOTH)
	scrollbary_text.config(command=code_text.yview)
	scrollbarx_text.config(command=code_text.xview)
	
# 	设置右侧的结果界面
	scrollbary = Scrollbar(framerightup)
	scrollbary.pack(side=RIGHT,fill=Y)
	
	scrollbarx = Scrollbar(framerightup,orient = HORIZONTAL)
	scrollbarx.pack(side=BOTTOM,fill=X)
	
	result_listBox = Tkinter.Listbox(framerightup, yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
	result_listBox.pack(side=RIGHT,ipadx=400,ipady=180)
	result_listBox.see(20)
	scrollbary.config(command=result_listBox.yview)
	scrollbarx.config(command=result_listBox.xview)
	

# 	设置下面的按钮
	compile_btn = Button(frame2,text='COMPILE',command=on_click)
	compile_btn.pack(side='left')
	
	compile_from_file_btn = Button(frame2,text='COMPILE FROM FILE',command=onclick_file)
	compile_from_file_btn.pack(side='right')
	
	syntax_analysis_kernel.compiler_init()

	mainloop()

if __name__ == '__main__':
	main()
