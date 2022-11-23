import uvicorn

# from fast_api_test import app

if __name__ == "__main__":
    uvicorn.run("fast_api_test:app", host="0.0.0.0", port=8000, reload=True)
