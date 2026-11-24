a, b = map(int, input().split())
x, y = map(int, input().split())

if a > b:
    a, b = b, a
if x > y:
    x, y = y, x
if a <= x and b <= y:
    print('Влезет')
else:
    print('Не влезет')