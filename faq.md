---
layout: page
title: faq
nav_order: 2
has_children: false
has_toc: false
---

# Frequently Asked Questions

There are usually multiple ways to achieve the same result. 

Some of the actions rely on using the keyboard, there is no menu item for every action.

## Terminology:

Bespoke synth sometimes uses different terminology than other DAWs or it uses familiar words in unusual way.

There you can find where to look when you are looking for something:

- **control voltage** - pulse
- **filter** - *biquad* or *butterworth* in *effectchain*, but most complex synths has filter already built-in
- **oscillator** - Bespoke oscillator is in fact full featured synth, use *signalgenerator* if you want low level oscillator
- **reverb** - look for *freeverb* in *effectchain*
- **sequencer** - look to *instruments* menu
- **transpose** - use *capo* for transposing notes by semitones, *noteoctaver* for transposing by octave and *transposefrom* for transposing according to scale
- **oscilloscope** - *waveformviewer* or *spectrum*

## Adding modules

- choose from main menu
- hold first letter of module name (e.g. o for `oscillator`) and then choose from the menu
- if you cannot find desired module, see [terminology](#terminology) to find out what you really need
	
## Copying modules

- hold alt and drag module by it's title bar

## Deactivating and activating modules

- click dot before module name in title bar

## Deleting modules

- lasso select modules you want to delete and then press backspace
- use triangle menu in module title bar and *delete module* button

## Patching cables

- drag from dot at the bottom of source module to destination module
- click the dot at the bottom of source module and then dot in title bar of destination module
- note that you can only connect which have right type of signal (e.g. cannot connect `notesequencer` output to `gain`)

## Splitting cables

- hold shift and drag from where you want to split cable
- if you are splitting audio cable, `send` module is created

## Deleting cables

- drag cable from either end and hit backspace

## Inserting a module into cable path

- hold shift and then drag bottom dot of module to target

## Setting the precise value for a slider

- hover the mouse over slider, enter the desired value using number keys and hit enter

## Setting the precise value for an envelope

- press F2 to switch envelope from graphics view to sliders view

## Creating an LFO on a slider

- right click slider and LFO popup appears

## Turning an LFO into a regular module

- click *pin* in LFO popup

## Managing VST plugins

- choose 'manage VSTs...' from the 'vst plugins' dropdown in the title bar
