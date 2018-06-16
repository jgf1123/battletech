# -*- coding: utf-8 -*-
"""
Created on Thu May 31 20:18:44 2018

@author: jgf1123
"""

#import json
#import os
#
#mechDir = 'C:\\Python\\battletech\\mech'  # folder of mech json
#mechFiles = [os.path.join(mechDir,file) for file in os.listdir(mechDir) \
#             if 'Template' not in file]
#
#weaponDict = {}
#for file in mechFiles:
#    fh = open(file,'r')
#    jsonStr = fh.read()
#    fh.close()
#    jsonDict = json.loads(jsonStr)
#    
#    if not jsonDict['Description']['Purchasable']:
#        continue
#    
#    print(jsonDict['Description']['Id'])
#    
#    for i in jsonDict['inventory']:
#        name = i['ComponentDefID']
#        if name.startswith('Weapon_'):
#            try:
#                weaponDict[name] += 1
#            except KeyError:
#                weaponDict[name] = 1
#                
#print(weaponDict)

import random

hitTable = {'H':1, 'CT':16, 'LT':14, 'RT':14, 'LA':10, 'RA':10, 'LL':8, 'RL':8}
adjacent = {'H':('CT','LT','RT'),
            'CT':('LT','RT'),
            'LT':('CT','LA','LL'),
            'RT':('CT','RA','RL'),
            'LA':('CT',),
            'RA':('CT',),
            'LL':('CT',),
            'RL':('CT',) }

lrmBool = True
N = 5
nTrials = 100000
s = 0
for trial in range(nTrials):
    first = True
    
    hitList = []
    for k,v in hitTable.items():
        hitList += [k] * v
            
    hits = {}
    for m in range(N):
        if random.random() > 0.775:  # if miss
            continue
        hit = random.choice(hitList)
        
        try:
            hits[hit] += 1
        except KeyError:
            hits[hit] = 1
            
        if lrmBool and first:
            firstHit = hit
            hitList = []
            for k,v in hitTable.items():
                if k == 'H':
                    continue
                if k == firstHit:
                    v *= 8
                if k in adjacent[firstHit]:
                    v *= 4
                hitList += [k] * v
                
            first = False
                
    if len(hits) == 0:
        continue
    s += max(hits.values())
        
print(s / nTrials / N)