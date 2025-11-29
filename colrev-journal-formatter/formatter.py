def standardize_journal_name(name: str) -> str:
    """Standardizes a journal name by replacing common abbreviations."""
    abbreviations = {
        "J": "Journal",
        "Comput": "Computing",
        "Syst": "Systems",
        "Sci": "Science",
    }
    words = name.split()
    standardized_words = [abbreviations.get(word, word) for word in words]
    return " ".join(standardized_words)
