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

                exit_err = res['ENTRY'].split(",")
                if len(exit_err) != 2:
                    raise ValueError("Invalid configuration file")
                else:
                    res['ENTRY'] = (int(exit_err[0]), int(exit_err[1]))
               
                exit_err = res['EXIT'].split(",")
                if len(exit_err) != 2:
                    raise ValueError("Invalid configuration file")
                else:
                    res['EXIT'] = (int(exit_err[0]), int(exit_err[1]))

                bool_map = {"TRUE": True, "FALSE": False}
                res['PERFECT'] = bool_map[res['PERFECT'].upper()]
            except Exception as e:
                print(e)
                return None
        return res
    else:
        print("No valid configuration file, please try again!")


