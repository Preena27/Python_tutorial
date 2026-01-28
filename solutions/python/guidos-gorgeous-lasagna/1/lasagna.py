#time the lasagna should be in the oven according to the cookbook.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
 
   :param elapsed_bake_time: int baking time already elapsed
   :return: int remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'
 
   Function that takes the actual minutes the lasagna has been in the oven as
   an argument and returns how many minutes the lasagna still needs to bake
   based on the `EXPECTED_BAKE_TIME`.
   """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of lasagna layers
    :return: int - total preparation time in minutes

    Function that takes the number of layers in the lasagna and returns
    the total preparation time based on the PREPARATION_TIME constant.
    """
    return number_of_layers * PREPARATION_TIME
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    :param number_of_layers: int - number of lasagna layers
    :param elapsed_bake_time: int - minutes already spent baking
    :return: int - total elapsed time in minutes

    Function that returns the sum of preparation time and the elapsed
    baking time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time