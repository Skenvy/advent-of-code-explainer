# [Devlog](https://github.com/Skenvy/advent-of-code-explainer/blob/main/devlog.md)
This is the beginning of development on a WIP+PoC test to deploy a python package on PyPI and create a static site (via pelican probably) that utilises pyscript to run the package in the browser. Specifically, this will be done with a toy package centred on "advent of code solving" -- the [Advent of Code](https://adventofcode.com/) is an annual fun code challenge exercise, done as an advent calender, so every December. Of course, part of the fun is finding something to use it as an excuse to learn, beyond the scope of just solving the actual puzzles.

This year I've decided to use Advent of Code as an excuse to play around with publishing a pypi package and then using it in a static site that loads pyscript.

[Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) changes very frequently so check it just to see whats current, since the last one I did.
[Configuring setuptools using `pyproject.toml` files](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html).
[Writing your `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
[Project Metadata: Project URLs](https://docs.pypi.org/project_metadata/#project-urls).

## Empty Orphans `gh-pages-*`
I'll just reuse my established pattern for having multiple things in a repo build and contribute their own pages to a `gh-pages` deployment. My method is having a deployment of pages run on an artifact built from a `gh-pages` branch, after that branch has had any one of several "sub pages" merged to it. Although many applications or tools provide very concise easy and simple methods for publishing _their own output_ to `gh-pages` branch (often geared towards gh's default jekyll build) it is not common for them to have capabilities for publishing to only sub-pages. Start with creating the empty orphans we later push to and merge between. We only have two this time round, one for the "package" pages (which will be built by sphinx) and one for the "pyscript / pelican" pages.
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

## `pelican-quickstart`
Without yet knowing how easy pelican will be to use, the amount of questions that the "quickstart" asked, without necessarilly explaining what they meant, was enough that I had to google what some of them were, or the possible answers that could be given.
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

## pyscript
Of course, although we will (probably) be using pelican to build the site, I already followed the pyscript initial steps earlier before deciding to do this, and found a [blog post of someone else experimenting with this](https://www.castoriscausa.com/posts/2023/05/13/pyscript_toy_example/), so I know it's doable. Although, by doing the pyscript stuffed inside pelican config, it might not be the clearest what's happening.
