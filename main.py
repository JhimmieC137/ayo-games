import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="assets/templates")

app.mount("/static", StaticFiles(directory="assets/static"), name="static")

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    comment = "It's beginning to look a lot like Christmas"
    board = [0 for x in range(0, 12)]
    return templates.TemplateResponse(request=request, name="index.html" , context={"request": request, "comment": comment, "title": "Ayo game app", "board": board, "board_length": len(board)})

if __name__ == "__main__": 
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5500,
        reload=True,
    )
