import json

md = open("../../_includes/autodocs/help.md", "w")

md.write(open("../help.txt","r").read())