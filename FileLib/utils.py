def format_size(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f'{bytes:.2f} {unit}'
        bytes /= 1024