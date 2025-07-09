from neomodel import StringProperty, StructuredNode, UniqueIdProperty  # type: ignore


class PersonOld(StructuredNode):
    """
    Represents a person in the Neo4j database.
    """

    uid = UniqueIdProperty()
    name = StringProperty(required=True)
    email = StringProperty(unique_index=True, required=True)

    def __str__(self):
        return f"Person(name={self.name}, email={self.email})"

    def __repr__(self):
        return f"Person(name={self.name}, email={self.email})"
