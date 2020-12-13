#!usr/local/bin/python
# acc, jmp, or nop
ACC = 'acc'
JMP ='jmp'
NOP= 'nop'


def run_instructions(p):
	directives_executed = {}
	
	def execute_instruction(line, acu):
		# have we executed this line before, if so we should exit
		if line in directives_executed.keys():
			print "acumulator"
			
			return acu
		elif line > len(p) -1:
			return -1	
		elif line == len (p) - 1:
			print "program terminated"
			return acu	
		directives_executed[line] = 1

		(instr, arg) = p[line]
		
		if instr == NOP:
			return execute_instruction(line + 1 , acu)
		elif instr == ACC:
			return execute_instruction(line + 1, acu + arg) 
		elif instr == JMP:
			return execute_instruction(line + arg, acu)

	acu = execute_instruction(0, 0)

	return (acu, len(directives_executed)) 

def main():

	f = open('./input8.txt')

	# acc increases or decreases a single global value called the accumulator by the value given in the argument.
	# jmp jumps to a new instruction relative to itself
	# nop stands for no operation it does nothing
	main_program = []


	for l in f:
		(instr, arg) = l.split()
		main_program.append((instr, int(arg)))

	# to the acumulator

	# now change one by one one jmp to noop

	for  i in range(0, len(main_program)):
		(instr, arg) = main_program[i]
		program = main_program[:]
		if instr == ACC:
			next
		elif instr == NOP:
			program[i] = (JMP, arg)
		elif instr == JMP:
			program[i] = (NOP, arg)	

		(acu, lines_executed) = run_instructions(program)
		print "acu {0}, lines:{1}".format(acu, lines_executed)

if __name__=="__main__":
	main()

		
