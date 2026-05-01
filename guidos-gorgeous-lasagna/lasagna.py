EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time in minutes.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.
    
    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate elapsed time in minutes.
    
    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time