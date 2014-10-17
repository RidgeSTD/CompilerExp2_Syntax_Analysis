G ={
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
'constant':['integer','decimal','char','string'],
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

nonterminal=['program','function_statement','function_defination','type',
			'params','param','function_body','function_internal','declare',
			'ids','idN','assign','assign_idN','function','constant','expression',
			'single_expression','double_expression','double_operator','loop_expression',
			'jump_signal','for_expression','for_internal_expression','loop_body',
			'loop_internal','while_expression','do_expression','if_expression',
			'if_remain','if_internal'
			]
terminal=['$','null','id',';','void','char','byte','shot','int','long','float','double',
		',','=','integer','decimal','character','string','!','^','&','++','--','+','-','*','/',
		'&&','||','{','}','break','continue','goto','return','for','while','do','if','else'
		]

first={}
follow={}

def getFirst():
	global G, nonterminal, terminal, first
	print("__ingetFirst__")
	for each in terminal:
		first[each]=[each]
	stop = 0
	while(stop==0):
		for eachNTerminal in nonterminal:
			for eachSequence in G.get(eachNTerminal, []):
				if(eachSequence==[]):
					print('Wrong! in Kernel.line(77)')
				

	# print(first)


def main():
	print('__in main__')
	getFirst()


if __name__ == '__main__':
	main()
