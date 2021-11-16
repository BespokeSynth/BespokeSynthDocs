
# note effects
         
<a name=arpeggiator></a><br>

### <b>arpeggiator</b>

<img src="https://www.bespokesynth.com/docs/screenshots/arpeggiator.png"><br>

<div style="display:inline-block;margin-left:50px;">
arpeggiates held notes. there are several vestigial features in this module that should be cleaned up.<br><br>
<b>interval</b>: arpeggiation rate<br>
                   
<b>octaves</b>: how many octaves to step through<br>
                   
<b>step</b>: direction and distance to step through arpeggiation. a value of zero is "pingpong".<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=capo></a><br>

### <b>capo</b>

<img src="https://www.bespokesynth.com/docs/screenshots/capo.png"><br>

<div style="display:inline-block;margin-left:50px;">
shifts incoming notes by semitones<br><br>
<b>capo</b>: number of semitones to shift<br>
                   
<b>retrigger</b>: immediately replay current notes when changing the capo amount<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=chorddisplayer></a><br>

### <b>chorddisplayer</b>

<img src="https://www.bespokesynth.com/docs/screenshots/chorddisplayer.png"><br>

<div style="display:inline-block;margin-left:50px;">
display which chord is playing, in the context of the current scale<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=chorder></a><br>

### <b>chorder</b>

<img src="https://www.bespokesynth.com/docs/screenshots/chorder.png"><br>

<div style="display:inline-block;margin-left:50px;">
takes an incoming pitch and plays additional notes to form chords<br><br>
<b>chord</b>: chord presets<br>
                   
<b>diatonic</b>: should the grid be chromatic, or locked to the scale only?<br>
                   
<b>inversion</b>: inversion presets<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=chordholder></a><br>

### <b>chordholder</b>

<img src="https://www.bespokesynth.com/docs/screenshots/chordholder.png"><br>

<div style="display:inline-block;margin-left:50px;">
keeps any notes pressed at the same time sustaining, until new notes are pressed<br><br>
<b>pulse to play</b>: when enabled, input notes aren't played immediately, but instead wait for an input pulse before playing<br>
                   
<b>stop</b>: stop notes from playing<br>
                   
<br>accepts: <font color=yellow>pulses</font> <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=gridnotedisplayer></a><br>

### <b>gridnotedisplayer</b>

<img src="https://www.bespokesynth.com/docs/screenshots/gridnotedisplayer.png"><br>

<div style="display:inline-block;margin-left:50px;">
use with a gridkeyboard to display currently playing notes, to visualize chords, arpeggiation, etc.<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=midicc></a><br>

### <b>midicc</b>

<img src="https://www.bespokesynth.com/docs/screenshots/midicc.png"><br>

<div style="display:inline-block;margin-left:50px;">
outputs midi control change messages to route to a "midioutput" module<br><br>
<b>control</b>: CC control number<br>
                   
<b>value</b>: outputs a CC value when this changes<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=midioutput></a><br>

### <b>midioutput</b>

<img src="https://www.bespokesynth.com/docs/screenshots/midioutput.png"><br>

<div style="display:inline-block;margin-left:50px;">
send midi to an external destination, such as hardware or other software<br><br>
<b>controller</b>: where to send midi to<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=modulationvizualizer></a><br>

### <b>modulationvizualizer</b>

<img src="https://www.bespokesynth.com/docs/screenshots/modulationvizualizer.png"><br>

<div style="display:inline-block;margin-left:50px;">
display MPE modulation values for notes<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=modwheel></a><br>

### <b>modwheel</b>

<img src="https://www.bespokesynth.com/docs/screenshots/modwheel.png"><br>

<div style="display:inline-block;margin-left:50px;">
adds an expression value to a note<br><br>
<b>modwheel</b>: expression level<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=modwheeltopressure></a><br>

### <b>modwheeltopressure</b>

<img src="https://www.bespokesynth.com/docs/screenshots/modwheeltopressure.png"><br>

<div style="display:inline-block;margin-left:50px;">
swaps expression input to midi pressure in the output<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=modwheeltovibrato></a><br>

### <b>modwheeltovibrato</b>

<img src="https://www.bespokesynth.com/docs/screenshots/modwheeltovibrato.png"><br>

<div style="display:inline-block;margin-left:50px;">
convert note mod wheel input rhythmic pitch bend<br><br>
<b>vibinterval</b>: rate of vibrato<br>
                   
<b>vibrato</b>: amount of pitch bend<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=mpetweaker></a><br>

### <b>mpetweaker</b>

<img src="https://www.bespokesynth.com/docs/screenshots/mpetweaker.png"><br>

<div style="display:inline-block;margin-left:50px;">
adjust incoming MPE modulation values<br><br>
<b>modwheel mult</b>: amount to multiply incoming modwheel<br>
                   
<b>modwheel offset</b>: amount to offset incoming modwheel<br>
                   
<b>pitchbend mult</b>: amount to multiply incoming pitchbend<br>
                   
<b>pitchbend offset</b>: amount to offset incoming pitchbend<br>
                   
<b>pressure mult</b>: amount to multiply incoming pressure<br>
                   
<b>pressure offset</b>: amount to offset incoming pressure<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notechance></a><br>

### <b>notechance</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notechance.png"><br>

<div style="display:inline-block;margin-left:50px;">
randomly allow notes through<br><br>
<b>chance</b>: probability that a note is allowed<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notedelayer></a><br>

### <b>notedelayer</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notedelayer.png"><br>

<div style="display:inline-block;margin-left:50px;">
delay input notes by a specified amount<br><br>
<b>delay</b>: amount of time to delay, in measures<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notedisplayer></a><br>

### <b>notedisplayer</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notedisplayer.png"><br>

<div style="display:inline-block;margin-left:50px;">
show input note info<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=noteduration></a><br>

### <b>noteduration</b>

<img src="https://www.bespokesynth.com/docs/screenshots/noteduration.png"><br>

<div style="display:inline-block;margin-left:50px;">
sets the length a note will play, ignoring the note-off message<br><br>
<b>duration</b>: length of the note in measures<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notefilter></a><br>

### <b>notefilter</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notefilter.png"><br>

<div style="display:inline-block;margin-left:50px;">
only allow a certain pitches through<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=noteflusher></a><br>

### <b>noteflusher</b>

<img src="https://www.bespokesynth.com/docs/screenshots/noteflusher.png"><br>

<div style="display:inline-block;margin-left:50px;">
send a note-off for all notes<br><br>
<b>flush</b>: click to flush notes<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notegate></a><br>

### <b>notegate</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notegate.png"><br>

<div style="display:inline-block;margin-left:50px;">
allow or disallow notes to pass through<br><br>
<b>open</b>: if notes are allowed to pass<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notehocket></a><br>

### <b>notehocket</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notehocket.png"><br>

<div style="display:inline-block;margin-left:50px;">
sends notes to random destinations<br><br>
<b>weight *</b>: chance that note goes to this destination<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notehumanizer></a><br>

### <b>notehumanizer</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notehumanizer.png"><br>

<div style="display:inline-block;margin-left:50px;">
add randomness to timing and velocity<br><br>
<b>time</b>: amount of timing randomness, in milliseconds.<br>
                   
<b>velocity</b>: amount of velocity randomness<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notelatch></a><br>

### <b>notelatch</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notelatch.png"><br>

<div style="display:inline-block;margin-left:50px;">
use note on messages to toggle notes on and off<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=noteoctaver></a><br>

### <b>noteoctaver</b>

<img src="https://www.bespokesynth.com/docs/screenshots/noteoctaver.png"><br>

<div style="display:inline-block;margin-left:50px;">
transpose a note by octaves<br><br>
<b>octave</b>: number of octaves to raise or lower<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notepanalternator></a><br>

### <b>notepanalternator</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notepanalternator.png"><br>

<div style="display:inline-block;margin-left:50px;">
sets a note's pan, alternating between two values, for the internal synths that support panned notes<br><br>
<b>one</b>: pan position, .5 is centered<br>
                   
<b>two</b>: pan position, .5 is centered<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notepanner></a><br>

### <b>notepanner</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notepanner.png"><br>

<div style="display:inline-block;margin-left:50px;">
sets a note's pan, for the internal synths that support panned notes<br><br>
<b>pan</b>: pan position, .5 is centered<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notepanrandom></a><br>

### <b>notepanrandom</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notepanrandom.png"><br>

<div style="display:inline-block;margin-left:50px;">
sets a note's pan to random values, for the internal synths that support panned notes<br><br>
<b>center</b>: center pan position<br>
                   
<b>spread</b>: amount of randomness<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=noterangefilter></a><br>

### <b>noterangefilter</b>

<img src="https://www.bespokesynth.com/docs/screenshots/noterangefilter.png"><br>

<div style="display:inline-block;margin-left:50px;">
only allows notes through within a certain pitch range<br><br>
<b>max</b>: maximum pitch allowed<br>
                   
<b>min</b>: minimum pitch allowed<br>
                   
<b>wrap</b>: instead of rejecting notes outside of this range, should we wrap them to the range instead?<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=noteratchet></a><br>

### <b>noteratchet</b>

<img src="https://www.bespokesynth.com/docs/screenshots/noteratchet.png"><br>

<div style="display:inline-block;margin-left:50px;">
rapidly repeat an input note over a duration<br><br>
<b>duration</b>: total length of time repeats should last<br>
                   
<b>subdivision</b>: length of each repeat<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=noterouter></a><br>

### <b>noterouter</b>

<img src="https://www.bespokesynth.com/docs/screenshots/noterouter.png"><br>

<div style="display:inline-block;margin-left:50px;">
allows you to control where notes are routed to using a UI control. to add destinations to the list, patch them as a target<br><br>
<b>route</b>: the noterouter's destination module<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notesorter></a><br>

### <b>notesorter</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notesorter.png"><br>

<div style="display:inline-block;margin-left:50px;">
separate notes by pitch. any unmapped pitches go through the standard outlet.<br><br>
<b>pitch *</b>: pitch to use for this outlet<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notestepper></a><br>

### <b>notestepper</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notestepper.png"><br>

<div style="display:inline-block;margin-left:50px;">
output notes through a round robin of patch cables, to create sequential variety<br><br>
<b>length</b>: length of the sequence<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notestream></a><br>

### <b>notestream</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notestream.png"><br>

<div style="display:inline-block;margin-left:50px;">
view a stream of notes as they're played<br><br>
<b>reset</b>: reset the pitch range<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notestrummer></a><br>

### <b>notestrummer</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notestrummer.png"><br>

<div style="display:inline-block;margin-left:50px;">
send a chord into this, and move a slider to strum each note of the chord<br><br>
<b>strum</b>: move the slider past each note to strum it<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=notewrap></a><br>

### <b>notewrap</b>

<img src="https://www.bespokesynth.com/docs/screenshots/notewrap.png"><br>

<div style="display:inline-block;margin-left:50px;">
wrap an input pitch to stay within a desired range<br><br>
<b>min</b>: bottom of pitch range<br>
                   
<b>range</b>: number of semitones before wrapping back down to min pitch<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=pitchbender></a><br>

### <b>pitchbender</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pitchbender.png"><br>

<div style="display:inline-block;margin-left:50px;">
add pitch bend to notes<br><br>
<b>bend</b>: bend amount, in semitones<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=pitchdive></a><br>

### <b>pitchdive</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pitchdive.png"><br>

<div style="display:inline-block;margin-left:50px;">
use pitchbend to settle into an input pitch from a starting offset<br><br>
<b>start</b>: semitone offset to start from<br>
                   
<b>time</b>: time in milliseconds to ramp from pitch offset into input pitch<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=pitchpanner></a><br>

### <b>pitchpanner</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pitchpanner.png"><br>

<div style="display:inline-block;margin-left:50px;">
add pan modulation to notes based upon input pitch, so low pitches are panned in one direction and high pitches are panned in another<br><br>
<b>left</b>: pitch that represents full left pan<br>
                   
<b>right</b>: pitch that represents full right pan<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=pitchremap></a><br>

### <b>pitchremap</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pitchremap.png"><br>

<div style="display:inline-block;margin-left:50px;">
remap input pitches to different output pitches<br><br>
<b>from*</b>: pitch to change<br>
                   
<b>to*</b>: desired pitch<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=pitchsetter></a><br>

### <b>pitchsetter</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pitchsetter.png"><br>

<div style="display:inline-block;margin-left:50px;">
set an incoming note to use a specified pitch<br><br>
<b>pitch</b>: the pitch to use<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=portamento></a><br>

### <b>portamento</b>

<img src="https://www.bespokesynth.com/docs/screenshots/portamento.png"><br>

<div style="display:inline-block;margin-left:50px;">
only allows one note to play at a time, and uses pitch bend to glide between notes<br><br>
<b>glide</b>: time to glide, in milliseconds<br>
                   
<b>require held</b>: if enabled, only glide to a new note if an old note is held. otherwise, always glide, based upon the prior input note.<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=pressure></a><br>

### <b>pressure</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pressure.png"><br>

<div style="display:inline-block;margin-left:50px;">
add pressure modulation to notes<br><br>
<b>pressure</b>: pressure amount<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=pressuretomodwheel></a><br>

### <b>pressuretomodwheel</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pressuretomodwheel.png"><br>

<div style="display:inline-block;margin-left:50px;">
takes midi pressure modulation input and changes it to modwheel modulation<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=pressuretovibrato></a><br>

### <b>pressuretovibrato</b>

<img src="https://www.bespokesynth.com/docs/screenshots/pressuretovibrato.png"><br>

<div style="display:inline-block;margin-left:50px;">
takes midi pressure modulation input and changes it to vibrato, using pitch bend<br><br>
<b>vibinterval</b>: vibrato speed<br>
                   
<b>vibrato</b>: amount of vibrato<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=previousnote></a><br>

### <b>previousnote</b>

<img src="https://www.bespokesynth.com/docs/screenshots/previousnote.png"><br>

<div style="display:inline-block;margin-left:50px;">
when receiving a note on, output the prior note on that we received<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=quantizer></a><br>

### <b>quantizer</b>

<img src="https://www.bespokesynth.com/docs/screenshots/quantizer.png"><br>

<div style="display:inline-block;margin-left:50px;">
delay inputs until the next quantization interval<br><br>
<b>quantize</b>: the quantization interval<br>
                   
<b>repeat</b>: when holding a note, should we repeat it every interval?<br>
                   
<br>accepts: <font color=yellow>pulses</font> <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=scaledegree></a><br>

### <b>scaledegree</b>

<img src="https://www.bespokesynth.com/docs/screenshots/scaledegree.png"><br>

<div style="display:inline-block;margin-left:50px;">
transpose input based on current scale<br><br>
<b>degree</b>: amount to transpose<br>
                   
<b>retrigger</b>: immediately replay current notes when changing the transpose amount<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=scaledetect></a><br>

### <b>scaledetect</b>

<img src="https://www.bespokesynth.com/docs/screenshots/scaledetect.png"><br>

<div style="display:inline-block;margin-left:50px;">
detect which scales fit a collection of entered notes. the last played pitch is used as the root.<br><br>
<b>matches</b>: matching scales for this root<br>
                   
<b>reset</b>: reset the input collection of notes<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=sustainpedal></a><br>

### <b>sustainpedal</b>

<img src="https://www.bespokesynth.com/docs/screenshots/sustainpedal.png"><br>

<div style="display:inline-block;margin-left:50px;">
keeps input notes sustaining<br><br>
<b>sustain</b>: should we hold the input notes?<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=transposefrom></a><br>

### <b>transposefrom</b>

<img src="https://www.bespokesynth.com/docs/screenshots/transposefrom.png"><br>

<div style="display:inline-block;margin-left:50px;">
transpose input from a specified root to the root of the current scale. the primary usage of this would be to allow you to play a keyboard in C, but it gets transposed to the current scale.<br><br>
<b>retrigger</b>: immediately replay current notes when changing the transpose root or the scale<br>
                   
<b>root</b>: root to transpose from<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=unstablemodwheel></a><br>

### <b>unstablemodwheel</b>

<img src="https://www.bespokesynth.com/docs/screenshots/unstablemodwheel.png"><br>

<div style="display:inline-block;margin-left:50px;">
mutate MPE slide with perlin noise<br><br>
<b>amount</b>: amount of mutation<br>
                   
<b>noise</b>: fast-later mutation rate<br>
                   
<b>warble</b>: slow-layer mutation rate<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=unstablepitch></a><br>

### <b>unstablepitch</b>

<img src="https://www.bespokesynth.com/docs/screenshots/unstablepitch.png"><br>

<div style="display:inline-block;margin-left:50px;">
mutate MPE pitchbend with perlin noise<br><br>
<b>amount</b>: amount of mutation<br>
                   
<b>noise</b>: fast-later mutation rate<br>
                   
<b>warble</b>: slow-layer mutation rate<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=unstablepressure></a><br>

### <b>unstablepressure</b>

<img src="https://www.bespokesynth.com/docs/screenshots/unstablepressure.png"><br>

<div style="display:inline-block;margin-left:50px;">
mutate MPE pressure with perlin noise<br><br>
<b>amount</b>: amount of mutation<br>
                   
<b>noise</b>: fast-later mutation rate<br>
                   
<b>warble</b>: slow-layer mutation rate<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=velocityscaler></a><br>

### <b>velocityscaler</b>

<img src="https://www.bespokesynth.com/docs/screenshots/velocityscaler.png"><br>

<div style="display:inline-block;margin-left:50px;">
scale a note's velocity to be higher or lower<br><br>
<b>scale</b>: amount to multiply velocity by<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=velocitysetter></a><br>

### <b>velocitysetter</b>

<img src="https://www.bespokesynth.com/docs/screenshots/velocitysetter.png"><br>

<div style="display:inline-block;margin-left:50px;">
set a note's velocity to this value<br><br>
<b>rand</b>: randomness to reduce output velocity by<br>
                   
<b>vel</b>: velocity to use<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=velocitystepsequencer></a><br>

### <b>velocitystepsequencer</b>

<img src="https://www.bespokesynth.com/docs/screenshots/velocitystepsequencer.png"><br>

<div style="display:inline-block;margin-left:50px;">
adjusts the velocity of incoming notes based upon a sequence<br><br>
<b>downbeat</b>: should we reset the sequence every downbeat?<br>
                   
<b>interval</b>: speed to advance sequence<br>
                   
<b>len</b>: length of sequence<br>
                   
<b>vel*</b>: velocity for this step<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=vibrato></a><br>

### <b>vibrato</b>

<img src="https://www.bespokesynth.com/docs/screenshots/vibrato.png"><br>

<div style="display:inline-block;margin-left:50px;">
add rhythmic oscillating pitch bend to notes<br><br>
<b>vibinterval</b>: speed of pitch bend oscillation<br>
                   
<b>vibrato</b>: amount of pitch bend to add<br>
                   
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=volcabeatscontrol></a><br>

### <b>volcabeatscontrol</b>

<img src="https://www.bespokesynth.com/docs/screenshots/volcabeatscontrol.png"><br>

<div style="display:inline-block;margin-left:50px;">
outputs MIDI data to control various aspects of the KORG volca beats drum machine<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>

<a name=whitekeys></a><br>

### <b>whitekeys</b>

<img src="https://www.bespokesynth.com/docs/screenshots/whitekeys.png"><br>

<div style="display:inline-block;margin-left:50px;">
remap the white keys that correspond to the C major scale to instead play the current global scale<br><br>
<br>accepts: <font color=orange>notes</font> <br>
             
<br><br><br><br></div>
