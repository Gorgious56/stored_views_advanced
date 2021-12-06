def get_viewport_area(context):
    try:
        return next(area for area in context.screen.areas if area.type == "VIEW_3D")
    except StopIteration:
        return None
