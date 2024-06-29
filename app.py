from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
 
app.mount("/images", StaticFiles(directory="images"), name='images')
 

@app.get("/home")
def show():
    return {"This site shows fruits."}
@app.get("/apple", response_class=HTMLResponse)
def serve():
    return """
    <html>
        <head>
            <title></title>
        </head>
        <body>
        <h1>This is an apple</h1>
        <img src="images/apple.jpg", width="500", height="500">
        
        </body>
    </html>
    """

@app.get("/banana", response_class=HTMLResponse)
def serve():
    return """
    <html>
        <head>
            <title></title>
        </head>
        <body>
        <h1>This is an apple</h1>
        <img src="images/banana.jpg", width="500", height="500">
        </body>
    </html>
    """

