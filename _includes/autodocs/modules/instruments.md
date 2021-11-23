
# instruments
         
<a name=circlesequencer></a><br>

### <b>circlesequencer</b>

<img src="images/circlesequencer.png"><br>

<div style="display:inline-block;margin-left:50px;">
polyrhythmic sequencer that displays a loop as a circle<br><br>
<b>length*</b>: number of steps in this ring<br>
                   
<b>note*</b>: pitch to use for this ring<br>
                   
<b>offset*</b>: timing offset for this ring<br>
                   
<br><br><br><br></div>

<a name=drumsequencer></a><br>

### <b>drumsequencer</b>

<img src="images/drumsequencer.png"><br>

<div style="display:inline-block;margin-left:50px;">
step sequencer intended for drums. hold shift when dragging on the grid to adjust step velocity.<br><br>
<b><</b>: shift whole pattern one step earlier<br>
                   
<b>></b>: shift whole pattern one step later<br>
                   
<b>column</b>: current column, to use for visualizing the step on a midi controller<br>
                   
<b>grid</b>: patch a grid in here from a "midicontroller" module<br>
                   
<b>measures</b>: length of the sequence in measures<br>
                   
<b>metastep</b>: patch a grid in here from a "midicontroller" module to control the "meta step". I forget what this does. oops.<br>
                   
<b>offset*</b>: shift row forward/backward in time. try making your snares a little early, your hats a little late, etc.<br>
                   
<b>offsets</b>: show "offsets" sliders<br>
                   
<b>preset</b>: select a pattern preset<br>
                   
<b>r amt</b>: the chance that each step will change when being randomized. low values will only change a small amount of the sequence, high values will replace more of the sequence.<br>
                   
<b>r den</b>: density of the randomizer output. the higher this is, the busier the random output will be.<br>
                   
<b>randomize</b>: randomize the sequence<br>
                   
<b>repeat</b>: repeat input notes at this rate<br>
                   
<b>rowpitch*</b>: output pitch for this row<br>
                   
<b>step</b>: length of each step<br>
                   
<b>str</b>: velocity to use when setting a step via a grid controller, if the checkbox next to this slider is checked<br>
                   
<b>use str</b>: if the "str" slider should be used for setting velocity<br>
                   
<b>velocity</b>: patch a grid in here from a "midicontroller" module to control the velocity<br>
                   
<b>yoff</b>: vertical offset for grid controller's view of the pattern<br>
                   
<br>accepts: <font color=yellow>pulses</font> <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=fouronthefloor></a><br>

### <b>fouronthefloor</b>

<img src="images/fouronthefloor.png"><br>

<div style="display:inline-block;margin-left:50px;">
sends note 0 every beat, to trigger a kick drum<br><br>
<b>two</b>: sends note only every two beats<br>
                   
<br><br><br><br></div>

<a name=gridkeyboard></a><br>

### <b>gridkeyboard</b>

<img src="images/gridkeyboard.png"><br>

<div style="display:inline-block;margin-left:50px;">
grid-based keyboard, intended primarily for 64-pad grid controllers<br><br>
<b>arrangement</b>: what style of layout should we use?<br>
                   
<b>ch.latch</b>: latch chord button presses<br>
                   
<b>grid</b>: patch a grid in here from a "midicontroller" module<br>
                   
<b>latch</b>: latch key presses, so you press once to play a note, and press again to release a note<br>
                   
<b>layout</b>: keyboard style<br>
                   
<b>octave</b>: base octave<br>
                   
<b>p.root</b>: for chorder, make root note always play<br>
                   
<br><br><br><br></div>

<a name=keyboarddisplay></a><br>

### <b>keyboarddisplay</b>

<img src="images/keyboarddisplay.png"><br>

<div style="display:inline-block;margin-left:50px;">
displays input notes on a keyboard, and allows you to click the keyboard to create notes<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=m185sequencer></a><br>

### <b>m185sequencer</b>

<img src="images/m185sequencer.png"><br>

<div style="display:inline-block;margin-left:50px;">
sequencer using the unique paradigm of the the m185 or intellijel metropolis<br><br>
<b>gate*</b>: behavior for each row: "repeat" plays every step, "once" plays just the first step, "hold" holds across all steps, "rest" plays no steps<br>
                   
<b>interval</b>: interval per step<br>
                   
<b>pitch*</b>: pitch to use for this row<br>
                   
<b>pulses*</b>: number of steps this row should last<br>
                   
<b>reset step</b>: resets counter to first step<br>
                   
<br>accepts: <font color=yellow>pulses</font> <br>
             
<br><br><br><br></div>

<a name=midicontroller></a><br>

### <b>midicontroller</b>

<img src="images/midicontroller.png"><br>

<div style="display:inline-block;margin-left:50px;">
get midi input from external devices. to get a nice display in the "layout" view, create a .json file with the same name as your controller to describe your controller's layout, and place it in your "data/controllers" directory. look at the other files in that directory for examples.<br><br>
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
                   
<br><br><br><br></div>

<a name=notecanvas></a><br>

### <b>notecanvas</b>

<img src="images/notecanvas.png"><br>

<div style="display:inline-block;margin-left:50px;">
looping note roll<br><br>
<b>canvas</b>: canvas of notes. canvas controls:
-shift-click to add a note
-hold shift and drag a note to duplicate
-hold alt to drag a note without snapping
-hold ctrl while dragging to snap to an interval
-hold shift and scroll to zoom
-hold alt and grab empty space to move slide the canvas view
-hold ctrl and grab empty space to zoom the canvas view<br>
                   
<b>clear</b>: delete all elements<br>
                   
<b>delete</b>: delete highlighted elements<br>
                   
<b>drag mode</b>: direction that elements can be dragged<br>
                   
<b>free rec</b>: enable record mode, and extend canvas if we reach the end<br>
                   
<b>interval</b>: interval to quantize to<br>
                   
<b>measures</b>: loop length<br>
                   
<b>play</b>: play notes on canvas<br>
                   
<b>quantize</b>: quantize selected notes to interval<br>
                   
<b>rec</b>: record input notes to canvas<br>
                   
<b>scrollh</b>: horizontal scrollbar<br>
                   
<b>scrollv</b>: vertical scrollbar<br>
                   
<b>show chord intervals</b>: show brackets to indicate chord relationships<br>
                   
<b>timeline</b>: control loop points<br>
                   
<b>view rows</b>: number of visible rows<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notechain></a><br>

### <b>notechain</b>

<img src="images/notechain.png"><br>

<div style="display:inline-block;margin-left:50px;">
trigger a note, followed by a pulse to trigger another note after a delay<br><br>
<b>duration</b>: duration of note, in measures<br>
                   
<b>next</b>: interval until sending pulse<br>
                   
<b>pitch</b>: pitch to play<br>
                   
<b>trigger</b>: play note for this chain node<br>
                   
<b>velocity</b>: velocity for note<br>
                   
<br>accepts: <font color=yellow>pulses</font> <br>
             
<br><br><br><br></div>

<a name=notecounter></a><br>

### <b>notecounter</b>

<img src="images/notecounter.png"><br>

<div style="display:inline-block;margin-left:50px;">
advance through pitches sequentially. useful for driving the "notesequencer" or "drumsequencer" modules.<br><br>
<b>div</b>: measure division, when using "div" as the interval<br>
                   
<b>interval</b>: rate to advance<br>
                   
<b>length</b>: length of the sequence<br>
                   
<b>random</b>: output random pitches within the range, rather than sequential<br>
                   
<b>start</b>: pitch at the start of the sequence<br>
                   
<b>sync</b>: if the output pitch should be synchronized to the global transport<br>
                   
<br><br><br><br></div>

<a name=notecreator></a><br>

### <b>notecreator</b>

<img src="images/notecreator.png"><br>

<div style="display:inline-block;margin-left:50px;">
create a one-off note<br><br>
<b>duration</b>: note length when "trigger" button is used<br>
                   
<b>on</b>: turn on to start note, turn off to end note<br>
                   
<b>pitch</b>: output note pitch<br>
                   
<b>trigger</b>: press to trigger note for specified duration<br>
                   
<b>velocity</b>: note velocity<br>
                   
<br>accepts: <font color=yellow>pulses</font> <br>
             
<br><br><br><br></div>

<a name=notelooper></a><br>

### <b>notelooper</b>

<img src="images/notelooper.png"><br>

<div style="display:inline-block;margin-left:50px;">
note loop recorder with overdubbing and replacement functionality<br><br>
<b>canvas</b>: canvas of recorded notes<br>
                   
<b>clear</b>: clear pattern<br>
                   
<b>del/mute</b>: if "write" is enabled, erase notes as the playhead passes over them. otherwise, just mute them.<br>
                   
<b>load*</b>: restore pattern<br>
                   
<b>num bars</b>: set loop length in measures<br>
                   
<b>store*</b>: save pattern<br>
                   
<b>write</b>: should input should be recorded?<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notesequencer></a><br>

### <b>notesequencer</b>

<img src="images/notesequencer.png"><br>

<div style="display:inline-block;margin-left:50px;">
looping sequence of notes at an interval. pair with a "pulser" module for more interesting step control. hold "shift" to adjust step length.<br><br>
<b><</b>: shift the sequence to the left<br>
                   
<b>></b>: shift the sequence to the right<br>
                   
<b>clear</b>: clear all steps<br>
                   
<b>grid</b>: patch a grid in here from a "midicontroller" module<br>
                   
<b>interval</b>: note length<br>
                   
<b>len</b>: randomize the length of each step's note.<br>
                   
<b>len*</b>: length for this column<br>
                   
<b>length</b>: length that the sequence below should play. the overall grid length can be changed by adjusting "gridsteps" in the triangle menu.<br>
                   
<b>loop reset</b>: when sequence loops, reset to here instead. send a "downbeat"-style message from a pulser to restart the sequence from the first step.<br>
                   
<b>notemode</b>: which set of pitches should the rows represent?<br>
                   
<b>octave</b>: octave of the bottom pitch of this sequence<br>
                   
<b>pitch</b>: randomize pitches in the sequence. hold shift to constrain the randomization to only pick roots and fifths.<br>
                   
<b>rand len chance</b>: when clicking the random length button, what is the chance that a step gets changed?<br>
                   
<b>rand len range</b>: when clicking the random length button, how much will the length change?<br>
                   
<b>rand pitch chance</b>: when clicking the random pitch button, what is the chance that a step gets changed?<br>
                   
<b>rand pitch range</b>: when clicking the random pitch button, how far will the pitch change?<br>
                   
<b>rand vel chance</b>: when clicking the random velocity button, what is the chance that a step gets changed?<br>
                   
<b>rand vel density</b>: when clicking the random velocity button, what are the chances that a step should have a note?<br>
                   
<b>tone*</b>: pitch for this column<br>
                   
<b>vel</b>: randomize the velocity of each step's note.<br>
                   
<b>vel*</b>: velocity for this column<br>
                   
<b>x offset</b>: x offset of attached grid controller<br>
                   
<b>y offset</b>: y offset of attached grid controller<br>
                   
<br>accepts: <font color=yellow>pulses</font> <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notesinger></a><br>

### <b>notesinger</b>

<img src="images/notesinger.png"><br>

<div style="display:inline-block;margin-left:50px;">
output a note based on a detected pitch<br><br>
<b>oct</b>: octave to adjust output pitch by<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=playsequencer></a><br>

### <b>playsequencer</b>

<img src="images/playsequencer.png"><br>

<div style="display:inline-block;margin-left:50px;">
drum sequencer that allows you to punch in to record and overdub steps, inspired by the pulsar-23 drum machine<br><br>
<b>grid</b>: patch a grid in here from a "midicontroller" module<br>
                   
<b>interval</b>: the step size<br>
                   
<b>link columns</b>: if the mute/delete control should be shared across the entire column<br>
                   
<b>load*</b>: load the sequence stored in this slot<br>
                   
<b>measures</b>: the loop length<br>
                   
<b>mute/delete*</b>: if write is disabled, mute this row. if write is enabled, clear the steps as the playhead passes them<br>
                   
<b>note repeat</b>: if held notes should repeat every step<br>
                   
<b>store*</b>: store the current sequence to this slot<br>
                   
<b>write</b>: if the current input should be written to the sequence. this will also delete steps if mute/delete is enabled for this row<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=polyrhythms></a><br>

### <b>polyrhythms</b>

<img src="images/polyrhythms.png"><br>

<div style="display:inline-block;margin-left:50px;">
looping sequence with lines on different divisions<br><br>
<b>length*</b>: number of steps for this line<br>
                   
<b>note*</b>: pitch to use for this line<br>
                   
<br><br><br><br></div>

<a name=randomnote></a><br>

### <b>randomnote</b>

<img src="images/randomnote.png"><br>

<div style="display:inline-block;margin-left:50px;">
play a note at a given interval with a random chance<br><br>
<b>interval</b>: the note length<br>
                   
<b>offset</b>: the amount of time to offset playback within the interval<br>
                   
<b>pitch</b>: the pitch to use<br>
                   
<b>probability</b>: the chance that a note will play each interval<br>
                   
<b>skip</b>: after a note plays, don't play a note the next n-1 times that it would have played<br>
                   
<b>velocity</b>: the velocity to use<br>
                   
<br><br><br><br></div>

<a name=slidersequencer></a><br>

### <b>slidersequencer</b>

<img src="images/slidersequencer.png"><br>

<div style="display:inline-block;margin-left:50px;">
trigger notes along a continuous timeline<br><br>
<b>division</b>: rate to progress<br>
                   
<b>note*</b>: pitch for this element<br>
                   
<b>playing*</b>: is this element playing?<br>
                   
<b>time*</b>: time to trigger this element<br>
                   
<b>vel*</b>: velocity of this element<br>
                   
<br><br><br><br></div>
