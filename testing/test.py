from parGen import parGen
import time
from xlwt import Workbook
import os

wb = Workbook()
sheet = wb.add_sheet("times")

par_03_gpu = parGen("3e-07 3e-07 3e-07","1","material.mat","test_03_gpu.par")
par_3_gpu = parGen("3e-06 3e-06 3e-06","1","material.mat","test_3_gpu.par")
par_30_gpu = parGen("3e-05 3e-05 3e-05","1","material.mat","test_30_gpu.par")
par_03_cpu = parGen("3e-07 3e-07 3e-07","0","material.mat","test_03_cpu.par")
par_3_cpu = parGen("3e-06 3e-06 3e-06","0","material.mat","test_3_cpu.par")
par_30_cpu = parGen("3e-05 3e-05 3e-05","0","material.mat","test_30_cpu.par")

pars = [par_03_gpu,par_3_gpu,par_30_gpu,par_03_cpu,par_3_cpu,par_30_cpu]


i = 1
for par in pars:
    par.generate()

    start = time.time()
    os.system("gsvit "+par.getName())
    stop = time.time()

    sheet.write(i,0,par.getName())
    sheet.write(i,1,(stop-start)/60)
    
    i = i+1

wb.save("test_results.xls")

