`readCustomer(doc1)`[tool#completed -> true; tool#status -> "failed";
    error -> "provider unavailable"].

expect true: doc1[readError -> "provider unavailable"].
expect unknown: doc1[customer -> "Acme AG"].
expect unknown: doc1[accepted(1) -> "Acme AG"].
