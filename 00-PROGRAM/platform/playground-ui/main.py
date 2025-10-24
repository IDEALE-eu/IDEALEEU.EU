"""
Playground UI server.
"""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


app = FastAPI(
    title="IDEALE-EU LLM Playground",
    description="Multi-tenant LLM sandbox",
    version="0.1.0"
)

# Setup templates
templates_dir = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))


@app.get("/")
async def home(request: Request):
    """Render playground home page."""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "LLM Playground"
        }
    )


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "playground-ui"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
