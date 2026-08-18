from app.models.order import PriorityTier

def determine_priority(distance_km: float) -> PriorityTier:
    if distance_km < 15.0:
        return PriorityTier.HIGH
    elif distance_km <= 50.0:
        return PriorityTier.MEDIUM
    else:
        return PriorityTier.LOW