
<a name=oscoutput></a><br>
# <b>oscoutput</b>
<img src="../images/oscoutput.png"><br>
<div style="display:inline-block;margin-left:50px;">
send OSC messages when slider values change or when notes are received<br/><br/>
<b>label*</b>: label to send slider value. the message will be sent in the format /bespoke/[label] [value]<br>

<b>note out address</b>: label to send input notes. the message will be sent in the format /bespoke/[label] [pitch] [velocity]<br>

<b>osc out address</b>: destination to send OSC messages to<br>

<b>osc out port</b>: port to send OSC messages to<br>

<b>slider*</b>: sends a value to the address. try patching a modulator into this, such as a leveltocv module to send audio levels.<br>

<br>accepts: <font color=orange>notes</font> <br></div>
