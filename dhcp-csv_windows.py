#!/usr/bin/python

import argparse
parser = argparse.ArgumentParser(description='DHCP Parser')
parser.add_argument('-i', '--input', help='Input File selection', required=1)
parser.add_argument('-o', '--output', help='Output File', required=1)
parser.add_argument('-f', '--filter', help='Target can be IP, MAC, or Hostname')
args = parser.parse_args()



infile = args.input
outputfile = args.output
filterobject = args.filter
if not filterobject:
	filterobject = ''
	
	
lookup = '''Description,IP Address,Host Name,MAC Address'''
copy_decision = 0


f2 = open(outputfile, 'w')
with open(infile) as f1:
	for line_number, line_value in enumerate(f1, 0):
		current_item_header = 0
		if lookup in line_value: 
			header_line_number = line_number-1 #Identifies what line the header row is
			copy_decision = 1
			current_item_header = 1
			f2.write(line_value)
		if copy_decision == 1:
			if current_item_header == 0:
				if filterobject in line_value:
					f2.write(line_value)
		end_line_number = line_number	

		
f1.close()
f2.close()

print '###############################################'
print '#              Script Info                     '
print '###############################################'
print '# Header found @ line : ', header_line_number
print '# Header String query : ', lookup
print '# User Query string   : ', filterobject
print '# Total lines in file : ', end_line_number 
print '# Dump line read      : ', line_value 
print '# Filename is         : ', infile 
print '# Output File         : ', outputfile
print '###############################################'
