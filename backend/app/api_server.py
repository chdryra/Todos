import argparse

import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server_config import ServerConfig, get_db_uri
from routers import todos, users, root

def run_server(config: ServerConfig) -> None:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
    app.include_router(users.router)
    app.include_router(todos.router)
    app.include_router(root.router)
 
    uvicorn.run(app, host=config.ip, port=config.port, log_level="info", proxy_headers=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Host parameters')
    parser.add_argument('-i', '--ip', default="127.0.0.1", required=False)
    parser.add_argument('-p', '--port', default=5000, required=False)
    args = parser.parse_args()

    db_uri = get_db_uri()
    run_server(ServerConfig(ip=args.ip, port=int(args.port)))
