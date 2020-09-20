import logging
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.api_key import APIKey
from src.security.security import get_api_key
import uvicorn
from src.service.example_service import service_dummy
from src.schemas.example_data_request import ExampleRequestBody
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s: %(levelname)s - %(message)s", datefmt="%y-%m-%d %H:%M"
)

# Start application
app = FastAPI(title="APIName")

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    response = {
        "message": "API running!"
    }
    return response


@app.post("/test")
async def test_data(request: ExampleRequestBody, api_key: APIKey = Depends(get_api_key)):
    response = await service_dummy(request=request)

    if not response:
        logging.error(f"Request: {request}")
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Ops... internal error!")

    logging.info(f"Request: {request}")
    logging.info(f"Response: {response}")

    return response

# Include this handler for AWS lambda serverless
# handler = Mangum(app, enable_lifespan=False)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

# uvicorn index:app --host 0.0.0.0 --port 8080 --reload
# docker build -t pcdtoolsapi .
# docker run -p 8080:8080 pcdtoolsapi
