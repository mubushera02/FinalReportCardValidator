def read_json_file(file_path):
    import json
    with open(file_path, "r") as f:
        return json.load(f)

def compute_file_hash(file_path):
    import hashlib
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()
