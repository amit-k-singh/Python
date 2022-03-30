# p2. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal

decimal = int(input("Enter Decimal number = "))
binary=0
ctr=0
temp=decimal

while(temp > 0):
    binary = ((temp%2)*(10**ctr)) + binary
    temp = int(temp/2)
    ctr += 1

print("\nDecimal = {x} \nBinary  = {y}".format(x=decimal,y=binary))

octal=0
cnt=0
dec=decimal
while(dec > 0):
    octal = ((dec%8)*(10**cnt)) + octal
    dec = int(dec/8)
    cnt += 1

print("Octal   = {x}".format(x=octal))   

convert = { 0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',
            6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',
            12:'C',13:'D',14:'E',15:'F'}
hexadecimal = ''
hexa=decimal
tempcount=0
while(hexa > 0):
    reminder=hexa%16
    hexadecimal = convert[reminder]+hexadecimal
    hexa=int(hexa/16)

print("Octal   = {x}".format(x=hexadecimal))

