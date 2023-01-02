s = []
for i in range(256):
    s.append(i)

kunci = 'saputra1'
k = bytearray(kunci, "utf8")

j = 0
for i in range(len(kunci)):
    j = (j + s[i] + k[i % len(kunci)]) % 256
    x = s[i] 
    s[j] = x
    s[i] = j

print(s)    
