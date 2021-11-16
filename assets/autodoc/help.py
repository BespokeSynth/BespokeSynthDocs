import json

html = open("../../_includes/help.md", "w")

html.write(open("../resource/help.txt","r").read())