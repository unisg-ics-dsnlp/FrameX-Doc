// Each row fails a different gate: source quote, quoted value, allowed slot.
`readCustomer(doc1)`[
    tool#completed -> true; tool#status -> "succeeded";
    row(1, "slot") -> "customer";
    row(1, "value") -> "Other AG";
    row(1, "quote") -> "Other AG (the Customer)";
    row(1, "quoteFound") -> false;
    row(1, "valueQuoted") -> true;
    row(2, "slot") -> "customer";
    row(2, "value") -> "Other AG";
    row(2, "quote") -> "Acme AG (the Customer)";
    row(2, "quoteFound") -> true;
    row(2, "valueQuoted") -> false;
    row(3, "slot") -> "bankAccount";
    row(3, "value") -> "Acme AG";
    row(3, "quote") -> "Acme AG (the Customer)";
    row(3, "quoteFound") -> true;
    row(3, "valueQuoted") -> true].

expect unknown: doc1[accepted(1) -> "Other AG"].
expect unknown: doc1[accepted(2) -> "Other AG"].
expect unknown: doc1[accepted(3) -> "Acme AG"].
expect unknown: doc1[customer -> "Other AG"].
expect unknown: doc1[customer -> "Acme AG"].
