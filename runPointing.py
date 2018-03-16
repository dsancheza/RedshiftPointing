#!/usr/bin/env python


import sys
from RSRRunPointing import RSRRunPointing
from rsrFileSearch import rsrFileSearch
from rsrFileSearch import rsrFileSearchAll
from vlbi1mmFileSearch import vlbi1mmFileSearchAll
from lmtTpmFileSearch import lmtTpmFileSearchAll

argv = ["-d", "2014-08-20", "-s", "101000003", "--show", "True"]
argv = ["-d", "2014-03-03", "-s", "16887", "--show", "True"]
argv = ["-d", "2014-11-01", "-s", "27064", "--show", "True"]
argv = ["-d", "2015-03-01", "-s", "37603", "--show", "True", "--chassis", "[0]"]
argv = ["-d", "2015-03-02", "-s", "37668", "--show", "True", "--throw" , "0", "--chassis", "[0]", "--board", "[0,1]", "--beam", "0"]
argv = ["-d", "2015-03-18", "-s", "38496", "--show", "True"]
argv = ["-d", "2016-02-16", "-s", "10056830", "--show", "True"]
argv = ["-d", "2018-02-27", "-s", "73014", "--chassis", "[1,2,3]", "--show", "True"]

root = "/data_lmt"
filelist = []

try:
    if sys.argv[1][0] == 'v':
        obsnum = 70868 #70880
        chassis = [0]
        board = [i for i in range(10)]
        #board = [0,1,2,3]
        filelist = vlbi1mmFileSearchAll (obsnum, root, full = True)
    elif sys.argv[1][0] == 'l':
        print 'LmtTpm'
        obsnum = 102663
        obsnum = 73677
        chassis = [0]
        board = [i for i in range(1)]
        filelist = lmtTpmFileSearchAll (obsnum, root, full = True)
except Exception as e:
    obsnum = 73014
    chassis = [1,2,3]
    board = [0,1,2,3,4,5]
    filelist = rsrFileSearchAll(obsnum, root, full = True)
    pass


argv = ["-d", " ", "-s", str(obsnum), "--chassis", str(chassis), "--board", str(board), "--show", "True"]

rsr = RSRRunPointing()
F = rsr.run(argv, filelist)
#F = rsr.run(argv)
print ('Average Pointing:      %5.1f %5.1f    %5.1f %5.1f    %5.1f %5.1f            %5.1f %5.1f' % 
       (F.mean_az_map_offset,
        F.mean_el_map_offset,
        F.mean_az_model_offset,
        F.mean_el_model_offset,
        F.mean_az_total_offset,
        F.mean_el_total_offset,
        F.mean_sep,
        F.mean_ang)
       )


raw_input("press any key to exit: ")
