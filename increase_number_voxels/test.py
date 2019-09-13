
import time
from xlwt import Workbook
import os

wb = Workbook()
sheet = wb.add_sheet("times")


start = time.time()
os.system("gsvit test.par")
stop = time.time()

sheet.write(1,0,"increased voxel size")
sheet.write(1,1,(stop-start)/60)


wb.save("test_results.xls")

