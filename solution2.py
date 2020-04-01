def fun(nesteddict,dic,currentkey):
for key in nesteddict.key():
if type(nesteddict[key])==int:
dic[(currentkey+"."+key).strip(".")]=nesteddict[key]
else:
dic=fun(nesteddict[key],dic,(currentkey+"."+key).strip('.'))
return dic
def func_dic(nesteddic):
return fun(nesteddic,dict(),"")
def main():
nesteddictionary={
"key":3,
"foo":{
"a":5,
"bar":{
"baz":8
}
}
}
dicten=func_dic(nesteddictionary)
print(dicten)
if_name_=="_main_":
main()
