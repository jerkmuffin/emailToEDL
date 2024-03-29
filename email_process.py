#!/usr/bin/env python3
import re
import os
import sys
import eml_parser
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-m', dest='eml_file',
                        help='input file', required=True)
options = parser.parse_args()

if os.path.exists(options.eml_file):
    with open(options.eml_file, 'rb') as f:
        data = f.read()

#eml_file = '/Users/mschroffel/Desktop/EDL stuffs..eml'


parsed = eml_parser.eml_parser.decode_email_b(data, include_raw_body=True)

eml_text = parsed['body'][0]['content']

for line in eml_text.split('\n'):
    m = re.search("([\d]{2}:)??([\d]{2}:[\d]{2}:[\d]{2})(?!:)", line)
    if m:
        if m.groups()[0]:
            updated_stamp = m.groups()[0] + m.groups()[1]
        else:
            updated_stamp = "01:" + m.groups()[1]

        print("{}: **:::** {}".format(line, updated_stamp))
