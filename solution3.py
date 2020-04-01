l=eval(input())
s=input()
t=[]
for i in l:
  if i.startswith(s):
    t.append(i)
  else:
    pass
print(t)
