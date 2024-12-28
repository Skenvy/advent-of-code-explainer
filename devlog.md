# [Devlog](https://github.com/Skenvy/advent-of-code-explainer/blob/main/devlog.md)
[Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) changes very frequently so check it just to see whats current.
[Configuring setuptools using `pyproject.toml` files](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
[Writing your `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
[Project Metadata: Project URLs](https://docs.pypi.org/project_metadata/#project-urls)

## Empty Orphans `gh-pages-*`
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
