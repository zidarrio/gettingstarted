# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:33:34 2018

@author: Stormfront
"""
t = 0
u = 0
v = 0
new_dict = {0:"b",1:"c",2:"d",3:"e",4:"f",5:"g",
            6:"h",7:"i",8:"j",9:"k",10:"l",11:"m",
            12:"n",13:"o",14:"p",15:"q",16:"r",17:"s",
            18:"t",19:"u",20:"v",21:"w",22:"x",23:"y",
            24:"z",25:"A"}
one = "a"
two = "a"
three = "a"
four = 0
five = 0
for x in range(5000):
    
    if five >= 0:
        five = int(five) + 1
        
        print(one + two.lower() + three.lower() + str(four) + str(five))
    
        if five == 9:
            four += 1
            five = 0
        
            
            if four == 10:               
                four = 0
                three = new_dict[t]
                
                t += 1
                if three == "A":
                        t = 0
                        two = new_dict[u]
                        u += 1
                        
                        if two == "A":
                            u = 0
                            one = new_dict[v]
                            v += 1
                            if one == "A":
                                break
                    