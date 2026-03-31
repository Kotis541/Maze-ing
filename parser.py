import sys
import os


def read_config() -> dict:
    res = {}
    if len(sys.argv) != 2:
        print("No valid configuration file, please try again!")
    elif os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as file:
            for line in file:
                if not line or line.startswith("#"):
                    continue
                if '=' in line:
                    key, value = line.strip().split("=")
                    res[key] = value
                else:
                    print("No valid configuration file, please try again!")
                    return None
            try:
                res['WIDTH'] = int(res['WIDTH'])
                res['HEIGHT'] = int(res['HEIGHT'])
                res['ENTRY'] = int(res['ENTRY'].split(","))
                res['EXIT'] = (int(res['EXIT'].split(",")))
            except (ValueError, KeyError) as e:
                print(e)
        return res
    else:
        print("No valid configuration file, please try again!")


print(read_config())
