import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Calculate BMI (Body Mass Index) for multiple individuals.
    
    Args:
        height: List of heights in meters.
        weight: List of weights in kilograms.
    
    Returns:
        list: BMI values calculated as weight / (height^2).
    """
    assert len(height) > 0 and len(height) == len(weight), "Height and weight lists must have the same positive length."

    height_array = np.array(height)
    weight_array = np.array(weight)

    bmi_array = weight_array / (height_array ** 2)  # BMI formula
    return bmi_array.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check which BMI values exceed a given limit.
    
    Args:
        bmi: List of BMI values.
        limit: Threshold value to compare against.
    
    Returns:
        list: Boolean list indicating which values exceed the limit.
    """
    assert len(bmi) > 0, "BMI list must have a positive length."

    bmi_array = np.array(bmi)

    return (bmi_array > limit).tolist()
