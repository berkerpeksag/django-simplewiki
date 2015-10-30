import difflib


def create_diff(old, new):
    return '<br>'.join(difflib.unified_diff(
        old.splitlines(keepends=True), new.splitlines(keepends=True)
    ))
