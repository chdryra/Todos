from typing import Annotated

from fastapi import APIRouter, Depends

from server_config import get_db
from sql.sqlutils import PostgresDb

PREFIX = "/notes"

router = APIRouter(
    prefix=PREFIX,
    tags=["notes"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_notes(db: Annotated[PostgresDb, Depends(get_db)]):
    api = f"{PREFIX} GET"
    db.insert(f"""
    INSERT into api_calls(api) values("{api}") 
    """)


@router.get("/{note_id}")
async def read_note(note_id: str, db: Annotated[PostgresDb, Depends(get_db)]):
    api = f"{PREFIX}/{note_id} GET"
    db.insert(f"""
    INSERT into api_calls(api) values("{api}") 
    """)


@router.put("/{note_id}",
            tags=["custom"],
            responses={403: {"description": "Operation forbidden"}},
)
async def update_note(note_id: str, db: Annotated[PostgresDb, Depends(get_db)]):
    api = f"{PREFIX}/{note_id} POST"
    db.insert(f"""
    INSERT into api_calls(api) values("{api}") 
    """)
