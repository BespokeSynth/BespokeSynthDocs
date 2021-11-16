---
layout: page
title: faq
parent: bespoke synth
nav_order: 3
---

# frequently asked questions
<br>

There are usually multiple ways to achieve same result. 

Some of the actions rely on using keyboard, there is no menu item for every action.

## adding new module

- choose from main menu
- hold first letter of module name (e.g. o for `oscillator`) and then choose from the menu
- if you cannot find desired module, see chapter [terminology](terminology.md) to find out what you really need
	
## copy module

- hold alt and drag module by it's title bar

## deactivating and activating module

- click dot before module name in title bar

## deleting module

- lasso select modules you want to delete and then press backspace
- use triangle menu in module title bar and *delete module* button

## patching cables

- drag from dot at the bottom of source module to destination module
- click the dot at the bottom of source module and then dot in title bar of destination module
- note that you can only connect which have right type of signal (e.g. cannot connect `notesequencer` output to `gain`)

## splitting cables

- hold shift and drag from where you want to split cable
- if you are splitting audio cable, `send` module is created

## deleting cables

- drag cable from either end and hit backspace

## inserting module into cable path

- hold shift and then drag bottom dot of module to target

## set precise value for slider

- hover the mouse over slider, enter the desired value using number keys and hit enter

## set precise values for envelope

- press F2 to switch envelope from graphics view to sliders view

## create LFO on slider

- right click slider and LFO popup appears

## turn LFO into regular module

- click *pin* in LFO popup

## manage VST plugins

- set your `vstsearchdir` (in config) to directory where you have limited amout of VSTs which you want to use with Bespoke

or (on Windows)

use [BespokePluginScanner](https://www.bespokesynth.com/builds/BespokePluginScanner.exe):

> this is a separate app (an example juce app that I ripped pieces out of) that can scan for VSTs better than bespoke can, and then export the scanned list into bespoke 
> to use it:
> 
> - close bespoke
> - run this app
> - go to Options->Edit the List of Available Plug-ins...
> - click the Options... button below to initiate the scans
> - edit the list to however you would like it (you can remove plugins you don't care about, for example)
> - close that window, then in the main window, go to Options->Export plugins list to Bespoke
> - now open bespoke, and you should (hopefully) be all set, with all scanned VSTs accessible! 
if this band-aid works, then I will integrate a nicer version of this process into bespoke 1.0.1


