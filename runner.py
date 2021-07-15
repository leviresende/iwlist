import iwlist
import json
import time

# distance between cellphone and notebook
distance = "1m"

# repeat this task for 100 times
for x in range(0, 100):

    # scanning networks
    content = iwlist.scan(interface="wlo1")

    # parsing the contents
    cells = iwlist.parse(content)

    # save each run in a different json file
    file = "./reads/" + distance + "/read_" + str(x) + ".json"
    with open(file, 'w') as json_file:
        json.dump(cells, json_file)
    
    print('Processing ...')
    time.sleep(5)