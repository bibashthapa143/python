# try:
#     risky_code()
# except SpecificError:
#     handle_it()

def get_price(item):
    # Dictionary of available items and their prices
    prices = {"apple": 30, "banana": 20}
    try:
        # Try to look up the item's price
        return prices[item]
    except KeyError as e:
        # If item isn't in the dictionary, raise a clearer error
        # "from e" links this new error to the original KeyError
        raise ValueError(f"'{item}' is not sold here") from e

get_price("mango")  # This will trigger the KeyError -> ValueError chain
