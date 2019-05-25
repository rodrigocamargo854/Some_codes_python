a=int(input(" digite um numero"))
b=int(input(" digite outro numero"))

while a%b !=0:
      a,b = b,a % b
      
print ( " o mdc é %d" %b) 
