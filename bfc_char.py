import sys
import os
def usage():
    print("usage: bfc.py input_file [output_file]")
if len(sys.argv) < 2:
    usage()
infile = open(sys.argv[1],"r")
outname = sys.argv[1].replace(".bf","")+".cpp"
if len(sys.argv) == 3:
    outname = sys.argv[2].replace(".cpp","")+".cpp"
bfcode = infile.read()
bfcode = "".join([c for c in bfcode if c in "+-<>,.[]"])
cppcode = "#include <iostream>\n#include <vector>\n"
cppcode += "using namespace std;\n"
cppcode += "int main(void){\n"
cppcode += "vector<char> cells {0};\n"
cppcode += "int v=0;"
for c in bfcode:
    if c == "-":
        cppcode += "cells[v]--;\n"
    elif c == "+":
        cppcode += "cells[v]++;\n"
    elif c == ">":
        cppcode += "v++;if(v>=cells.size())cells.push_back(0);\n"
    elif c == "<":
        cppcode += "v--;if(v<0)v++;\n"
    elif c == ",":
        cppcode += "scanf(\"%d\",&cells[v]);\n"
    elif c == ".":
        cppcode += "printf(\"%c\",cells[v]);\n"
    elif c == "[":
        cppcode += "while(cells[v]>0){\n"
    elif c == "]":
        cppcode += "}\n"

cppcode += "}"
infile.close()
outf = open(outname,"w")
outf.write(cppcode)
outf.close()
os.system("g++ --std=c++17 -O2 "+outname+" -o "+outname.replace(".cpp",""))
