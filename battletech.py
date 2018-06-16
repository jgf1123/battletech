# -*- coding: utf-8 -*-
"""
Created on Wed May  2 17:59:36 2018

@author: jgf1123
"""

import json
import os

# heat sink efficiency in each biome
biomeHeatSinkEfficiency = {'lunar':     0.65,
                           'martian':   0.75,
                           'parched':   0.85,
                           'temperate': 1.0,
                           'tundra':    1.1,
                           'polar':     1.2}

# probability of each biome
biomeProbability = {'lunar':     0.04118,
                    'martian':   0.08882,
                    'parched':   0.27286,
                    'temperate': 0.33703,
                    'tundra':    0.09947,
                    'polar':     0.16064}

# Original values
# defensive factor by walking speed
DFWalkTT = {95:1.2, 120:1.2, 140:1.3, 165:1.3, 190:1.4, 210:1.4}

# defensive factor by number of jump jets
DFJumpTT = {0:0, 1:1.1, 2:1.1, 3:1.2, 4:1.2, 5:1.3, 6:1.3, 7:1.4, 8:1.4}

# New values
# defensive factor by walking speed
DFWalkHBS = {95:1.0305, 120:1.0762, 140:1.0762,
             165:1.1295, 190:1.1867, 210:1.2457}

# defensive factor by number of jump jets
DFJumpHBS = {0:0, 1:1.0305, 2:1.0762, 3:1.1295, 4:1.1867,
             5:1.2457, 6:1.3057, 7:1.3057, 8:1.3057}

# heat from max jump by number of jump jets
jumpHeat = {0:0, 1:10, 2:15, 3:20, 4:25, 5:30, 6:35, 7:40, 8:43}
#jumpHeat = {0:0, 1:3, 2:6, 3:9, 4:12, 5:15, 6:18, 7:21, 8:24}

# max jump distance by number of jump jets
jumpDistance = {0:0, 1:60, 2:90, 3:120, 4:150, 5:180, 6:210, 7:240, 8:255}

# max jump hexes by number of jump jets
jumpTable = {0:0, 1:2.5, 2:3.75, 3:5, 4:6.25, 5:7.5, 6:8.75, 7:10, 8:10.625}

clusterTable = {'Weapon_LRM_LRM5_0-STOCK':              0.460,
                'Weapon_LRM_LRM10_0-STOCK':             0.398,
                'Weapon_LRM_LRM15_0-STOCK':             0.374,
                'Weapon_LRM_LRM20_0-STOCK':             0.361,
                'Weapon_MachineGun_MachineGun_0-STOCK': 0.341,
                'Weapon_SRM_SRM2_0-STOCK':              0.519,
                'Weapon_SRM_SRM4_0-STOCK':              0.368,
                'Weapon_SRM_SRM6_0-STOCK':              0.322}

def parse_half_tons(s):
    '''parse_half_tons(s) -> int
    Parse tonnage string s into half tons.'''
    f = 2 * float(s)  # float half tons
    return int(f + 0.5)  # round to nearest int
    
class Weapon:
    '''Represents a weapon.  Does not include ammo.'''
    
    def __init__(self,weaponJson):
        '''Weapon(weaponJson) -> Weapon
        Constructs a Weapon from weaponJson.'''
        # Load data from file
        fh = open(weaponJson,'r')
        jsonStr = fh.read()
        jsonDict = json.loads(jsonStr)
        
        # Grab attributes
        self.name = jsonDict['Description']['Id']
        self.ammo = jsonDict['AmmoCategory']  # ammo type used
        if self.ammo == 'NotSet':  # check if no ammo
            self.ammo = None
        self.category = jsonDict['Category']  # Ballistic/Energy/Missile/etc.
        self.heat = int(jsonDict['HeatGenerated'])
        # used to filter out LosTech
        self.rarity = int(jsonDict['Description']['Rarity'])
        self.size = int(jsonDict['InventorySize'])  # crit slots used
        # track tonnage in half ton increments
        self.halfTons = parse_half_tons(jsonDict['Tonnage'])
        
        # Calculate weapon BV
        damage = jsonDict['Damage']
        
        effectiveDamage = jsonDict['ShotsWhenFired'] * (damage
                      + 0.6 * jsonDict['Instability'] + jsonDict['HeatDamage'])
        # convert to hexes, reduce range by 25%
        minRange = jsonDict['MinRange'] // 30
        maxRange = jsonDict['MaxRange'] // 30
        medRange = jsonDict['RangeSplit'][1] // 30
        accuracyModifier = -0.05 * (jsonDict['AccuracyModifier']
                                    + jsonDict['RefireModifier'] / 2)
        
        bv = 0  # will contain BV
        for r in range(1,25):  # for each hex
            if r < minRange:  # inside minimum range
                bv += (0.375 + accuracyModifier) * effectiveDamage
            elif r <= medRange:  # inside medium range
                bv += (0.775 + accuracyModifier) * effectiveDamage
            elif r <= maxRange:  # long range
                bv += (0.575 + accuracyModifier) * effectiveDamage
            # otherwise add 0
            
        bv *= 0.82 / 5  # balance factor
#        bv *= 2.49 / 5 / medRange ** 0.5  # alt weapon BV
        if jsonDict['AmmoCategory'] == 'NotSet':  # if energy weapon
            bv *= 1.25  # bonus BV
        
        # Modifier for concentrated damage
        try:  # if in clusterTable
            modifier = 1 + 0.002 * clusterTable[self.name] \
                           * jsonDict['ShotsWhenFired'] * damage
        except KeyError:
            modifier = 1 + 0.002 * jsonDict['ShotsWhenFired'] * damage
        if damage >= 100:  # headshot bonus
            modifier += 0.05
        elif damage >= 75:
            modifier += 0.03
        elif damage >= 60:
            modifier += 0.01
        bv *= modifier
        
        self.BV = bv
        if jsonDict['AmmoCategory'] != 'NotSet':  # if not energy weapon
            self.ammoBV = bv / 8
            
#        print(self.name, self.BV)
        
        
class Chassis:
    '''Represents a chassis.'''
    
    def __init__(self,chassisJson):
        '''Mech(chassisJson) -> Mech
        Constructs a chassis from chassisJson.'''
        # Load data from file
        fh = open(chassisJson,'r')
        jsonStr = fh.read()
        fh.close()
        jsonDict = json.loads(jsonStr)
        
        # Grab attributes
        self.chassisName = jsonDict['Description']['Id']
        # used to filter normal mechs
        self.chassisPurchasable = jsonDict['Description']['Purchasable']
        # maximum half tons on chassis
        self.maxHalfTons = parse_half_tons(jsonDict['Tonnage'])
        # half tons taken up by default equipment
        self.initialHalfTons = parse_half_tons(jsonDict['InitialTonnage'])
        self.weightClass = jsonDict['weightClass']  # LIGHT/MEDIUM/etc.
        # engine comes with 10 heat sinks
        self.freeHeatSinks = 10 + int(jsonDict['Heatsinks'])
        self.maxJumpJets = int(jsonDict['MaxJumpjets'])
        
        # Load movement file
        moveJson = '{}\\{}.json'.format(movementDir,
                                        jsonDict['MovementCapDefID'])
        fh = open(moveJson,'r')
        jsonStr = fh.read()
        fh.close()
        moveDict = json.loads(jsonStr)
        self.walk = int(moveDict['MaxWalkDistance'] + 0.5)  # round to int
        
        # Parse locations
        # Initialize running totals
        self.internalStructure = 0
        self.maxArmor = 0  # includes forward and rear armor
        self.slots = 0  # critical slots
        self.weaponSlots = 0  # total slots for weapons
        # critical slots available for each weapon category
        self.categorySlots = {'Ballistic':0, 'Energy':0,
                              'Missile':0, 'AntiPersonnel':0}
        # mounts available for each weapon category
        self.categoryMounts = {'Ballistic':0, 'Energy':0,
                               'Missile':0, 'AntiPersonnel':0}
        for location in jsonDict['Locations']:
            # I think this attribute is ignored?
            #assert location['Tonnage'] == 0, \
            #       '{} {}'.format(self.chassisName, location['Location'])
            self.internalStructure += int(location['InternalStructure'])
            self.maxArmor += int(location['MaxArmor'])
            maxRearArmor = int(location['MaxRearArmor'])
            if maxRearArmor > 0:  # -1 used to represent no rear armor
                self.maxArmor += maxRearArmor
            
            # Keep track of slots and mounts for different weapon categories
            slots = int(location['InventorySlots'])
            self.slots += slots
            # mounts for each weapon category in this location
            mounts = {'Ballistic':0, 'Energy':0,
                      'Missile':0, 'AntiPersonnel':0}
            for hardpoint in location['Hardpoints']:
                mounts[hardpoint['WeaponMount']] += 1  # add this mount
            if sum(mounts.values()) > 0:  # if location can have weapons
                self.weaponSlots += slots  # max slots available for weapons
            for category in mounts:
                if mounts[category] > 0:  # if this location has this category
                    # max slots available for this weapon category
                    self.categorySlots[category] += slots
                    # mounts available for this weapon category
                    self.categoryMounts[category] += mounts[category]
                    
                    
class Mech(Chassis):
    '''Represents a mech.'''
    
    def __init__(self,mechJson,mechHash=None):
        '''Mech(mechJson,[blank]) -> Mech
        Constructs a Mech from mechJson. If mechHash not specified, constructs
        the mech in the json. Otherwise constructs the mech in the hash.'''
        # Load data from file
        fh = open(mechJson,'r')
        jsonStr = fh.read()
        fh.close()
        jsonDict = json.loads(jsonStr)
        
        chassisFile = '{}\\{}.json'.format(chassisDir, jsonDict['ChassisID'])
        Chassis.__init__(self,chassisFile)
        
        self.mechName = jsonDict['Description']['UIName']
        # used to filter normal mechs 
        self.blacklisted = 'BLACKLISTED' in jsonDict['MechTags']['items']
        if self.blacklisted:
            return  # skip rest of constructor
        
        # Initialize attributes
        self.ammo = {}
        self.heatSinks = 0  # number of standard heat sinks
        self.jumpJets = 0  # number of heat sinks; determine tons separately
        self.weapons = {'Ballistic':[], 'Energy':[],
                        'Missile':[], 'AntiPersonnel':[]}
        
        if mechHash is not None:  # if hash specified
            self.read_hash(mechHash)
            self.calc_bv()  # calculate BV
            return  # ignore rest of file
        
        # Get armor from locations
        self.currentArmor = 0  # running total of armor
        for location in jsonDict['Locations']:
            self.currentArmor += location['CurrentArmor']
            rearArmor = location['CurrentRearArmor']
            if rearArmor > 0:  # -1 used to represent no rear armor
                self.currentArmor += rearArmor
                
        # Parse inventory
        for item in jsonDict['inventory']:
            defType = item['ComponentDefType']
            defID = item['ComponentDefID']
            if defType == 'AmmunitionBox':
                # 'Ammo_AmmunitionBox_Generic_LRM' -> 'LRM'
                defID = defID.split('_')[-1]
                try:  # add ammo to dict
                    self.ammo[defID] += 1
                except KeyError:
                    self.ammo[defID] = 1
            elif defType == 'HeatSink':
                self.heatSinks += 1  # assume all heat sinks are standard
            elif defType == 'JumpJet':
                self.jumpJets += 1  # just count heat sinks
            elif defType == 'Weapon':
                weapon = weaponDict[defID]  # get Weapon object
                self.weapons[weapon.category].append(weapon)
                
        self.audit()  # check mech follows construction rules
        self.calc_bv()  # calculate BV
        
    def find_hash(self):
        '''Mech.find_hash() -> str
        Returns the hash of the Mech's current loadout.'''
        s = '{}{}'.format(str(self.heatSinks),str(self.jumpJets))
        for category in ('Ballistic','Energy','Missile','AntiPersonnel'):
            s += '|'  # mark category boundary
            # for each weapon
            for name,weapon,ammo in weaponTupleDict[category]:
                # number of weapons
                s += str(self.weapons[weapon.category].count(weapon))
                try:  # number of ammo
                    s += str(self.ammo[ammo])
                except KeyError:
                    s += '0'
        return s
    
    def read_hash(self,h):
        '''Mech.read_hash(h)
        Read in loadout from Mech hash h.'''
        self.heatSinks = int(h[0])  # read in heat sinks
        self.jumpJets = int(h[1])  # and jump jets
        self.ammo = {}  # clear ammo
        index = 3  # current index in hash
        for category in ('Ballistic','Energy','Missile','AntiPersonnel'):
            self.weapons[category] = []  # clear weapons in category
            # for each weapon
            for name,weapon,ammo in weaponTupleDict[category]:
                num = int(h[index])  # number of weapon
                if num > 0:  # if at least one weapon
                    self.weapons[category].extend(num * [weapon]) # add weapons
                numAmmo = int(h[index + 1])  # number of ammo
                if numAmmo > 0:  # if at least one ammo
                    self.ammo[ammo] = numAmmo
                index += 2  # move index to next weapon
            index += 1  # skip category boundary
                    
        self.currentArmor = self.calc_armor()  # assign armor
        self.audit()  # check mech follows construction rules
        
    def calc_armor(self):
        '''Mech.calc_armor() -> int
        Calculates armor for Mech, constrained by remaining weight and
        maxArmor.'''
        halfTons = self.maxHalfTons - self.initialHalfTons  # available weight
        for category in self.weapons:  # for each category of weapons
            for weapon in self.weapons[category]: # for each weapon in category
                halfTons -= weapon.halfTons
        halfTons -= 2 * sum(self.ammo.values())  # 2 half tons per ammo
        halfTons -= 2 * self.heatSinks  # 2 half tons per standard heat sinks
        if self.maxHalfTons <= 110:  # standard jump jets
            halfTons -= self.jumpJets
        elif self.maxHalfTons <= 170:  # heavy jump jets
            halfTons -= 2 * self.jumpJets
        else:  # assault jump jets
            halfTons -= 4 * self.jumpJets
        
        return min(self.maxArmor, 40 * halfTons)
                    
    def audit(self):
        '''Mech.audit() -> bool
        Returns True if all of the following are True:
            * Mech does not exceed maximum number of jump jets
            * Each weapon has at least 1 ton of ammo
            * Mech has enough hardpoints for weapons
            * Mech has enough slots in locations for each weapon category
            * Mech has enough slots for everything
            * Mech uses all of it tonnage'''
        flag = True  # init flag if mech checks out    
        
        if self.jumpJets > self.maxJumpJets:  # if too many jump jets
            print('{}: too many jump jets'.format(self.mechName))
            flag = False
            
        slots = 0  # running total of critical slots used
        
        for category in self.weapons:  # for each category of weapons
            hardpoints = 0  # running total of hardpoints used for category
            categorySlots = 0  # running total of slots used for category
            for weapon in self.weapons[category]: # for each weapon in category
                ammoCategory = weapon.ammo  # get ammo category
                # if not enough ammo
                if ammoCategory not in [None, 'Flamer'] \
                        and self.ammo[ammoCategory] < 1:
                    print('{}: no {} ammo'.format(self.mechName, weapon.ammo))
                    flag = False
                
                hardpoints += 1  # use a hardpoint
                # Account for critical slots
                slots += weapon.size
                categorySlots += weapon.size
                
            # if not enough mounts for this weapon category
            if hardpoints > self.categoryMounts[category]:
                print('{} {}: {} weapons, {} mounts'.format(self.mechName,
                        category, hardpoints, self.categoryMounts[category]))
                flag = False
            
            # if locations with these mounts don't have enough slots
            if categorySlots > self.categorySlots[category]:
                print('{}: {} weapons use too many slots'.format(
                        self.mechName, category))
                flag = False
            
        if self.currentArmor != self.calc_armor():  # if armor is off
            print('{}: correct armor: {}; current armor: {}'.format(
                    self.mechName, self.calc_armor(), self.currentArmor))
            flag = False
        
        return flag
    
    def calc_bv(self):
        '''Mech.calc_bv() -> dict
        Returns a dict with biomes as keys and BV as values.'''
        defBV = 0  # init defensive BV
        
        # TT: standard armor 8 armor/halfTon * 2.5 pts/armor = 20 pts/halfTon
        # HBS: 40 armor/halfTon -> 0.5 pt / armor
        defBV += 0.5 * self.currentArmor
        
        # TT: 2 internal structure (IS) * 1.5 pts/IS * 1.0 (standard IS)
        #     * 1.0 (standard engine) = 3 pts
        # HBS: 10 IS -> 0.3 pts / IS
        defBV += 0.3 * self.internalStructure
        
        # TT: 1 ton * 0.5 pts/ton (standard gyro) = 0.5 pts
        # HBS: 2 halfTons -> 0.25 pt / halfTons
        defBV += 0.25 * self.maxHalfTons
        
        # No defensive equipment
        
        # -15 pts / ton of ammo
        defBV -= 15 * sum(self.ammo.values())
        # TODO: Gauss weapons
        
        # use better defensive factor from movement
        defensiveFactor = max(DFWalkHBS[self.walk],
                              DFJumpHBS[self.jumpJets])
        if self.maxHalfTons <= 70:  # if light mech
            defensiveFactor += 0.06
        elif self.maxHalfTons <= 110:  # if medium mech
            defensiveFactor += 0.03
        defensiveFactor += 0.1051  # balance old and new factors
        
        self.defBase = defBV
        self.defensiveFactor = defensiveFactor
        
        defBV *= defensiveFactor
        self.defBV = defBV  # save for debugging
        
        # Find most heat efficient weapons
        tupList = []  # list of (heat,BV) tuples
        # list of weapons in each weapon category
        for weaponList in self.weapons.values():
            for weapon in weaponList:  # for each weapon
                tupList.append( (weapon.heat, weapon.BV) )
        tupList.sort(key=lambda t:t[0]/t[1])  # sort most heat efficient first
        
        # 10 free heat sinks, add extra heat sinks, formula adds 6 more
        # 3 heat per heat sink
        heatCapacity = 3 * (16 + self.heatSinks)
        offBV = {}  # will hold offensive BV per biome
        for biome,eff in biomeHeatSinkEfficiency.items():  # for each biome
            # adjust for biome heat efficiency
            heatEfficiency = heatCapacity * eff
            # 0 jump jets means walking, which is 0 heat
            # otherwise subtract heat from max jump
            heatEfficiency = max(0, heatEfficiency - jumpHeat[self.jumpJets])

            offBV[biome] = 0  # initialize
            for heat,bv in tupList:  # start with most heat efficient weapon
                if heat <= heatEfficiency:  # if enough heat efficiency left
                    offBV[biome] += bv  # full battle value
                    heatEfficiency -= heat  # use heat
                elif heatEfficiency == 0:  # if out of heat efficiency
                    offBV[biome] += bv / 2  # half battle value
                else:  # prorate remaining heat efficiency
                    # fraction of heat covered by remaining heat efficiency
                    p = heatEfficiency / heat
                    offBV[biome] += bv * p + (bv / 2) * (1 - p)
                    heatEfficiency = 0  # use remaining heat efficiency
        
        # Find value of each ton of ammo and total value of weapons
        eachAmmo = {}  # will contain value of each ammo
        ammoCap = {}  # total value of weapons for each ammo
        for category in self.weapons:  # for each weapon category
            for weapon in self.weapons[category]:  # for each weapon
                ammo = weapon.ammo  # ammo type
                if ammo is None:  # skip if no ammo
                    continue
                
                try:
                    # ammo BV equal to highest weapon ammo
                    eachAmmo[ammo] = max(eachAmmo[ammo], weapon.ammoBV)
                    ammoCap[ammo] += weapon.BV  # update cap
                except KeyError:
                    eachAmmo[ammo] = weapon.ammoBV
                    ammoCap[ammo] = weapon.BV
                    
        ammoBV = 0  # total BV of ammo
        for ammo,num in self.ammo.items():  # for each ammo
            # each ton of ammo has BV in eachAmmo, capped at ammoCap
            ammoBV += min(num * eachAmmo[ammo], ammoCap[ammo])

        # Speed factor
        walkR = self.walk / 1.05  # walking radius
        jumpR = jumpDistance[self.jumpJets]  # jumping radius
        # speed factor formula has typo
#        speedFactor = (1 + (walkMP + jumpMP / (8 / 3) - 93.73) / 203.63) ** 1.2
        speedFactor = (1 + (walkR + jumpR / 2.2 - 72.33) / 300) ** 1.1
            
        self.BV = {}  # dict of biome:BV
        for biome in offBV:  # for each biome
            offBV[biome] += ammoBV  # add ammo BV
            offBV[biome] += self.maxHalfTons // 2  # add tonnage
            
            if biome == 'temperate':
                self.offBase = offBV[biome]  # save for debugging
                
            offBV[biome] *= speedFactor  # multiply by speed factor
            if biome == 'temperate':
                self.offBV = offBV[biome]
            
            self.BV[biome] = defBV + offBV[biome]  # BV in this biome
        
        return self.BV
        

chassisDir = 'C:\\Python\\battletech\\chassis'  # folder of chassis json
mechDir = 'C:\\Python\\battletech\\mech'  # folder of mech json
movementDir = 'C:\\Python\\battletech\\movement'  # folder of movement json
weaponDir = 'C:\\Python\\battletech\\weapon'  # folder of weapon json

# Load weapons
# get files with stock weapons
weaponFiles = [os.path.join(weaponDir,file) for file in os.listdir(weaponDir) \
                   if 'STOCK' in file]
weaponDict = {}  # name:Weapon items
weaponTupleDict = {}  # category:list items
                      # list contains (name,Weapon,ammo) tuples
for file in weaponFiles:
    newWeapon = Weapon(file)  # read in from json
    if newWeapon.rarity > 0:  # skip if not common
        continue
    weaponDict[newWeapon.name] = newWeapon  # save in table
    t = (newWeapon.name, newWeapon, newWeapon.ammo)
    try:
        weaponTupleDict[newWeapon.category].append(t)
    except KeyError:
        weaponTupleDict[newWeapon.category] = [t]

for tupleList in weaponTupleDict.values():  # for each category
    tupleList.sort(key=lambda t:t[0])  # sort weapon names alphabetically
    
# Load chassis
# get chassis files, ignore template file
chassisFiles = [os.path.join(chassisDir,file) for file in
                os.listdir(chassisDir) if 'Template' not in file]
chassisDict = {}
for file in chassisFiles:
    newChassis = Chassis(file)  # read in from json
    if not newChassis.chassisPurchasable:  # skip if not common
        continue
    chassisDict[newChassis.chassisName] = newChassis  # save in table
    
# Load mechs
# get mech files, ignore template files
mechFiles = [os.path.join(mechDir,file) for file in os.listdir(mechDir) \
             if 'Template' not in file]
mechDict = {}
bvList = []  # list of (name,BV) tuples
for file in mechFiles:
    newMech = Mech(file)  # read in from json
    if newMech.blacklisted:  # skip if blacklisted
        continue
    mechDict[newMech.mechName] = newMech  # save in table

    averageBV = 0  # weighted average by biome
    for biome,p in biomeProbability.items():  # for each biome
        averageBV += p * newMech.BV[biome]  # weighted BV
    bvList.append( (newMech, averageBV) )

## For BV analysis
#    s = '{};{};{};{};{}'.format(newMech.mechName,
#         newMech.walk,
#         newMech.jumpJets,
#         newMech.defBV,
#         newMech.offBV)
#    print(s)
    
## For BV biome results
#bvList.sort(key=lambda t:t[1], reverse=True)  # sort by decreasing BV
#for mech,bv in bvList:  # for each mech
#    s = '{};{};{};{};{};{};{};{}'.format(mech.mechName,
#         bv,
#         mech.BV['lunar'],
#         mech.BV['martian'],
#         mech.BV['parched'],
#         mech.BV['temperate'],
#         mech.BV['tundra'],
#         mech.BV['polar'] )
#    print(s)

# Parameter search for speed factor
#walk2RunHex = {95:5, 120:6, 140:8, 165:9, 190:11, 210:12}
#
#jumpScale = 0.1
#distanceScale = 10
#hexScale = 10
#expScale = 0.01
#tList = []
#for jumpFactor in [22]:  # 2.0000 to 2.6667
#    j = jumpFactor * jumpScale
#    for distance in range(0,13):  # 0.00 to 120.00
#        d = distance * distanceScale
#        for hexFactor in [30]:  # 120.00 to 300.00
#            h = hexFactor * hexScale
#            for expFactor in range(110,121):  # 1.1000 to 1.2000
#                e = expFactor * expScale
#                ss = 0
#                for mech,foo in bvList:
#                    TTRun = walk2RunHex[mech.walk]
#                    TTJump = mech.jumpJets
#                    TTSF = (1 + (TTRun + TTJump / 2 - 5) / 10) ** 1.2
#                        
#                    HBSWalk = mech.walk
#                    HBSJump = jumpDistance[mech.jumpJets]
#                    HBSSF = (1 + (HBSWalk / 1.05 + HBSJump / j - d) / h) ** e
#                        
#                    ss += (mech.maxHalfTons * (TTSF - HBSSF)) ** 2
#                    
#            tList.append( (ss,j,d,h,e) )
#                
#tList.sort(key=lambda t:t[0])
#for ss,j,d,h,e in tList[:10]:
#    print(ss,j,d,h,e)
    
# Parameter search for defensive factor
#walkDF = {95:1.2, 120:1.2, 140:1.3, 165:1.3, 190:1.4, 210:1.4}
#jumpDF = {0:0, 1:1.1, 2:1.1, 3:1.2, 4:1.2, 5:1.3, 6:1.3, 7:1.4, 8:1.4}
#fScale = 0.0001
#tList = []
#for fFactor in range(1040,1061):
#    f = fFactor * fScale
#    ss = 0
#    for mech,foo in bvList:
#        TTRun = walkDF[mech.walk]
#        TTJump = jumpDF[mech.jumpJets]
#        TTDF = max(TTRun, TTJump)
#        
#        HBSWalk = DFWalkHBS[mech.walk]
#        HBSJump = DFJumpHBS[mech.jumpJets]
#        HBSDF = max(HBSWalk,HBSJump)
#        if mech.maxHalfTons <= 70:
#            HBSDF += 0.06
#        elif mech.maxHalfTons <= 110:
#            HBSDF += 0.03
#        HBSDF += f
#        
#        ss += (mech.defBase * (TTDF - HBSDF)) ** 2
#        
#    tList.append( (ss,f) )
#    
#tList.sort(key=lambda t:t[0])
#for ss,f in tList[:10]:
#    print(ss,f)