import re

def rename(filename):
    match = re.match(r"(\d{2})-(\d{2})-(\d{4})(\.\w+)", filename)
    if match:
        return f"{match.group(2)}-{match.group(1)}-{match.group(3)}{match.group(4)}"
    return filename
