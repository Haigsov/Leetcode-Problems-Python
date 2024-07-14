def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        # initialize 
        s = []
        # go throught every token
        for token in tokens:
            if token == "+":
                s.append(s.pop() + s.pop())
            elif token == "-":
                a, b = s.pop(), s.pop()
                s.append(b - a)
            elif token == "*":
                s.append(s.pop() * s.pop())
            elif token == "/":
                a, b = s.pop(), s.pop()
                s.append(int(float(b) / a))
            else:
                s.append(int(token))
        
        return s[0]