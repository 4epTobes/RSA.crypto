Kb_cl = open("Numbers_from_B\Kb.txt","r")
Kb = int(Kb_cl.read())
Kb_cl.close()

N_cl = open("Numbers_from_B\cN.txt","r")
N = int(N_cl.read())
N_cl.close()

crypt_input_cl = open("crypt_input.txt","r")
input_msg_len = len(crypt_input_cl.read())
crypt_input_cl.close()
crypt_input_cl = open("crypt_input.txt","r")

input_msg = []

for i in range(1,input_msg_len+1):
	input_msg.append(crypt_input_cl.read(1))

input_msg_int = [None for j in range(len(input_msg))]

for k in range(len(input_msg)):
	input_msg_int[k] = ord(input_msg[k])

input_msg_crypted = [None for j in range(len(input_msg))]

for t in range(len(input_msg)):
	input_msg_crypted[t] = (input_msg_int[t]**Kb)%N

output_msg = open("crypt_output.txt","w")

for d in range(len(input_msg)):
        output_msg.write(str(input_msg_crypted[d])+"\n")

output_msg.close()
crypt_input_cl.close()	
