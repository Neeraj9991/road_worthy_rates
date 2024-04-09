import joblib
import pandas as pd

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

from car_data_model import Car

app = FastAPI(
    title="Road Worthy Rates",
    description="Road Worthy Rates: Your go-to solution for accurate car price predictions. Powered by advanced analytics and machine learning, we provide valuable insights to help you make informed decisions in the automotive market."
)


@app.get("/")
def index():
    return FileResponse('index.html')


@app.post("/predict")
async def predict(car: Car):
    x_new = pd.DataFrame(data=dict(
        company=[car.company],
        year=[car.year],
        owner=[car.owner],
        fuel=[car.fuel],
        km_driven=[car.km_driven],
        mileage_mpg=[car.mileage_mpg],
        engine_cc=[car.engine_cc],
        seats=[car.seats]
    ))

    model = joblib.load("./model.joblib")
    predicted_value = model.predict(x_new)[0]

    return f"The car of given specifications will cost {predicted_value:,.0f} INR"
