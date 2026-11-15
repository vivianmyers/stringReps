def deBruijnFromString(k: int, text: str) -> list[list[str]]:
    """Return the de Bruijn graph of text as rows [source, destination] (BA3D).

    Each row contains one directed edge, with the source first.
    Row order does not matter. Preserve duplicate rows for parallel edges.
    """
    
    result = []
    for i in range(len(text) - k + 1):
        start = text[i : (i + k - 1)]
        end = text[(i + 1) : (i + k)]
        result.append([start, end])
    return result
