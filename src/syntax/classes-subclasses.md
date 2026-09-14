# Classes and Subclasses

`extends` builds the taxonomy. A subclass inherits everything declared for
its superclasses, so membership in a subclass implies membership in every
superclass.

```prolog
// Taxonomy: each level inherits from the one above.
Person { hasName: String }.
Man extends Person.
CommunicationDevice extends Component.
DirectAntenna extends CommunicationDevice.
```
