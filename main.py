from polygon import RESTClient
import json
import re

client = RESTClient(api_key="cONqvzinqAUbQ0TSqI7MAYOo3hdsf5d8")
GME = client.get_aggs("GME", 1, "day", "2024-07-23", "2024-07-27", sort="asc")
with open("temp.json", "w") as f:
    items = [json.dumps(item, default=str) for item in GME]
    out = "[\n" + ",\n".join(items) + "\n]"
    f.write(out)

with open("GME.json", "r") as infile:
    data = json.load(infile)

# Your JSON string
for item in GME:
    json_string = str(GME[item])

    data = json.loads(json_string)

    data_string = data[0]

    match = re.search(r'close=([0-9\.]+)', data_string)
    if match:
        close_value = float(match.group(1))
        with open("temp.json", "w") as f:
            f.write(close_value)
            f.write("\n")
    else:
        print('Close value not found')