#import csv
import pandas as pd
import numpy as np
with open('samplecsv.csv','r') as f:
    psteel=[]
    data = pd.read_csv(f)
    for item in data:
        if 'Steel' in f[1]:
            psteel.append(item[3])
