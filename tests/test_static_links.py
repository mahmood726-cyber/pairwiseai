from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]


class AssetParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for attr in ("href", "src"):
            value = attrs.get(attr)
            if value:
                self.references.append((tag, attr, value))


def local_references(html):
    parser = AssetParser()
    parser.feed(html)
    for tag, attr, value in parser.references:
        parsed = urlparse(value)
        if parsed.scheme or value.startswith(("#", "mailto:", "tel:", "data:")):
            continue
        yield tag, attr, parsed.path


def test_landing_page_local_links_exist_and_stay_in_repo():
    html = (ROOT / "index.html").read_text(encoding="utf-8")

    assert "{{" not in html
    assert "C:\\" not in html
    assert "D:\\" not in html

    missing = []
    escaped = []
    for tag, attr, ref in local_references(html):
        target = (ROOT / ref).resolve()
        if ROOT not in (target, *target.parents):
            escaped.append(f"{tag} {attr}={ref}")
            continue
        if not target.exists():
            missing.append(f"{tag} {attr}={ref}")

    assert escaped == []
    assert missing == []


def test_pairwise_app_entrypoints_are_available():
    html = (ROOT / "index.html").read_text(encoding="utf-8")

    expected = [
        "e156-submission/assets/Main screen.html",
        "e156-submission/assets/pairwise-pro-v2_2_evalue (5).html",
        "e156-submission/assets/test_advanced.html",
    ]
    for ref in expected:
        assert ref in html
        assert (ROOT / ref).exists()
