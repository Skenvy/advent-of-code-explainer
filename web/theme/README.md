# [Custom Pelican Theme: Simple PyScript Articles](https://github.com/Skenvy/advent-of-code-explainer/tree/main/web/theme)
> [!TIP]
> This is a custom pelican theme to enable PyScript working on articles. This theme is [licensed MIT](https://github.com/Skenvy/advent-of-code-explainer/blob/main/web/theme/LICENSE), and was inspired by [rcassani/pelican-kis](https://github.com/rcassani/pelican-kis/tree/master) ([specifically this](https://github.com/rcassani/pelican-kis/blob/4f8be1076549b7ffca59a2ca9d5cf7810a05b8fb/templates/article.html#L3-L13)).

To have an article include PyScript, set the following on them
```md
PyScript: js+css
PyScriptVersion: default
```
`PyScriptVersion` can be any version that yields a valid `https://pyscript.net/releases/{{ PyScriptVersion }}/core.js`. Check the article template for the default version.

> [!NOTE]
> Besides this, the root index has been modified to hide summaries of articles that use the above metadata fields, to prevent the rendering of included components that would appear interactive, when they are not interactive until clicking through to the articles.
