from fastapi import FastAPI, HTTPException
from formatter_1 import format_transscript

app = FastAPI

@app.get("/")
async def root():
    return "please create a directory and add your Teams transscripts 'docx' files to it."

@app.get("/formatting")
async def root(path_of_directory: str, firstname: str, lastname:str):
    if format_transscript(directory=path_of_directory, firstname=firstname, lastname=lastname):
        return "your transscripts have been formatted, check your directory for the new files"
    raise HTTPException(
        status_code=404,
        detail=f"There are no '.docx' files found in the given directory path. Please check if the path is correct and check if you added the Teams transscript files to this directory"
    )