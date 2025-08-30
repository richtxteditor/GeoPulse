from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .data_loader import load_all_processed_data

# Initialize the FastAPI app
app = FastAPI(
    title="Global Economic Impact API",
    description="API for accessing preprocessed global economic and defense data.",
    version="1.0.0"
)

# Load data on startup. This acts as a simple in-memory cache.
data_sources = load_all_processed_data()

@app.get("/", tags=["Root"])
async def read_root():
    """A simple health check endpoint."""
    return {"status": "ok", "message": "Welcome to the Global Economic Impact API!"}

@app.get("/datasets", tags=["Data"])
async def list_datasets():
    """Returns a list of all available dataset names."""
    if not data_sources:
        raise HTTPException(status_code=404, detail="No datasets loaded. Please run the data pipeline.")
    return {"datasets": list(data_sources.keys())}

@app.get("/datasets/{dataset_name}", tags=["Data"])
async def get_dataset(dataset_name: str):
    """
    Returns the data for a specific dataset in JSON format.
    The data is returned in a 'split' orientation (columns, index, data).
    """
    if dataset_name not in data_sources:
        raise HTTPException(status_code=404, detail=f"Dataset '{dataset_name}' not found.")
    
    df = data_sources[dataset_name].get_data()
    # Convert dataframe to JSON in a structured format
    json_data = df.to_json(orient='split', indent=4)
    # Return as a JSONResponse to ensure correct content type
    return JSONResponse(content=json.loads(json_data))

# Example of how to add a simple JSON import for the line above
import json