#!/usr/bin/python3

#this script written by devendra singh

import csv
import sys, os

class Inventgent:

     def __init__(self, filename=None, wfilename=None):
         if filename == None:
            raise ValueError("you haven't define filename")
         self.filename = filename
         self.wfilename = wfilename

     def readfile(self):
         with open(self.filename, encoding='cp1252') as csv_file:
              csv_reader = csv.DictReader(csv_file)
              for row in csv_reader:
        # print(row['Server'],"Des=",row['Server_Description'],"ow=",row['Owner'],"prod=",row['Production'])
                 yield('{} Des="{}" ow="{}" prod="{}"'.format(row['Server'],row['Server_Description'],row['Owner'],row['Production']))

     def writefile(self):
         with open(self.wfilename, 'w') as csv_file:
              for i in self.readfile():
                  csv_file.write(i + '\n')


# I am putting this block so that in Linux enviormt end user execute it directly via CLI by passing their server info file and new  inventory name
if len(sys.argv) == 3 and os.path.isfile(sys.argv[1]):
   info_csv = sys.argv[1]
   inv_file = sys.argv[2]
else:
   print ("you need to enter 2 arugements, 1st aurgument must be existing csv file and second arugment new inventory file name")
   sys.exit()

cc = Inventgent(info_csv, inv_file)
cc.writefile()


