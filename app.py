
"""
FastAPI Server for Jenkins Build Information

This module implements a FastAPI server that serves dummy Jenkins build information
using Pydantic models for structured data representation. It includes endpoints to
retrieve information about build collections.

Usage:
1. Install FastAPI and uvicorn:
    ```python
    pip install fastapi
    ```

2. Run the server:
    ```bash
    uvicorn app:app --reload
    ```

3. Access the API documentation at http://127.0.0.1:8000/docs.

Endpoints:
- GET /: Returns dummy data for build collections.

Dummy data is generated based on provided Pydantic models.
"""
from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

# Define Pydantic models
class RevisionPayLoad(BaseModel):
    module: str
    revision: str

class ChangePayLoad(BaseModel):
    author: str
    changed_file_paths: List[str]
    comments: str
    time_stamp: datetime
    library: str

class BuildJobPayLoad(BaseModel):
    changes: List[ChangePayLoad]
    manually_started: bool
    changed_libraries: List[str]
    build_nr: int
    build_url: str

class BuildCollections(BaseModel):
    builds: List[BuildJobPayLoad]

# Dummy data
dummy_data = BuildCollections(builds=[
    BuildJobPayLoad(
        build_nr=181,
        build_url="https://jenkins-build-server/jenkins/view/ESME/181/",
        manually_started=False,
        changed_libraries=["Lib1"],
        changes=[
            ChangePayLoad(
                author="Müller, Max",
                changed_file_paths=[
                    "/trunk/Lib1/Files/Changes/1.txt",
                    "/trunk/Lib1/Files/Changes/2.txt",
                    "/trunk/Lib1/Files/Changes/3.txt",
                    "/trunk/Lib1/Files/Changes/4.txt",
                    "/trunk/Lib1/Files/Changes/5.txt",
                    "/trunk/Lib1/Files/Changes/6.txt",
                    "/trunk/Lib1/Files/Changes/7.txt",
                    "/trunk/Lib1/Files/Changes/8.txt"
                ],
                comments="Version 6.1.6",
                time_stamp=datetime(2024, 6, 6, 11, 9, 31, 584226),
                library="Lib1"
            )
        ]
    ),
    BuildJobPayLoad(
        build_nr=182,
        build_url="https://jenkins-build-server/jenkins/view/ESME/182/",
        manually_started=False,
        changed_libraries=["Lib2"],
        changes=[
            ChangePayLoad(
                author="Müller, Max",
                changed_file_paths=[
                    "/trunk/Lib2/Files/Changes/1.txt",
                    "/trunk/Lib2/Files/Changes/2.txt",
                    "/trunk/Lib2/Files/Changes/3.txt",
                    "/trunk/Lib2/Files/Changes/4.txt",
                    "/trunk/Lib2/Files/Changes/5.txt"
                ],
                comments="Mod: Improve handling from functions",
                time_stamp=datetime(2024, 6, 6, 14, 20, 7, 768970),
                library="Lib2"
            )
        ]
    )
])

# Create FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Jenkins Build Info API",
            "builds": f"{len(dummy_data.builds)}"}

@app.get("/build_collections", response_model=BuildCollections)
def get_build_collections():
    return dummy_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
