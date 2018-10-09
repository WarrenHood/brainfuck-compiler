import sys
import os
def usage():
    print("usage: bfc.py input_file [output_file]")
if len(sys.argv) < 2:
    usage()
    sys.exit(0)
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
c_ind = 0
while c_ind < len(bfcode):
    current_count = 1
    while c_ind+1 < len(bfcode) and bfcode[c_ind]==bfcode[c_ind+1] and bfcode[c_ind] in ["+","-",">","<"]:
        c_ind += 1
        current_count += 1
    c = bfcode[c_ind]
    if c == "-":
        if current_count == 1:
            cppcode += "cells[v]--;\n"
        else:
            cppcode += "cells[v]-="+str(current_count)+";\n"
    elif c == "+":
        if current_count == 1:
            cppcode += "cells[v]++;\n"
        else:
            cppcode += "cells[v]+="+str(current_count)+";\n"
    elif c == ">":
        if current_count == 1:
            cppcode += "v++;if(v>=cells.size())cells.push_back(0);\n"
        else:
            cppcode += "v+="+str(current_count)+";\nwhile(v>=cells.size())cells.push_back(0);\n"
    elif c == "<":
        if current_count == 1:
            cppcode += "v--;if(v<0)v=0;\n"
        else:
            cppcode += "v-="+str(current_count)+";if(v<0)v=0;\n"
    elif c == ",":
        cppcode += "scanf(\"%d\",&cells[v]);\n"
    elif c == ".":
        cppcode += "printf(\"%c\",cells[v]);\n"
    elif c == "[":
        cppcode += "while(cells[v]>0){\n"
    elif c == "]":
        cppcode += "}\n"
    c_ind += 1
cppcode += "}"
infile.close()
outf = open(outname,"w")
outf.write(cppcode)
outf.close()
os.system("g++ --std=c++17 "+outname+" -o "+outname.replace(".cpp",""))
