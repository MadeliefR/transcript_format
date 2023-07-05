from fastapi import FastAPI, HTTPException
from formatter_1 import format_transscript

app = FastAPI()

@app.get("/")
async def root():
    return "please create a directory and add your Teams transscripts '.docx' files to it. Next go to http://localhost:8080/docs#/default/formatting_formatting_get and fill in the form "

@app.get("/formatting")
async def formatting(path_of_directory: str, firstname: str, lastname:str):
    if not format_transscript(directory=path_of_directory, firstname=firstname, lastname=lastname):
        raise HTTPException(
            status_code=404,
            detail=f"There are no '.docx' files found in the given directory path. Please check if the path is correct and check if you added the Teams transscript files to this directory"
        )
    return "your transscripts have been formatted, check your directory for the new files"