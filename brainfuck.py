import sys
import os
def usage():
    print("usage: brainfuck.py input_file [output_file]")
if len(sys.argv) < 2:
    usage()
infile = open(sys.argv[1],"r")
outname = sys.argv[1].replace(".bf",".cpp")
if len(sys.argv) == 3:
    outname = sys.argv[2]
bfcode = infile.read()
bfcode = "".join([c for c in bfcode if c in "+-<>,.[]"])
cppcode = "#include <iostream>\n#include <vector>\n"
cppcode += "using namespace std;\n"
cppcode += "int main(void){\n"
cppcode += "vector<int> cells {0};\n"
cppcode += "int v=0;char c;vector<int> cstack;bool ignore = false;int ic=0;int nx;"
cppcode += "char bfc[] = \""+bfcode+"\\0\";\n"
cppcode += "for(int ind=0;bfc[ind] != '\\0';ind++){\n"
cppcode += "c = bfc[ind];"
cppcode += "if(ic==0){if(c == '+')cells[v]++;"
cppcode += "else if(c == '-')cells[v]--;"
cppcode += "else if(c == '<')v--;if(v<0)v++;"
cppcode += "else if(c == '>')v++;if(v>=cells.size())cells.push_back(0);"
cppcode += "else if(c == ',')scanf(\"%d\",&cells[v]);"
cppcode += "else if(c == '.')printf(\"%d\\n\",cells[v]);};"
cppcode += "if(c == '['){cstack.push_back(ind);if(cells[v]==0||ic>0)ic++; }"
cppcode += "else if(c == ']'){if(cstack.size()>0)nx=cstack[cstack.size()-1];cstack.pop_back();if(ic>0)ic--;;if(cells[v]>0)ind=nx-1;};"
cppcode += "};"
cppcode += "}"
infile.close()
outf = open(outname,"w")
outf.write(cppcode)
outf.close()
os.system("g++ -O2 "+outname+" -o "+outname.replace(".cpp",""))
