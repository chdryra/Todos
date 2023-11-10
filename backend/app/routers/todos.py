from typing import Annotated

from fastapi import APIRouter, Depends

from server_config import get_db
from sql.sqlutils import PostgresDb

PREFIX = "/todos"

router = APIRouter(
    prefix=PREFIX,
    tags=["todos"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_todos(db: Annotated[PostgresDb, Depends(get_db)]):
    return [{"1": "Eat"}, {"2": "Sleep"}]


@router.get("/{todo_id}")
async def read_todo(todo_id: str, db: Annotated[PostgresDb, Depends(get_db)]):
    return {todo_id: "This is a todo"}


@router.put("/{todo_id}",
            tags=["custom"],
            responses={403: {"description": "Operation forbidden"}},
)
async def update_note(todo_id: str, db: Annotated[PostgresDb, Depends(get_db)]):
    return []
