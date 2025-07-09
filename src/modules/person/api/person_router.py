from typing import Any, Dict

from fastapi import APIRouter, HTTPException, Query, status

from ....shared.DIContainer.container import container
from ..app import SavePersonUseCase
from ..domain import Person, PersonService

router = APIRouter(prefix="/person", tags=["Person"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_person_by_email(
    email: str = Query(..., description="Person's email")
) -> Dict[str, Any]:
    """
    Retrieve a person by their email address.
    """
    try:
        use_case: PersonService = container.get("person_service")
        person = use_case.get_person_by_email(email)
        if not person:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Person not found"
            )
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err)
        )

    return {
        "message": "Person retrieved successfully!",
        "data": person,
    }


@router.post("/", status_code=status.HTTP_201_CREATED)
async def save_person(person_data: Person) -> Dict[str, Any]:
    """
    Save a new person entity.
    """
    try:
        use_case: SavePersonUseCase = container.get("save_person_use_case")
        success = use_case.execute(person_data)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to save person"
            )
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err)
        )

    return {"message": "Person saved successfully!"}
