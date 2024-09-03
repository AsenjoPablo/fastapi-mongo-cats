from fastapi import FastAPI
from routes.route import router

# CORS
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
uri = 'mongodb://localhost:27017'
app.include_router(router)



# cors preventions
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)