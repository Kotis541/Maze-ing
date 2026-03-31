def read_config() -> dict:
    res = {}
    with open('config.txt', 'r') as file:
        for line in file:
            if not line or line.startswith("#"):
                continue
            key, value = line.strip().split("=")
            res[key] = value
    return res
