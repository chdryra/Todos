from typing import Annotated

from fastapi import APIRouter, Depends

from server_config import get_db
from sql.sqlutils import PostgresDb

PREFIX = ""

router = APIRouter(
    prefix=PREFIX,
    tags=["root"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root(db: Annotated[PostgresDb, Depends(get_db)]):
    api = f"/ GET"
    db.insert(f"""
       INSERT into api_calls(api) values('{api}')
       """)
    return {"message": "Hello Bigger Applications!"}
