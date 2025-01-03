import json

from base import upytest
from pyscript import web

results = await upytest.run("./tests")
output = web.div(json.dumps(results), id="results")
web.page.append(output)
