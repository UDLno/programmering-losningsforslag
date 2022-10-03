start = 10
end = 25

print("Her er løsning med for-løkke")
for i in range(start, end, 2):
    print(i)

print("Her er løsning med while-løkke")
current = start
while current < end:
    print(current)
    current += 2
