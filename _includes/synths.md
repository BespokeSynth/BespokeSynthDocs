
# synths
         
<a name=beats></a><br>

### <b>beats</b>

<img src="images/beats.png"><br>

<div style="display:inline-block;margin-left:50px;">
multi-loop player, for mixing sample layers together<br><br>
<b>bars*</b>: how many measures long are the samples in this slot?<br>
                   
<b>double*</b>: enable this to play at double speed<br>
                   
<b>filter*</b>: layer filter. negative values bring in a low pass, positive values bring in a high pass.<br>
                   
<b>pan*</b>: layer panorama<br>
                   
<b>selector*</b>: which sample should we play in this slot? drag samples onto here to add them to this slot.<br>
                   
<b>volume*</b>: layer volume<br>
                   
<br><br><br><br></div>

<a name=drumplayer></a><br>

### <b>drumplayer</b>

<img src="images/drumplayer.png"><br>

<div style="display:inline-block;margin-left:50px;">
sample player intended for drum playback<br><br>
<b>aud</b>: scroll to audition samples in the current pad's head category, or a directory last dropped onto a pad<br>
                   
<b>edit</b>: show pads for editing<br>
                   
<b>envelope *</b>: should we apply a volume envelope to the sample?<br>
                   
<b>envelopedisplay *A</b>: envelope attack<br>
                   
<b>envelopedisplay *D</b>: envelope decay<br>
                   
<b>envelopedisplay *R</b>: envelope release<br>
                   
<b>envelopedisplay *S</b>: envelope sustain<br>
                   
<b>grid</b>: patch a grid in here from a "midicontroller" module<br>
                   
<b>hitcategory*</b>: folder to choose from, when clicking the "random" button. these folders are found in the data/drums/hits/ directory<br>
                   
<b>linkid *</b>: if linkid is not -1, silence any other sample with a matching linkid (useful for linking open and closed hats)<br>
                   
<b>mono</b>: force output to mono<br>
                   
<b>pan *</b>: stereo pan position of sample<br>
                   
<b>quantize</b>: quantize input to this interval<br>
                   
<b>random *</b>: choose a random sample from the selected hitcategory<br>
                   
<b>repeat</b>: if quantizing, should held notes repeat at that interval?<br>
                   
<b>shuffle</b>: random is samples, speeds, and pans<br>
                   
<b>single out *</b>: should the sample have its own individual output?<br>
                   
<b>speed</b>: global sample speed multiplier<br>
                   
<b>speed *</b>: speed of sample<br>
                   
<b>speed rnd</b>: global sample speed randomization amount<br>
                   
<b>start *</b>: start offset percentage of sample<br>
                   
<b>test *</b>: play this sample<br>
                   
<b>view ms *</b>: envelope view length in milliseconds<br>
                   
<b>vol</b>: the output volume<br>
                   
<b>vol *</b>: volume of sample <br>
                   
<b>widen *</b>: stereo delay of sample to create width<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=drumsynth></a><br>

### <b>drumsynth</b>

<img src="images/drumsynth.png"><br>

<div style="display:inline-block;margin-left:50px;">
oscillator+noise drum synth<br><br>
<b>cutoffmax*</b>: filter start cutoff frequency<br>
                   
<b>cutoffmin*</b>: filter end cutoff frequency<br>
                   
<b>edit</b>: display parameters for each hit<br>
                   
<b>freqmax*</b>: oscillator start frequency<br>
                   
<b>freqmin*</b>: oscillator end frequency<br>
                   
<b>noise*</b>: noise volume<br>
                   
<b>q*</b>: filter resonance<br>
                   
<b>type*</b>: oscillator type<br>
                   
<b>vol</b>: the output volume<br>
                   
<b>vol*</b>: oscillator volume<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=fmsynth></a><br>

### <b>fmsynth</b>

<img src="images/fmsynth.png"><br>

<div style="display:inline-block;margin-left:50px;">
polyphonic fm synthesis<br><br>
<b>harmratio</b>: harmonic ratio of first-order modulator to input pitch<br>
                   
<b>harmratio2</b>: harmonic ratio of second-order modulator to input pitch<br>
                   
<b>mod</b>: amount to modulate first-order modulator<br>
                   
<b>mod2</b>: amount to modulate second-order modulator<br>
                   
<b>phase0</b>: phase offset for base oscillator<br>
                   
<b>phase1</b>: phase offset for first-order modulator<br>
                   
<b>phase2</b>: phase offset for second-order modulator<br>
                   
<b>tweak</b>: multiplier to harmonic ratio for first-order modulator<br>
                   
<b>tweak2</b>: multiplier to harmonic ratio for second-order modulator<br>
                   
<b>vol</b>: the output volume<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=karplusstrong></a><br>

### <b>karplusstrong</b>

<img src="images/karplusstrong.png"><br>

<div style="display:inline-block;margin-left:50px;">
polyphonic plucked string physical modeling synth<br><br>
<b>feedback</b>: amount of feedback for resonance<br>
                   
<b>filter</b>: amount to filter resonance<br>
                   
<b>invert</b>: should the feedback invert?<br>
                   
<b>lite cpu</b>: only recalculate some parameters once per buffer, to reduce CPU load. can make pitch bends and rapid modulation sound worse in some scenarios.<br>
                   
<b>pitchtone</b>: adjust how pitch influences filter amount. a value of zero gives even filtering across the entire pitch range, higher values filter high pitches less, low values filter low pitches less.<br>
                   
<b>source type</b>: audio to use for excitation<br>
                   
<b>vel2env</b>: how much velocity should affect excitation attack time<br>
                   
<b>vel2vol</b>: how much velocity should affect voice volume<br>
                   
<b>vol</b>: output volume<br>
                   
<b>x att</b>: fade in time for excitation audio<br>
                   
<b>x dec</b>: fade out time for excitation audio<br>
                   
<b>x freq</b>: frequency of excitation audio<br>
                   
<br>accepts: <font color=orange>notes</font> <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=metronome></a><br>

### <b>metronome</b>

<img src="images/metronome.png"><br>

<div style="display:inline-block;margin-left:50px;">
beeps to the beat<br><br>
<b>vol</b>: metronome volume<br>
                   
<br><br><br><br></div>

<a name=oscillator></a><br>

### <b>oscillator</b>

<img src="images/oscillator.png"><br>

<div style="display:inline-block;margin-left:50px;">
polyphonic enveloped oscillator. modulations (with MPE support): modwheel closes filter further (if filter is enabled), pressure decreases detune amount<br><br>
<b>adsr len</b>: view length of ADSR controls<br>
                   
<b>detune</b>: when unison is 1, detunes oscillator by this amount. when unison is 2, one oscillator is tuned normally and the other is detuned by this amount. when unison is >2, oscillators are randomly detuned within this range.<br>
                   
<b>envA</b>: volume envelope attack<br>
                   
<b>envD</b>: volume envelope decay<br>
                   
<b>envR</b>: volume envelope release<br>
                   
<b>envS</b>: volume envelope sustain<br>
                   
<b>envfilterA</b>: filter envelope attack<br>
                   
<b>envfilterD</b>: filter envelope decay<br>
                   
<b>envfilterR</b>: filter envelope release<br>
                   
<b>envfilterS</b>: filter envelope sustain<br>
                   
<b>fmax</b>: frequency cutoff of lowpass filter at the max of the envelope. set this slider to the max to disable the filter<br>
                   
<b>fmin</b>: frequency cutoff of lowpass filter at the min of the envelope<br>
                   
<b>lite cpu</b>: only recalculate some parameters once per buffer, to reduce CPU load. can make pitch bends and rapid modulation sound worse in some scenarios.<br>
                   
<b>mult</b>: multiply frequency of incoming pitch<br>
                   
<b>osc</b>: oscillator type<br>
                   
<b>phase</b>: phase offset of oscillator, and phase offset between unison voices. useful to patch into with a very fast modulator, to achieve phase modulation.<br>
                   
<b>pw</b>: pulse width (or shape for non-square waves)<br>
                   
<b>q</b>: resonance of lowpass filter<br>
                   
<b>shuffle</b>: stretches and squeezes every other cycle of the waveform<br>
                   
<b>soften</b>: soften edges of square and saw waveforms<br>
                   
<b>sync</b>: turns on "sync" mode, to reset the phase at syncf's frequency<br>
                   
<b>syncf</b>: frequency to reset the phase, when "sync" is enabled<br>
                   
<b>unison</b>: how many oscillators to play for one note<br>
                   
<b>vel2env</b>: how much should the input velocity affect the speed of the volume and filter envelopes?<br>
                   
<b>vel2vol</b>: how much should the input velocity affect the output volume?<br>
                   
<b>vol</b>: this oscillator's volume<br>
                   
<b>width</b>: controls how voices are panned with unison is greater than 1<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=samplecanvas></a><br>

### <b>samplecanvas</b>

<img src="images/samplecanvas.png"><br>

<div style="display:inline-block;margin-left:50px;">
sample arranging view<br><br>
<b>canvas</b>: canvas of samples. drag and drop samples onto here. canvas controls:
-hold shift and drag a sample to duplicate
-hold alt to drag a sample without snapping
-hold ctrl while dragging to snap to an interval
-hold shift and scroll to zoom
-hold alt and grab empty space to move slide the canvas view
-hold ctrl and grab empty space to zoom the canvas view<br>
                   
<b>clear</b>: delete all elements<br>
                   
<b>delete</b>: delete highlighted elements<br>
                   
<b>drag mode</b>: direction that elements can be dragged<br>
                   
<b>interval</b>: grid subdivision interval<br>
                   
<b>measures</b>: length of canvas in measures<br>
                   
<b>scrollh</b>: horizontal scrollbar<br>
                   
<b>scrollv</b>: vertical scrollbar<br>
                   
<b>timeline</b>: control loop points<br>
                   
<b>view rows</b>: number of visible rows<br>
                   
<br><br><br><br></div>

<a name=sampleplayer></a><br>

### <b>sampleplayer</b>

<img src="images/sampleplayer.png"><br>

<div style="display:inline-block;margin-left:50px;">
sample playback with triggerable cue points, clip extraction, and youtube search/download functionality. resize this module larger to access additional features. if you have a youtube URL in your clipboard, a button will appear to allow you to download the audio.<br><br>
<b>16</b>: auto-slice 16 slices<br>
                   
<b>32</b>: auto-slice 32 slices<br>
                   
<b>4</b>: auto-slice 4 slices<br>
                   
<b>8</b>: auto-slice 8 slices<br>
                   
<b>append to rec</b>: when recording, append to the previous recording, rather than clearing the sample first<br>
                   
<b>attack</b>: speed at which gate blends open<br>
                   
<b>click sets cue</b>: when true, clicking on the waveform will set the start position of the current cue<br>
                   
<b>cue len</b>: length in seconds of the current cue. a value of zero will play to the end of the sample.<br>
                   
<b>cue speed</b>: playback speed of the current cue<br>
                   
<b>cue start</b>: start point in seconds of the current cue<br>
                   
<b>cuepoint</b>: sets the current cue to edit<br>
                   
<b>grabhovered</b>: grab a sample of this cue to drop onto another module<br>
                   
<b>load</b>: show a file chooser to load a sample<br>
                   
<b>loop</b>: wrap playhead to beginning when it reaches end<br>
                   
<b>pause</b>: pause playing and leave playhead where it is<br>
                   
<b>play</b>: start playing from the current playhead<br>
                   
<b>play cue</b>: play the current cue<br>
                   
<b>playhovered</b>: play this cue<br>
                   
<b>record</b>: record audio input into our sample buffer. clears the current sample.<br>
                   
<b>record as clips</b>: when recording, only record when there is enough input to open the gate, and mark up each recorded segment with cue points<br>
                   
<b>release</b>: speed at which gate blends closed<br>
                   
<b>save</b>: save this sample to a file<br>
                   
<b>searchresult*</b>: click to download this youtube search result. downloading long videos may take a while.<br>
                   
<b>select played</b>: when true, any cue point played via incoming notes will become the current cue<br>
                   
<b>show grid</b>: show a quarter note grid (when zoomed in far enough)<br>
                   
<b>speed</b>: current playback speed<br>
                   
<b>stop</b>: stop playing and reset playhead<br>
                   
<b>threshold</b>: volume threshold to open up the gate for recording<br>
                   
<b>trim</b>: discard all audio outside the current zoom range<br>
                   
<b>volume</b>: output gain<br>
                   
<b>youtube</b>: download the audio of the youtube URL currently on your clipboard<br>
                   
<b>yt:</b>: search youtube for this string<br>
                   
<br>accepts: <font color=orange>notes</font> <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=sampler></a><br>

### <b>sampler</b>

<img src="images/sampler.png"><br>

<div style="display:inline-block;margin-left:50px;">
very basic polyphonic pitched sample player and recorder. send audio in, and use note input to play the recorded audio.<br><br>
<b>env</b>: volume envelope<br>
                   
<b>envA</b>: volume envelope attack<br>
                   
<b>envD</b>: volume envelope decay<br>
                   
<b>envR</b>: volume envelope release<br>
                   
<b>envS</b>: volume envelope sustain<br>
                   
<b>passthrough</b>: should input audio pass through as we're recording?<br>
                   
<b>pitch</b>: should we attempt pitch-correct the audio?<br>
                   
<b>rec</b>: enable to clear the current recording, and record new audio once the input threshold is reached<br>
                   
<b>thresh</b>: when recording is enabled, exceed this threshold with input audio to begin recording<br>
                   
<b>vol</b>: output volume<br>
                   
<br>accepts: <font color=orange>notes</font> <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=seaofgrain></a><br>

### <b>seaofgrain</b>

<img src="images/seaofgrain.png"><br>

<div style="display:inline-block;margin-left:50px;">
granular synth, playable with sliders or MPE input<br><br>
<b>display length</b>: amount of sample to view<br>
                   
<b>gain *</b>: volume of this voice<br>
                   
<b>keyboard base pitch</b>: midi pitch that represents the start of the sample<br>
                   
<b>keyboard num pitches</b>: amount of pitches to assign across the sample<br>
                   
<b>len ms *</b>: length of each grain in milliseconds<br>
                   
<b>load</b>: load a sample file<br>
                   
<b>octaves *</b>: should we add octaves and fifths?<br>
                   
<b>offset</b>: where to start view of the sample<br>
                   
<b>overlap *</b>: number of overlapping grains<br>
                   
<b>pan *</b>: stereo panorama of grain placement<br>
                   
<b>pos *</b>: position of this voice within the sample<br>
                   
<b>pos r *</b>: randomization of grain start point<br>
                   
<b>record</b>: record input as the granular buffer, to use seaofgrain a live granular delay<br>
                   
<b>spacing r*</b>: randomization of time between grains<br>
                   
<b>speed *</b>: speed of grain playback<br>
                   
<b>speed r *</b>: randomization of grain speed<br>
                   
<b>volume</b>: output volume<br>
                   
<b>width *</b>: stereo width of grain placement<br>
                   
<br>accepts: <font color=orange>notes</font> <font color=cyan>audio</font> <br>
             
<br><br><br><br></div>

<a name=signalgenerator></a><br>

### <b>signalgenerator</b>

<img src="images/signalgenerator.png"><br>

<div style="display:inline-block;margin-left:50px;">
basic oscillator signal<br><br>
<b>detune</b>: amount to detune from specified frequency<br>
                   
<b>freq</b>: signal frequency<br>
                   
<b>freq mode</b>: what mode should we use for input notes? "instant" changes to the input note's frequency instantly, "ramp" ramps to the frequency over time, and "slider" allows you to use a slider to interpolate between the last two input notes<br>
                   
<b>mult</b>: multiplier for frequency<br>
                   
<b>osc</b>: oscillator type<br>
                   
<b>phase</b>: phase offset<br>
                   
<b>pw</b>: pulse width (or shape for non-square waves)<br>
                   
<b>ramp</b>: amount of time to ramp to input frequency<br>
                   
<b>shuffle</b>: stretches and squeezes every other cycle of the waveform<br>
                   
<b>slider</b>: slider to interpolate between last two input pitches<br>
                   
<b>soften</b>: soften edges of square and saw waveforms<br>
                   
<b>sync</b>: turns on "sync" mode, to reset the phase at syncf's frequency<br>
                   
<b>syncf</b>: frequency to reset the phase, when "sync" is enabled<br>
                   
<b>vol</b>: output volume<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>
