import re

def html2markdown(html):
    html = re.sub(r'\s+', r" ", html)
    html = re.sub(r'<em>(.+?)</em>', r'*\1*', html)
    html = re.sub(r'<p>(.+?)</p>', r'\1\n\n', html)
    html = re.sub(r'<a href="(.+?)">(.+?)</a>', r'[\2](\1)', html)
    return html.strip()
