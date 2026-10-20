// Authored receipt fixture, not a recorded model measurement.
`readCustomer(doc1)`[
    tool#completed -> true; tool#status -> "succeeded";
    row(1, "slot") -> "customer";
    row(1, "value") -> "Acme AG";
    row(1, "quote") -> "Acme AG (the Customer)";
    row(1, "quoteFound") -> true;
    row(1, "valueQuoted") -> true].

expect true: doc1[accepted(1) -> "Acme AG"].
expect true: doc1[customer -> "Acme AG"].
expect unknown: doc1[readError -> "provider unavailable"].
