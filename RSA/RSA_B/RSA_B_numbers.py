import random

P_cl = open("Primes\P.txt","r")
P = int(P_cl.read())
P_cl.close()

Q_cl = open("Primes\Q.txt","r")
Q = int(Q_cl.read())
Q_cl.close()

N = P*Q
fi_N = (P-1)*(Q-1)
i = 1

random.seed(version=2)

c = False
d =1000

while not c:

	Kb = random.randint(1,fi_N)

	a = Kb
	b = fi_N

	def Eucl(a,b):
		while not a == 0 and not b == 0:
			if a > b:
				a = a%b
			else:
				b = b%a	
		res = a+b
		a = Kb
		b = fi_N
		return res		

	while not (Kb > 1) and not Eucl == 1:
		Kb = random.randint(1,fi_N)

	for alp in range(1,d):
		kb = (alp*fi_N+1)/Kb
		if (kb-int(kb)) == 0:
			break
	d += 1000 		
	if kb-int(kb) == 0:
		c = True
		kb = int(kb)





N_cl = open("Numbers_to_A\cN.txt","w")
N_cl.write(str(N))
N_cl.close()

kb_cl = open("Encrypt_msg_from_A\kb.txt","w")
kb_cl.write(str(kb))
kb_cl.close()


Kb_cl = open("Numbers_to_A\Kb.txt","w")
Kb_cl.write(str(Kb))
Kb_cl.close()
