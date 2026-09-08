from pathlib import Path
import sys

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


PROJECT_ROOT = Path(__file__).resolve().parent.parent

ML_PATH = PROJECT_ROOT / "ML"

STATIC_PATH = PROJECT_ROOT / "app" / "static"

TEMPLATE_PATH = PROJECT_ROOT / "app" / "templates"


if str(ML_PATH) not in sys.path:
    sys.path.insert(0, str(ML_PATH))


from predict import predict_url


app = FastAPI(
    title="PhishGuard",
    description="Machine Learning based phishing URL detection system",
    version="1.0.0"
)


app.mount(
    "/static",
    StaticFiles(
        directory=str(STATIC_PATH)
    ),
    name="static"
)


templates = Jinja2Templates(
    directory=str(TEMPLATE_PATH)
)


class URLRequest(BaseModel):
    url: str


@app.get(
    "/",
    response_class=HTMLResponse
)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/predict")
def predict(request: URLRequest):

    try:

        result = predict_url(
            request.url
        )

        return {
            "url": request.url,
            "prediction": result["prediction"],
            "risk_score": result["risk_score"],
            "risk_level": result["risk_level"],
            "model_probability":
                result["model_probability"],
            "reasons": result["reasons"],
            "features": result["features"]
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except FileNotFoundError as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(error)}"
        )