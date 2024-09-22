

def f(x: int) -> int:
  return x ** 3 - 3 * x + 1


s = input("Enter an interval: ")
eps = float(input("Enter an epsilon: "))
strictly = s.find("(")
for i in "[]();": s = s.replace(i, " ")
s = s.strip()
a, b = map(int, s.split())
if f(a)*f(b)>0: exit("Not exist roots on this interval")
while True:
  x0 = (a + b) / 2
  if f(a) * f(x0) < 0:
    if abs(f(x0) - f(a)) <= eps: print(f"Root on the interval {list(map(int, s.split()))} == {x0}"); exit()
    b = x0
  if f(x0) * f(b) < 0:
    if abs(f(x0) - f(a)) <= eps: print(f"Root on the interval {list(map(int, s.split()))} == {x0}"); exit()
    a = x0
