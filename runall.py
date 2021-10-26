# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:59:25 2021

@author: PREDATOR
"""

import glob, os
for file in glob.glob("*.py"):
    if file != "runall.py":
        print(file)
        exec(open(file).read())
# 