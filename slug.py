"""Text helpers for building URL-friendly slugs."""

import re
import unicodedata

_SEPARATOR_RUN = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Convert text to a lowercase, ASCII, hyphen-separated slug.

    Accents are stripped (``é`` becomes ``e``), every run of non-alphanumeric
    characters collapses to a single ``-``, and leading/trailing ``-`` are trimmed.
    Characters with no ASCII decomposition (e.g. ``ß``, CJK) act as separators.

    Args:
        text: Arbitrary input text.

    Returns:
        The slug, or an empty string if ``text`` has no alphanumeric content.
    """
    decomposed = unicodedata.normalize("NFKD", text)
    unaccented = "".join(c for c in decomposed if not unicodedata.combining(c))
    return _SEPARATOR_RUN.sub("-", unaccented.lower()).strip("-")
