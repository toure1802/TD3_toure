import sys
def mul(x,y):
    return x*y
if __name__=="__main__":
	print(sys.argv)    
	if(len(sys.argv)==3):
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		print(mul(x,y))
	elif(len(sys.argv)==2):
		x = int(sys.argv[1])
		y = int(input("Entrez la troisieme valeur svp ? "))
		print(mul(x,y))
	if(len(sys.argv)==2):
		print("error")
	elif(len(sys.argv)==1):
		x = int(input("Entrez la deuxieme la valeur svp ? "))
		y = int(input("Entrez la troixieme valeur svp ? "))
		print(mul(x,y))
	else:
		print("Desoler erreur"))
		print("error")
        else:
                x = int(sys.argv[1])
                y = int(sys.argv[2])
                print(mul(x,y)i)
