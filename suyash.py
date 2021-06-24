C = [57,4,40,93,76,70,0]

J = [44,22,38,32,143,157,0]

F = [36,111,54,72,181,292,1]

D = [42,6,29,45,200,85,2]

K = [58,14,3,41,85,0,31]


WR = [30,20,20,20,20,20,20]
Min = [54.59,5.49,28.07,63.49,90.67,108.00,83.33]
Max = [58.63,6.27,39.30,81.63,113.33,129.60,100.00]

PL = [8,1,5,10,10,30,20]

MM = [50,30,30,20,20,20,30]

bsc = 0
comb = [None,None,None,None,None]

for i in range(101):
	for j in range(101):
		for k in range(101):
			for n in range(101):
				if(i + j + k + n > 100):
					continue
				l = 100 - i - j - k - n
				sc = 0
				for m in range(7):
					val = C[m]*i + J[m]*j + F[m]*k + D[m]*l + K[m]*n
					val /= 100
					if(val > Min[m] and val <= Max[m]):
						sc += WR[m]
					elif(val > Max[m]):
						sc += MM[m]
					elif(val > Min[m] - PL[m]):
						sc += 10
				if(sc >= bsc):
					bsc = sc
					comb = [i,j,k,l,n]
				
			
print(bsc)
print(comb)
