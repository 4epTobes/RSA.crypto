kb_cl = open("Encrypt_msg_from_A\kb.txt","r")
kb = int(kb_cl.read())
kb_cl.close()

N_cl = open("Numbers_to_A\cN.txt","r")
N = int(N_cl.read())
N_cl.close()

crypt_input_cl = open("Encrypt_msg_from_A\crypt_output.txt","r")

with open('Encrypt_msg_from_A\crypt_output.txt') as myfile:
    count = sum(1 for line in myfile)

crypt_input_int = [None for i in range(count)]

for j in range(count):
	crypt_input_int[j] = int(crypt_input_cl.readline())

crypt_input_cl.close()	

encrypt_output = [None for i in range(count)]
	
for c in range(count):
	encrypt_output[c] = chr((crypt_input_int[c]**kb)%N)

crypt_output_cl = open("Encrypt_msg_from_A\encrypted_msg.txt","w")

for a in range(count):
	crypt_output_cl.write(encrypt_output[a])

crypt_output_cl.close()