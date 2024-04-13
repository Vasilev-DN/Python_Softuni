import re

pattern = re.compile(
    r"www.([A-Za-z0-9\-]+)(\.[a-z]+)+")

while True:
    main_string = input()
    if main_string:
        result = re.finditer(pattern, main_string)
        for show in result:
            print(show[0])
    else:
        break


