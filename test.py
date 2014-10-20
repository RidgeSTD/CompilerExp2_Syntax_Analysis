#coding:utf-8
import re

def main():
	string = '<N>	->	[STR][[]<normal expr>[]]<155>[<<][>>]'
	# string = '[<<][]][>>]'
	tmp=''
	bracket = ''
	last = ''
	terminals=[]
	nonterminals=[]
	sequence=[]

	for i in xrange(0,len(string)):
		if bracket=='':
			if last==']' and string[i]==']':
				terminals[len(terminals)-1]=terminals[len(terminals)-1]+']'
				sequence[len(sequence)-1]=sequence[len(sequence)-1]+']'
			if string[i]=='[':
				bracket=']'
			elif string[i]=='<':
				bracket='>'
				
		else:
			if string[i]==bracket:
				if string[i]==']':
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
				tmp=tmp+string[i]
		last = string[i]

	print(sequence)
	print(nonterminals)
	print(terminals)

		
	


if __name__ == '__main__':
	main()