---
layout: page
title: building bespoke
parent: guides
has_toc: false
---

# building bespoke from source
<br>

Building Bespoke from source is easy and fun! The basic cmake prescription gives you a completed
executable which is ready to run on your system in many cases.

```shell
git clone --recursive https://github.com/BespokeSynth/BespokeSynth  # replace this with your fork if you forked
cd BespokeSynth
cmake -Bignore/build -DCMAKE_BUILD_TYPE=Release
cmake --build ignore/build --parallel 4 --config Release
```

This will produce a release build in `ignore/build/Source/BespokeSynth_artefacts`.

## required tools

To be able to build you will need a few things, depending on your OS.

All systems require an install of [Git](https://git-scm.com/downloads) and [CMake](https://cmake.org/download/) (Mac users can alternatively use [Homebrew](https://brew.sh/) (`brew install cmake`)

* On **Windows**: 
  * Install [Visual Studio Community 2019](https://visualstudio.microsoft.com/downloads/#visual-studio-community-2019) or [Build Tools for Visual Studio 2019](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019). When you install Visual Studio, make sure to include CLI tools and CMake, which are included in
    'Optional CLI support' and 'Toolset for Desktop' install bundles
  * [Python](https://www.python.org/downloads/)
  * Run all commands from the visual studio command shell which will be available after you install VS.

* On **MacOS**: install Xcode from [App Store](https://apps.apple.com/ca/app/xcode/id497799835) or [Apple.com](https://developer.apple.com/xcode/); install xcode command line tools with `xcode-select --install` and install cmake with `brew install cmake` if you use homebrew or from cmake.org if not

* On **Linux** you probably already have everything (gcc, git, etc...), but you will need to install required packages. The full list we
install on a fresh ubuntu 20 box are listed in the azure-pipelines.yml

## optional cmake commands

There are a few useful options to the *first* cmake command which many folks choose to use.

* `-DBESPOKE_VST2_SDK_LOCATION=/path/to/sdk` will activate VST2 hosting support in your built 
copy of Bespoke if you have access to the VST SDK
* `-DBESPOKE_ASIO_SDK_LOCATION=/path/to/sdk` (windows only) will activate ASIO support on windows in your built copy of Bespoke if you have access to the ASIO SDK
* `-DBESPOKE_PYTHON_ROOT=/...` will override the automatically detected python root. In some cases with M1 mac builds in homebrew this is useful.
* `-DCMAKE_BUILD_TYPE=Debug` will produce a build with debug information available
* `-A x64` (windows only) will force visual studio to build for 64 bit architectures, in the event this is not your default
* `-GXcode` (mac only) will eject xcode project files rather than the default make files
* `-DCMAKE_INSTALL_PREFIX=/usr` (only used on Linux) will set the `CMAKE_INSTALL_PREFIX` which guides both where your
built bespoke looks for resources and also where it installs. After a build on Linux with this configured, you can
do `sudo cmake --install ignore/build` and bespoke will install correctly into this directory. The cmake default is `/usr/local`.

The directory name `ignore/build` is arbitrary. Bespoke is set up to `.gitignore` everything in the `ignore` directory but you
can use any directory name you want for a build or have multiple builds also.
