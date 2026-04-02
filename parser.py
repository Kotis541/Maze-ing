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
                if res['WIDTH'] <= 1:
                    raise ValueError("WIDTH cannot be less than 2")
                res['HEIGHT'] = int(res['HEIGHT'])
                if res['HEIGHT'] <= 1:
                    raise ValueError("HEIGHT cannot be less than 2")
                exit_err = res['ENTRY'].split(",")
                if len(exit_err) != 2:
                    raise ValueError(f"ENTRY: {exit_err}")
                else:
                    res['ENTRY'] = (int(exit_err[0]), int(exit_err[1]))
                    if res['ENTRY'][0] < 0 or res['ENTRY'][0] > res['WIDTH'] - 1:
                        raise ValueError("ENTRY cannot be outside width x height")
                    elif res['ENTRY'][1] < 0 or res['ENTRY'][1] > res['WIDTH'] - 1:
                        raise ValueError("ENTRY cannot be outside width x height")

                exit_err = res['EXIT'].split(",")
                if len(exit_err) != 2:
                    raise ValueError(f"EXIT: {exit_err}")
                else:
                    res['EXIT'] = (int(exit_err[0]), int(exit_err[1]))

                bool_map = {"TRUE": True, "FALSE": False}
                res['PERFECT'] = bool_map[res['PERFECT'].upper()]
            except KeyError as e:
                print(
                    "Configuration Error: Missing or",
                    f"misspelled mandatory key {e}"
                    )
                return None
            except ValueError as e:
                print(f"Configuration Error: Invalid data format or value {e}")
                return None
            except Exception as e:
                print(f"An unxepected error occured: {e}")
                return None
        return res
    else:
        print("No valid configuration file, please try again!")

read_config()