#Two random prime number

p=int(input("Enter the value of p(prime number)= \n"))
q=int(input("Enter the value of q(prime number)= \n"))
n = p*q

print("The value of n is =\n",n)

#Finding other part of the public key.

phi=((p-1)*(q-1))

print("The value of phi is =\n",phi)

#e stands for encrypt
e=int(input("Enter the value of e:\n"))
while 1<e:
    if e<phi:
         break
    else:
        print("You have enter wrong number")
        break

    
#private key generation

k=2
d=(1+(k*phi))/e
print("The value of d is=\n",d)


msg='BA'

msg=12

#encryption c = (msg^g) % n

c = pow(12,e,n)
print("The value c(CipherText) = \n", c)

#Decryption m = (c ^ d) % n

s = pow(c,d)
m=s%n
print("The value of m(PlainText-Origional text)\n",m)



#OUTPUT

Enter the value of p(prime number)= 
3
Enter the value of q(prime number)= 
7
The value of n is =
 21
The value of phi is =
 12
Enter the value of e:
5
The value of d is=
 5.0
The value c(CipherText) = 
 3
The value of m(PlainText-Origional text)
 12.0


    


