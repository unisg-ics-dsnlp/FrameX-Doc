world open.

doc1:Document[text -> "Acme AG (the Customer)."].

external readCustomer(?Document) using _llm[
    prompt -> "Extract the customer. Return JSON with rows of slot, value and quote. Use slot customer, copy the value and quote exactly, and return no other claims.";
    document -> ?Text; groundIn -> ?Text]
    <- ?Document:Document[text -> ?Text].

// Only the customer field is admitted, and both host checks must hold.
?Document[accepted(?Row) -> ?Value] <- ?Document:Document
    AND ?Call[tool#name -> "_llm"; tool#arg1 -> ?Document;
              tool#completed -> true; tool#status -> "succeeded";
              row(?Row, "slot") -> "customer";
              row(?Row, "value") -> ?Value;
              row(?Row, "quoteFound") -> true;
              row(?Row, "valueQuoted") -> true].

?Document[customer -> ?Value] <- ?Document:Document
    AND ?Document[accepted(?Row) -> ?Value].

?Document[readError -> ?Message] <- ?Document:Document
    AND ?Call[tool#name -> "_llm"; tool#arg1 -> ?Document;
              tool#completed -> true; tool#status -> "failed";
              error -> ?Message].

?- doc1[customer -> ?Customer].
?- doc1[readError -> ?Message].
