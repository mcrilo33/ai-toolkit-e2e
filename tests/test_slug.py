import pytest

from slug import slugify


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello World", "hello-world"),
        ("Crème Brûlée", "creme-brulee"),
        ("é", "e"),
        ("a!!!b", "a-b"),
        ("a - _ . b", "a-b"),
        ("--Hello--", "hello"),
        ("  Hello  ", "hello"),
        ("!!!", ""),
        ("", ""),
        ("Python 3.12 rocks", "python-3-12-rocks"),
        ("already-a-slug", "already-a-slug"),
    ],
)
def test_slugify(text, expected):
    assert slugify(text) == expected
