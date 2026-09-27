from fastapi import FastAPI, HTTPException, Request 
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Unit Converter")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/length")
def length(input: float, from_unit: str, to_unit: str):

    conversions = {"kilometers":1000,"meters":1,"centimeters":0.01,"millimeters":0.001,"feet":0.3048,"inches":0.0254,"yards":0.9144}
    from_value = conversions.get(from_unit)
    to_value = conversions.get(to_unit)

    if from_value is None or to_value is None:
        raise HTTPException(status_code=400, detail="Invalid unit")
    if type(input) != float:
        raise HTTPException(status_code=400, detail="Input was not a number")
    
    return {
    "input": input,
    "output": input*conversions[from_unit]/conversions[to_unit],
    "from": from_unit,
    "to": to_unit
    }




