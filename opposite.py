def is_opposite(s1,s2):
    if s1.swapcase() == s2 and not s1=="":
        return True
    else:
        return False
    
#better solution
    def is_opposite(s1,s2):
        return s1!="" and s1.swapcase() == s2