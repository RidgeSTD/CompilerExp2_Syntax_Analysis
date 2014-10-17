#coding:utf-8

# 测试小数据

GRAMMER ={
'e':[['t','e\'']],
'e\'':[['+','t','e\''],['null']],
't':[['f','t\'']],
't\'':[['*','f','t\''],['null']],
'f':[['(','e',')'],['id']]
}

NONTERMINAL=['e','e\'','t','t\'','f']
TERMINAL=['id','+','*','(',')','$','null']

FIRST={}
FOLLOW={}
PARSING_TABLE={}


def getFirst():
	global GRAMMER, NONTERMINAL, TERMINAL, FIRST
	print("__ingetFirst__")
	for each in TERMINAL:
		FIRST[each]=[each]

	for each_nonterminal in NONTERMINAL:
		FIRST[each_nonterminal]=[]
		# 如果X->null 是产生式，将null加入X的first集
		for each_sequence in GRAMMER[each_nonterminal]:
			if each_sequence==['null']:
				FIRST[each_nonterminal]=['null']
	stop = False

	while(not stop):
		stop=True
		for each_nonterminal in NONTERMINAL:
			# 将Y0中新增的first填入并处理连续的有null
			for each_sequence in GRAMMER.get(each_nonterminal, []):
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
	global GRAMMER, NONTERMINAL, TERMINAL, FOLLOW

	for each in TERMINAL:
		FOLLOW[each]=[]

	for each_nonterminal in NONTERMINAL:
		FOLLOW[each_nonterminal] = []
	
	FOLLOW['e']=['$']

	# 放入first集,第二步
	for each_nonterminal in NONTERMINAL:
		for each_sequence in GRAMMER[each_nonterminal]:
			for i in xrange(0,len(each_sequence)-1):
				for each_next_marks_first in FIRST[each_sequence[i+1]]:
					if (not each_next_marks_first in FOLLOW[each_sequence[i]])and (not each_next_marks_first=='null'):
						FOLLOW[each_sequence[i]].append(each_next_marks_first)

	stop = False
	while (not stop):
		stop = True
		# 第三步
		for each_nonterminal in NONTERMINAL:
			for each_sequence in GRAMMER[each_nonterminal]:
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
		for i in xrange(0,len(GRAMMER[each_nonterminal])):
			counter = 0
			for each_mark in GRAMMER[each_nonterminal][i]:
				for each_marks_first in FIRST[each_mark]:
					if PARSING_TABLE[each_nonterminal][each_marks_first]>0:
						print('语法不是LL1')
					else:
						PARSING_TABLE[each_nonterminal][each_marks_first]=i
				if not 'null' in FIRST[each_mark]:
					break
				else:
					counter+=1
			if counter==len(GRAMMER[each_nonterminal][i]):
				for each_follow in FOLLOW[each_nonterminal]:
					if each_follow in TERMINAL:
						if PARSING_TABLE[each_nonterminal][each_follow]>0:
							print('语法不是LL1')
						else:
							PARSING_TABLE[each_nonterminal][each_follow]=i


def main():
	print('__in main__')
	getFirst()
	getFollow()
	get_parsing_table()

	for each_nonterminal in NONTERMINAL:
		print(each_nonterminal,FOLLOW[each_nonterminal])

	s="   "
	for each_terminal in TERMINAL:
		s = s+each_terminal+"  "
	print(s)
	print('')
	for each_nonterminal in NONTERMINAL:
		s = each_nonterminal+"\t  "
		for each_terminal in TERMINAL:
			s = s+"\t\t"+str(PARSING_TABLE[each_nonterminal][each_terminal])
		print(s)

if __name__ == '__main__':
	main()
