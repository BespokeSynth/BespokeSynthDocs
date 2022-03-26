
<a name=vocoder></a><br>
# <b>vocoder</b>
<img src="../images/vocoder.png"><br>
<div style="display:inline-block;margin-left:50px;">
frequency band-based vocoder. this must be paired with a "vocodercarrier" module. voice should be routed into this module, and a synth should be patched into the vocodercarrier.<br/><br/>
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

<br>accepts: <font color=cyan>audio</font> <br></div>
