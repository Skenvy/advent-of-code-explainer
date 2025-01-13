# [Devlog](https://github.com/Skenvy/advent-of-code-explainer/blob/main/devlog.md)
<!-- References Start -->
[PyPI]: https://pypi.org/
[pelican]: https://getpelican.com/
[pyscript]: https://pyscript.net/
[pyscript com]: https://pyscript.com/
[Advent of Code]: https://adventofcode.com/
[Using PyScript with Pelican]: https://www.castoriscausa.com/posts/2023/05/13/pyscript_toy_example/
[how to host pyscript based sites]: https://docs.pyscript.net/2024.11.1/beginning-pyscript/#from-a-web-server
<!-- References End -->
## Preamble
### Preamble preamble: What is this?
This is the beginning of development on a WIP+PoC test to deploy a python package on [PyPI][PyPI] and create a static site (via [pelican][pelican] probably) that utilises [pyscript][pyscript] to run the package in the browser. Specifically, this will be done with a toy package centred on "advent of code solving" -- the [Advent of Code][Advent of Code] is an annual fun code challenge exercise, done as an advent calender, so every December. Of course, part of the fun is finding something to use it as an excuse to learn, beyond the scope of just solving the actual puzzles.

This year I've decided to use Advent of Code as an excuse to play around with publishing a [PyPI][PyPI] package and then using it in a static site that loads [pyscript][pyscript]. There are plenty of sites out there already that act as sites you can paste your input into and get the solution for, so this isn't trying to be the best at that thing, it's purely just to learn and play around with having one repo host the code for a package, and also the static site (generation) that consumes that package via pyscript.

If you're more interested in the sites that stay up to date and cover all previous years for Advent of Code specifically, rather than my journey making this small thing, have a look at:
1. [fornwall's solver](https://aoc.fornwall.net/) ([source](https://github.com/fornwall/advent-of-code) afaik a rust crate running as an api on [fly.io](https://fly.io/), but there's a lot of good stuff to have a look at in there)
1. [mgtezak's solver](https://aoc-puzzle-solver.streamlit.app/) ([source](https://github.com/mgtezak/Advent-of-Code-Puzzle-Solver) a [streamlit](https://streamlit.io/) hosted app.)
1. [shahata's solver](https://shahata.github.io/adventofcode-solver/) ([source](https://github.com/shahata/adventofcode-solver) a static site on gh-pages that uses included node code.)
1. [wimglenn's solver](https://pypi.org/project/advent-of-code-data/) ([source](https://github.com/wimglenn/advent-of-code-data) a python package)

Having a look at existing online solvers like these informed the choice to pick a bastard child combination of them. **I wanted to do something**.

### Motivation: What exists, and what I want to make
I wanted to do it **in python**, because it's not hard to see that it's an easy scripting language for people getting started with Advent of Code, so as a language that it seems like most people would do the puzzles with, it makes the most sense. As impressive as the people doing code golf, or getting on the leaderboards are, the closest I've come was being the `1676th` person to solve day 11 this year (2024), so this is about just getting it done eventually, not racing the leaderboards.

I wanted to do it **as a static site**. Hosting, especially with sites that offer free hosting, seems like an ok choice, but the first two pre-existing sites I stumbled across that already offer what this will eventually hopefully be, did that already. It wouldn't be a lot of fun to tread the path already trodden, and "just go look at how someone else did it" would feel like too readily available a solution to what is supposed to be an excuse to learn something by building it yourself. If I were happy with using a hosted app somewhere in python, then I would have ended up just following along with [mgtezak's solver source](https://github.com/mgtezak/Advent-of-Code-Puzzle-Solver).

Instead, I didn't even know [pyscript][pyscript] was a thing until I searched if python could be run natively in browsers. But it looks like the primary building block for what I want to do already exists, so the plan is certainly viable. Of course, [their commerical site][pyscript com] includes a section on [how to host pyscript based sites][how to host pyscript based sites] that says;
> Just host the three files (pyscript.json, index.html and main.py) in the same directory on a static web server somewhere.
>
> Clearly, we recommend you use pyscript.com for this, but any static web host will do (for example, GitHub Pages, Amazon's S3, Google Cloud or Microsoft's Azure).

I'm already comfortable with gh-pages, and it would pair easily with automatically deploying built documentation sites. So to draw a line in the sand, at least initially, this will be about deploying a static site that uses pyscript to gh-pages, but once that's all done, we might have a look at deploying whatever part of it we can to [pyscript.com][pyscript com].

## Begin init'ing things
### Package
Now, to start the project, I'll begin with making an essentially empty [PyPI][PyPI] package to fill out later, so that I can also start making the part of the project that will consume the package.
[Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) changes frequently so check it just to see whats current, since the last time I did this.
[Configuring setuptools using `pyproject.toml` files](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html).
[Writing your `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
[Project Metadata: Project URLs](https://docs.pypi.org/project_metadata/#project-urls).
I'll also copy a paired down version of my python package makefile. Even though it'll only be relevant in its entirety to the package component `./pkg/`, and might get clobbered by recipes added on top of it in the `./web/` makefile, I want to include it into the `./web/` one to re-use my venv wrappers but I don't really want to break it apart, even though that'd probably be the cleaner thing to do. If I'm developing the package I'd rather only have one makefile open, and let my CI hit me if I break something between the root make and the `./web/` make.

### Empty Orphans `gh-pages-*`
I'll just reuse my established pattern for having multiple things in a repo build and contribute their own pages to a `gh-pages` deployment. My method is having a deployment of pages run on an artifact built from a `gh-pages` branch, after that branch has had any one of several "sub pages" merged to it. Although many applications or tools provide very concise easy and simple methods for publishing _their own output_ to `gh-pages` branch (often geared towards gh's default jekyll build) it is not common for them to have capabilities for publishing to only sub-pages. Start with creating the empty orphans we later push to and merge between. We only have two this time round, one for the "package" pages (which will be built by sphinx) and one for the "[pyscript][pyscript] / pelican" pages.
```sh
git checkout --orphan gh-pages
rm .git/index ; git clean -fdx
git commit -m "Initial empty orphan" --allow-empty
git push --set-upstream origin gh-pages

git checkout --orphan gh-pages-pkg
git commit -m "Initial empty orphan" --allow-empty
git push --set-upstream origin gh-pages-pkg

git checkout --orphan gh-pages-web
git commit -m "Initial empty orphan" --allow-empty
git push --set-upstream origin gh-pages-web
```

### [Pelican][pelican] basic stuff
[Pelican Quickstart](https://getpelican.com/#quickstart) generates a makefile, which is nice, but it assumes you're running it globally. Because lines in a make recipe are run in new shells, we need to inherit our custom recipes and variables for wrapping local development with virtual envs.
There's quite a few recipes that are automatically generated. As one of the steps I use in CI is checking that the target (output) is checked in as what would be built by the checked in content (input), I am in a habit of manually running `make ~site` or `make ~serve` each time anyway (and often at the behest of my CI failing when I forget to). So we can get rid of all the watcher / live reloading recipes, even if they're a good practice.

We're then left with whatever the difference is between the `pelicanconf.py` and the `publishconf.py`. [This SO question](https://stackoverflow.com/questions/20817192/what-is-the-difference-between-pelicanconf-and-publishconf-when-using-pelican) answers it (although the names might make it obvious and the generated makefile had an explanation, it's good to know _why_).
For our purpose, we don't really care much about keeping a barrier between the two. That is to say, I would like to know that I'm previewing the site using the "publishing" settings, so I'd like to just use one settings file. This can be done, but we would still need two recipes, one that uses the relative urls setting, and another that doesn't, because without relative urls, building the site using the publishing `SITEURL` and previewing it, shows a very different page to using relative urls, which are not recommended for published pages.

I guess because we'd still be publishing with relative urls to view the publishconf build locally we may as well just not change it from building with two different settings files, as either way there'd be an extra recipe to remember. Plus, it doesn't really matter, I'm trying to not have a contrary opinion on this.

### `pelican-quickstart`
Without yet knowing how easy [pelican][pelican] will be to use, the amount of questions that the "quickstart" asked, without necessarilly explaining what they meant, was enough that I had to google what some of them were, or the possible answers that could be given.
```
Welcome to pelican-quickstart v4.10.2.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.

    
> Where do you want to create your new web site? [.] 
> What will be the title of this web site? Advent of Code: Explainer
> Who will be the author of this web site? Skenvy
> What will be the default language of this web site? [C] en
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) Y
> What is your URL prefix? (see above example; no trailing slash) https://skenvy.github.io/advent-of-code-explainer/web
> Do you want to enable article pagination? (Y/n) Y
> How many articles per page do you want? [10] 25
> What is your time zone? [Europe/Rome] UTC
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) Y
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) n
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) n
Done. Your new project is available at (here)
```

## [pyscript][pyscript] initial example
Of course, although we will (probably) be using [pelican][pelican] to build the site, I already followed the [pyscript][pyscript] initial steps earlier before deciding to do this, and found a [blog post of someone else experimenting with this][Using PyScript with Pelican], so I know it's doable. Although, by doing the [pyscript][pyscript] stuffed inside pelican config, it might not be the clearest what's happening.
It's easiest to see pyscript working from a minimal example, before diving in to the deep end. Of course, we know from [how to host pyscript based sites][how to host pyscript based sites] that such a minimal example would be;
> Just host the three files (pyscript.json, index.html and main.py) in the same directory on a static web server somewhere.

I did initially stumble upon [this example](https://pyscript.com/@anicete/pirate/latest) although I can't retrace the steps I took to find it. From this though we can see the minimal components we need, are;
1. A `./pyscript.toml` which contains `packages = ["advent-of-code-explainer==0.0.1"]` (the `==0.0.1` is optional, but we definitely want it)
1. A `./main.py` that looks something like
    ```python
    import advent_of_code_explainer as aoce
    from pyscript import document

    def do_a_thing(event):
        input_text = document.querySelector("#input_number")
        input_number = input_text.value
        output_div = document.querySelector("#output_number")
        # The current version this is just a placeholder function that adds 2.
        output_div.innerText = str(aoce.puzzles.year_2024.day_1.solve_one(int(input_number)))
    ```
1. An `./index.html` that looks like
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width,initial-scale=1" />
        <title>Test of this pyscript thing</title>
        <link rel="stylesheet" href="https://pyscript.net/releases/2024.11.1/core.css">
        <script type="module" src="https://pyscript.net/releases/2024.11.1/core.js"></script>
    </head>
    <body>
        <h1>Pyscript Test: AOCE</h1>
        <p>Run AOCE function</p>
        <input type="text" id="input_number" placeholder="Type number here..." />
        <button py-click="do_a_thing">Get next value</button>
        <div id="output_number"></div>
        <script type="py" src="./main.py" config="./pyscript.toml"></script>
    </body>
    </html>
    ```
1. Use some command to locally serve the file to avoid a CORS policy issue. Something like the root makefile's `make server`.

If we just put these 3 files in gh-pages, it'll work. But it wont be very pretty or useful, and touching a lot of html does seem excessive. So we might as well wrap pyscript with pelican. Any blogging / static site generation tool could be viable, pelican just happened to be the first one I read in a list when I searched python static site generators. It also ended up having a [blog post][Using PyScript with Pelican] running through an example of getting pyscript working within a pelican generated site, so it's viable. But this example is an important grounding point to come back to if there's issues later on, because we at least have this as an MVP.

Of course my very very first attempt with pyscript can be seen [here](https://pyscript.com/@skenvy/my-first-pyscript-attempt/latest).

Worth mentioning is that pyscript can run with either pyodide or micropython. In a `<script/>` tag, `type="py"` is how we run with pyodide and `type="mpy"` is how we run with micropython. Micropython can only run embedded python or included python files, it can't pull packages from PyPI. So for us wanting to use a published package, we will need to use pyodide.

## PyScript within Pelican
Thanks once again to this [blog post][Using PyScript with Pelican], we have a path to getting pelican to create a site that makes use of pyscript.

### Custom Theme init
The first thing we need is our own custom pelican theme. It doesn't actually need to be _heavily_ customised, we just need our own quick-start theme to add a piece to it that will add the required `<script/>` that loads pyscript in the `<head/>`. We can follow [Pelican Themes](https://docs.getpelican.com/en/latest/themes.html) docs to see how to add a minimal theme. Excessive customisation of this isn't the point, it's entirely just to let pelican add the required head script. There exists [community maintained themes](https://github.com/getpelican/pelican-themes). The end of the page for themes includes an easy way to start, with just a `templates/base.html` file, and a `static/css/style.css` file. We'll put these in our `./web/theme/` folder, so we can just locally target the theme.

It does appear very simple though. Extending the "simple" theme is very minimalist, which is fine, but I assumed that simple was just the name of the default theme. It'd be nice to extend the default theme. The "notmyidea" theme is apparently the default. We can see two issues for this on the pelican repo [2745](https://github.com/getpelican/pelican/issues/2745) and [1092](https://github.com/getpelican/pelican/issues/1092). Of course, we are developing locally with pelican, the package of which includes the default "notmyidea" theme. Can we just escape out to the location of that theme installed in our virtual env? No, we can't. It appears that the simple theme is the only one that we can extend from in the base. Our `./web/theme/templates/base.html` can either start with `{% extends "!simple/base.html" %}` or extend a file, so long as the file is only forward. We'll accept `!simple` for now.

### Custom Theme adding PyScript
We will be writing each day as an "article" (our markdown pages in the content folder). Article's metadata declared at the top i.e. `Title: My First Post` will be exposed in our `templates/article.html` as `{{ article.title }}`. From reading the blog linked above it looks like [rcassani's method for implementing this](https://github.com/rcassani/pelican-kis/commit/a6d975444b47696c49b5170d06d7e659a195e4d5) is a good simple choice, although we aren't concerned with whether or not to load pyscript conditionally, because every article should load it, it would behove us to extend this with a choice of how to load which version of the pyscript script. I'll put the theme under the same MIT license they use because it should be more permissive than the GNU3 that everything else here is under, but given that it's one small example component I'm taking inspiration from (even if it's the important part for here) and I'm preserving the license terms, this comment feels attribution enough.

The method we'll adopt is similar. Use of the `pyscript` metadata on an article to specify the version used ~ our example uses version `2024.11.1`
```html
<link rel="stylesheet" href="https://pyscript.net/releases/2024.11.1/core.css">
<script type="module" src="https://pyscript.net/releases/2024.11.1/core.js"></script>
```
But it would appear that the releases on [the pyscript repo release page](https://github.com/pyscript/pyscript/releases) all work for this (at least, if they aren't pre-releases). The `latest` version appears in older examples, but has been deprecated apparently. So we'll add a "default" -- that is, if an article has metadata `pyscript: default` then it will just get the default we assign in the template. Loading the CSS on an independent check is probably something we could preserve. We could let `PyScript: js+css` control what gets loaded, and use the version under as `PyScriptVersion: x.y.z`

For now, I've set it up so that the articles

### Some small other things for a sec
Generating the site and viewing it to test that the articles have the expected pyscript pages yields a few warnings about missing icons. They don't really matter that much but any red sign is mid, so we can have a look at ["Tips-n-Tricks"](https://github.com/getpelican/pelican/wiki/Tips-n-Tricks) to see what we can do about this.

### Testing an article using the theme
Following on along with the post, we see we can just embed html into the md files pelican will process. We need to extend the static files to let us include `scripts`, and reference them from within the embedded html. A key step in the process of setting this up is buried in this subparagraph, but that key step is including the `pyscript.toml` file in our `content` folder, and making sure our `pelicanconf` is such that it will be included in the output, and knowing what the path to it will be so our embedded html can use it.

For here, I've added it in `content/scripts/pyscript.toml` because I'm expecting to share it on all pages, but that wouldn't necessarily be required, i.e. different `pyscript.toml`'s could be used, which seems like it pairs nicely with our theme being able to take a required release version, but it's unnecessary complication for the MVP. For now, we will stick to using our `PyScriptVersion: default` in our article metadata, as well as one shared `content/scripts/pyscript.toml` that each `<script/>` tag can source with `config="./scripts/pyscript.toml"`.

And having it work, when viewing individual articles, is a nice place to call this for tonight. Even if it's not very intuitive looking at the moment.

### Testing pyscript
In looking for ways to test pyscript scripts, we can see [pyscript/upytest](https://github.com/pyscript/upytest) exists, and [some `pyscript.web` tests in pyscript/pyscript](https://github.com/pyscript/pyscript/blob/main/core/tests/python/tests/test_web.py) show similar things to what we'd want to use it for here. Step one is that we need a local copy of the `upytest.py` file, that will exist in the context of where our site will be generated from, such that the file can end up in the site output.
I've since learnt after a few days of testing this that the way I had originally intended to use [pyscript/upytest](https://github.com/pyscript/upytest) to test each page as an embeddable page automation test is not its intended use case. I can't be bothered to reword these, so these are some comments I left in the pyscript discord that explain what I was confused about and how I thought it was supposed to be used, as well as how I intend to possibly bastardise it to make a truly ungodly creation of test pages that hijack the way the page works and injects the functions that are supposed to be typically attached and runs them during the test. This means the tests will end up running the things that they are supposed to be testing from across the boundary of both being independent scripts on the same page, in a very inter-meshed way, by combining them into one script, that still kind of tests something, but not in the best way.

The messages I left that summarise this are as follows. They're probably missing some context but eh.
> I am assuming that the intent of upytest is to run a test suite on a page by interacting with the elements and whatnot -- similar browser automation tests e.g. selenium -- but my problem is that I can't just "add" a `<script type="py" src="main.py" config="pyscript.toml" terminal></script>` sort of script, to test an already present script, because there's a race condition, i.e. the script that I already have on the page AND the upytest invoking script. Having both, the page behaves as expected but obviously the upytest case finishes ahead of when the page actually updates so reports it failed. The only reliable way I can get upytest to assert the result of another script is by including the required scripts in my [files], importing the actual script into the test script and executing the function from within the test case upytest runs -- which feels like a lot of manual decoration as well as being a pretty big gap between "having the thing be the way it is and test it as is" and "have a test pretend to be the actual thing and just test itself not the actual thing" -- so I can't tell if I'm just wildly misunderstanding the intent or how to use upytest.

> I'm not sure how this would work with what I'm trying to do.. running all the tests from one page? My goal is to be able to have it run on each page that already contains another `<script type="py"` to test the functionality of the other script and whether or not the other script is successfully updating the correct elements on the page or not. So I'd have two `<script type="py"` on each of several pages, one that is "the regular script to test" and one that is "the upytest invoker" but my problem is that the upytest invoker is unaware of or unable to wait on the timing of the other script completing its action.

> Primarily because it seemed like the easiest way to be able to dynamically build a static site with or without the test script included i.e. build it with test=true or something and be able to check each page and see tests pass, or build it with test=false and have the test script not built in. I realise that's an elaborate explanation that might have a different simpler answer, it's just the journey of trying to get different things to work that took me to that being the thing I was trying to do when I hit the obvious roadblock of realising that there would be a race condition between two scripts executing on the same page without awareness of each other.
>
> The simplest way to state the problem is "I was playing around making a site that uses pyscript, and I want some way to test each of the pages" -- of course browser automation would be an easy answer, but my goal was to try and learn what I could about the pyscript ecosystem and its tools and stumbled across upytest and found examples of the core pyscript repo using it to test the state of components on a page, and figured from that that it could be used the way I envisioned, and that's how I ended up wanting "a regular script" plus "a script that tests the other script already on the page."

> Hmm good idea! The way I had thought about it so far I had one test page for each regular page and replaced the regular script with a test script that would import the python file the regular script pointed to and include the function that was intended for a certain action in the test method, i.e. a regular page would have a script add a function to a button, and a test page would have the invoker read a test file that imported that function and ran it on the simulated click. But that seemed like a lot of steps and way too wide a gap for locality of concern, so thats when I realised I'd probably misunderstood and joined the server to ask lol.

> I still like the idea of attaching the div with the terminal output if it's a test but wouldn't want to if it was the "not test" version of the page, so that'd be the next thing for me to figure out if I use that "check the query string" method.
