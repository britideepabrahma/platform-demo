import random, time
from fastapi import FastAPI, HTTPException

app = FastAPI()
CHAOS = {"latency_ms": 0, "error_rate": 0.0}

@app.get("/healthz")
def health():
    return {"ok": True}

@app.post("/orders")
def create_order():
    time.sleep(CHAOS["latency_ms"] / 1000)
    if random.random() < CHAOS["error_rate"]:
        raise HTTPException(500, "chaos!")
    return {"order_id": random.randint(1000, 9999), "status": "created"}

@app.post("/chaos")
def chaos(latency_ms: int = 0, error_rate: float = 0.0):
    CHAOS.update(latency_ms=latency_ms, error_rate=error_rate)
    return CHAOS