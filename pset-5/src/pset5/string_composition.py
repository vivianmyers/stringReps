def stringComposition(k: int, text: str) -> list[str]:
    """Return the k-mer composition of text, including repeated k-mers (BA3A)."""
    # TODO: Write your code here.
    raise NotImplementedError("Implement stringComposition")
    return [text[i : i + k] for i in range(len(text) - k + 1)]
