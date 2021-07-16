import json

# define the format of the info
data = '{"mac": "XX:YY:ZZ:XX:YY:ZZ", "cellnumber": "XX", "signal_total": "XX", "signal_quality": "XX", "encryption": "XXXX", "signal_level_dBm": "XXX", "essid": "XXX"}'

# passed the data to string
parsed_json = (json.loads(data))

# printing to check
# print(json.dumps(parsed_json, indent=4, sort_keys=True))

# distance between cellphone and notebook
distance = ["1m","2m","3m","4m","5m","6m","7m","8m","9m","10m"]

# array to receive the reads
signal_level = []

# iterating in all directories
for dist in distance:
    # read the directory with the json files
    for x in range (1, 100):

        # oppening the files and save the information in a string
        with open("./reads/" + dist + "/read_" + str(x) + ".json", 'r') as f:
            info = json.load(f)

        # iterating the to get the signal's strength
        for resp in info:
            if (resp["essid"] == "AndroidAP"):
                # print (resp['signal_level_dBm'])
                signal_level.append(resp['signal_level_dBm'])

        # priting information
        print (signal_level)

    # save information in a file to access later
    file = "./results/" + dist + ".txt"

    with open(file, 'w') as f:
        for item in signal_level:
            f.write("%s\n" % item)
    
    # cleaning the array to be empty in the next iterarion of distance
    signal_level = []