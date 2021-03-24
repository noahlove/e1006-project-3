#Noah love

#example sentence

#   Alabama#Albertville Farmers Market#116 Main Street#Albertville#35950#-86.2092#34.2679
#   Alabama#Alexander City Downtown Market#Braod Street#Alexander City#35010#0#0


def read_markets(filename):
    """
    Read in the farmers market data from the file named filename and return 
    a tuple of two objects:
    1) A dictionary mapping zip codes to lists of farmers market tuples.
    2) A dictionary mapping towns to sets of zip codes.
    """
    # create file, read only
    file = open(filename, "r")

    # create blanks
    zip_farmers = {}
    towns_zip = {}

    # read
    line = file.readline()

    # stripping the pieces apart:
    while line:
        # by line
        line = line.rstrip('\n')

        #state, market name, street address, city, zip code, longitude, latitude.
        #0:3 are the name and location, 4 is zip, 5,6 is long lat (don't need)

        # separate pieces of info (into 7 pieces)
        market_pieces = line.split("#")

        # get rid of long and lat
        market_pieces = market_pieces[0:5]

        # part name and location
        state = market_pieces[0]
        market_name = market_pieces[1]
        street = market_pieces[2]
        town = market_pieces[3]
        zip_code = market_pieces[4]

        # make market pieces into a tuple
        market_tuple = tuple(market_pieces)

        # create a loop to map each zipcode to associated
        #only needs to go on zips that are in our list
        if zip_code in zip_farmers:
            zip_code_mapping = zip_farmers[zip_code]
            zip_code_mapping.append(market_tuple)
            zip_farmers[zip_code] = zip_code_mapping

        else:
            zip_farmers[zip_code] = [market_tuple]

    return zip_farmers, towns_zip

def print_market(market):
    """
    Returns a human-readable string representing the farmers market tuple
    passed to the market parameter.
    """

    readable_string = "" # initialize
    readable_string += market[1] + "\n"  # market name
    readable_string += market[2] + "\n"  # street name
    readable_string += market[3] + ", " + market[0] + " " + market[4] + "\n" # town, State zip

    return readable_string


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
