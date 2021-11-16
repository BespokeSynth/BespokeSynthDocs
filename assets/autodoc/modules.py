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

html = open("../../_includes/modules.md", "w")

for moduleType in moduleTypes:
   html.write('''
## '''+moduleType+'''
         ''')
   for module in modulesByType[moduleType]:
      moduleInfo = documentation[module]
      if moduleInfo["description"][0] == '[':
         continue
      html.write('''
<a name='''+module+'''></a><br>

### <b>'''+module+'''</b>

<img src="https://www.bespokesynth.com/docs/screenshots/'''+module+'''.png"><br>

<div style="display:inline-block;margin-left:50px;">
''')

      if "description" in moduleInfo:
         html.write(
moduleInfo["description"]+"<br><br>"
             )
      if "controls" in moduleInfo:
         for control in moduleInfo["controls"].keys():
            tooltip = moduleInfo["controls"][control]
            if tooltip != "" and tooltip != "[todo]" and tooltip != "[none]":
               html.write('''
<b>'''+control+'''</b>: '''+tooltip+'''<br>
                   ''')
      acceptsInputs = getAcceptsInputsString(moduleInfo)
      if acceptsInputs != "":
         html.write(
"<br>"+acceptsInputs+"<br>"
             )
      html.write('''
<br><br><br><br></div>
''')