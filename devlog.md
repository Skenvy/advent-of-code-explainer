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
