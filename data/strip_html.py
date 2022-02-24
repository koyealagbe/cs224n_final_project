"""
strip_html.py()

Removes all html tags from a text file
"""

import sys
from os.path import exists
import re

if len(sys.argv) < 2:
  print("Usage: python strip_html.py file1.txt file2.txt ...")
  exit()

# Validate command line arguments
for arg in sys.argv[1:]:
  if not arg.endswith(".txt"):
    print("Usage: python strip_html.py file1.txt file2.txt ...")
    print("Can only strip .txt files")
    exit()
  if not exists(arg):
    print("File", arg, "not found in current directory")
    exit()

# All arguments valid

tags = [re.compile(r"<head>.*?</head>", re.DOTALL), re.compile(r"<!--.*?-->", re.DOTALL), re.compile(r"<!.*?>", re.DOTALL), "<b>", "</b>", "<pre>", "</pre>", "<html>", "</html>", "<script>", "</script>", "<title>", "</title>", "<u>", "</u>", re.compile(r"<p.*?>"), "</p>", re.compile(r"<table.*?>"), "</table>", re.compile(r"<tr.*?>"), "</tr>", re.compile(r"<td.*?>"), "</td>", re.compile(r"<ol.*?>"), "</ol>", re.compile(r"<ul.*?>"), "</ul>", re.compile(r"<li.*?>"), "</li>", re.compile(r"<body.*?>"), "</body>", re.compile(r"<font.*?>"), "</font>", re.compile(r"<style.*?>"), "</style>", re.compile(r"<div.*?>"), "</div>", re.compile(r"<a.*?>"), "</a>"]
for infilename in sys.argv[1:]:
  outfilename = infilename[:-4] + "-stripped.txt"
  #print(outfilename)
  infile = open(infilename, "r")
  infile_text = infile.read()
  infile.close()
  outfile = open(outfilename, "w+")
  outfile_text = infile_text
  
  # Remove all tags
  for tag in tags:
    outfile_text = re.sub(tag, "", outfile_text)

  outfile.write(outfile_text)
  outfile.close()
  