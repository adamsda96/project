from parGen import parGen
import time
from xlwt import Workbook
import os

wb = Workbook()
sheet = wb.add_sheet("times")

dim = [240,270]

gpus = []
cpus = []
for i in dim:
    matFile = str(i) + "_material.mat"
    fileName = str(i) + "_test.par"
    outFile = str(i) + "_out.gwy"
    gpus.append(parGen(dim=i,matFile=matFile,fileName="gpu_"+fileName,outFile="gpu_"+outFile))
    #cpus.append(parGen(dim=i,matFile=matFile,fileName="cpu_"+fileName,outFile="cpu_"+outFile,gpu=0))

i = 16
for gpu in gpus:
    gpu.generate()

    start = time.time()
    os.system("gsvit "+gpu.getName())
    stop = time.time()

    sheet.write(i,0,gpu.getName())
    sheet.write(i,1,(stop-start)/60)
    wb.save("test_results.xls")
    i = i+1
    if (stop-start)/60/60>24:
        break

for cpu in cpus:
    cpu.generate()

    start = time.time()
    os.system("gsvit "+cpu.getName())
    stop = time.time()

    sheet.write(i,0,cpu.getName())
    sheet.write(i,1,(stop-start)/60)
    wb.save("test_results.xls")
    i = i+1
    if (stop-start)/60/60>24:
        break


wb.save("test_results.xls")

