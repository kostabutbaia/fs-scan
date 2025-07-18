import re

def object_json_serializer(obj):
    if hasattr(obj, 'to_dict'):
        return obj.to_dict
    
def flatten_path(path: str) -> str:
    """ 
    Replace all characters in the inputted path that are not letters or digits,
    with underscores.

    Used for naming report files for directories.
    """
    return re.sub(r'[^a-zA-Z0-9_-]', '_', path)