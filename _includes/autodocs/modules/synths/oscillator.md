
<a name=oscillator></a><br>
# <b>oscillator</b>
<img src="../images/oscillator.png"><br>
<div style="display:inline-block;margin-left:50px;">
polyphonic enveloped oscillator. modulations (with MPE support): modwheel closes filter further (if filter is enabled), pressure decreases detune amount<br/><br/>
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

<br>accepts: <font color=orange>notes</font> <br></div>
