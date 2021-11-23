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

documentation = json.load(open("../module_documentation.json","r"))

moduleTypes = ["instruments","note effects","synths","audio effects","modulators","pulse","effect chain","other"]
modulesByType = {}
longestColumn = 0
for moduleName in documentation.keys():
   module = documentation[moduleName]
   if not module["type"] in modulesByType:
      modulesByType[module["type"]] = []
   modulesByType[module["type"]].append(moduleName)
   longestColumn = max(longestColumn, len(modulesByType[module["type"]]))
   module["type"] = module["type"].replace(' ', '')
   md = open(f'../../_includes/autodocs/modules/{module["type"]}/{moduleName}.md', 'w')
   md.write('''
<a name='''f'{moduleName}''''></a><br>''')
   md.write('''
# <b>'''f'{moduleName}''''</b>
<img src="../images/'''f'{moduleName}''''.png"><br>
<div style="display:inline-block;margin-left:50px;">
''')

   moduleInfo = documentation[moduleName]
   if "description" in moduleInfo:
      md.write(
moduleInfo["description"]+"<br/><br/>"
)

   if "controls" in moduleInfo:
         for control in moduleInfo["controls"].keys():
            tooltip = moduleInfo["controls"][control]
            if tooltip != "" and tooltip != "[todo]" and tooltip != "[none]":
               md.write('''
<b>'''+control+'''</b>: '''+tooltip+'''<br>
''')
   acceptsInputs = getAcceptsInputsString(moduleInfo)
   if acceptsInputs != "":
      md.write('''
<br>'''+acceptsInputs+'''<br></div>
''')