
# audio effects
         
<a name=audiometer></a><br>

### <b>audiometer</b>

<img src="images/audiometer.png"><br>

<div style="display:inline-block;margin-left:50px;">
sets a slider to an audio level's volume. useful to map a midi display value to.<br><br>
<b>level</b>: the input audio level. hook this up to an LED-display midi control to see the value displayed on your controller.<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=audiorouter></a><br>

### <b>audiorouter</b>

<img src="images/audiorouter.png"><br>

<div style="display:inline-block;margin-left:50px;">
selector for switching where audio is routed to. connect to targets to add them to the list.<br><br>
<b>route</b>: audio destination<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=dcoffset></a><br>

### <b>dcoffset</b>

<img src="images/dcoffset.png"><br>

<div style="display:inline-block;margin-left:50px;">
add a constant offset to an audio signal<br><br>
<b>offset</b>: amount of offset to add<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=effectchain></a><br>

### <b>effectchain</b>

<img src="images/effectchain.png"><br>

<div style="display:inline-block;margin-left:50px;">
container to hold a list of effects, applied in series. the effects can be easily reordered with the < and > buttons, and deleted with the x button. hold shift to expose a x button for all effects.<br><br>
<b><</b>: move this effect to earlier in the chain<br>
                   
<b>></b>: move this effect to later in the chain<br>
                   
<b>effect</b>: select which effect to add<br>
                   
<b>exit effect</b>: on push2, back effect control out to the main effectchain controls<br>
                   
<b>mix*</b>: wet/dry slider for this effect<br>
                   
<b>spawn</b>: spawn the currently highlighted effect<br>
                   
<b>volume</b>: output gain<br>
                   
<b>x</b>: delete this effect<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=eq></a><br>

### <b>eq</b>

<img src="images/eq.png"><br>

<div style="display:inline-block;margin-left:50px;">
multi-band equalizer, to adjust output levels at frequency ranges<br><br>
<b>enabled*</b>: enable this band?<br>
                   
<b>f*</b>: frequency cutoff for this band<br>
                   
<b>g*</b>: gain for this band<br>
                   
<b>q*</b>: resonance for this band<br>
                   
<b>type*</b>: what type of filter should this band use<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=feedback></a><br>

### <b>feedback</b>

<img src="images/feedback.png"><br>

<div style="display:inline-block;margin-left:50px;">
feed delayed audio back into earlier in the signal chain. use the "feedback out" connector for sending the audio back up the chain, and the primary output connector for sending the resulting audio forward. using feedback can often lead to extreme and difficult-to-control results!<br><br>
<b>limit</b>: clip the feedback audio to this range, to avoid issues with feedback blowing out too intensely.<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=fftvocoder></a><br>

### <b>fftvocoder</b>

<img src="images/fftvocoder.png"><br>

<div style="display:inline-block;margin-left:50px;">
FFT-based vocoder<br><br>
<b>carrier</b>: carrier signal gain<br>
                   
<b>cut</b>: how many bass partials to remove<br>
                   
<b>dry/wet</b>: how much original input vs vocoded signal to output<br>
                   
<b>fric thresh</b>: fricative detection sensitivity, to switch between using the carrier signal and white noise for vocoding<br>
                   
<b>input</b>: input signal gain<br>
                   
<b>phase off</b>: how much we should offset the phase of the carrier signal's partials<br>
                   
<b>volume</b>: output gain<br>
                   
<b>whisper</b>: how much the carrier signal partial's phases should be randomized, which affects how whispery the output sound is<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=freqdelay></a><br>

### <b>freqdelay</b>

<img src="images/freqdelay.png"><br>

<div style="display:inline-block;margin-left:50px;">
delay effect with delay length based upon input notes<br><br>
<b>dry/wet</b>: how much of the effect to apply<br>
                   
<br>accepts: <font color=orange>notes</font> <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=gain></a><br>

### <b>gain</b>

<img src="images/gain.png"><br>

<div style="display:inline-block;margin-left:50px;">
adjusts volume of audio signal<br><br>
<b>gain</b>: amount to adjust signal. a value of 1 will cause no change to the signal.<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=input></a><br>

### <b>input</b>

<img src="images/input.png"><br>

<div style="display:inline-block;margin-left:50px;">
get audio from input source, like a microphone<br><br>
<b>ch</b>: which channel (or channels, if you want stereo) to use<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=inverter></a><br>

### <b>inverter</b>

<img src="images/inverter.png"><br>

<div style="display:inline-block;margin-left:50px;">
multiply a signal by -1. enables some pretty interesting effects when used with sends, to subtract out parts of signals when recombined.<br><br>
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=lissajous></a><br>

### <b>lissajous</b>

<img src="images/lissajous.png"><br>

<div style="display:inline-block;margin-left:50px;">
draw input audio as a lissajous curve. turn off "autocorrelation" in the module's triangle menu to use stereo channels to show stereo width.<br><br>
<b>scale</b>: visual scale of lissajous image<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=looper></a><br>

### <b>looper</b>

<img src="images/looper.png"><br>

<div style="display:inline-block;margin-left:50px;">
loop input audio. use with a "looperrecorder" for full functionality.<br><br>
<b> m </b>: take the contents of this looper and merge it into another. click this button on the merge source, then on the merge target.<br>
                   
<b>.5x</b>: make loop play at half speed<br>
                   
<b>2x</b>: make loop play at double speed<br>
                   
<b>auto</b>: should pitch shift auto-adjust as the transport tempo adjusts?<br>
                   
<b>b</b>: bake current volume into waveform<br>
                   
<b>capture</b>: when the next loop begins, record input for the duration of the loop<br>
                   
<b>clear</b>: clear the loop audio<br>
                   
<b>commit</b>: commit the current looperrecorder buffer to this loop<br>
                   
<b>copy</b>: take the contents of this looper and copy it onto another. click this button on the copy source, then on the copy target.<br>
                   
<b>decay</b>: amount to lower volume each loop<br>
                   
<b>fourtet</b>: use a textural trick I saw four tet illustrate in a video once: slice the audio into chunks, and for each chunk it at double speed followed by playing it in reverse at double speed. this slider adjusts the mix between the original audio and this "fourtetified" audio.<br>
                   
<b>fourtetslices</b>: chunk size to use for "fourtet" effect<br>
                   
<b>mute</b>: silence this looper<br>
                   
<b>num bars</b>: loop length in measures<br>
                   
<b>offset</b>: amount to offset looper's playhead from transport position<br>
                   
<b>pitch</b>: amount to pitch shift looper output<br>
                   
<b>resample for tempo</b>: this button appears when the current global tempo no longer matches the tempo that the buffer was recorded at. click this to resample the buffer to match the new tempo.<br>
                   
<b>save</b>: save this loop to a wav file<br>
                   
<b>scr</b>: allow loop to be scrached by adjusting "scrspd"<br>
                   
<b>scrspd</b>: playback speed, used with "scr" is enabled. modulate quickly for a vinyl-like scratching effect.<br>
                   
<b>set</b>: shift the contents of the looper so the current offset is the start of the buffer<br>
                   
<b>swap</b>: swap the contents of this looper and with another. click this button on two loopers to swap them.<br>
                   
<b>undo</b>: undo last loop commit<br>
                   
<b>volume</b>: output volume<br>
                   
<b>write</b>: write input audio to loop buffer<br>
                   
<br>accepts: <font color=orange>notes</font> <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=looperrecorder></a><br>

### <b>looperrecorder</b>

<img src="images/looperrecorder.png"><br>

<div style="display:inline-block;margin-left:50px;">
command center to manage recording into multiple loopers, and allow retroactive loop capture (i.e., always-on recording)<br><br>
<b>.5tempo</b>: halve global transport tempo, while keeping connected loopers sounding the same<br>
                   
<b>1</b>: capture the last measure to the currently-targeted looper<br>
                   
<b>2</b>: capture the last 2 measures to the currently-targeted looper<br>
                   
<b>2xtempo</b>: double global transport tempo, while keeping connected loopers sounding the same<br>
                   
<b>4</b>: capture the last 4 measures to the currently-targeted looper<br>
                   
<b>8</b>: capture the last 8 measures to the currently-targeted looper<br>
                   
<b>cancel free rec</b>: if "free rec" is enabled, cancel recording without setting the loop length<br>
                   
<b>clear</b>: clear the recorded buffer<br>
                   
<b>free rec</b>: enable to start recording a loop with no predetermined length. disable to end recording, adjust global transport to match the loop length, and switch the recorder's mode to "loop"<br>
                   
<b>length</b>: length in measures to use when connected loopers use the "commit" button<br>
                   
<b>mode</b>: recorder mode: use "record" to record input and allow it to be committed to buffers when you're ready to loop, use "overdub" to record input and play the loop at our specified length, and use "loop" to play the current loop without adding input<br>
                   
<b>orig speed</b>: reset looper to tempo that loops were recorded at<br>
                   
<b>resample</b>: resample all connected loopers to new tempo<br>
                   
<b>resample & set key</b>: snap tempo to nearest value that matches a key (based upon the current key and the tempo change), resample all connected loopers to that new tempo, and change global scale to the new key<br>
                   
<b>snap to pitch</b>: snap tempo to nearest value that matches a key<br>
                   
<b>target</b>: looper to commit audio to when using the on-buffer capture buttons to the left<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=looperrewriter></a><br>

### <b>looperrewriter</b>

<img src="images/looperrewriter.png"><br>

<div style="display:inline-block;margin-left:50px;">
rewrites the contents of a looper with received input, to help you resample your own loops. attach the grey dot to a "looper" module.

the ideal way to use this module is to hook the "looper" directly up to a "send", hook the leftmost outlet of the "send" up to your effects processing (like an "effectchain"), hook the effect processing up to this "rewriter", and then also connect the rightmost outlet of the "send" up to this "rewriter"<br><br>
<b> go </b>: rewrite the connected looper, and if that looper is connected to a send, set that send to output only to the right outlet<br>
                   
<b>new loop</b>: start recording a dynamic loop length. press "go" when you want to rewrite it to the looper. this will also change bespoke's global tempo to match this new loop, so it's quite powerful and scary! click it again to cancel.<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=multitapdelay></a><br>

### <b>multitapdelay</b>

<img src="images/multitapdelay.png"><br>

<div style="display:inline-block;margin-left:50px;">
delay with multiple tap points<br><br>
<b>delay *</b>: tap delay time, in milliseconds<br>
                   
<b>display length</b>: length of buffer display, in seconds<br>
                   
<b>dry</b>: how much dry signal to allow through<br>
                   
<b>feedback *</b>: how much delayed audio from this tap should feed back in to the input<br>
                   
<b>gain *</b>: tap delay amount<br>
                   
<b>pan *</b>: stereo pan for this tap<br>
                   
<br>accepts: <font color=orange>notes</font> <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=output></a><br>

### <b>output</b>

<img src="images/output.png"><br>

<div style="display:inline-block;margin-left:50px;">
route audio in here to send it to an output channel (your speakers or audio interface)<br><br>
<b>ch</b>: channel (or channels, if you want stereo) to send audio to<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=panner></a><br>

### <b>panner</b>

<img src="images/panner.png"><br>

<div style="display:inline-block;margin-left:50px;">
pan audio left and right. also, converts a mono input to a stereo output.<br><br>
<b>pan</b>: amount to send signal to the left and right channels. a value of .5 is centered.<br>
                   
<b>widen</b>: delay a channel by this many samples. results in a pan-like effect where the sound seems to come from from a direction.<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=ringmodulator></a><br>

### <b>ringmodulator</b>

<img src="images/ringmodulator.png"><br>

<div style="display:inline-block;margin-left:50px;">
modulate a signal's amplitude at a frequency<br><br>
<b>dry/wet</b>: how much of the original audio to use vs modulated audio<br>
                   
<b>freq</b>: frequency to use. can also be set by patching a note input into this module.<br>
                   
<b>glide</b>: how long an input note should take to glide to the desired frequency<br>
                   
<b>volume</b>: volume output<br>
                   
<br>accepts: <font color=orange>notes</font> <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=samplergrid></a><br>

### <b>samplergrid</b>

<img src="images/samplergrid.png"><br>

<div style="display:inline-block;margin-left:50px;">
record input onto pads, and play back the pads. intended to be used with an 64-pad grid controller.<br><br>
<b>clear</b>: when enabled, clears any pressed grid squares<br>
                   
<b>duplicate</b>: what enabled, duplicates last pressed sample onto any pressed grid squares<br>
                   
<b>edit</b>: enable controls to adjust recorded sample for last pressed grid square<br>
                   
<b>end</b>: sample end<br>
                   
<b>grid</b>: patch a grid in here from a "midicontroller" module<br>
                   
<b>passthrough</b>: should the incoming audio pass through to the output?<br>
                   
<b>start</b>: sample start<br>
                   
<b>vol</b>: the output volume<br>
                   
<br>accepts: <font color=orange>notes</font> <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=send></a><br>

### <b>send</b>

<img src="images/send.png"><br>

<div style="display:inline-block;margin-left:50px;">
duplicate a signal and send it to a second destination<br><br>
<b>amount</b>: amount to send out the right-side cable<br>
                   
<b>crossfade</b>: when true, output of the left-side cable is reduced as "amount" increases<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=signalclamp></a><br>

### <b>signalclamp</b>

<img src="images/signalclamp.png"><br>

<div style="display:inline-block;margin-left:50px;">
clamps an audio signal's value within a range<br><br>
<b>max</b>: maximum output value<br>
                   
<b>min</b>: minimum output value<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=spectrum></a><br>

### <b>spectrum</b>

<img src="images/spectrum.png"><br>

<div style="display:inline-block;margin-left:50px;">
display audio signal's spectral data<br><br>
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=splitter></a><br>

### <b>splitter</b>

<img src="images/splitter.png"><br>

<div style="display:inline-block;margin-left:50px;">
splits a stereo signal into two mono signals, or duplicates a mono signal<br><br>
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=stutter></a><br>

### <b>stutter</b>

<img src="images/stutter.png"><br>

<div style="display:inline-block;margin-left:50px;">
captures and stutters input<br><br>
<b>16th</b>: 16th note stutter<br>
                   
<b>32nd</b>: 32nd note stutter<br>
                   
<b>64th</b>: 64th note stutter<br>
                   
<b>8th</b>: 8th note stutter<br>
                   
<b>dotted eighth</b>: stutter on a dotted eighth interval<br>
                   
<b>double speed</b>: stutter at double speed, high pitched<br>
                   
<b>free</b>: stutter with the settings specified by the following sliders<br>
                   
<b>free length</b>: length in seconds for "free" stutter mode<br>
                   
<b>free speed</b>: rate for "free" stutter mode<br>
                   
<b>grid</b>: patch a grid in here from a "midicontroller" module<br>
                   
<b>half note</b>: half note stutter<br>
                   
<b>half speed</b>: stutter at half speed, low pitched<br>
                   
<b>quarter</b>: quarter note stutter<br>
                   
<b>ramp in</b>: stutter with speed climbing up from zero to one<br>
                   
<b>ramp out</b>: stutter with speed quickly falling to zero<br>
                   
<b>reverse</b>: reversed half note stutter<br>
                   
<b>triplets</b>: stutter on a triplet interval<br>
                   
<b>tumble down</b>: decelerating stutter<br>
                   
<b>tumble up</b>: accelerating stutter<br>
                   
<br>accepts: <font color=orange>notes</font> <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=vocoder></a><br>

### <b>vocoder</b>

<img src="images/vocoder.png"><br>

<div style="display:inline-block;margin-left:50px;">
frequency band-based vocoder. this must be paired with a "vocodercarrier" module. voice should be routed into this module, and a synth should be patched into the vocodercarrier.<br><br>
<b>bands</b>: how many frequency bands to use<br>
                   
<b>carrier</b>: carrier signal gain<br>
                   
<b>f base</b>: frequency for lowest band<br>
                   
<b>f range</b>: frequency range to highest band<br>
                   
<b>input</b>: input signal gain<br>
                   
<b>max band</b>: volume limit for each frequency band<br>
                   
<b>mix</b>: how much original input vs vocoded signal to output<br>
                   
<b>q</b>: resonance of the bands<br>
                   
<b>ring</b>: how long it should take the bands to "cool down"<br>
                   
<b>spacing</b>: how frequency bands should be spaced<br>
                   
<b>volume</b>: output gain<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=vocodercarrier></a><br>

### <b>vocodercarrier</b>

<img src="images/vocodercarrier.png"><br>

<div style="display:inline-block;margin-left:50px;">
connect to "vocoder" or "fftvocoder" modules. send the synth audio into this module, and the voice audio into the vocoder module.<br><br>
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=waveformviewer></a><br>

### <b>waveformviewer</b>

<img src="images/waveformviewer.png"><br>

<div style="display:inline-block;margin-left:50px;">
waveform display<br><br>
<b>draw gain</b>: adjust waveform display scale<br>
                   
<b>freq</b>: frequency to sync display to. gets automatically set if you patch a note input into this module<br>
                   
<b>length</b>: number of samples to capture<br>
                   
<br>accepts: <font color=orange>notes</font> <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=waveshaper></a><br>

### <b>waveshaper</b>

<img src="images/waveshaper.png"><br>

<div style="display:inline-block;margin-left:50px;">
waveshaping with expressions<br><br>
<b>a</b>: variable to use in expressions<br>
                   
<b>b</b>: variable to use in expressions<br>
                   
<b>c</b>: variable to use in expressions<br>
                   
<b>d</b>: variable to use in expressions<br>
                   
<b>e</b>: variable to use in expressions<br>
                   
<b>rescale</b>: rescales input before feeding it into expression<br>
                   
<b>y=</b>: waveshaping expression. try something like "x+sin(x*pi*a)". available variables: a,b,c,d,e = the slider + sin(s below. t = time. x1,x2,y1,y2 = biquad state storage.<br>
                   
<br>accepts: <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>
