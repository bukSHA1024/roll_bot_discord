# search int in string A and return founded int or default value B in case of exception
# usage: parse_number(string A, int B)
def parse_number(string, default_value):
    try:
        return int(string)
    except ValueError:
        return default_value
