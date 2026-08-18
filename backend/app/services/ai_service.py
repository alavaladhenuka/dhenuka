def verify_pick_and_pack_images(pick_img_path: str, pack_img_path: str) -> bool:
    """
    Mock AI Vision verification comparing picked and packed item images.
    In production, integrate OpenCV, TensorFlow, or an AI Vision API.
    """
    # Returns True if items match
    return True

def process_customer_damage_claim(damage_severity_score: float) -> float:
    """
    Evaluates customer damage photo and assigns refund percentage:
    - Minor Damage (<0.3) -> 10%
    - Moderate Damage (<0.7) -> 25%
    - Severe Damage (>=0.7) -> 40%
    """
    if damage_severity_score < 0.3:
        return 10.0
    elif damage_severity_score < 0.7:
        return 25.0
    return 40.0