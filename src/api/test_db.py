from fastapi import APIRouter
from ..models.person import Person

router = APIRouter(prefix="/test_db", tags=["Test Database"])

@router.get("/test-neo4j")
async def test_neo4j():
    """
    Test the connection to the Neo4j database by creating a person node.
    """
    try:
        # Create a test person node
        person: Person = Person(name="Test User", email="test@email.com")
        person.save() # type: ignore
        person.delete()  # type: ignore
        return {"message": "Neo4j connection is working!", "person": str(person)}
    except Exception as err:
        return {"error": str(err), "message": "Failed to connect to Neo4j database."}
