class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # parsing the input is the most complicated part here
        import collections

        l = list(s.strip())

        operators = set(['+', '-'])
        left_paren = "("
        right_paren = ")"

        # evaluates an expresion that comes as a list with no parenthesis
        def evaluate_expr(expr):

            # expr = "[2 ,+, 3, +, 4]"
            total = int(expr[0])
            i = 1
            while (i < len(expr)):
                if expr[i] == '+':
                    total += int(expr[i+1])
                elif expr[i] == '-':
                    total -= int(expr[i+1])
                i = i + 1
            return total


        def filter_input(s):

            l_clean=[]
            i = 0

            while (i < len(s)):
                if s[i] == left_paren or s[i] == right_paren or s[i] in operators:
                    l_clean.append(s[i])
                elif s[i].isdigit():
                    # this is a digit
                    d = s[i]
                    while (i + 1 < len(s) and s[i+1].isdigit()):
                        d = d  + s[i + 1]
                        i = i + 1

                    l_clean.append(d)
                i = i + 1

            return l_clean

        l = filter_input(l)

        # now we have all items parsed
        q = collections.deque()

        for item in l:
            # append to queue
            if item == right_paren:
                # backtrack
                expr = []
                while (q[-1] != left_paren):
                    expr.append(q.pop())

                # remove left_paren
                q.pop()
                # now reverse
                expr.reverse()
                value = evaluate_expr(expr)
                q.append(value)

            else:
                q.append(item)

        return evaluate_expr(q)




