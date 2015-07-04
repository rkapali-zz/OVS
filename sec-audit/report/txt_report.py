__author__ = 'sabin'

# class to make the txt format report

import datetime
import sys

now = datetime.datetime.now()
date_stamp = now.strftime("-%Y-%m-%d-%H-%M-%S")
filename = "audit_report_"
f_filename = filename + date_stamp + ".html"
newline = "\n"
# create new txt file
def create_txt_file():
    #with open(f_filename, 'a') as f:
    f = open(f_filename,'a')
    sys.stdout = f


#create_txt_file()
