from covid import Covid
import json

covid = Covid()

x=covid.get_data()

print(json.dumps(x, sort_keys=True, indent=4))