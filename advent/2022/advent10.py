#!/usr/bin
import sys

def main():
    f = open(sys.argv[1])
    
    program = []
    for l in f:
        l = l.strip()
        program.append(l)

    cycle = 1
    x = 1
    # if we need to do an addition for that cycle
    # gets added here
    instructions = {}

    i = 0
    
    LAST_CYCLE = 220 
    executing = False
    
    values = []
    values.append('N/A')

    while cycle <= LAST_CYCLE:
        print "{0}, X: {1}".format(cycle, x)
        
        values.append(x)

        if not executing:
            _input = program[i]
        
            if _input.startswith('noop'):
                pass
                i = i + 1
            else:
                (tmp, amount) = _input.split(' ')
                instructions[cycle+1] = int(amount)
                executing = True
                
        else:
            # second cycle of execution 
            # finish cycle, increment if needed
            if instructions.get(cycle) is not None:
                x = x + instructions[cycle] 
            executing = False
            i = i + 1
        
        cycle = cycle + 1
        if i >=len(program):
            # reset index for instructions
            i = 0

        


    print "X"
    l= [20 *values[20],60* values[60],100* values[100], 140 * values[140], 180 *values[180] ,220* values[220]]
    print sum(l)


if __name__=="__main__":
    main()
