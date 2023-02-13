# -*- ecoding: utf-8 -*-
# @ModuleName: demo1
# @Author: Kerris
# @Time: 2023/2/7 15:45


nmu = 0

for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if((a!=b)and(a!=c)and(c!=b)):
                print(a,b,c)
                nmu+=1

print(nmu)