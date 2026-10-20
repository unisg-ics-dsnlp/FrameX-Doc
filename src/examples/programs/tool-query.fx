world open.
socrates:Human.

external checkHuman(?Person) using _query[query -> "?- socrates:Human."]
    <- ?Person:Human.

?Person[answer -> ?Status] <- ?Person:Human
    AND ?Call[tool#name -> "_query"; tool#arg1 -> ?Person;
              tool#completed -> true; tool#status -> "succeeded";
              result("status") -> ?Status].

?- socrates[answer -> "true"].
