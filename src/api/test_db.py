from typing import Any, Dict

from fastapi import APIRouter, HTTPException, Query, status
from neomodel import DoesNotExist  # type: ignore

from ..models.person import PersonOld as Person  # type: ignore

router = APIRouter(prefix="/test_db", tags=["Test Database"])


@router.get("/test-neo4j")
async def test_neo4j():
    """
    Test the connection to the Neo4j database by creating a person node.
    """
    try:
        # Create a test person node
        person: Person = Person(name="Test User", email="test@email.com")
        person.save()  # type: ignore
        person.delete()  # type: ignore
        return {"message": "Neo4j connection is working!", "person": str(person)}
    except Exception as err:
        return {"error": str(err), "message": "Failed to connect to Neo4j database."}


@router.get("/", status_code=status.HTTP_200_OK)
async def get_by_email(
    email: str = Query(..., description="Person's email")
) -> Dict[str, Any]:
    """
    A simple endpoint to test the database connection.
    """
    try:
        person: Person = Person.nodes.get(email=email)  # type: ignore
    except DoesNotExist:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Person not found"
        )
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err)
        )
    return {
        "message": "Test database endpoint is working!",
        "data": str(person),
        "email": person.email,
        "name": person.name,
        "uid": person.uid,
    }
