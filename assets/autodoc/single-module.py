import json

def getAcceptsInputsString(moduleInfo):
   ret = ""
   if "canReceivePulses" in moduleInfo:
      if moduleInfo["canReceivePulses"]:
         ret += "<font color=yellow>pulses</font> "
   if "canReceiveNote" in moduleInfo:
      if moduleInfo["canReceiveNote"]:
         ret += "<font color=orange>notes</font> "
   if "canReceiveAudio" in moduleInfo:
      if moduleInfo["canReceiveAudio"]:
         ret += "<font color=cyan>audio</font> "   
   if ret != "":
      ret = "accepts: "+ret
   return ret

documentation = json.load(open("../resource/module_documentation.json","r"))

moduleTypes = ["instruments","note effects","synths","audio effects","modulators","pulse","effect chain","other"]
modulesByType = {}
longestColumn = 0
for moduleName in documentation.keys():
   module = documentation[moduleName]
   if not module["type"] in modulesByType:
      modulesByType[module["type"]] = []
   modulesByType[module["type"]].append(moduleName)
   longestColumn = max(longestColumn, len(modulesByType[module["type"]]))
   md = open(f'../../modules/{module["type"]}/{moduleName}.md', 'w')
   md.write('''---
layout: page
title: '''f'{moduleName}''''
parent: '''f'{module["type"]}''''
grand_parent: modules
---
''')
   md.write('''
{% include modules/'''f'{module["type"]}/{moduleName}.md'''' %}
''')