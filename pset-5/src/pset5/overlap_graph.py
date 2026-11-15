def overlapGraph(patterns: list[str]) -> list[list[str]]:
    """Return the overlap graph as rows [source, destination] (BA3C).

    Each row contains one directed edge, with the source first.
    Row order does not matter.
    """
    
    result = []

    for pattern1 in patterns:
        suffix = pattern1[1:]
        for pattern2 in patterns:
            prefix = pattern2[:-1]
            if pattern1 != pattern2 and suffix == prefix:
                result.append([pattern1, pattern2])

    return result