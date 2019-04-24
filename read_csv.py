# coding: utf-8
"""
之前一直都是拿pd.read_csv() 来读csv的, 但是根据时间和内存计算, 这个方法特别不好.
想来也是, 毕竟要先 init 一个 class.
因此考虑使用 csv 这个库.
1. csv_reader return: generator
"""

import csv
import time
import sys

CSV_PATH = 'E:\PyLearn\data\small_fts.csv'
# <editor-fold desc="csv.reader">
start = time.clock()
with open(CSV_PATH, 'r') as f:
    reader = csv.reader(f)
    # 这里的reader是一个 generator, 所以一旦关闭 file, 就会 I/O error.
print(time.clock() - start) # 0.0003039
# </editor-fold>

start = time.clock()
with open(CSV_PATH, 'r')  as f:
    reader = csv.DictReader(f)
    # 这里的reader是一个 generator, 所以一旦关闭 file, 就会 I/O error.
print(time.clock() - start) # 0.0001742

