import cdblib
import requests

url = "http://ddb.glidernet.org/download/?j=1"
cdb_file = "ogn.cdb"

response = requests.get(url)
data = response.json()

nb_devices = 0

with open(cdb_file, "wb") as cdbfile:
    writer=cdblib.Writer(cdbfile)

    for device in enumerate(data['devices']):
        details = device[1]['aircraft_model'].encode("utf-8")+b'|'+device[1]['registration'].encode("utf-8")+b'|'+device[1]['cn'].encode("utf-8")
        if (details != b'||'):
            writer.put(device[1]['device_id'].encode("utf-8"),details)
            nb_devices += 1

    writer.finalize()

print(f"OGN DDB with {nb_devices} devices has been converted to CDB file '{cdb_file}'.")
