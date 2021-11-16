
# modulators
         
<a name=accum></a><br>

### <b>accum</b>

<img src="https://www.bespokesynth.com/docs/screenshots/accum.png"><br>

<div style="display:inline-block;margin-left:50px;">
accumulate a value over time<br><br>
<b>value</b>: output value<br>
                   
<b>velocity</b>: amount to accumulate<br>
                   
<br><br><br><br></div>

<a name=add></a><br>

### <b>add</b>

<img src="https://www.bespokesynth.com/docs/screenshots/add.png"><br>

<div style="display:inline-block;margin-left:50px;">
outputs the result of value 1 plus value 2. value 1 and value 2 are intended to be patch targets for modulators.<br><br>
<b>value 1</b>: value to sum<br>
                   
<b>value 2</b>: value to sum<br>
                   
<br><br><br><br></div>

<a name=addcentered></a><br>

### <b>addcentered</b>

<img src="https://www.bespokesynth.com/docs/screenshots/addcentered.png"><br>

<div style="display:inline-block;margin-left:50px;">
outputs the result of value 1 plus value 2, multiplied by range 2. optimized for using to modulation value 1 by range 2 at a frequency. value 1 or value 2 are intended to be patch targets for modulators.<br><br>
<b>range 2</b>: modulation amount<br>
                   
<b>value 1</b>: center value<br>
                   
<b>value 2</b>: modulation value<br>
                   
<br><br><br><br></div>

<a name=audiotocv></a><br>

### <b>audiotocv</b>

<img src="https://www.bespokesynth.com/docs/screenshots/audiotocv.png"><br>

<div style="display:inline-block;margin-left:50px;">
use an audio signal to modulate a control. allow for audio-rate modulation, to achieve effects such as FM.<br><br>
<b>gain</b>: multiply incoming audio<br>
                   
<b>max</b>: maximum output value<br>
                   
<b>min</b>: minimum output value<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=controlsequencer></a><br>

### <b>controlsequencer</b>

<img src="https://www.bespokesynth.com/docs/screenshots/controlsequencer.png"><br>

<div style="display:inline-block;margin-left:50px;">
modulate a control step-wise at an interval<br><br>
<b>interval</b>: rate to advance<br>
                   
<b>length</b>: length of the sequence<br>
                   
<b>random</b>: randomize sequence values<br>
                   
<br><br><br><br></div>

<a name=curve></a><br>

### <b>curve</b>

<img src="https://www.bespokesynth.com/docs/screenshots/curve.png"><br>

<div style="display:inline-block;margin-left:50px;">
remap an input over its range with a curve. double-click on the curve to add points, right click on points to remove them, drag on lines to bend them.<br><br>
<b>input</b>: input value (intended as a modulation target)<br>
                   
<br><br><br><br></div>

<a name=curvelooper></a><br>

### <b>curvelooper</b>

<img src="https://www.bespokesynth.com/docs/screenshots/curvelooper.png"><br>

<div style="display:inline-block;margin-left:50px;">
modulate a value over time with a looping curve<br><br>
<b>length</b>: length of the loop<br>
                   
<b>randomize</b>: create a random curve<br>
                   
<br><br><br><br></div>

<a name=envelope></a><br>

### <b>envelope</b>

<img src="https://www.bespokesynth.com/docs/screenshots/envelope.png"><br>

<div style="display:inline-block;margin-left:50px;">
modulate a value with a triggered envelope<br><br>
<b>adsr</b>: envelope view<br>
                   
<b>adsrA</b>: envelope attack<br>
                   
<b>adsrD</b>: envelope decay<br>
                   
<b>adsrR</b>: envelope release<br>
                   
<b>adsrS</b>: envelope sustain<br>
                   
<b>advanced</b>: switch to advanced envelope editor (allows for a more complicated envelope than just an ADSR). double-click on an advanced envelope line to add stages, right click on points to remove them, drag on lines to bend them.<br>
                   
<b>has sustain</b>: should this envelope have a sustain stage?<br>
                   
<b>high</b>: output high value<br>
                   
<b>length</b>: length of envelope display<br>
                   
<b>low</b>: output low value<br>
                   
<b>max sustain</b>: what's the maximum length of the sustain, in milliseconds? a value of -1 indicates no maximum<br>
                   
<b>sustain stage</b>: which step of the envelope should have the sustain?<br>
                   
<b>use velocity</b>: should envelope output be scaled by input velocity?<br>
                   
<br>accepts: <font color=yellow>pulses</font> <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=expression></a><br>

### <b>expression</b>

<img src="https://www.bespokesynth.com/docs/screenshots/expression.png"><br>

<div style="display:inline-block;margin-left:50px;">
shape modulation with a text-based mathematical expression<br><br>
<b>a</b>: variable to use in expressions<br>
                   
<b>b</b>: variable to use in expressions<br>
                   
<b>c</b>: variable to use in expressions<br>
                   
<b>d</b>: variable to use in expressions<br>
                   
<b>e</b>: variable to use in expressions<br>
                   
<b>input</b>: input to use as x variable<br>
                   
<b>y=</b>: expression to modify input. try something like "x+sin(x*pi*a)". available variables: a,b,c,d,e = the slider + sin(s below. t = time. x1,x2,y1,y2 = biquad state storage.<br>
                   
<br><br><br><br></div>

<a name=fubble></a><br>

### <b>fubble</b>

<img src="https://www.bespokesynth.com/docs/screenshots/fubble.png"><br>

<div style="display:inline-block;margin-left:50px;">
draw on an X/Y pad and replay the drawing to modulate values. based on a concept proposed by olivia jack<br><br>
<b>clear</b>: clear the drawing<br>
                   
<b>length</b>: the interval to quantize to<br>
                   
<b>mutate amount</b>: amount to affect drawing by perlin noise field<br>
                   
<b>mutate noise</b>: rate to move through perlin noise field<br>
                   
<b>mutate warp</b>: scale of perlin noise field<br>
                   
<b>quantize</b>: should we quantize playback to a specified rhythmic interval?<br>
                   
<b>reseed</b>: jump to a different location in the perlin noise field<br>
                   
<b>speed</b>: speed up or slow down playback<br>
                   
<br><br><br><br></div>

<a name=gravity></a><br>

### <b>gravity</b>

<img src="https://www.bespokesynth.com/docs/screenshots/gravity.png"><br>

<div style="display:inline-block;margin-left:50px;">
make a modulation value rise and fall with physics<br><br>
<b>drag</b>: the resistance force to apply opposite the velocity<br>
                   
<b>gravity</b>: the gravitational force to apply downwards<br>
                   
<b>kick</b>: click to apply kick force (or, pulse this module for the same result)<br>
                   
<b>kick amt</b>: the amount of upward force to apply when kicking<br>
                   
<br>accepts: <font color=yellow>pulses</font> <br>
             
<br><br><br><br></div>

<a name=gridsliders></a><br>

### <b>gridsliders</b>

<img src="https://www.bespokesynth.com/docs/screenshots/gridsliders.png"><br>

<div style="display:inline-block;margin-left:50px;">
use a grid controller to control multiple sliders<br><br>
<b>direction</b>: should the grid display the sliders vertically, or horizontally?<br>
                   
<b>grid</b>: patch a grid in here from a "midicontroller" module<br>
                   
<br><br><br><br></div>

<a name=leveltocv></a><br>

### <b>leveltocv</b>

<img src="https://www.bespokesynth.com/docs/screenshots/leveltocv.png"><br>

<div style="display:inline-block;margin-left:50px;">
output a modulation value based on the level of incoming audio<br><br>
<b>attack</b>: rise to the input level at this rate<br>
                   
<b>gain</b>: multiply the input audio by this value<br>
                   
<b>max</b>: output when level is one<br>
                   
<b>min</b>: output when level is zero<br>
                   
<b>release</b>: decay from the input level at this rate<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=macroslider></a><br>

### <b>macroslider</b>

<img src="https://www.bespokesynth.com/docs/screenshots/macroslider.png"><br>

<div style="display:inline-block;margin-left:50px;">
take a value and send scaled versions of that value to multiple destinations<br><br>
<b>end*</b>: the output value at the top of the input's range<br>
                   
<b>input</b>: the input value. intended to be a modulation patch target.<br>
                   
<b>start*</b>: the output value at the bottom of the input's range<br>
                   
<br><br><br><br></div>

<a name=modwheeltocv></a><br>

### <b>modwheeltocv</b>

<img src="https://www.bespokesynth.com/docs/screenshots/modwheeltocv.png"><br>

<div style="display:inline-block;margin-left:50px;">
take a note's modwheel value and convert it to a modulation value<br><br>
<b>max</b>: output for modwheel value 127<br>
                   
<b>min</b>: output for modwheel value 0<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=mult></a><br>

### <b>mult</b>

<img src="https://www.bespokesynth.com/docs/screenshots/mult.png"><br>

<div style="display:inline-block;margin-left:50px;">
outputs the result of value 1 multiplier by value 2. value 1 and value 2 are intended to be patch targets for modulators.<br><br>
<br><br><br><br></div>

<a name=notetofreq></a><br>

### <b>notetofreq</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notetofreq.png"><br>

<div style="display:inline-block;margin-left:50px;">
takes an input note, and outputs that note's frequency in hertz<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notetoms></a><br>

### <b>notetoms</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notetoms.png"><br>

<div style="display:inline-block;margin-left:50px;">
takes an input note, and outputs the period of that note's frequency in milliseconds. useful for setting delay lines to create specific pitches.<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=pitchtocv></a><br>

### <b>pitchtocv</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pitchtocv.png"><br>

<div style="display:inline-block;margin-left:50px;">
take a note's pitch and convert it to a modulation value<br><br>
<b>max</b>: output for pitch 127<br>
                   
<b>min</b>: output for pitch 0<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=pitchtospeed></a><br>

### <b>pitchtospeed</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pitchtospeed.png"><br>

<div style="display:inline-block;margin-left:50px;">
convert an input pitch to a speed ratio. you could use this to control a sample's playback speed and make it playable with a keyboard.<br><br>
<b>ref freq</b>: the output is the input frequency divided by this number<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=pressuretocv></a><br>

### <b>pressuretocv</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pressuretocv.png"><br>

<div style="display:inline-block;margin-left:50px;">
take a note's pressure and convert it to a modulation value<br><br>
<b>max</b>: output for pressure 127<br>
                   
<b>min</b>: output for pressure 0<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=ramper></a><br>

### <b>ramper</b>

<img src="https://www.bespokesynth.com/docs/screenshots/ramper.png"><br>

<div style="display:inline-block;margin-left:50px;">
blend a control to a specified value over a specified time<br><br>
<b>length</b>: length of time to blend over<br>
                   
<b>start</b>: begin blending (or, send a pulse to this module for the same result)<br>
                   
<b>target</b>: the value to arrive at when the ramp is over<br>
                   
<br>accepts: <font color=yellow>pulses</font> <br>
             
<br><br><br><br></div>

<a name=smoother></a><br>

### <b>smoother</b>

<img src="https://www.bespokesynth.com/docs/screenshots/smoother.png"><br>

<div style="display:inline-block;margin-left:50px;">
outputs a smoothed value of the input<br><br>
<b>input</b>: set a value to smooth, patch a modulator into here<br>
                   
<b>smooth</b>: amount of smoothing to apply<br>
                   
<br><br><br><br></div>

<a name=subtract></a><br>

### <b>subtract</b>

<img src="https://www.bespokesynth.com/docs/screenshots/subtract.png"><br>

<div style="display:inline-block;margin-left:50px;">
outputs the result of value 2 subtracted from value 1. value 1 and value 2 are intended to be patch targets for modulators.<br><br>
<br><br><br><br></div>

<a name=valuesetter></a><br>

### <b>valuesetter</b>

<img src="https://www.bespokesynth.com/docs/screenshots/valuesetter.png"><br>

<div style="display:inline-block;margin-left:50px;">
set a specified value on a targeted control<br><br>
<b>set</b>: click here to send the value (or, send a pulse to this module for the same result)<br>
                   
<b>value</b>: value to set<br>
                   
<br>accepts: <font color=yellow>pulses</font> <br>
             
<br><br><br><br></div>

<a name=velocitytocv></a><br>

### <b>velocitytocv</b>

<img src="https://www.bespokesynth.com/docs/screenshots/velocitytocv.png"><br>

<div style="display:inline-block;margin-left:50px;">
take a note's velocity and convert it to a modulation value<br><br>
<b>max</b>: output for velocity 127<br>
                   
<b>min</b>: output for velocity 0<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=vinylcontrol></a><br>

### <b>vinylcontrol</b>

<img src="https://www.bespokesynth.com/docs/screenshots/vinylcontrol.png"><br>

<div style="display:inline-block;margin-left:50px;">
modulator which outputs a speed value based upon control vinyl input audio. provide it with a stereo signal from control vinyl (like you'd use to control serato) patched in from an "input" module.<br><br>
<b>control</b>: enable/disable transport control. when you enable it, it will use the current speed as the reference speed (so, the output will output a value of 1 until you change the vinyl's speed)<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>
