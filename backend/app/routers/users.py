from fastapi import APIRouter

PREFIX = "/users"

router = APIRouter(
    prefix=PREFIX,
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["users"])
async def read_users():
    return [{"username": "Riz"}, {"username": "Rizwan"}]


@router.get("/me", tags=["users"])
async def read_user_me():
    return {"username": "Riz"}


@router.get("/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
