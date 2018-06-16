# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 22:25:48 2018

@author: jgf1123
"""

import json
import os

starDir = 'C:\\Python\\battletech\\starsystem'  # folder of star systems
# ignore contested and flipped star systems
starFiles = [os.path.join(starDir,file) for file in \
                 os.listdir(starDir) if file.count('_') < 2]

biomes = {}
for starJson in starFiles:
    fh = open(starJson,'r')
    jsonStr = fh.read()
    jsonDict = json.loads(jsonStr)
    
    nBiomes = len(jsonDict['SupportedBiomes'])
    for biome in jsonDict['SupportedBiomes']:
        try:
            biomes[biome] += 1 / nBiomes
        except KeyError:
            biomes[biome] = 1 / nBiomes
            
print(biomes)

# A: 0.96453
# A: 1.07046, B: 0.80751
# A: 0.93289, B: 1.16176, C: 0.71833
# A: 1.00000, B: 0.85000, C: 1.16176, D: 0.71833