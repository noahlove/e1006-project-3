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
    zip_code_to_market = {}
    towns_zip = {}

    # read
    line = file.readline()

    # stripping the pieces apart:
    while line:
        # by line
        line = line.rstrip("\n")

        # state, market name, street address, city, zip code, longitude, latitude.
        # 0:3 are the name and location, 4 is zip, 5,6 is long lat (don't need)

        # separate pieces of info (into 7 pieces)
        market_pieces = line.split("#")

        # get rid of long and lat
        market_pieces = market_pieces[0:5]

        # fixes the ones without a zip code
        if not market_pieces[4]:
            market_pieces[4] = "00000"
        market_tuple = tuple(market_pieces)

        # part name and location
        state = market_tuple[0]
        market_name = market_tuple[1]
        street = market_tuple[2]
        town = market_tuple[3]
        zip_code = market_tuple[4]

        # create a loop to map each zipcode to associated
        # only needs to go on zips that are in our list
        if zip_code in zip_code_to_market:
            zip_code_mapping = zip_code_to_market[zip_code]
            zip_code_mapping.append(market_tuple)
            zip_code_to_market[zip_code] = zip_code_mapping

            # TA suggested exclude ones without zip
            # i.e. like 209, shows as zip = "none"

        else:
            zip_code_to_market[zip_code] = [market_tuple]

        if town in towns_zip.keys():
            town_mapping_loop = towns_zip[town]
            town_mapping_loop.add(zip_code)
            towns_zip[town] = town_mapping_loop # this may not work and need dif name

        else:
            town_mapping_loop_else = set()
            town_mapping_loop_else.add(zip_code)
            towns_zip[town] = town_mapping_loop_else # breaks it

        line = file.readline()

    return zip_code_to_market, towns_zip



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

        input_zip = input("What is your zipcode or town? \n")
        while True:
            # exit if "quit"
            # piazza said only terminate on quit, not on error
            if input_zip == "quit":
                break

            # sort into two loops, numeric and alphabetical

            # zip codes numeric

            if input_zip.isnumeric():
                # if not there
                if input_zip not in zip_to_market:
                    print("Not found")

                # search for with zip
                else:
                    for market in zip_to_market[input_zip]:
                        print(print_market(market))

            # city search
            else:
                # wrong input
                if input_zip not in town_to_zips:
                    print("Not found")

                # city search
                else:
                    for town in town_to_zips[input_zip]:
                        for market in zip_to_market[town]:
                            print(print_market(market))

            # prompt
            input_zip = input("Enter a zipcode or town\n")

    except (FileNotFoundError, IOError): # given, I assume this is all error exceptions
        print("Error reading {}".format(FILENAME))  # checks for file
