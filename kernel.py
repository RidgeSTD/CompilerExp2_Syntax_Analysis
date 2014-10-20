#coding:utf-8

import re

GRAMMAR ={}

NONTERMINAL=[]
TERMINAL=[]

FIRST={}
FOLLOW={}
PARSING_TABLE={}


def grammar_scanner():

	fp = open('grammar.ds','r')
	grammar_lines = fp.readlines()
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
		

def getFirst():
	global GRAMMAR, NONTERMINAL, TERMINAL, FIRST
	print("__ingetFirst__")
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
				if(each_sequence==[]):
					print('Wrong! in Kernel(#1)')
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
	# 初始化
	for each_nonterminal in NONTERMINAL:
		PARSING_TABLE[each_nonterminal]={}
		for each_terminal in TERMINAL:
			PARSING_TABLE[each_nonterminal][each_terminal]=-1


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


def main():
	global GRAMMAR, NONTERMINAL, TERMINAL
	grammar_scanner()
	getFirst()
	getFollow()
	get_parsing_table()

	# print('语法:')
	# for each in NONTERMINAL:
	# 	for each_sequence in GRAMMAR[each]:
	# 		print(each,'->',each_sequence)


	# for each_nonterminal in NONTERMINAL:
	# 	print(each_nonterminal,FOLLOW[each_nonterminal])

	# s="   "
	# for each_terminal in TERMINAL:
	# 	s = s+each_terminal+"  "
	# print(s)
	# print('')
	# for each_nonterminal in NONTERMINAL:
	# 	s = each_nonterminal+"\t  "
	# 	for each_terminal in TERMINAL:
	# 		s = s+"\t\t"+str(PARSING_TABLE[each_nonterminal][each_terminal])
	# 	print(s)

if __name__ == '__main__':
	main()
