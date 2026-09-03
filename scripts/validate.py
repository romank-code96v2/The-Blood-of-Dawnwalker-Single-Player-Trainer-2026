# Build: dee0390caaf0fdbce95d3d8690c1f2ea

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
