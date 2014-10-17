#coding:utf-8

GRAMMER ={
'program':[['function_statement','declare','function_defination']],
'function_statement':[['null'],['type','id','params',';']],
'function_defination':[['null'], ['type','id','params','funcbody']],
'type':[['void','char','byte','int','long','float','double']],
'params':[['param','paramn'],['null']],
'paramn':[['null'],[',','param','paramn']],
'param':[['type','id']],
'function_body':[['{','function_internal','}']],
'function_internal':[['assign','function_internal'],
					['expression','function_internal'],
					['loop_expression','function_internal'],
					['declare','function_internal'],
					['function_statement','function_internal'],
					['jump_signal','function_internal']],
'declare':[['null'],['type','ids',';']],
'ids':[['id','idN'],['id','=','constant','idN']],
'idN':[[',','id','idN'],['null'],[',','id','constant','idN']],
'assign':[['null'],['id','assign_idN','=','expression',';']],
'assign_idN':[['null'],['=','id','assign_idN']],
'function':[['id','(','params',')']],
'constant':[['integer'],['decimal'],['char'],['string']],
'expression':[['constant'],['function'],['id'],['single_expression'],['double_expression']],
'single_expression':[['single_operator','expression'],['expression','single_operator']],
'single_operator':[['!'],['^'],['&'],['++'],['--']],
'double_expression':[['expression','double_operator','expression']],
'double_operator':[['+'],['-'],['*'],['/'],['&&'],['||']],
'loop_expression':[['for_expression'],['while_expression'],['do_expression']],
'jump_signal':[['break',';'],['continue',';'],['goto','id',';'],['return',';'],['return','expression',';']],
'for_expression':[['for','for_internal_expression',',','for_internal_expression',',','for_internal_expression',')','loop_body']],
'for_internal_expression':[['null'],['expression']],
'loop_body':[['{','loop_internal','}']],
'loop_internal':[['assign','loop_internal'],
				['expression','loop_internal'],
				['loop_expression','loop_internal'],
				['declare','loop_internal'],
				['function_statement','loop_internal'],
				['jump_signal','loop_internal']],
'while_expression':[['while','(','expression',')','loop_body']],
'do_expression':[['do','loop_expression','while','(','expression',')',';']],
'if_expression':[['if','(','expression',')','if_internal','if_remain']],
'if_remain':[['null'],['else','if_internal'],['else','if_expression']],
'if_internal':[['assign','if_internal'],
				['expression','if_internal'],
				['loop_expression','if_internal'],
				['declare','if_internal'],
				['function_statement','if_internal'],
				['jump_signal','if_internal']]
}

NONTERMINAL=['program','function_statement','function_defination','type',
			'params','param','function_body','function_internal','declare',
			'ids','idN','assign','assign_idN','function','constant','expression',
			'single_expression','single_operator','double_expression','double_operator',
			'loop_expression','jump_signal','for_expression','for_internal_expression',
			'loop_body','loop_internal','while_expression','do_expression','if_expression',
			'if_remain','if_internal'
			]
TERMINAL=['null','id',';','void','char','byte','shot','int','long','float','double',
		',','=','integer','decimal','character','string','!','^','&','++','--','+','-','*','/',
		'&&','||','{','}','break','continue','goto','return','for','while','do','if','else'
		]

FIRST={}
FOLLOW={}


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
	FOLLOW['program']=['$']
	stop = False
	while (not stop):

	



def main():
	print('__in main__')
	getFirst()
	print('ans')
	for each_nonterminal in NONTERMINAL:
		print(each_nonterminal, FIRST[each_nonterminal])


if __name__ == '__main__':
	main()
