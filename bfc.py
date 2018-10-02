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
cppcode += "vector<int> cells {0};\n"
cppcode += "int v=0;"
for c in bfcode:
    if c == "-":
        cppcode += "cells[v]--;"
    elif c == "+":
        cppcode += "cells[v]++;"
    elif c == ">":
        cppcode += "v++;if(v>=cells.size())cells.push_back(0);"
    elif c == "<":
        cppcode += "v--;if(v<0)v++;"
    elif c == ",":
        cppcode += "scanf(\"%d\",&cells[v]);"
    elif c == ".":
        cppcode += "printf(\"%d\\n\",cells[v]);"
    elif c == "[":
        cppcode += "while(cells[v]!=0){"
    elif c == "]":
        cppcode += "}"

cppcode += "}"
infile.close()
outf = open(outname,"w")
outf.write(cppcode)
outf.close()
os.system("g++ -O2 "+outname+" -o "+outname.replace(".cpp",""))
