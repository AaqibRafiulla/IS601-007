class OutOfStockException(Exception): 
    """Raised when something is out of stock"""
    pass

# My ucid is ar2576 and this code was done in 10/22/2022 by passing a display message indicating the exceptions and printing the same in the output when encountered 
# an exception 
class NeedsCleaningException(Exception):
    display = "We are cleaning the machine, Can you like check in after sometime?."
    """Raised when the icecream machine needs cleaning"""
    pass

class InvalidChoiceException(Exception):
    display  = "Please select a valid option."
    """Raised when an invalid choice is picked"""
    pass

class ExceededRemainingChoicesException(Exception):
    display = "You cannot select more than 3 flavours or toppings, kindly proceed to next step."
    """Raised when there are too many scoops of icecream"""
    pass

class InvalidPaymentException(Exception):
    display = "Please pay the exact amount as mentioned in the bill."
    """Raised when an invalid payment amount is given"""
    pass