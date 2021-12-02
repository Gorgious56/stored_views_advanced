def get_family_down(col, include_parent=True):
    if include_parent:
        yield col
    for child in col.children:
        yield from get_family_down(child, include_parent=True)
