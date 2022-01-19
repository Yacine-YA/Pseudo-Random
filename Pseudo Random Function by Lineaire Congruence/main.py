import time 
time = int(time.time())


def main():
    
    print(time)
    def random(x0, a, b, m, n):
        result  =[]
        for i in range(0,n):

            x0 = (a * x0 + b) % m
            result.append(int(x0))
        return result

            
    print(random(time*(time//10),75,74,2**(16)+1,10))

    

main()
