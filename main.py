# /usr/bin/env python3
import os

# Relative position of the photo
dirPath = r"./image"

# location of bionic.xml
edit_file=open("./contest/bionic.xml", "w")

# Read the absolute path of main.py
SaveDirectory = os.getcwd()

# Find all photo files in the image folder
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]

str_0 = '''<background>
  <starttime>
    <year>2009</year>
    <month>08</month>
    <day>04</day>
    <hour>00</hour>
    <minute>00</minute>
    <second>00</second>
  </starttime>
<!-- This animation will start at midnight. -->\n'''
str_1 = "  <static>\n"
str_2 = "    <duration>1795.0</duration>\n"
str_3 = "  </static>\n"
str_4 = "  <transition>\n"
str_5 = "    <duration>5.0</duration>\n"
str_6 = "  </transition>\n"

edit_file.write(str_0)
for x in range(0, len(result)-1):  # len(result)
    edit_file.write(str_1), edit_file.write(str_2)
    edit_file.write("    <file>%s/image/%s</file>\n" %(SaveDirectory, result[x]))
    edit_file.write(str_3), edit_file.write(str_4), edit_file.write(str_5)
    edit_file.write("    <from>%s/image/%s</from>\n" %(SaveDirectory, result[x]))
    edit_file.write("    <to>%s/image/%s</to>\n" %(SaveDirectory, result[x+1]))
    edit_file.write(str_6)

edit_file.write(str_1), edit_file.write(str_2)
edit_file.write("    <file>%s/image/%s</file>\n" %(SaveDirectory, result[len(result)-1]))
edit_file.write(str_3), edit_file.write(str_4), edit_file.write(str_5)
edit_file.write("    <from>%s/image/%s</from>\n" %(SaveDirectory, result[len(result)-1]))
edit_file.write("    <to>%s/image/%s</to>\n" %(SaveDirectory, result[0]))
edit_file.write(str_6), edit_file.write("</background>")

edit_file.close()
