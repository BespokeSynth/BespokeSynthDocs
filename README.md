# [Community-built documentation](https://bespokesynth.github.io/BespokeSynthDocs/) for [Bespoke Synth](https://www.bespokesynth.com/). Official docs [here](https://www.bespokesynth.com/docs/).

- You can find the most recent builds for Mac/Windows/Linux at [bespokesynth.com](https://www.bespokesynth.com/), or in the [Releases](https://github.com/BespokeSynth/BespokeSynth/releases) section on GitHub

- Sign up [here](http://bespokesynth.substack.com/) to receive an email for new releases

- Join the [Bespoke Discord](https://discord.gg/YdTMkvvpZZ) for support and to discuss with the community

# How to contribute:

## Local development requirements:

We are using a [Jekyll](https://jekyllrb.com/) theme called [Just The Docs](https://github.com/just-the-docs/just-the-docs) and [GitHub Pages](https://docs.github.com/en/pages).

The easiest way to contribute is to edit or add markdown files to this GitHub repo, and GitHub will automatically update the site. Editing directly in GitHub will create a fork which you can use to send a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests). If you have git you can develop the site locally.

Download Ruby:

- [Ruby](https://www.ruby-lang.org/en/downloads/)

Once you have installed Ruby, install the bundler gem:

```
gem install bundler
```

Or if you prefer a user install of bundler:

```
gem install --user-install bundler
```

Once you have installed Ruby and cloned the repo, you can optionally set the bundle path to install gems into the repo by running this command in the main repo folder:

```
bundle config set --local path 'vendor/bundle'
```

Then you can install the bundle by running this command in the main repo folder:

```bundle install```

Finally, run ```bundle exec jekyll serve``` to serve the site at http://127.0.0.1:4000
