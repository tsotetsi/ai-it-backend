from fastapi import FastAPI


API_VERSION, API_ENV = "0.0.1", "development"


app = FastAPI(
    debug=True,
    title="Job Applications Management System.",
    description="Job Applications Management System.",
    version=API_VERSION
)


@app.get("/")
def root():
    return {
        "api_version": API_VERSION,
        "environment": API_ENV
    }
