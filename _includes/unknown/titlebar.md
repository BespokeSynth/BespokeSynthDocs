
<a name=titlebar></a><br>
# <b>titlebar</b>
<img src="../images/titlebar.png"><br>
<div style="display:inline-block;margin-left:50px;">
<br/><br/>
<b> ? </b>: show help<br>

<b>autosave</b>: every time a new module is added, trigger a save to data/savestate/autosave/, to help reload state in the event of a crash. can be quite slow if using modules with large samples.<br>

<b>load</b>: load a saved .bsk file to restore state<br>

<b>lookahead (exp.)</b>: use lookahead scheduling, which is necessary for scriptmodule. gets automatically turned on when you use scriptmodule. so far, lookahead scheduling seems to not create any issues, but leaving this checkbox here just in case.<br>

<b>play/pause</b>: stop all audio processing (shift-p)<br>

<b>reset layout</b>: reset to the layout specified in "layout" in userprefs.json<br>

<b>save</b>: save current state as .bsk file, to be restored later<br>

<b>save as</b>: save current state as a new .bsk file<br>

<b>settings</b>: adjust preferences, saved as userprefs.json<br>

<b>write audio</b>: write the last 30 minutes of audio to your specified recordings_path<br>
