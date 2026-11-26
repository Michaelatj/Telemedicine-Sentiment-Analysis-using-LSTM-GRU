"""Conservative Indonesian review text preprocessing."""
import html
import re

_URL_RE = re.compile(r"https?://\S+|www\.\S+", flags=re.IGNORECASE)
_HTML_RE = re.compile(r"<[^>]+>")
_WHITESPACE_RE = re.compile(r"\s+")


def clean_text(value: object) -> str:
    """Normalize text without removing negation or applying stemming.

    This intentionally avoids stopword removal. Words such as 'tidak', 'bukan',
    and 'belum' can reverse the meaning of a review.
    """
    if value is None:
        return ""
    text = html.unescape(str(value))
    text = _HTML_RE.sub(" ", text)
    text = _URL_RE.sub(" ", text)
    text = text.lower()
    text = _WHITESPACE_RE.sub(" ", text).strip()
    return text
