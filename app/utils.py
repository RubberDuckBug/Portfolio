from urllib.parse import urlparse, urljoin
from flask import request

def url_has_allowed_host_scheme(target, host):
    if not target:
        return True
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc