names=input()
orName=names;
names=names.split(" ")
unique=[]
nameDic={}
for i in range(0,len(names)):
  name=names[i]
  if name not in unique:
    nameDic[name]=1
    unique.append(name)
  else:
    nameDic[name]=nameDic[name]+1
if len(names)==len(unique):
  print(-1)
else:
  for k in range(len(unique)):
    if nameDic[unique[k]]!=1:
      print(unique[k]+" "+str(nameDic[unique[k]]))
