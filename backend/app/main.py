from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth as auth_router
from app.routers import faculty_profile as faculty_router
from app.db import init_indexes
from app.routers import auth as auth_router

app = FastAPI(title="Benny WebApp Backend")

# Adjust CORS for your React frontend
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(faculty_router.router)


@app.get("/")
async def root():
    return {"message": "Benny backend running"}
