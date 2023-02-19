#!/usr/bin/env python3
from bs4 import BeautifulSoup
import glob

save = open('output.txt', 'w')
totals = 0
success = 0
def readdir( path ):
  return glob.glob( path )

def parse( file ):
  global totals, success
  html = open(file, 'r', encoding='big5', errors='replace').read()
  soup = BeautifulSoup(html, 'html.parser')
  msg_divs = soup.find_all('div', {'class': 'msg'})
  totals+=1
  try:
    question = msg_divs[0].text.replace('\n', ' ')
    answers = msg_divs[1].text.replace('\n', ' ')
    content = f"""Question:{question}
----------
Answer:{answers}
=========="""
    save.write( content )
    success+=1
  except:
    print( file, 'parse failed.' )
  print( f"Converted: {success}/{totals}" )
files = readdir('./raw_data/*')

for file in files:
  print( 'Current progress: ', file )
  parse( file )  
#parse(files[0])
# print(files)