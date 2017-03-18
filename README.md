# DHCP Log to CSV
The main purpose of this script is to convert windows DHCP logs into CSV. This is pretty simple as you just need to remove the top 30 or so lines from the file.

# How to use
usage: dhcp-csv_windows.py [-h] -i INPUT -o OUTPUT [-f FILTER]

DHCP Parser

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input File selection
  -o OUTPUT, --output OUTPUT
                        Output File
  -f FILTER, --filter FILTER
                        Target can be IP, MAC, or Hostname
