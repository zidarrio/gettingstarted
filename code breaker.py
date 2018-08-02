# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 11:50:40 2018

@author: Stormfront
"""

import string

x = string.printable[:-5]
list2 = []
list1 = ['0','1','2','3','4','5','6','7','8','9']
for x in x:
    list2.append(x)
    

def num_run():
    password = "josh5288"
    x = 0
    while x<10:
        if x == 0:
            x+=1
            for a in list2:
                print(a)
                if a == password:
                    print("horray")
                    return
                
        
        elif x == 1:
            x+=1
            for a in list2:
                for b in list2:
                    print(a+b)
                    if a+b == password:
                        print("horray")
                        return
        elif x == 2:
            x+=1
            for a in list2:
                for b in list2:
                    for c in list2:
                        print(a+b+c)
                        if a+b+c == password:
                            print("horray")
                            return
        elif x == 3:
            x+=1
            for a in list2:
                for b in list2:
                    for c in list2:
                        for d in list2:
                            print(a+b+c+d)
                            if a+b+c+d == password:
                                print("horray")
                                return
                                
        elif x == 4:
            x+=1
            for a in list2:
                for b in list2:
                    for c in list2:
                        for d in list2:
                            for e in list2:
                                print(a+b+c+d+e)
                                if a+b+c+d+e == password:
                                    print("horray")
                                    return
        elif x == 5:
            x+=1
            for a in list2:
                for b in list2:
                    for c in list2:
                        for d in list2:
                            for e in list2:
                                for f in list2:
                                    print(a+b+c+d+e+f)
                                    if a+b+c+d+e+f == password:
                                        print("horray")
                                        return
        elif x == 6:
            x+=1
            for a in list2:
                for b in list2:
                    for c in list2:
                        for d in list2:
                            for e in list2:
                                for f in list2:
                                    for g in list2:
                                        print(a+b+c+d+e+f+g)
                                        if a+b+c+d+e+f+g == password:
                                            print("horray")
                                            return
        elif x == 7:
            x+=1
            for a in list2:
                for b in list2:
                    for c in list2:
                        for d in list2:
                            for e in list2:
                                for f in list2:
                                    for g in list2:
                                        for h in list2:
                                            print(a+b+c+d+e+f+g+h)
                                            if a+b+c+d+e+f+g+h == password:
                                                print("horray")
                                                return
        elif x == 8:
            x+=1
            for a in list2:
                for b in list2:
                    for c in list2:
                        for d in list2:
                            for e in list2:
                                for f in list2:
                                    for g in list2:
                                        for h in list2:
                                            for i in list2:
                                                print(a+b+c+d+e+f+g+h+i)
                                                if a+b+c+d+e+f+g+h+i == password:
                                                    print("horray")
                                                    return
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                