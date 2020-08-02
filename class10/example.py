import os
from os import path

content = """
exactly the same? ok.
"""
fileName = 'example.txt'
with open(fileName, 'w') as f:
    f.write(content)
    f.write("i think i can understand it now. i think.")
newContent = """
*insert monika speech here*
"""
with open(fileName, 'w') as f:
    f.write(newContent)

with open(fileName, 'a') as f:
    f.write("CANYOUHEARME")

with open(fileName) as f:
    fileContent = f.read()

print(fileContent)

if not path.exists('output'):
    os.makedirs('output')

with open('output/new.txt', 'w') as f:
    f.write('aaaaaaaaaaa')

htmlContent = """
<html>
    <a href="http://www.google.com" target = "blank">Link to Google.</a>
</html>
"""
with open('output/example.html', 'w') as f:
    f.write(htmlContent)

htmlContent2 = """
<html>
    <img src = "lemon.png" width="500" height="600">
</html>
"""
with open('output/example2.html', 'w') as f:
    f.write(htmlContent2)
