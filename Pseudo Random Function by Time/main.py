/**
 * @author [Yacine YA]
 * @email [alloul.yacine@protonmail.com]
 * @create date 2022-01-19 00:0:06
 * @modify date 2022-01-19 00:29:06
 * @desc [Pseudo Random Algorithm...]
 */
import time 

def main():
    """ Our pseudo-random function will generate a number between two
     numbers by taking the time in nanoseconds which will allow us to get closer to a random event"""

     def findNumberofUnit(time):
         return len(time)%10

     def getPseudoRandomVar(n,m):
         time = list(str(time.time_ns()))
         time.pop()
         time.pop()
         numberOfUnit1 = findNumberofUnit(time)
         numberOfUnit2 = m%10
         time = time[:-1]
         pseudoRandom = []
         for l in range(0,numberOfUnit2):
             pseudoRandom.append(int(time[l]))

         return pseudoRandom



     def intervale(n,m):

         pseudoRandomVar = getPseudoRandomVar(n,m)
         #We now have "number" in the state of string

         for i in range(len(pseudoRandomVar)):
             iTab = pseudoRandomVar[i:len(pseudoRandomVar)]
             k = sum(iTab)
             if k <= m  and k >= n:
                 for i in iTab:
                     print(i,end="")
             else:
                 intervale(n,m) #Then we retry 
 


     

main()