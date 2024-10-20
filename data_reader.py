def get_data(file_name):
    with open(file_name,'r') as f:
        data = f.read()
    return data