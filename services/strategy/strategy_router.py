from services.strategy.interactions.stock_prediction_deep_learning import stock_prediction_deep_learning
from fastapi import Depends, APIRouter, HTTPException
from fastapi.responses import JSONResponse


strategy_router = APIRouter()

@strategy_router.post('/get_stock_predictions')
def get_stock_predictions_api(stoke_name):
    try:
        return stock_prediction_deep_learning(stoke_name)
    except HTTPException:
        raise
    except Exception as e:
        # raise in sentry as well
        return JSONResponse(
            status_code=500, content={"success": False, "error": str(e)}
        )