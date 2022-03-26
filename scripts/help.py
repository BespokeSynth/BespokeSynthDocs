import json

md = open("../_includes/help.md", "w")

md.write(open("help.txt","r").read())
