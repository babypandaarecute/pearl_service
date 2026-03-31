from fastapi import FastAPI
from pydantic import BaseModel
from pearldgs_toolbox import pearl_dgs  # adjust to real module name

app = FastAPI()

class PearlInputs(BaseModel):
    al_mm: float
    k1_d: float
    k2_d: float
    acd_mm: float
    lt_mm: float
    cct_um: float
    wtw_mm: float | None = None
    target_refraction_d: float = 0.0
    iol_constant: float
    iol_model: str

class PearlResult(BaseModel):
    theoretical_power_d: float
    selected_power_d: float

@app.post("/pearl-sphere", response_model=PearlResult)
def compute_pearl(inputs: PearlInputs):
    # TODO: replace this with the actual PEARL-DGS call using pearl_dgs_toolbox
    power = 0.0
    return PearlResult(
        theoretical_power_d=power,
        selected_power_d=power,
    )