import os

#Creates a json file from the cleaned svgs

json = '{\n'
for filename in os.listdir('../svg/cleaned/'):
  name = filename.split('.')[0]
  svg = open('../svg/cleaned/' + filename, 'r').read()
  svg = svg.replace('"', '\\"')
  svg = svg.replace('\'', '\\\'')
  json += '"' + name + '":"' + svg + '",\n'
json = json[:-2] + '}';

open('data/svgs.json', 'w').write(json)