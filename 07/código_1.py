p = 5
q = 3

n = p*q
fi = (p-1)*(q-1)

c = [i for i in range(1,fi+1) if fi % i == 0]
ne = 3
ce = [ i for i in range (1,ne + 1) if ne % i == 0]

print(f'cfi{fi}, {c}')
print(f'c{ne}, {ce}, {set(c) & set(ce)}')
