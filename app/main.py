from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import initialize_firebase
# Initialize Firebase
initialize_firebase()
from router import router

# Create FastAPI application
app = FastAPI(
    title="User Management API",
    description="API sederhana untuk manajemen data pengguna dengan FastAPI dan Firebase",
    version="1.0.0"
)
# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Untuk produksi, tentukan origins yang spesifik
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include router
app.include_router(router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Selamat datang di API Manajemen Pengguna. Kunjungi /docs untuk dokumentasi."}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
