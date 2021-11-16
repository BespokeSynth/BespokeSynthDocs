---
layout: page
title: midi mapping
parent: guides
has_toc: false
---

# midi mapping
<br>

you need these modules:

- `midicontroller` which you want to map (and physical MIDI controller)
- some VST plugin or `oscillator` or whatever parameters you want to control

Then:

1. switch your `midicontroller` to *layout* view
2. move knobs on your controller to highlight them on `midicontroller` view
3. drag from control centerpoint (shown white when hovered) to the parameter you want to map, semitransparent cable appears
4. check if your parameters are mapped correctly
5. delete those what are not needed (most easy in *list* view of `midicontroller`)

![](images/midi_mapping.png)
