#!usr/local/bin/python

f = open('./input8.txt')

# acc, jmp, or nop
ACC = 'acc'
JMP ='jmp'
NOP= 'nop'

acu = 0
# acc increases or decreases a single global value called the accumulator by the value given in the argument.
# jmp jumps to a new instruction relative to itself
# nop stands for No OPeration it does nothing
program = []


for l in f:
	(instr, arg) = l.split()
	program.append((instr, int(arg)))


directives_executed = {}
# execute program

# to the acumulator
def execute_instruction(line, acu):
	# have we executed this line before, if so we should exit
	if line in directives_executed.keys():
		print "acumulator"
		
		return acu
		
	print line 
	
	directives_executed[line] = 1

	(instr, arg) = program[line]
	
	if instr == NOP:
		return execute_instruction(line + 1 , acu)
	elif instr == ACC:
		return execute_instruction(line + 1, acu + arg) 
	elif instr == JMP:
		return execute_instruction(line + arg, acu)
	

acu = execute_instruction(0, 0)

print acu


	
	 

#for i in program:
#	print i	
