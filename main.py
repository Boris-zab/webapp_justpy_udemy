import justpy as jp
import inspect
from webapp import page
from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary
import os

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and hasattr(obj, "path"):
            jp.Route(obj.path, obj.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)

# Render provides the port number in the environment variable PORT
port = int(os.environ.get("PORT", 8000))

jp.justpy(host="0.0.0.0", port=port)