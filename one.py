#This is a python script
s = """    Hello--World--how--are--you--?   """
s = s.strip() #leading and trailing spaces are trimmed
print("After strip",s)
#Hello--World--how--are--you--?
s =s.split("--")# [ "Hello","World","how","are","you","?"]
s = s[::-1] # ["?","you","are","how","World","Hello"]
print("After Slice ",s)
s = "".join()
print("Final o/p = ",s)
