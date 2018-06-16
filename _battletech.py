# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 09:04:09 2018

@author: jgf1123
"""

# 0.92, 1.15 multiplier
## BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       83.85,
#            'Weapon_Autocannon_AC5_0-STOCK':      117.63,
#            'Weapon_Autocannon_AC10_0-STOCK':     150.64,
#            'Weapon_Autocannon_AC20_0-STOCK':     168.98,
#            'Weapon_Flamer_Flamer_0-STOCK':         5.92,
#            'Weapon_Laser_LargeLaser_0-STOCK':    113.02,
#            'Weapon_Laser_MediumLaser_0-STOCK':    41.21,
#            'Weapon_Laser_SmallLaser_0-STOCK':     10.88,
#            'Weapon_LRM_LRM5_0-STOCK':             62.73,
#            'Weapon_LRM_LRM10_0-STOCK':           127.11,
#            'Weapon_LRM_LRM15_0-STOCK':           193.08,
#            'Weapon_LRM_LRM20_0-STOCK':           260.61,
#            'Weapon_MachineGun_MachineGun_0-STOCK': 5.92,
#            'Weapon_PPC_PPC_0-STOCK':             187.45,
#            'Weapon_SRM_SRM2_0-STOCK':             23.37,
#            'Weapon_SRM_SRM4_0-STOCK':             47.06,
#            'Weapon_SRM_SRM6_0-STOCK':             71.10}
#
## ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':       10.48,
#          'Weapon_Autocannon_AC5_0-STOCK':       14.70,
#          'Weapon_Autocannon_AC10_0-STOCK':      18.83,
#          'Weapon_Autocannon_AC20_0-STOCK':      21.12,
#          'Weapon_Flamer_Flamer_0-STOCK':         0.74,
#          'Weapon_LRM_LRM5_0-STOCK':              7.84,
#          'Weapon_LRM_LRM10_0-STOCK':            15.89,
#          'Weapon_LRM_LRM15_0-STOCK':            24.13,
#          'Weapon_LRM_LRM20_0-STOCK':            32.58,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 0.74,
#          'Weapon_SRM_SRM2_0-STOCK':              2.92,
#          'Weapon_SRM_SRM4_0-STOCK':              5.88,
#          'Weapon_SRM_SRM6_0-STOCK':              8.89}

# 0.9, 1.125 multiplier
## BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       82.03,
#            'Weapon_Autocannon_AC5_0-STOCK':      115.07,
#            'Weapon_Autocannon_AC10_0-STOCK':     147.36,
#            'Weapon_Autocannon_AC20_0-STOCK':     165.31,
#            'Weapon_Flamer_Flamer_0-STOCK':         5.79,
#            'Weapon_Laser_LargeLaser_0-STOCK':    110.57,
#            'Weapon_Laser_MediumLaser_0-STOCK':    40.31,
#            'Weapon_Laser_SmallLaser_0-STOCK':     10.65,
#            'Weapon_LRM_LRM5_0-STOCK':             61.36,
#            'Weapon_LRM_LRM10_0-STOCK':           124.35,
#            'Weapon_LRM_LRM15_0-STOCK':           188.88,
#            'Weapon_LRM_LRM20_0-STOCK':           254.94,
#            'Weapon_MachineGun_MachineGun_0-STOCK': 5.80,
#            'Weapon_PPC_PPC_0-STOCK':             183.37,
#            'Weapon_SRM_SRM2_0-STOCK':             22.86,
#            'Weapon_SRM_SRM4_0-STOCK':             46.04,
#            'Weapon_SRM_SRM6_0-STOCK':             69.56}
#
## ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':       10.25,
#          'Weapon_Autocannon_AC5_0-STOCK':       14.38,
#          'Weapon_Autocannon_AC10_0-STOCK':      18.42,
#          'Weapon_Autocannon_AC20_0-STOCK':      20.66,
#          'Weapon_Flamer_Flamer_0-STOCK':         0.72,
#          'Weapon_LRM_LRM5_0-STOCK':              7.67,
#          'Weapon_LRM_LRM10_0-STOCK':            15.54,
#          'Weapon_LRM_LRM15_0-STOCK':            23.61,
#          'Weapon_LRM_LRM20_0-STOCK':            31.87,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 0.72,
#          'Weapon_SRM_SRM2_0-STOCK':              2.86,
#          'Weapon_SRM_SRM4_0-STOCK':              5.76,
#          'Weapon_SRM_SRM6_0-STOCK':              8.69}

# 0.89, 1.125 multiplier
# BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       81.11,
#            'Weapon_Autocannon_AC5_0-STOCK':      113.79,
#            'Weapon_Autocannon_AC10_0-STOCK':     145.73,
#            'Weapon_Autocannon_AC20_0-STOCK':     163.47,
#            'Weapon_Flamer_Flamer_0-STOCK':         5.73,
#            'Weapon_Laser_LargeLaser_0-STOCK':    109.34,
#            'Weapon_Laser_MediumLaser_0-STOCK':    39.86,
#            'Weapon_Laser_SmallLaser_0-STOCK':     10.53,
#            'Weapon_LRM_LRM5_0-STOCK':             60.68,
#            'Weapon_LRM_LRM10_0-STOCK':           122.97,
#            'Weapon_LRM_LRM15_0-STOCK':           186.78,
#            'Weapon_LRM_LRM20_0-STOCK':           252.11,
#            'Weapon_MachineGun_MachineGun_0-STOCK': 5.73,
#            'Weapon_PPC_PPC_0-STOCK':             181.34,
#            'Weapon_SRM_SRM2_0-STOCK':             22.61,
#            'Weapon_SRM_SRM4_0-STOCK':             45.53,
#            'Weapon_SRM_SRM6_0-STOCK':             68.79}
#
## ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':       10.14,
#          'Weapon_Autocannon_AC5_0-STOCK':       14.22,
#          'Weapon_Autocannon_AC10_0-STOCK':      18.22,
#          'Weapon_Autocannon_AC20_0-STOCK':      20.43,
#          'Weapon_Flamer_Flamer_0-STOCK':         0.72,
#          'Weapon_LRM_LRM5_0-STOCK':              7.59,
#          'Weapon_LRM_LRM10_0-STOCK':            15.37,
#          'Weapon_LRM_LRM15_0-STOCK':            23.35,
#          'Weapon_LRM_LRM20_0-STOCK':            31.51,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 0.72,
#          'Weapon_SRM_SRM2_0-STOCK':              2.83,
#          'Weapon_SRM_SRM4_0-STOCK':              5.69,
#          'Weapon_SRM_SRM6_0-STOCK':              8.60}

# 0.88, 1.1 multiplier
## BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       80.20,
#            'Weapon_Autocannon_AC5_0-STOCK':      112.51,
#            'Weapon_Autocannon_AC10_0-STOCK':     144.09,
#            'Weapon_Autocannon_AC20_0-STOCK':     161.63,
#            'Weapon_Flamer_Flamer_0-STOCK':         5.67,
#            'Weapon_Laser_LargeLaser_0-STOCK':    108.11,
#            'Weapon_Laser_MediumLaser_0-STOCK':    39.41,
#            'Weapon_Laser_SmallLaser_0-STOCK':     10.41,
#            'Weapon_LRM_LRM5_0-STOCK':             60.00,
#            'Weapon_LRM_LRM10_0-STOCK':           121.58,
#            'Weapon_LRM_LRM15_0-STOCK':           184.68,
#            'Weapon_LRM_LRM20_0-STOCK':           249.28,
#            'Weapon_MachineGun_MachineGun_0-STOCK': 5.67,
#            'Weapon_PPC_PPC_0-STOCK':             179.30,
#            'Weapon_SRM_SRM2_0-STOCK':             22.36,
#            'Weapon_SRM_SRM4_0-STOCK':             45.02,
#            'Weapon_SRM_SRM6_0-STOCK':             68.01}
#
## ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':       10.03,
#          'Weapon_Autocannon_AC5_0-STOCK':       14.06,
#          'Weapon_Autocannon_AC10_0-STOCK':      18.01,
#          'Weapon_Autocannon_AC20_0-STOCK':      20.20,
#          'Weapon_Flamer_Flamer_0-STOCK':         0.71,
#          'Weapon_LRM_LRM5_0-STOCK':              7.50,
#          'Weapon_LRM_LRM10_0-STOCK':            15.20,
#          'Weapon_LRM_LRM15_0-STOCK':            23.09,
#          'Weapon_LRM_LRM20_0-STOCK':            31.16,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 0.71,
#          'Weapon_SRM_SRM2_0-STOCK':              2.79,
#          'Weapon_SRM_SRM4_0-STOCK':              5.63,
#          'Weapon_SRM_SRM6_0-STOCK':              8.50}

# 0.85, 1.06 multiplier
## BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       77.47,
#            'Weapon_Autocannon_AC5_0-STOCK':      108.68,
#            'Weapon_Autocannon_AC10_0-STOCK':     139.18,
#            'Weapon_Autocannon_AC20_0-STOCK':     156.12,
#            'Weapon_Flamer_Flamer_0-STOCK':         5.47,
#            'Weapon_Laser_LargeLaser_0-STOCK':    104.42,
#            'Weapon_Laser_MediumLaser_0-STOCK':    38.07,
#            'Weapon_Laser_SmallLaser_0-STOCK':     10.06,
#            'Weapon_LRM_LRM5_0-STOCK':             57.95,
#            'Weapon_LRM_LRM10_0-STOCK':           117.44,
#            'Weapon_LRM_LRM15_0-STOCK':           178.38,
#            'Weapon_LRM_LRM20_0-STOCK':           240.78,
#            'Weapon_MachineGun_MachineGun_0-STOCK': 5.47,
#            'Weapon_PPC_PPC_0-STOCK':             173.19,
#            'Weapon_SRM_SRM2_0-STOCK':             21.59,
#            'Weapon_SRM_SRM4_0-STOCK':             43.48,
#            'Weapon_SRM_SRM6_0-STOCK':             65.69}
#
## ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':        9.68,
#          'Weapon_Autocannon_AC5_0-STOCK':       13.58,
#          'Weapon_Autocannon_AC10_0-STOCK':      17.40,
#          'Weapon_Autocannon_AC20_0-STOCK':      19.52,
#          'Weapon_Flamer_Flamer_0-STOCK':         0.68,
#          'Weapon_LRM_LRM5_0-STOCK':              7.24,
#          'Weapon_LRM_LRM10_0-STOCK':            14.68,
#          'Weapon_LRM_LRM15_0-STOCK':            22.30,
#          'Weapon_LRM_LRM20_0-STOCK':            30.10,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 0.68,
#          'Weapon_SRM_SRM2_0-STOCK':              2.70,
#          'Weapon_SRM_SRM4_0-STOCK':              5.44,
#          'Weapon_SRM_SRM6_0-STOCK':              8.21}

# 0.84, 1.05 multiplier
## BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       76.56,
#            'Weapon_Autocannon_AC5_0-STOCK':      107.40,
#            'Weapon_Autocannon_AC10_0-STOCK':     137.54,
#            'Weapon_Autocannon_AC20_0-STOCK':     154.29,
#            'Weapon_Flamer_Flamer_0-STOCK':         5.41,
#            'Weapon_Laser_LargeLaser_0-STOCK':    103.19,
#            'Weapon_Laser_MediumLaser_0-STOCK':    37.62,
#            'Weapon_Laser_SmallLaser_0-STOCK':      9.94,
#            'Weapon_LRM_LRM5_0-STOCK':             57.27,
#            'Weapon_LRM_LRM10_0-STOCK':           116.06,
#            'Weapon_LRM_LRM15_0-STOCK':           176.29,
#            'Weapon_LRM_LRM20_0-STOCK':           237.95,
#            'Weapon_MachineGun_MachineGun_0-STOCK': 5.41,
#            'Weapon_PPC_PPC_0-STOCK':             171.15,
#            'Weapon_SRM_SRM2_0-STOCK':             21.34,
#            'Weapon_SRM_SRM4_0-STOCK':             42.97,
#            'Weapon_SRM_SRM6_0-STOCK':             64.92}
#
## ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':        9.57,
#          'Weapon_Autocannon_AC5_0-STOCK':       13.42,
#          'Weapon_Autocannon_AC10_0-STOCK':      17.19,
#          'Weapon_Autocannon_AC20_0-STOCK':      19.29,
#          'Weapon_Flamer_Flamer_0-STOCK':         0.68,
#          'Weapon_LRM_LRM5_0-STOCK':              7.16,
#          'Weapon_LRM_LRM10_0-STOCK':            14.51,
#          'Weapon_LRM_LRM15_0-STOCK':            22.04,
#          'Weapon_LRM_LRM20_0-STOCK':            29.74,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 0.68,
#          'Weapon_SRM_SRM2_0-STOCK':              2.67,
#          'Weapon_SRM_SRM4_0-STOCK':              5.37,
#          'Weapon_SRM_SRM6_0-STOCK':              8.12}

# 0.83, 1.04 multiplier
## BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       75.65,
#            'Weapon_Autocannon_AC5_0-STOCK':      106.12,
#            'Weapon_Autocannon_AC10_0-STOCK':     135.90,
#            'Weapon_Autocannon_AC20_0-STOCK':     152.45,
#            'Weapon_Flamer_Flamer_0-STOCK':         5.34,
#            'Weapon_Laser_LargeLaser_0-STOCK':    101.97,
#            'Weapon_Laser_MediumLaser_0-STOCK':    37.17,
#            'Weapon_Laser_SmallLaser_0-STOCK':      9.82,
#            'Weapon_LRM_LRM5_0-STOCK':             56.59,
#            'Weapon_LRM_LRM10_0-STOCK':           114.28,
#            'Weapon_LRM_LRM15_0-STOCK':           174.19,
#            'Weapon_LRM_LRM20_0-STOCK':           235.11,
#            'Weapon_MachineGun_MachineGun_0-STOCK': 5.35,
#            'Weapon_PPC_PPC_0-STOCK':             169.11,
#            'Weapon_SRM_SRM2_0-STOCK':             21.09,
#            'Weapon_SRM_SRM4_0-STOCK':             42.46,
#            'Weapon_SRM_SRM6_0-STOCK':             64.15}
#
## ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':        9.46,
#          'Weapon_Autocannon_AC5_0-STOCK':       13.27,
#          'Weapon_Autocannon_AC10_0-STOCK':      16.99,
#          'Weapon_Autocannon_AC20_0-STOCK':      19.06,
#          'Weapon_Flamer_Flamer_0-STOCK':         0.67,
#          'Weapon_LRM_LRM5_0-STOCK':              7.07,
#          'Weapon_LRM_LRM10_0-STOCK':            14.33,
#          'Weapon_LRM_LRM15_0-STOCK':            21.77,
#          'Weapon_LRM_LRM20_0-STOCK':            29.39,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 0.67,
#          'Weapon_SRM_SRM2_0-STOCK':              2.64,
#          'Weapon_SRM_SRM4_0-STOCK':              5.31,
#          'Weapon_SRM_SRM6_0-STOCK':              8.02}

# 0.825, 1.03125 multiplier
## BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       75.19,
#            'Weapon_Autocannon_AC5_0-STOCK':      105.48,
#            'Weapon_Autocannon_AC10_0-STOCK':     135.08,
#            'Weapon_Autocannon_AC20_0-STOCK':     151.53,
#            'Weapon_Flamer_Flamer_0-STOCK':         5.81,
#            'Weapon_Laser_LargeLaser_0-STOCK':    101.35,
#            'Weapon_Laser_MediumLaser_0-STOCK':    36.95,
#            'Weapon_Laser_SmallLaser_0-STOCK':     10.62,
#            'Weapon_LRM_LRM5_0-STOCK':             56.25,
#            'Weapon_LRM_LRM10_0-STOCK':           113.98,
#            'Weapon_LRM_LRM15_0-STOCK':           173.14,
#            'Weapon_LRM_LRM20_0-STOCK':           233.70,
#            'Weapon_MachineGun_MachineGun_0-STOCK': 5.81,
#            'Weapon_PPC_PPC_0-STOCK':             168.09,
#            'Weapon_SRM_SRM2_0-STOCK':             20.96,
#            'Weapon_SRM_SRM4_0-STOCK':             42.20,
#            'Weapon_SRM_SRM6_0-STOCK':             63.76}
#
## ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':        9.40,
#          'Weapon_Autocannon_AC5_0-STOCK':       13.19,
#          'Weapon_Autocannon_AC10_0-STOCK':      16.89,
#          'Weapon_Autocannon_AC20_0-STOCK':      18.94,
#          'Weapon_Flamer_Flamer_0-STOCK':         0.73,
#          'Weapon_LRM_LRM5_0-STOCK':              7.03,
#          'Weapon_LRM_LRM10_0-STOCK':            14.25,
#          'Weapon_LRM_LRM15_0-STOCK':            21.64,
#          'Weapon_LRM_LRM20_0-STOCK':            29.21,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 0.73,
#          'Weapon_SRM_SRM2_0-STOCK':              2.62,
#          'Weapon_SRM_SRM4_0-STOCK':              5.24,
#          'Weapon_SRM_SRM6_0-STOCK':              7.97}

# 0.82, 1.025 multiplier
## BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       74.73,
#            'Weapon_Autocannon_AC5_0-STOCK':      104.84,
#            'Weapon_Autocannon_AC10_0-STOCK':     134.26,
#            'Weapon_Autocannon_AC20_0-STOCK':     150.61,
#            'Weapon_Flamer_Flamer_0-STOCK':         5.78,
#            'Weapon_Laser_LargeLaser_0-STOCK':    100.74,
#            'Weapon_Laser_MediumLaser_0-STOCK':    36.73,
#            'Weapon_Laser_SmallLaser_0-STOCK':     10.55,
#            'Weapon_LRM_LRM5_0-STOCK':             55.91,
#            'Weapon_LRM_LRM10_0-STOCK':           113.29,
#            'Weapon_LRM_LRM15_0-STOCK':           172.09,
#            'Weapon_LRM_LRM20_0-STOCK':           232.28,
#            'Weapon_MachineGun_MachineGun_0-STOCK': 5.78,
#            'Weapon_PPC_PPC_0-STOCK':             167.07,
#            'Weapon_SRM_SRM2_0-STOCK':             20.83,
#            'Weapon_SRM_SRM4_0-STOCK':             41.95,
#            'Weapon_SRM_SRM6_0-STOCK':             63.38}
#
## ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':        9.34,
#          'Weapon_Autocannon_AC5_0-STOCK':       13.11,
#          'Weapon_Autocannon_AC10_0-STOCK':      16.78,
#          'Weapon_Autocannon_AC20_0-STOCK':      18.83,
#          'Weapon_Flamer_Flamer_0-STOCK':         0.72,
#          'Weapon_LRM_LRM5_0-STOCK':              6.99,
#          'Weapon_LRM_LRM10_0-STOCK':            14.16,
#          'Weapon_LRM_LRM15_0-STOCK':            21.51,
#          'Weapon_LRM_LRM20_0-STOCK':            29.03,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 0.72,
#          'Weapon_SRM_SRM2_0-STOCK':              2.60,
#          'Weapon_SRM_SRM4_0-STOCK':              5.24,
#          'Weapon_SRM_SRM6_0-STOCK':              7.92}

# 0.81, 1.0125 multiplier
## BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       73.82,
#            'Weapon_Autocannon_AC5_0-STOCK':      103.56,
#            'Weapon_Autocannon_AC10_0-STOCK':     132.63,
#            'Weapon_Autocannon_AC20_0-STOCK':     148.78,
#            'Weapon_Flamer_Flamer_0-STOCK':         5.71,
#            'Weapon_Laser_LargeLaser_0-STOCK':     99.51,
#            'Weapon_Laser_MediumLaser_0-STOCK':    36.28,
#            'Weapon_Laser_SmallLaser_0-STOCK':     10.42,
#            'Weapon_LRM_LRM5_0-STOCK':             55.23,
#            'Weapon_LRM_LRM10_0-STOCK':           111.91,
#            'Weapon_LRM_LRM15_0-STOCK':           169.99,
#            'Weapon_LRM_LRM20_0-STOCK':           229.45,
#            'Weapon_MachineGun_MachineGun_0-STOCK': 5.71,
#            'Weapon_PPC_PPC_0-STOCK':             165.04,
#            'Weapon_SRM_SRM2_0-STOCK':             20.58,
#            'Weapon_SRM_SRM4_0-STOCK':             41.44,
#            'Weapon_SRM_SRM6_0-STOCK':             62.60}
#
## ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':        9.23,
#          'Weapon_Autocannon_AC5_0-STOCK':       12.95,
#          'Weapon_Autocannon_AC10_0-STOCK':      16.58,
#          'Weapon_Autocannon_AC20_0-STOCK':      18.60,
#          'Weapon_Flamer_Flamer_0-STOCK':         0.71,
#          'Weapon_LRM_LRM5_0-STOCK':              6.90,
#          'Weapon_LRM_LRM10_0-STOCK':            13.99,
#          'Weapon_LRM_LRM15_0-STOCK':            21.25,
#          'Weapon_LRM_LRM20_0-STOCK':            28.68,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 0.71,
#          'Weapon_SRM_SRM2_0-STOCK':              2.57,
#          'Weapon_SRM_SRM4_0-STOCK':              5.18,
#          'Weapon_SRM_SRM6_0-STOCK':              7.83}

# 0.8, 1.00 multiplier
## BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       72.91,
#            'Weapon_Autocannon_AC5_0-STOCK':      102.29,
#            'Weapon_Autocannon_AC10_0-STOCK':     130.99,
#            'Weapon_Autocannon_AC20_0-STOCK':     146.94,
#            'Weapon_Flamer_Flamer_0-STOCK':         5.15,
#            'Weapon_Laser_LargeLaser_0-STOCK':     98.28,
#            'Weapon_Laser_MediumLaser_0-STOCK':    35.83,
#            'Weapon_Laser_SmallLaser_0-STOCK':      9.46,
#            'Weapon_LRM_LRM5_0-STOCK':             54.55,
#            'Weapon_LRM_LRM10_0-STOCK':           110.53,
#            'Weapon_LRM_LRM15_0-STOCK':           167.89,
#            'Weapon_LRM_LRM20_0-STOCK':           226.61,
#            'Weapon_MachineGun_MachineGun_0-STOCK': 5.15,
#            'Weapon_PPC_PPC_0-STOCK':             163.00,
#            'Weapon_SRM_SRM2_0-STOCK':             20.32,
#            'Weapon_SRM_SRM4_0-STOCK':             40.93,
#            'Weapon_SRM_SRM6_0-STOCK':             61.83}
#
## ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':        9.11,
#          'Weapon_Autocannon_AC5_0-STOCK':       12.79,
#          'Weapon_Autocannon_AC10_0-STOCK':      16.37,
#          'Weapon_Autocannon_AC20_0-STOCK':      18.37,
#          'Weapon_Flamer_Flamer_0-STOCK':         0.64,
#          'Weapon_LRM_LRM5_0-STOCK':              6.82,
#          'Weapon_LRM_LRM10_0-STOCK':            13.82,
#          'Weapon_LRM_LRM15_0-STOCK':            20.99,
#          'Weapon_LRM_LRM20_0-STOCK':            28.33,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 0.64,
#          'Weapon_SRM_SRM2_0-STOCK':              2.54,
#          'Weapon_SRM_SRM4_0-STOCK':              5.12,
#          'Weapon_SRM_SRM6_0-STOCK':              7.73}

# 2.52, 3.15 multiplier
## alt BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       57.42,
#            'Weapon_Autocannon_AC5_0-STOCK':       93.01,
#            'Weapon_Autocannon_AC10_0-STOCK':     130.48,
#            'Weapon_Autocannon_AC20_0-STOCK':     188.96,
#            'Weapon_Flamer_Flamer_0-STOCK':        10.25,
#            'Weapon_Laser_LargeLaser_0-STOCK':     97.90,
#            'Weapon_Laser_MediumLaser_0-STOCK':    46.08,
#            'Weapon_Laser_SmallLaser_0-STOCK':     18.72,
#            'Weapon_LRM_LRM5_0-STOCK':             45.92,
#            'Weapon_LRM_LRM10_0-STOCK':            93.05,
#            'Weapon_LRM_LRM15_0-STOCK':           141.34,
#            'Weapon_LRM_LRM20_0-STOCK':           190.78,
#            'Weapon_MachineGun_MachineGun_0-STOCK':10.25,
#            'Weapon_PPC_PPC_0-STOCK':             148.22,
#            'Weapon_SRM_SRM2_0-STOCK':             26.14,
#            'Weapon_SRM_SRM4_0-STOCK':             52.63,
#            'Weapon_SRM_SRM6_0-STOCK':             79.51}
#
## alt ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':        7.18,
#          'Weapon_Autocannon_AC5_0-STOCK':       11.63,
#          'Weapon_Autocannon_AC10_0-STOCK':      16.31,
#          'Weapon_Autocannon_AC20_0-STOCK':      23.62,
#          'Weapon_Flamer_Flamer_0-STOCK':         1.28,
#          'Weapon_LRM_LRM5_0-STOCK':              5.74,
#          'Weapon_LRM_LRM10_0-STOCK':            11.63,
#          'Weapon_LRM_LRM15_0-STOCK':            17.67,
#          'Weapon_LRM_LRM20_0-STOCK':            23.85,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 1.28,
#          'Weapon_SRM_SRM2_0-STOCK':              3.27,
#          'Weapon_SRM_SRM4_0-STOCK':              6.58,
#          'Weapon_SRM_SRM6_0-STOCK':              9.94}

# 2.48, 3.10 multiplier
## alt BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       56.51,
#            'Weapon_Autocannon_AC5_0-STOCK':       91.53,
#            'Weapon_Autocannon_AC10_0-STOCK':     128.41,
#            'Weapon_Autocannon_AC20_0-STOCK':     185.96,
#            'Weapon_Flamer_Flamer_0-STOCK':        10.09,
#            'Weapon_Laser_LargeLaser_0-STOCK':     96.34,
#            'Weapon_Laser_MediumLaser_0-STOCK':    45.35,
#            'Weapon_Laser_SmallLaser_0-STOCK':     18.43,
#            'Weapon_LRM_LRM5_0-STOCK':             45.19,
#            'Weapon_LRM_LRM10_0-STOCK':            91.58,
#            'Weapon_LRM_LRM15_0-STOCK':           139.10,
#            'Weapon_LRM_LRM20_0-STOCK':           187.75,
#            'Weapon_MachineGun_MachineGun_0-STOCK':10.09,
#            'Weapon_PPC_PPC_0-STOCK':             145.87,
#            'Weapon_SRM_SRM2_0-STOCK':             25.72,
#            'Weapon_SRM_SRM4_0-STOCK':             51.79,
#            'Weapon_SRM_SRM6_0-STOCK':             78.25}
#
## alt ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':        7.06,
#          'Weapon_Autocannon_AC5_0-STOCK':       11.44,
#          'Weapon_Autocannon_AC10_0-STOCK':      16.05,
#          'Weapon_Autocannon_AC20_0-STOCK':      23.25,
#          'Weapon_Flamer_Flamer_0-STOCK':         1.26,
#          'Weapon_LRM_LRM5_0-STOCK':              5.65,
#          'Weapon_LRM_LRM10_0-STOCK':            11.45,
#          'Weapon_LRM_LRM15_0-STOCK':            17.39,
#          'Weapon_LRM_LRM20_0-STOCK':            23.47,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 1.26,
#          'Weapon_SRM_SRM2_0-STOCK':              3.22,
#          'Weapon_SRM_SRM4_0-STOCK':              6.47,
#          'Weapon_SRM_SRM6_0-STOCK':              9.78}

# 2.44, 3.05 multiplier
## alt BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       55.60,
#            'Weapon_Autocannon_AC5_0-STOCK':       90.06,
#            'Weapon_Autocannon_AC10_0-STOCK':     126.34,
#            'Weapon_Autocannon_AC20_0-STOCK':     182.96,
#            'Weapon_Flamer_Flamer_0-STOCK':         9.92,
#            'Weapon_Laser_LargeLaser_0-STOCK':     94.79,
#            'Weapon_Laser_MediumLaser_0-STOCK':    44.62,
#            'Weapon_Laser_SmallLaser_0-STOCK':     18.13,
#            'Weapon_LRM_LRM5_0-STOCK':             44.46,
#            'Weapon_LRM_LRM10_0-STOCK':            90.10,
#            'Weapon_LRM_LRM15_0-STOCK':           136.86,
#            'Weapon_LRM_LRM20_0-STOCK':           184.72,
#            'Weapon_MachineGun_MachineGun_0-STOCK': 9.92,
#            'Weapon_PPC_PPC_0-STOCK':             143.51,
#            'Weapon_SRM_SRM2_0-STOCK':             25.31,
#            'Weapon_SRM_SRM4_0-STOCK':             50.96,
#            'Weapon_SRM_SRM6_0-STOCK':             76.99}
#
## alt ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':        6.95,
#          'Weapon_Autocannon_AC5_0-STOCK':       11.26,
#          'Weapon_Autocannon_AC10_0-STOCK':      15.79,
#          'Weapon_Autocannon_AC20_0-STOCK':      22.87,
#          'Weapon_Flamer_Flamer_0-STOCK':         1.24,
#          'Weapon_LRM_LRM5_0-STOCK':              5.56,
#          'Weapon_LRM_LRM10_0-STOCK':            11.26,
#          'Weapon_LRM_LRM15_0-STOCK':            17.11,
#          'Weapon_LRM_LRM20_0-STOCK':            23.09,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 1.24,
#          'Weapon_SRM_SRM2_0-STOCK':              3.16,
#          'Weapon_SRM_SRM4_0-STOCK':              6.37,
#          'Weapon_SRM_SRM6_0-STOCK':              9.62}

# 2.4, 3.00 multiplier
## alt BV of weapon
#weaponBV = {'Weapon_Autocannon_AC2_0-STOCK':       54.68,
#            'Weapon_Autocannon_AC5_0-STOCK':       88.58,
#            'Weapon_Autocannon_AC10_0-STOCK':     124.96,
#            'Weapon_Autocannon_AC20_0-STOCK':     179.96,
#            'Weapon_Flamer_Flamer_0-STOCK':         9.76,
#            'Weapon_Laser_LargeLaser_0-STOCK':     93.24,
#            'Weapon_Laser_MediumLaser_0-STOCK':    43.88,
#            'Weapon_Laser_SmallLaser_0-STOCK':     17.83,
#            'Weapon_LRM_LRM5_0-STOCK':             43.73,
#            'Weapon_LRM_LRM10_0-STOCK':            88.62,
#            'Weapon_LRM_LRM15_0-STOCK':           134.61,
#            'Weapon_LRM_LRM20_0-STOCK':           181.70,
#            'Weapon_MachineGun_MachineGun_0-STOCK': 9.76,
#            'Weapon_PPC_PPC_0-STOCK':             141.16,
#            'Weapon_SRM_SRM2_0-STOCK':             24.89,
#            'Weapon_SRM_SRM4_0-STOCK':             50.12,
#            'Weapon_SRM_SRM6_0-STOCK':             75.73}
#
## alt ammo BV of weapon
#ammoBV = {'Weapon_Autocannon_AC2_0-STOCK':        6.84,
#          'Weapon_Autocannon_AC5_0-STOCK':       11.07,
#          'Weapon_Autocannon_AC10_0-STOCK':      15.53,
#          'Weapon_Autocannon_AC20_0-STOCK':      22.50,
#          'Weapon_Flamer_Flamer_0-STOCK':         1.22,
#          'Weapon_LRM_LRM5_0-STOCK':              5.47,
#          'Weapon_LRM_LRM10_0-STOCK':            11.08,
#          'Weapon_LRM_LRM15_0-STOCK':            16.83,
#          'Weapon_LRM_LRM20_0-STOCK':            22.71,
#          'Weapon_MachineGun_MachineGun_0-STOCK': 1.22,
#          'Weapon_SRM_SRM2_0-STOCK':              3.11,
#          'Weapon_SRM_SRM4_0-STOCK':              6.27,
#          'Weapon_SRM_SRM6_0-STOCK':              9.47}
