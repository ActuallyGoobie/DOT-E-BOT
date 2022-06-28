import requests
import json
def getData(APIendpoint, key = "key", publickey = 'key'):
    with open("db/servers.json") as fp: 
        serverList = json.load(fp)
    for server in serverList['servers']:
        if server['number'] == 'L':
            pass
        else:
            serverID = server["id"]
            serverEndpoint = f"https://tycoon-{serverID}.users.cfx.re/status" # Goodluck with this one
            try:
                response = str(requests.get(serverEndpoint + "/alive", headers={"X-Tycoon-Key": key, "X-Tycoon-Public-Key": publickey}, verify=True, timeout=1))
                if response == "<Response [204]>":
                    try:
                        data = requests.get(serverEndpoint + APIendpoint, headers={"X-Tycoon-Key": key, "X-Tycoon-Public-Key": publickey}, verify=True, timeout=2)
                        if str(data) == "<Response [200]>":
                            return data
                        if str(data) == "<Response [400]>":
                            return "400"
                        if str(data) == "<Response [412]>":
                            return "412"
                        if str(data) == "<Response [423]>":
                            return "423"
                        else:
                            pass
                    except requests.exceptions.RequestException:
                        pass
                elif response == "<Response [408]>":
                    pass 
                else:
                    pass
            except requests.exceptions.RequestException:
                pass