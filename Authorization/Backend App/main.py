from fastapi import FastAPI
# from fastapi_sqlalchemy import DBSessionMiddleware
import Auth.api as auth
import Users.api as user
app = FastAPI(
    title="ShareNest",
    description="Rest API for ShareNest",
    version="0.1",
    openapi_tags=[
    {
        "name": "Auth",
        "description": "Authorization flow. All login logic is here.",
    },
     {
        "name": "User",
        "description": "Operations with users. The user crud operations are defined here.",
    }
    ]
   
)
# app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

app.include_router(auth.api)
app.include_router(user.api)
