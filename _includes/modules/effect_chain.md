
# effect chain
         
<a name=basiceq></a><br>

### <b>basiceq</b>

<img src="https://www.bespokesynth.com/docs/screenshots/basiceq.png"><br>

<div style="display:inline-block;margin-left:50px;">
simple multiband EQ<br><br>
<b>even</b>: reset EQ<br>
                   
<br><br><br><br></div>

<a name=biquad></a><br>

### <b>biquad</b>

<img src="https://www.bespokesynth.com/docs/screenshots/biquad.png"><br>

<div style="display:inline-block;margin-left:50px;">
filter using biquad formula<br><br>
<b>F</b>: frequency cutoff<br>
                   
<b>G</b>: gain<br>
                   
<b>Q</b>: resonance<br>
                   
<b>type</b>: filter type<br>
                   
<br><br><br><br></div>

<a name=bitcrush></a><br>

### <b>bitcrush</b>

<img src="https://www.bespokesynth.com/docs/screenshots/bitcrush.png"><br>

<div style="display:inline-block;margin-left:50px;">
reduce sample resolution and sample rate for lo-fi effects<br><br>
<b>crush</b>: sample resolution reduction<br>
                   
<b>downsamp</b>: sample rate reduction<br>
                   
<br><br><br><br></div>

<a name=butterworth></a><br>

### <b>butterworth</b>

<img src="https://www.bespokesynth.com/docs/screenshots/butterworth.png"><br>

<div style="display:inline-block;margin-left:50px;">
filter using the butterworth formula<br><br>
<b>F</b>: frequency cutoff<br>
                   
<b>Q</b>: resonance<br>
                   
<br><br><br><br></div>

<a name=compressor></a><br>

### <b>compressor</b>

<img src="https://www.bespokesynth.com/docs/screenshots/compressor.png"><br>

<div style="display:inline-block;margin-left:50px;">
try to keep volume at a certain level<br><br>
<b>attack</b>: speed to apply gain reduction<br>
                   
<b>lookahead</b>: how much time to "look ahead" to adjust the compression envelope. this necessarily introduces a delay into your output, which could be compensated for by running sequencers slightly early.<br>
                   
<b>mix</b>: amount of compression. lower this value for a "parallel compression" effect. you should use this mix slider instead of the effectchain's mix slider, to compensate for lookahead.<br>
                   
<b>output</b>: makeup gain, to increase volume<br>
                   
<b>ratio</b>: how much gain reduction to apply when the single passes the threshold<br>
                   
<b>release</b>: speed to remove gain reduction<br>
                   
<b>threshold</b>: threshold where gain should start to be reduced<br>
                   
<br><br><br><br></div>

<a name=dcremover></a><br>

### <b>dcremover</b>

<img src="https://www.bespokesynth.com/docs/screenshots/dcremover.png"><br>

<div style="display:inline-block;margin-left:50px;">
high pass filter with a 10hz cutoff to remove DC offset, to keep signal from drifting away from zero<br><br>
<br><br><br><br></div>

<a name=delay></a><br>

### <b>delay</b>

<img src="https://www.bespokesynth.com/docs/screenshots/delay.png"><br>

<div style="display:inline-block;margin-left:50px;">
echoing delay<br><br>
<b>amount</b>: amount of delay that returns<br>
                   
<b>delay</b>: delay in milliseconds<br>
                   
<b>dry</b>: should the dry signal pass through, or just the delayed signal?<br>
                   
<b>feedback</b>: should the output audio feed back into the delay?<br>
                   
<b>input</b>: should we accept input into the delay?<br>
                   
<b>interval</b>: sets delay length to a musical duration<br>
                   
<b>invert</b>: should the delayed audio have its signal inverted? this can give a different sound, and also cancel out DC offset to prevent it from accumulating with feedback.<br>
                   
<b>short</b>: shortcut to shrink the range of the delay slider, to allow for audible-rate delays and comb filter sounds<br>
                   
<br><br><br><br></div>

<a name=distortion></a><br>

### <b>distortion</b>

<img src="https://www.bespokesynth.com/docs/screenshots/distortion.png"><br>

<div style="display:inline-block;margin-left:50px;">
waveshaping distortion<br><br>
<b>center input</b>: remove dc offset from input signal to distort in a more controlled way<br>
                   
<b>clip</b>: cutoff point of distortion, lower values result in more extreme distortion<br>
                   
<b>fuzz</b>: push input signal off-center to distort asymmetrically<br>
                   
<b>preamp</b>: signal gain before feeding into distortion<br>
                   
<b>type</b>: style of distortion to apply<br>
                   
<br><br><br><br></div>

<a name=freeverb></a><br>

### <b>freeverb</b>

<img src="https://www.bespokesynth.com/docs/screenshots/freeverb.png"><br>

<div style="display:inline-block;margin-left:50px;">
reverb using the "freeverb" algorithm<br><br>
<b>damp</b>: high frequency attenuation; a value of zero means all frequencies decay at the same rate, while higher settings will result in a faster decay of the high frequency range<br>
                   
<b>dry</b>: amount of untouched signal<br>
                   
<b>room size</b>: controls the length of the reverb, a higher value means longer reverb<br>
                   
<b>wet</b>: amount of reverb signal<br>
                   
<b>width</b>: stereo width of reverb<br>
                   
<br><br><br><br></div>

<a name=gainstage></a><br>

### <b>gainstage</b>

<img src="https://www.bespokesynth.com/docs/screenshots/gainstage.png"><br>

<div style="display:inline-block;margin-left:50px;">
control volume within an effectchain<br><br>
<b>gain</b>: volume multiplier<br>
                   
<br><br><br><br></div>

<a name=gate></a><br>

### <b>gate</b>

<img src="https://www.bespokesynth.com/docs/screenshots/gate.png"><br>

<div style="display:inline-block;margin-left:50px;">
only allow signal in when it's above a certain threshold. useful to eliminate line noise, or just as an effect.<br><br>
<b>attack</b>: speed at which gate blends open<br>
                   
<b>release</b>: speed at which gate blends closed<br>
                   
<b>threshold</b>: volume threshold to open up the gate<br>
                   
<br><br><br><br></div>

<a name=granulator></a><br>

### <b>granulator</b>

<img src="https://www.bespokesynth.com/docs/screenshots/granulator.png"><br>

<div style="display:inline-block;margin-left:50px;">
granulate live input<br><br>
<b>autocapture</b>: freeze input at this interval<br>
                   
<b>dry</b>: amount of dry signal to allow through<br>
                   
<b>frz</b>: freeze the current recorded buffer<br>
                   
<b>g oct</b>: should we add octaves and fifths?<br>
                   
<b>len ms</b>: length of each grain in milliseconds<br>
                   
<b>overlap</b>: number of overlapping grains<br>
                   
<b>pos</b>: playback position within the buffer<br>
                   
<b>pos r</b>: randomization of grain start point<br>
                   
<b>spa r</b>: randomization of time between grains<br>
                   
<b>spd r</b>: randomization of grain speed<br>
                   
<b>speed</b>: speed of grain playback<br>
                   
<b>width</b>: stereo width of grain placement<br>
                   
<br><br><br><br></div>

<a name=muter></a><br>

### <b>muter</b>

<img src="https://www.bespokesynth.com/docs/screenshots/muter.png"><br>

<div style="display:inline-block;margin-left:50px;">
mute an incoming signal<br><br>
<b>ms</b>: ramp time to mute/unmute signal<br>
                   
<b>pass</b>: when true, the signal is allowed through<br>
                   
<br><br><br><br></div>

<a name=noisify></a><br>

### <b>noisify</b>

<img src="https://www.bespokesynth.com/docs/screenshots/noisify.png"><br>

<div style="display:inline-block;margin-left:50px;">
multiply input signal by white noise<br><br>
<b>amount</b>: amount of noise to apply<br>
                   
<b>width</b>: how frequently a new noise sample should be chosen<br>
                   
<br><br><br><br></div>

<a name=pitchshift></a><br>

### <b>pitchshift</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pitchshift.png"><br>

<div style="display:inline-block;margin-left:50px;">
shifts a signal's pitch<br><br>
<b>ratio</b>: amount to pitchshift by (a value of 1 indicates no shift)<br>
                   
<b>ratioselector</b>: shortcuts to useful pitch ratios<br>
                   
<br><br><br><br></div>

<a name=pumper></a><br>

### <b>pumper</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pumper.png"><br>

<div style="display:inline-block;margin-left:50px;">
dip the volume of a signal rhythmically, to emulate a "pumping sidechain" effect<br><br>
<b>amount</b>: amount to lower volume<br>
                   
<b>attack</b>: how sharply the volume drops<br>
                   
<b>curve</b>: how the volume returns<br>
                   
<b>interval</b>: the rate to pump<br>
                   
<b>length</b>: length of pump<br>
                   
<br><br><br><br></div>

<a name=tremolo></a><br>

### <b>tremolo</b>

<img src="https://www.bespokesynth.com/docs/screenshots/tremolo.png"><br>

<div style="display:inline-block;margin-left:50px;">
modulate signal's volume rhythmically<br><br>
<b>amount</b>: amount to lower volume<br>
                   
<b>duty</b>: pulse width of LFO<br>
                   
<b>interval</b>: speed of LFO<br>
                   
<b>offset</b>: offsets LFO phase<br>
                   
<b>osc</b>: LFO oscillator type<br>
                   
<br><br><br><br></div>
