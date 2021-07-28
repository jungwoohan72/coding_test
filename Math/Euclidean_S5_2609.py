# 최대공약수
def GCD(a,b):
  if a < b:
    a,b = b,a

  if a%b == 0:
    return b
  else:
    return GCD(b,a%b)

# 최소공배수
def LCM(a,b):
  return int(a*b/GCD(a,b))

a,b = list(map(int, input().split()))

print(GCD(a,b))
print(LCM(a,b))