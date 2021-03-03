import os
import io

def check (w):
   s  = "grep {word} /Users/bobmarcus/Chains/words > /Users/bobmarcus/Chains/checkword"
   t = s.format(word = w)
   os.system(t)
   f = open("/Users/bobmarcus/Chains/checkword")
   l = f.readlines()
   c = l.count(w + "\n")
   if c == 0 :
      c =  checkplural(w)
   if c == 0:
      if len (w) >= 5:
         last = len (w) - 1
         if w[last] == "s" or w[last- 1: last +1] == "er" or w[last -1: last + 1] == "ed" or w[last - 2 : last + 1] == "ing":
            s ="Is {word} a word? Answer y or n  "
            t = s.format(word = w)
            ans = input(t)
            if ans == "y":
               c = 1       
   return(c)

def checkplural(w):
   if w [len(w) - 1]!= "s":
      return (0)
   else:
      w = w[0:len (w) - 1]
      c = check(w)
      return(c)


def new (s, pos, letter):
    l = list (s)
    l[pos - 1] = letter
    str = ""
    for i in range (0,len(l)):
        str = str + l[i]
    ok = check(str)
    if ok > 0:
       print("OK")
       return (str)
    else:
       print("Sorry")
       return (s)
      
def findchains(word):
   s = "grep {commaword} /Users/bobmarcus/Chains/chains.txt > /Users/bobmarcus/Chains/ch.txt"
   t = s.format(commaword ="," + word  + ",") 
   os.system(t)
   h = open("/Users/bobmarcus/Chains/ch.txt")
   s1 = h.read()
   s2 = s1.split("\n")
   s3 = s2[0]
   s4 = s3.split(",")
   s5 = s4 [1: len(s4) -1]
   return(s5)

def trim (list, string):
    if list.count (string)== 0:
       return(list)
    else:
       i = list.index(string)
       list = list[i: len(list)]
       return list
   
# findchainx returns [] if no match is found
print("Make finishing word 'aim', 'mare', or 'parts'to add chain to database")     
done = False
c = 0
print("If you give up, enter'quit'")
while c == 0 :
        start = input ("starting word? ")
        c = check(start)
        if c == 0:
           print ("Not a word. Try again")
c = 0
while c == 0 :
        finish = input ("finishing word? ")
        c = check(finish)
        if c == 0:
           print ("Not a word. Try again")
        elif len(start) != len (finish):
           print("Length of finishing word must be the same as starting word. Try again")
           c = 0
chain1 = findchains(start)
chain2 = findchains(finish)
if chain1 != [] and chain2 != []:
   chain1 = trim(chain1, start)
   chain2 = trim (chain2, finish)
   chain2.reverse()
   chain2 = chain2[1: len(chain2)]
   chain = chain1 + chain2
   print ("count = ", len(chain))
   print (chain)
   done = True
   lp ="Success"
   
if not (done):
   chain = "," + start + ","
s = start
while (s != finish) and not(done):
    while True:
        try:
           lp = input ("Enter new letter and position ")
           if lp == 'quit':
              done = True
              break
           lps = lp.split(" ")
           print(lps)
           letter = lps[0]
           pos = int(lps[1])
           snew = new(s,pos,letter)
           if snew != s:
              chain = chain + snew + ","      
           s = snew
           print(s)
           break
        except (ValueError, IndexError, RuntimeError, TypeError, NameError):
           print ("Bad Input, Try again")
if lp != 'quit':
   print("Success")
else:
   print("Better luck next time!")
if not(done):
   if finish == "mare" or finish == "aim" or finish == "parts":
      g = open("/Users/bobmarcus/Chains/chains.txt", 'a')
      g.write (chain + "\n")
      g. flush()

   chainlist = chain.split(",")
   chainlist = chainlist[1: len(chainlist) - 1]
   count = len (chainlist)
   print("count = ", count)
   print (chainlist)
