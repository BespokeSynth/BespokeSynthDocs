
<a name=midicontroller></a><br>
# <b>midicontroller</b>
<img src="https://www.bespokesynth.com/docs/screenshots/midicontroller.png"><br>
<div style="display:inline-block;margin-left:50px;">
get midi input from external devices. to get a nice display in the "layout" view, create a .json file with the same name as your controller to describe your controller's layout, and place it in your "data/controllers" directory. look at the other files in that directory for examples.<br/><br/>
<b> x </b>: delete this connection<br>

<b>add</b>: add a mapping manually<br>

<b>bind (hold shift)</b>: when this is enabled, you can map a midi input to a UI control by hovering over a UI control, holding shift, and then using desired midi input<br>

<b>blink</b>: when the targeted control is enabled, send alternating on/off messages, to blink the associated LED<br>

<b>channel</b>: which channel to pay attention to<br>

<b>control</b>: pitch or control to refer to<br>

<b>controller</b>: midi device to use<br>

<b>controltype</b>: how this control should modify the target.
 -slider: set the value interpolated between "midi off" and "midi on" to the slider's value
 -set: set the specified value directly when this button is pressed
 -release: set the specified value directly when this button is released
 -toggle: toggle the control's value to on/off when this button is pressed
 -direct: set the control to the literal midi input value<br>

<b>copy</b>: duplicate this connection<br>

<b>feedback</b>: which cc or note should we send the feedback to?<br>

<b>increment</b>: when "controltype" is "set" or "release", the targeted control is incremented by this amount (and the "value" field is ignored). when "controltype" is "slider", the targeted control is changed by this amount in the direction the control was changed (this setting is useful for "infinite encoders")<br>

<b>layout</b>: which layout file should we use for this controller? these can be created in your Documents/BespokeSynth/controllers folder.<br>

<b>mappingdisplay</b>: which mapping view to see<br>

<b>messagetype</b>: type of midi message<br>

<b>midi off</b>: the lower end of the midi range. send this value when the targeted control is off. if "scale" is enabled, this also controls the lower end of the slider range, and you can set midi off to be higher than midi on to reverse a slider's direction.<br>

<b>midi on</b>: the upper end of the midi range. send this value when the targeted control is on. if "scale" is enabled, this also controls the upper end of the slider range, and you can set midi off to be higher than midi on to reverse a slider's direction.<br>

<b>monome</b>: which monome should we use?<br>

<b>osc input port</b>: port to use for osccontroller input<br>

<b>page</b>: select which page of midi controls to use. each page acts like an independent midi controller, so you can use pages to allow one midi controller to switch between controlling many things<br>

<b>pageless</b>: should this connection work across all pages of the midicontroller?<br>

<b>path</b>: path to the control that should be affected<br>

<b>scale</b>: should the output of this midi slider be scaled between "midi off" and "midi on"?<br>

<b>twoway</b>: should we send feedback to the controller? (to control the LEDs associated with the button/knob)<br>

<b>value</b>: the value to set<br>
