
<a name=looperrewriter></a><br>
# <b>looperrewriter</b>
<img src="https://www.bespokesynth.com/docs/screenshots/looperrewriter.png"><br>
<div style="display:inline-block;margin-left:50px;">
rewrites the contents of a looper with received input, to help you resample your own loops. attach the grey dot to a "looper" module.

the ideal way to use this module is to hook the "looper" directly up to a "send", hook the leftmost outlet of the "send" up to your effects processing (like an "effectchain"), hook the effect processing up to this "rewriter", and then also connect the rightmost outlet of the "send" up to this "rewriter"<br/><br/>
<b> go </b>: rewrite the connected looper, and if that looper is connected to a send, set that send to output only to the right outlet<br>

<b>new loop</b>: start recording a dynamic loop length. press "go" when you want to rewrite it to the looper. this will also change bespoke's global tempo to match this new loop, so it's quite powerful and scary! click it again to cancel.<br>

<br>accepts: <font color=cyan>audio</font> <br></div>
