from importlib.metadata import version

import humanize
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Hello from mise-test-1",
        "example": humanize.naturalsize(123456789),
        # Installed versions, so you can compare environments at a glance
        "versions": {
            "fastapi": version("fastapi"),
            "humanize": version("humanize"),
            "uvicorn": version("uvicorn"),
        },
    }

#random edit