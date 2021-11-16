
# other
         
<a name=comment></a><br>

### <b>comment</b>

<img src="https://www.bespokesynth.com/docs/screenshots/comment.png"><br>

<div style="display:inline-block;margin-left:50px;">
a box to display some text, to explain a section of a patch<br><br>
<b>comment</b>: type text here<br>
                   
<br><br><br><br></div>

<a name=eventcanvas></a><br>

### <b>eventcanvas</b>

<img src="https://www.bespokesynth.com/docs/screenshots/eventcanvas.png"><br>

<div style="display:inline-block;margin-left:50px;">
schedule values to set over time<br><br>
<b>canvas</b>: canvas of events. canvas controls:
-shift-click to add an event
-hold shift and drag an event to duplicate
-hold alt to drag an event without snapping
-hold ctrl while dragging to snap to an interval
-hold shift and scroll to zoom
-hold alt and grab empty space to move slide the canvas view
-hold ctrl and grab empty space to zoom the canvas view<br>
                   
<b>clear</b>: delete all elements<br>
                   
<b>delete</b>: delete highlighted elements<br>
                   
<b>drag mode</b>: direction that elements can be dragged<br>
                   
<b>interval</b>: grid for snapping events to<br>
                   
<b>measures</b>: length of loop<br>
                   
<b>quantize</b>: quantizes events to grid<br>
                   
<b>record</b>: record connected values as they change<br>
                   
<b>scrollh</b>: horizontal scrollbar<br>
                   
<b>timeline</b>: control loop points<br>
                   
<b>view rows</b>: number of visible rows<br>
                   
<br><br><br><br></div>

<a name=globalcontrols></a><br>

### <b>globalcontrols</b>

<img src="https://www.bespokesynth.com/docs/screenshots/globalcontrols.png"><br>

<div style="display:inline-block;margin-left:50px;">
interface controls, intended to allow you to use midi controllers to navigate the canvas. controlling these sliders directly with the mouse is not recommended.<br><br>
<b>lissajous b</b>: amount of blue in background lissajous curve<br>
                   
<b>lissajous g</b>: amount of green in background lissajous curve<br>
                   
<b>lissajous r</b>: amount of red in background lissajous curve<br>
                   
<b>scroll x</b>: emulate horizontal mouse scrolling<br>
                   
<b>scroll y</b>: emulate vertical mouse scrolling<br>
                   
<b>x pos</b>: horizontal panning position<br>
                   
<b>y pos</b>: vertical panning position<br>
                   
<b>zoom</b>: zoom level<br>
                   
<br><br><br><br></div>

<a name=grid></a><br>

### <b>grid</b>

<img src="https://www.bespokesynth.com/docs/screenshots/grid.png"><br>

<div style="display:inline-block;margin-left:50px;">
generic grid, to be used by "script" module, to assist in writing scripts that use grid-based midi controllers<br><br>
<b>grid</b>: patch a grid in here, from a "midicontroller" module<br>
                   
<b>momentary</b>: should clicks be treated as momentary inputs?<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=groupcontrol></a><br>

### <b>groupcontrol</b>

<img src="https://www.bespokesynth.com/docs/screenshots/groupcontrol.png"><br>

<div style="display:inline-block;margin-left:50px;">
connect to several checkboxes, and control them all with one checkbox<br><br>
<b>group enabled</b>: controls the connected checkboxes<br>
                   
<br><br><br><br></div>

<a name=loopergranulator></a><br>

### <b>loopergranulator</b>

<img src="https://www.bespokesynth.com/docs/screenshots/loopergranulator.png"><br>

<div style="display:inline-block;margin-left:50px;">
use with a "looper" module to play the contents with granular synthesis<br><br>
<b>freeze</b>: stop advancing looper time<br>
                   
<b>len ms</b>: length of each grain in milliseconds<br>
                   
<b>loop pos</b>: playback position within loop<br>
                   
<b>octaves</b>: should we add octaves and fifths?<br>
                   
<b>on</b>: use granular synthesis for looper playback<br>
                   
<b>overlap</b>: number of overlapping grains<br>
                   
<b>pos rand</b>: randomization of grain start point<br>
                   
<b>spacing rand</b>: randomization of time between grains<br>
                   
<b>speed</b>: speed of grain playback<br>
                   
<b>speed rand</b>: randomization of grain speed<br>
                   
<b>width</b>: stereo width of grain placement<br>
                   
<br><br><br><br></div>

<a name=multitrackrecorder></a><br>

### <b>multitrackrecorder</b>

<img src="https://www.bespokesynth.com/docs/screenshots/multitrackrecorder.png"><br>

<div style="display:inline-block;margin-left:50px;">
record several synchronized tracks of audio, to write to disk for mixing in an external DAW<br><br>
<b>add track</b>: add an additional track<br>
                   
<b>bounce</b>: write the tracks to your recordings directory<br>
                   
<b>clear</b>: clear the audio in the tracks<br>
                   
<b>record</b>: record input to the tracks<br>
                   
<br><br><br><br></div>

<a name=oscoutput></a><br>

### <b>oscoutput</b>

<img src="https://www.bespokesynth.com/docs/screenshots/oscoutput.png"><br>

<div style="display:inline-block;margin-left:50px;">
send OSC messages when slider values change or when notes are received<br><br>
<b>label*</b>: label to send slider value. the message will be sent in the format /bespoke/[label] [value]<br>
                   
<b>note out address</b>: label to send input notes. the message will be sent in the format /bespoke/[label] [pitch] [velocity]<br>
                   
<b>osc out address</b>: destination to send OSC messages to<br>
                   
<b>osc out port</b>: port to send OSC messages to<br>
                   
<b>slider*</b>: sends a value to the address. try patching a modulator into this, such as a leveltocv module to send audio levels.<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=prefab></a><br>

### <b>prefab</b>

<img src="https://www.bespokesynth.com/docs/screenshots/prefab.png"><br>

<div style="display:inline-block;margin-left:50px;">
create a collection of modules that can be loaded from the "prefabs" menu. drag and drop modules onto here to add them to the prefab. drag the grey cable to any modules you want to remove from the prefab.<br><br>
<b>disband</b>: free all modules from this prefab<br>
                   
<b>load</b>: load a .pfb<br>
                   
<b>save</b>: save as a .pfb file<br>
                   
<br><br><br><br></div>

<a name=presets></a><br>

### <b>presets</b>

<img src="https://www.bespokesynth.com/docs/screenshots/presets.png"><br>

<div style="display:inline-block;margin-left:50px;">
save and restore sets of values. connect the grey circle to modules to affect all controls on that module. connect the purple circle to a control to affect only that control. shift-click on the grid to store a preset to that square, and click on a grid square to load that preset.<br><br>
<b>blend ms</b>: time to blend preset values over<br>
                   
<b>preset</b>: jump to a preset<br>
                   
<br><br><br><br></div>

<a name=push2control></a><br>

### <b>push2control</b>

<img src="https://www.bespokesynth.com/docs/screenshots/push2control.png"><br>

<div style="display:inline-block;margin-left:50px;">
use an ableton push 2 to control bespoke's interface<br><br>
<br><br><br><br></div>

<a name=radiosequencer></a><br>

### <b>radiosequencer</b>

<img src="https://www.bespokesynth.com/docs/screenshots/radiosequencer.png"><br>

<div style="display:inline-block;margin-left:50px;">
sequence to only enable one value at a time. patch it to the "enabled" checkbox on several modules to only enable one module at a time. works well in conjunction with "groupcontrol" module.<br><br>
<b>grid</b>: patch a grid in here from a "midicontroller" module<br>
                   
<b>interval</b>: rate to advance<br>
                   
<b>length</b>: length of sequence<br>
                   
<br><br><br><br></div>

<a name=samplebrowser></a><br>

### <b>samplebrowser</b>

<img src="https://www.bespokesynth.com/docs/screenshots/samplebrowser.png"><br>

<div style="display:inline-block;margin-left:50px;">
browse your system for samples. drag samples from here to your desired targets (sampleplayer, drumplayer, seaofgrain, etc)<br><br>
<b> < </b>: previous page<br>
                   
<b> > </b>: next page<br>
                   
<br><br><br><br></div>

<a name=scale></a><br>

### <b>scale</b>

<img src="https://www.bespokesynth.com/docs/screenshots/scale.png"><br>

<div style="display:inline-block;margin-left:50px;">
controls the global scale used by various modules<br><br>
<b>intonation</b>: which method to use to tune the scale<br>
                   
<b>note</b>: the pitch that maps to the frequency defined in "tuning"<br>
                   
<b>root</b>: root note of the scale<br>
                   
<b>scale</b>: which set of notes to use<br>
                   
<b>tet</b>: how many semitones make up an octave<br>
                   
<b>tuning</b>: what frequency does the pitch defined in "note" represent?<br>
                   
<br><br><br><br></div>

<a name=script></a><br>

### <b>script</b>

<img src="https://www.bespokesynth.com/docs/screenshots/script.png"><br>

<div style="display:inline-block;margin-left:50px;">
python scripting for livecoding notes and module control<br><br>
<b>?</b>: show scripting reference<br>
                   
<b>a</b>: variable for the script to use, can be modulation by other sources<br>
                   
<b>b</b>: variable for the script to use, can be modulation by other sources<br>
                   
<b>c</b>: variable for the script to use, can be modulation by other sources<br>
                   
<b>code</b>: write code here. press ctrl-R to execute the code, or ctrl-shift-R to just execute the current block.<br>
                   
<b>d</b>: variable for the script to use, can be modulation by other sources<br>
                   
<b>load</b>: load selected script<br>
                   
<b>loadscript</b>: choose a script from here, then press "load"<br>
                   
<b>run</b>: click here to execute the code, or press ctrl-R<br>
                   
<b>save as</b>: save the current script<br>
                   
<b>stop</b>: cancel any events scheduled by this script<br>
                   
<br>accepts: <font color=yellow>pulses</font> <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=scriptstatus></a><br>

### <b>scriptstatus</b>

<img src="https://www.bespokesynth.com/docs/screenshots/scriptstatus.png"><br>

<div style="display:inline-block;margin-left:50px;">
shows everything in the current python scope, for debugging<br><br>
<b>reset all</b>: resets scope variables<br>
                   
<br><br><br><br></div>

<a name=selector></a><br>

### <b>selector</b>

<img src="https://www.bespokesynth.com/docs/screenshots/selector.png"><br>

<div style="display:inline-block;margin-left:50px;">
radio button control to only enable one value at a time. patch it to the "enabled" checkbox on several modules to only enable one module at a time. works well in conjunction with "groupcontrol" module.<br><br>
<b>selector</b>: which value should be set to 1<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=timerdisplay></a><br>

### <b>timerdisplay</b>

<img src="https://www.bespokesynth.com/docs/screenshots/timerdisplay.png"><br>

<div style="display:inline-block;margin-left:50px;">
displays a timer to indicate how long a patch has been running<br><br>
<b>reset</b>: reset timer to zero<br>
                   
<br><br><br><br></div>

<a name=transport></a><br>

### <b>transport</b>

<img src="https://www.bespokesynth.com/docs/screenshots/transport.png"><br>

<div style="display:inline-block;margin-left:50px;">
controls tempo and current time position<br><br>
<b> + </b>: increase tempo by one<br>
                   
<b> - </b>: decrease tempo by one<br>
                   
<b> < </b>: nudge current time backward<br>
                   
<b> > </b>: nudge current time forward<br>
                   
<b>reset</b>: reset timeline to zero<br>
                   
<b>swing</b>: where the halfway point of musical time within the swing interval should fall. a value of .5 represents no swing.<br>
                   
<b>swing interval</b>: interval over which to apply swing<br>
                   
<b>tempo</b>: global tempo, in beats per minute<br>
                   
<b>timesigbottom</b>: time signature bottom value<br>
                   
<b>timesigtop</b>: time signature top value<br>
                   
<br><br><br><br></div>

<a name=valuestream></a><br>

### <b>valuestream</b>

<img src="https://www.bespokesynth.com/docs/screenshots/valuestream.png"><br>

<div style="display:inline-block;margin-left:50px;">
displays a control's value over time<br><br>
<b>speed</b>: how quickly display should scroll<br>
                   
<br><br><br><br></div>

<a name=vstplugin></a><br>

### <b>vstplugin</b>

<img src="https://www.bespokesynth.com/docs/screenshots/vstplugin.png"><br>

<div style="display:inline-block;margin-left:50px;">
a VST plugin instance<br><br>
<b>open</b>: show the plugin window<br>
                   
<b>preset</b>: choose from saved VST presets<br>
                   
<b>program change</b>: send a program change message to the VST instance<br>
                   
<b>save as</b>: save the current VST settings as a preset to load again later<br>
                   
<b>show parameter</b>: select parameters to display them, so they can be adjusted from within bespoke's interface. if a VST has more than 20 parameters, this list will initially be empty. in that case, to make a parameter appear in this list, wiggle it within the VST's interface.<br>
                   
<b>vol</b>: adjust the output volume<br>
                   
<br><br><br><br></div>
