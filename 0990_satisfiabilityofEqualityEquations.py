'''
Runtime: 53 ms, faster than 63.45% of Python3 online submissions for Satisfiability of Equality Equations.
Memory Usage: 14.2 MB, less than 56.52% of Python3 online submissions for Satisfiability of Equality Equations.
'''
def equationsPossible(equations: list) -> bool:
    equality = {"!=" : False, "==" : True}
    seen_vars = set()
    colour = 0
    colour_var = {}
    
    def same(var_1, var_1_seen, var_2, var_2_seen, colour):
        if not var_1_seen and not var_2_seen:
            colour_var[var_1] = colour
            colour_var[var_2] = colour
            return colour + 1
        elif var_1_seen and not var_2_seen:
            colour_var[var_2] = colour_var[var_1]
            return colour
        elif not var_1_seen and var_2_seen:
            colour_var[var_1] = colour_var[var_2]
            return colour
        else:
            if colour_var[var_1] != colour_var[var_2]:
                if colour_var[var_1] < colour_var[var_2]:
                    holder = colour_var[var_2]
                    change_color = colour_var[var_1]
                else:
                    holder = colour_var[var_1]
                    change_color = colour_var[var_2]
                colour_var[var_2] = change_color
                for var, colouring in colour_var.items():
                    if colouring == holder:
                        colour_var[var] = change_color
            return colour
    
    def different(var_1, var_1_seen, var_2, var_2_seen, colour):
        if not var_1_seen and not var_2_seen:
            colour_var[var_1] = colour
            colour_var[var_2] = colour + 1
            return colour + 2
        elif var_1_seen and not var_2_seen:
            colour_var[var_2] = colour
            return colour + 1
        elif not var_1_seen and var_2_seen:
            colour_var[var_1] = colour
            return colour + 1
        else:
            if colour_var[var_2] == colour_var[var_1]:
                return -1
            return colour

    equal = [equation for equation in equations if equality[equation[1:3]]]
    not_equal = [equation for equation in equations if not equality[equation[1:3]]]
    for equation in equal + not_equal:
        var_1 = equation[0]
        var_2 = equation[-1]
        var_1_seen = False
        var_2_seen = False
        if var_1 == var_2:
            if not equality[equation[1:3]]:
                return False
            else:
                continue
        else:
            if var_1 not in seen_vars:
                seen_vars.add(var_1)
            else: var_1_seen = True
            if var_2 not in seen_vars:
                seen_vars.add(var_2)
            else: var_2_seen = True
        
        if equality[equation[1:3]]:
            colour = same(var_1, var_1_seen, var_2, var_2_seen, colour)
        else:   
            colour = different(var_1, var_1_seen, var_2, var_2_seen, colour)
            if colour == -1: return False
    print(colour_var)
    return True

equations = ["a==b","e==c","b==c","a!=e"]
print(equationsPossible(equations))