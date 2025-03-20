from typing import Optional
from fastapi import FastAPI
from api.core.models import PredictPayload
from api.services.prediction import PredictionService
from api.services.weights import WeightsService

app = FastAPI(
    title="Minha API de Investimentos",
    description="API para calcular retorno de ações",
    version="1.0.0",
    docs_url="/docs",        # Rota do Swagger UI (pode mudar)
    redoc_url="/redoc",      # Rota do Redoc (pode mudar ou desativar)
)

@app.get("/")
async def root():
    return {"message": "Serviço no ar"}

@app.post("/predict")
def read_item(payload:PredictPayload):
    
    weights_service = WeightsService(payload.ticker)

    try:
        prediction_service = PredictionService(weights_service)
        return { "prediction": prediction_service.predict(payload) }
    except Exception as e:
        return { "error" : str(e) }