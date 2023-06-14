# transform sequence of numbers and characters into a sequence of letter where each letter is multiplied by the number preceding it
# some numbers may contain more than one digit

def recette(s):
    if len(s) == 0:
        return ""
    else:
        if s[0].isdigit() and not s[1].isdigit():
            return int(s[0]) * s[1] + recette(s[2:])
        elif s[0].isdigit() and s[1].isdigit():
            return int(s[0:2]) * s[2] + recette(s[3:])
        else:
            print("wtf")
            return s[0] + recette(s[1:])

        
print(recette("2i1s4i1s15d1o49i1o4d1o3i1o15d1o22d1o20d1o19i1o7d1o5d1o2i1o55i1o1d1o19d1o17d1o18d1o29i1o12i1o26i1o8d1o59d1o27i1o6d1o17i1o12d1o7d1o5i1o1d1o2d1o12i1o9d1o26d1o"))
    
