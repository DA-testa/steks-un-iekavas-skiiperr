# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return ((left + right) in ["()", "[]", "{}"])

def find_mismatch(text):
    opening_brackets_stack = []
    for i, char in enumerate(text):
        if char in "([{":
            
            opening_brackets_stack.append(char)
            

         if char in ")]}":
            try:
                if are_matching(opening_brackets_stack[-1], char):
                    opening_brackets_stack.pop()
                else:
                    return i+1
                pass
            except:
                return i+1
    if len(opening_brackets_stack)!=0:
            return i+1
    return("Success")



def main():
    text = input()
    if "I" in text:
        text = input()
    if "F" in text:
        text=""
    mismatch = find_mismatch(text)
    
    if not mismatch:
        print("Sucsess")
    else:
        print(mismatch) 


if __name__ == "__main__":
    main()
