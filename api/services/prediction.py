from api.core.models import PredictPayload
from api.services.weights import WeightsService

class PredictionService:
    
    def __init__(self, weights_service: WeightsService):
        self.weights_service = weights_service
    
    def predict(self, predict_info: PredictPayload):
        
        w0, w1, w2 = self.weights_service.get_weights()
            
        prev_close = predict_info.prev_close
        volume = predict_info.volume

        # Previsão do modelo de regressão linear simples
        return w0 + w1 * prev_close + w2 * volume