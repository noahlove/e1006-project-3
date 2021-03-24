def read_markets(filename):
    """
    Read in the farmers market data from the file named filename and return 
    a tuple of two objects:
    1) A dictionary mapping zip codes to lists of farmers market tuples.
    2) A dictionary mapping towns to sets of zip codes.
    """
    return {}, {} # replace this line

def print_market(market):
    """
    Returns a human-readable string representing the farmers market tuple
    passed to the market parameter.
    """
    return "" # replace this line

if __name__ == "__main__":

    # This main program first reads in the markets.txt once (using the function
    # from part (a)), and then asks the user repeatedly to enter a zip code or
    # a town name (in a while loop until the user types "quit").

    FILENAME = "markets.txt"

    try: 
        zip_to_market, town_to_zips = read_markets(FILENAME)

        # your main loop should be here

    except (FileNotFoundError, IOError): 
        print("Error reading {}".format(FILENAME))
