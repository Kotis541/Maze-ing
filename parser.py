import sys
import os
from typing import Any


def read_config() -> dict[Any, Any] | None:
    """
    Reads and validates the maze configuration
    from a file provided as a command-line argument.
    """

    res: dict[str, Any] = {}
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
                if not (1 < res['WIDTH'] < 45):
                    raise ValueError("invalid WIDTH size")
                res['HEIGHT'] = int(res['HEIGHT'])
                if not (1 < res['WIDTH'] < 45):
                    raise ValueError("invalid WIDTH size")
                exit_err = res['ENTRY'].split(",")
                if len(exit_err) != 2:
                    raise ValueError(f"ENTRY: {exit_err}")
                else:
                    res['ENTRY'] = (int(exit_err[0]), int(exit_err[1]))
                    x = res['ENTRY'][0]
                    y = res['ENTRY'][1]
                    if (not (0 <= x < res['WIDTH'])
                            or not (0 <= y < res['HEIGHT'])):
                        raise ValueError("ENTRY is out of bounds")
                exit_err = res['EXIT'].split(",")
                if len(exit_err) != 2:
                    raise ValueError(f"EXIT: {exit_err}")
                else:
                    res['EXIT'] = (int(exit_err[0]), int(exit_err[1]))
                    x = res['EXIT'][0]
                    y = res['EXIT'][1]
                    if (not (0 <= x < res['WIDTH'])
                            or not (0 <= y < res['HEIGHT'])):
                        raise ValueError("EXIT is out of bounds")
                bool_map = {"TRUE": True, "FALSE": False}
                res['PERFECT'] = bool_map[res['PERFECT'].upper()]
                if not res['OUTPUT_FILE']:
                    raise ValueError("OUTPUT_FILE")
                if 'SEED' in res:
                    if not res['SEED']:
                        raise ValueError("SEED")
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
    return None
