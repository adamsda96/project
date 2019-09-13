from parGen import parGen
import time
from xlwt import Workbook
import os

wb = Workbook()
sheet = wb.add_sheet("times")

par = parGen("3e-01 3e-01 3e-01","1","material.mat","test_large_gpu.par")

par.generate()

start = time.time()
os.system("gsvit "+par.getName())
stop = time.time()

sheet.write(1,0,par.getName())
sheet.write(1,1,(stop-start)/60)
    

wb.save("test_large_results.xls")

