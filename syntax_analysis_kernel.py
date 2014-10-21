#coding:utf-8

import lexical_analysis

GRAMMAR ={}

NONTERMINAL=[]
TERMINAL=[]

FIRST={}
FOLLOW={}
PARSING_TABLE={}

TOKEN_SEQUENCE=[]

STACK_MAX_DEPTH=2000

SYNTAX_RESULT=[]


def grammar_scanner():

	fp = open('grammar.ds','r')
	grammar_lines = fp.readlines()
	fp.close()
	for each_line in grammar_lines:
		tmp=''
		bracket = ''
		last = ''
		terminals=[]
		nonterminals=[]
		sequence=[]
		for i in xrange(0,len(each_line)):
			if bracket=='':
				if last==']' and each_line[i]==']':
					terminals[len(terminals)-1]=terminals[len(terminals)-1]+']'
					sequence[len(sequence)-1]=sequence[len(sequence)-1]+']'
				if each_line[i]=='[':
					bracket=']'
				elif each_line[i]=='<':
					bracket='>'
					
			else:
				if each_line[i]==bracket:
					if each_line[i]==']':
						terminals.append(tmp)
						sequence.append(tmp)
						tmp=''
						bracket=''
					else:
						nonterminals.append(tmp)
						sequence.append(tmp)
						tmp=''
						bracket=''
				else:
					tmp=tmp+each_line[i]
			last = each_line[i]

		if not sequence[0] in GRAMMAR:
			GRAMMAR[sequence[0]]=[]
		GRAMMAR[sequence[0]].append(sequence[1:len(sequence)])

		for each in nonterminals:
			if not each in NONTERMINAL:
				NONTERMINAL.append(each)
		for each in terminals:
			if not each in TERMINAL:
				TERMINAL.append(each)
				
		TERMINAL.append('$')
		

def getFirst():
	global GRAMMAR, NONTERMINAL, TERMINAL, FIRST
	for each in TERMINAL:
		FIRST[each]=[each]

	for each_nonterminal in NONTERMINAL:
		FIRST[each_nonterminal]=[]
		# 如果X->null 是产生式，将null加入X的first集
		for each_sequence in GRAMMAR[each_nonterminal]:
			if each_sequence==['null']:
				FIRST[each_nonterminal]=['null']
	stop = False

	while(not stop):
		stop=True
		for each_nonterminal in NONTERMINAL:
			# 将Y0中新增的first填入并处理连续的有null
			for each_sequence in GRAMMAR.get(each_nonterminal, []):
				counter=0
				for each_mark in each_sequence:
					for each_marks_first in FIRST[each_mark]:
						if ((each_marks_first!='null') and (not each_marks_first in FIRST[each_nonterminal])):
							FIRST[each_nonterminal].append(each_marks_first)
							stop=False
					if not 'null' in FIRST[each_mark]:
						break
					else:
						counter+=1
					
				#所有产生式的first集都有null，将null加入
				if (counter==len(each_sequence) and (not 'null' in FIRST[each_nonterminal])):
					FIRST[each_nonterminal].append('null')
					stop=False
					
def getFollow():
	global GRAMMAR, NONTERMINAL, TERMINAL, FOLLOW

	for each in TERMINAL:
		FOLLOW[each]=[]

	for each_nonterminal in NONTERMINAL:
		FOLLOW[each_nonterminal] = []
	
	FOLLOW['program']=['$']

	# 放入first集,第二步
	for each_nonterminal in NONTERMINAL:
		for each_sequence in GRAMMAR[each_nonterminal]:
			for i in xrange(0,len(each_sequence)-1):
				for each_next_marks_first in FIRST[each_sequence[i+1]]:
					if (not each_next_marks_first in FOLLOW[each_sequence[i]])and (not each_next_marks_first=='null'):
						FOLLOW[each_sequence[i]].append(each_next_marks_first)

	stop = False
	while (not stop):
		stop = True
		# 第三步
		for each_nonterminal in NONTERMINAL:
			for each_sequence in GRAMMAR[each_nonterminal]:
				for i in xrange(len(each_sequence)-1,-1,-1):
					for each_follow in FOLLOW[each_nonterminal]:
						if not each_follow in FOLLOW[each_sequence[i]]:
							FOLLOW[each_sequence[i]].append(each_follow)
							stop = False
					if not 'null' in FIRST[each_sequence[i]]:
						break;

def get_parsing_table():
	# 算法4.4
	global FIRST, FOLLOW, PARSING_TABLE
	# 初始化,将预测分析表中的空白处赋值为-100
	for each_nonterminal in NONTERMINAL:
		PARSING_TABLE[each_nonterminal]={}
		for each_terminal in TERMINAL:
			PARSING_TABLE[each_nonterminal][each_terminal]=-100


	# 构建预测分析表
	for each_nonterminal in NONTERMINAL:
		for i in xrange(0,len(GRAMMAR[each_nonterminal])):
			counter = 0
			for each_mark in GRAMMAR[each_nonterminal][i]:
				for each_marks_first in FIRST[each_mark]:
					if PARSING_TABLE[each_nonterminal][each_marks_first]>0:
						print('语法不是LL1,问题出在:')
						print((each_nonterminal+'->'),GRAMMAR[each_nonterminal][i])
						print('与：')
						print((each_nonterminal+'->'),GRAMMAR[each_nonterminal][PARSING_TABLE[each_nonterminal][each_marks_first]])
						print('each_marks_first:',each_marks_first)
						exit(0)
					else:
						PARSING_TABLE[each_nonterminal][each_marks_first]=i
				if not 'null' in FIRST[each_mark]:
					break
				else:
					counter+=1
			if counter==len(GRAMMAR[each_nonterminal][i]):
				for each_follow in FOLLOW[each_nonterminal]:
					if each_follow in TERMINAL:
						if PARSING_TABLE[each_nonterminal][each_follow]>0:
							print('语法不是LL1,问题出在:')
							print(each_nonterminal,'->',GRAMMAR[each_nonterminal][i])
							print('each follow:',each_follow)
							exit(0)
						else:
							PARSING_TABLE[each_nonterminal][each_follow]=i

		# 加入同步记号，同步记号标记位-1
		for each_nonterminal in NONTERMINAL:
			for each_follow in FOLLOW[each_nonterminal]:
				if PARSING_TABLE[each_nonterminal][each_follow]<0:
					PARSING_TABLE[each_nonterminal][each_follow]=-1
					
def syntax_parse():
	global SYNTAX_RESULT

	SYNTAX_RESULT=[]
	stack=range(2100)
	stack[0]='program'
	stack_top=0
	token_curse=0
	while(stack_top>=0):
		if stack_top>STACK_MAX_DEPTH:
			print('警告:预测分析栈深度超过2000,程序安全退出。如需调整请于开发者联系')
			exit(0)
		if(stack[stack_top] in TERMINAL):
			# 成功匹配终结符，出栈
			if stack[stack_top]==TOKEN_SEQUENCE[token_curse]:
				SYNTAX_RESULT.append('leaf:['+TOKEN_SEQUENCE[token_curse]+']')
				
			else:
				SYNTAX_RESULT.append('error: 不可接受的终结符: ['+TOKEN_SEQUENCE[token_curse]+']')
			stack_top=stack_top-1
			token_curse=token_curse+1
		
		#非终结符
		else:
			if PARSING_TABLE[stack[stack_top]][TOKEN_SEQUENCE[token_curse]]<0:
				if ['Lambda'] in GRAMMAR[stack[stack_top]]:
					tmp_str='success: ['+stack[stack_top]+']\t->\t[Lambda]'
					SYNTAX_RESULT.append(tmp_str)
					stack_top=stack_top-1
				else:
					if PARSING_TABLE[stack[stack_top]][TOKEN_SEQUENCE[token_curse]]==-1:
						# 弹出栈顶元素回复错误
						SYNTAX_RESULT.append('error: ['+TOKEN_SEQUENCE[token_curse]+']不可接受,进入同步恢复状态,栈顶元素为:'+stack[stack_top])
						stack_top=stack_top-1
					else:
						# 忽略该符号，恢复错误
						SYNTAX_RESULT.append('error: ['+TOKEN_SEQUENCE[token_curse]+']不可接受,忽略该符号以恢复错误,栈顶元素为:'+stack[stack_top])
						token_curse=token_curse+1
			else:
				# 状态可接受，替换栈顶元素
				tmp_sequence=GRAMMAR[stack[stack_top]][PARSING_TABLE[stack[stack_top]][TOKEN_SEQUENCE[token_curse]]]
				tmp_str='success: ['+stack[stack_top]+']\t->\t'
				stack_top=stack_top-1
				for x in xrange(0,len(tmp_sequence)):
					tmp_str=tmp_str+'['+tmp_sequence[x]+']'
					stack_top=stack_top+1
					stack[stack_top]=tmp_sequence[len(tmp_sequence)-1-x]
				SYNTAX_RESULT.append(tmp_str)
				
# 	for each in SYNTAX_RESULT:
# 		print(each)

def compiler_init():
	grammar_scanner()
	getFirst()
	getFollow()
	get_parsing_table()

def driver(code):
	global GRAMMAR, NONTERMINAL, TERMINAL,TOKEN_SEQUENCE,SYNTAX_RESULT
	TOKEN_SEQUENCE=lexical_analysis.scanner(code)
	syntax_parse()
	return SYNTAX_RESULT
	
def drive_from_file():
	fp = open('code.c','r')
	input_stream=fp.read()
	fp.close()
	return driver(input_stream)
					
def main():
	compiler_init()
	drive_from_file()
	for each in SYNTAX_RESULT:
		print(each)

if __name__ == '__main__':
	main()
