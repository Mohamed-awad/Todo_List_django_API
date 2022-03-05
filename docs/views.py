import os
from django.conf import settings
from django.contrib.staticfiles.views import serve


def serve_docs(request, path):
    """
    serving docs static files
    """
    docs_path = os.path.join(settings.DOCS_DIR, path)
    if os.path.isdir(docs_path):
        path = os.path.join(path, 'index.html')
    return serve(request, path, insecure=True)
