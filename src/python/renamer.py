import re, os

# renames all the files to their iso codes

countries = open('data/countries.csv').read().split('\n')

svgs = os.listdir('svg')

for country in countries:
  parts = country.split(',')
  name = parts[0].lower()
  name = name.replace(' ', '-')
  code = parts[1].lower()
  for svg in svgs:
    if name in svg:
      try:
        os.rename('svg/' + svg, 'svg/' + code + '.svg')
      except:
        print('Error: ' + svg)