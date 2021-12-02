def get_outliner_area(context):
    try:
        return next(area for area in context.screen.areas if area.type == "OUTLINER")
    except StopIteration:
        return None
