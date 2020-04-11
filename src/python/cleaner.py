import os

#Compresses the svg files.

repList = [
  '<g>\n</g>',
  '<?xml version="1.0" encoding="iso-8859-1"?>',
  '<!-- Generator: Adobe Illustrator 19.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->',
  '\n'
]

for filename in os.listdir('svg'):
  file = open('svg/' + filename, 'r').read()
  for rep in repList:
    file = file.replace(rep, '')
  open('newsvg/' + filename, 'w').write(file)