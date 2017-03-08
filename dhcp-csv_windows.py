#!/usr/bin/python

import argparse
parser = argparse.ArgumentParser(description='DHCP Parser')
parser.add_argument('-i', '--input', help='Input File selection')
parser.add_argument('-o', '--output', help='Output File')
#parser.add_argument('-d', '--directory', help='Directory location')
args = parser.parse_args()



infile = args.input
outputfile = args.output
#destination = args.directory
lookup = '''Description,IP Address,Host Name,MAC Address'''
copy_decision = 0


f2 = open(outputfile, 'w')

with open(infile) as f1:
	for line_number, line_value in enumerate(f1, 0):
		if lookup in line_value: 
			header_line_number = line_number-1 #Identifies what line the header row is
			copy_decision = 1
		if copy_decision == 1:
			f2.write(line_value)
		end_line_number = line_number	

f1.close()
f2.close()

print 'Script Parameters'
print '###############'
print 'Header found at     : ', header_line_number
print 'Filename is         : ', infile 
print 'Search String       : ', lookup
print 'Total lines in file : ', end_line_number 
print 'Last line in file   : ', line_value 
print 'Output File         : ', outputfile
