import re

my_file = open('file_task1')
file_read = my_file.read()
file_read = re.findall(r'\d{2}-\d{2}-\d{4}', file_read)

result_dates = []

for dt in file_read:
    try:
        result_dates.append(dt)
    except:
        next(dt)
print(result_dates)
my_file.close()
