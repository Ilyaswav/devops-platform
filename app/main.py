from fastapi import FastAPI

app = FastAPI(title="DevOps Platform")


@app.get("/")
def root():
    return {"message": "DevOps platform is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"version": "1.0.0"}
