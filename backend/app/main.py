import secure
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import admin_routes, movie_router


app = FastAPI(
    title="MovieShelf API",
    description="API for self-hosted MovieShelf app",
    version="0.0.1",
)
secure_headers = secure.Secure()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def set_secure_headers(request, call_next):
    response = await call_next(request)
    secure_headers.framework.fastapi(response)
    return response


app.include_router(admin_routes.router)
app.include_router(movie_router.router)
