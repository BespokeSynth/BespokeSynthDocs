
# pulse
         
<a name=audiotopulse></a><br>

### <b>audiotopulse</b>

<img src="https://www.bespokesynth.com/docs/screenshots/audiotopulse.png"><br>

<div style="display:inline-block;margin-left:50px;">
sends a pulse when the audio level surpasses a specified threshold<br><br>
<b>release</b>: the cooldown time for the audio signal before a pulse can be triggered again<br>
                   
<b>threshold</b>: send a pulse when the signal hits this threshold<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=notetopulse></a><br>

### <b>notetopulse</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notetopulse.png"><br>

<div style="display:inline-block;margin-left:50px;">
trigger a pulse whenever a note is received<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=pulsebutton></a><br>

### <b>pulsebutton</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pulsebutton.png"><br>

<div style="display:inline-block;margin-left:50px;">
trigger a pulse with a button press<br><br>
<b>pulse</b>: trigger a pulse<br>
                   
<br><br><br><br></div>

<a name=pulsechance></a><br>

### <b>pulsechance</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pulsechance.png"><br>

<div style="display:inline-block;margin-left:50px;">
randomly allow pulses through, based on chance<br><br>
<b>chance</b>: chance that pulses are allowed through<br>
                   
<br>accepts: <font color=yellow>pulses</font> <br>
             
<br><br><br><br></div>

<a name=pulsedelayer></a><br>

### <b>pulsedelayer</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pulsedelayer.png"><br>

<div style="display:inline-block;margin-left:50px;">
delay pulses<br><br>
<b>delay</b>: time to delay, in fractions of a measure<br>
                   
<br>accepts: <font color=yellow>pulses</font> <br>
             
<br><br><br><br></div>

<a name=pulsegate></a><br>

### <b>pulsegate</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pulsegate.png"><br>

<div style="display:inline-block;margin-left:50px;">
control if pulses are allowed through<br><br>
<b>allow</b>: can pulses pass through?<br>
                   
<br>accepts: <font color=yellow>pulses</font> <br>
             
<br><br><br><br></div>

<a name=pulsehocket></a><br>

### <b>pulsehocket</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pulsehocket.png"><br>

<div style="display:inline-block;margin-left:50px;">
sends pulses to randomized destinations<br><br>
<b>weight *</b>: chance that pulse goes to this destination<br>
                   
<br>accepts: <font color=yellow>pulses</font> <br>
             
<br><br><br><br></div>

<a name=pulser></a><br>

### <b>pulser</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pulser.png"><br>

<div style="display:inline-block;margin-left:50px;">
send pulse messages at an interval<br><br>
<b>div</b>: measure division, when using "div" as the interval<br>
                   
<b>interval</b>: rate to send pulses<br>
                   
<b>offset</b>: pulse time offset, in fractions of a measure<br>
                   
<b>random</b>: tell pulsed modules to randomize their position<br>
                   
<b>reset</b>: length of sequence before sending reset pulse<br>
                   
<b>t</b>: pulse interval in milliseconds<br>
                   
<b>timemode</b>: when to send downbeat pulses, or set to "free" for pulses not locked to the transport<br>
                   
<br><br><br><br></div>

<a name=pulsesequence></a><br>

### <b>pulsesequence</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pulsesequence.png"><br>

<div style="display:inline-block;margin-left:50px;">
defines a looping sequence of pulses<br><br>
<b><</b>: shift sequence to the left<br>
                   
<b>></b>: shift sequence to the right<br>
                   
<b>interval</b>: length of each step within the sequence<br>
                   
<b>length</b>: length of the sequence<br>
                   
<br>accepts: <font color=yellow>pulses</font> <br>
             
<br><br><br><br></div>

<a name=pulsetrain></a><br>

### <b>pulsetrain</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pulsetrain.png"><br>

<div style="display:inline-block;margin-left:50px;">
defines a list of pulses to execute, once pulsed<br><br>
<b>interval</b>: length of each step within the sequence<br>
                   
<b>length</b>: length of the sequence<br>
                   
<br>accepts: <font color=yellow>pulses</font> <br>
             
<br><br><br><br></div>
