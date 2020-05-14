# this file finds all the tags present in an html document
tc = int(input())
import re
li=[]
li2=[]
for i in range(tc):
    stri =input()
    result = re.findall(r"(?<=\<)\w*",stri)
    li.extend(list(result))
li=list(set(li))
for i in li:
    if i !="":
        li2.append(i)
li2.sort()
print(";".join(li2))
