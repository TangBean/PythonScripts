import sys
import csv
from datetime import datetime
import pyperclip


def gen_time_log_by_csv(filename: str) -> str:
    log_msgs = []

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            log_event = ''
            if row.__contains__('事件'):
                log_event = row['事件']
            if row.__contains__('\ufeff事件'):
                log_event = row['\ufeff事件']

            log_type = row['类型']
            duration = row['持续时间'] \
                           .split('分')[0] \
                           .replace(' ', '') \
                           .replace('小时', 'h') \
                       + 'm'

            log_end_time = datetime.strptime(row['终于'], '%Y-%m-%d %H:%M:%S')
            formatted_log_end_time = formatted_time = "{}:{:02d}".format(log_end_time.hour, log_end_time.minute)

            new_line = f"-{formatted_log_end_time}【{log_type}】{log_event}｜{duration}"
            log_msgs.append(new_line)

    return '\n'.join(log_msgs)


"""
Run script
"""
if len(sys.argv) > 1:
    input_filename = sys.argv[1]
    time_logs = gen_time_log_by_csv(input_filename)
    print(time_logs)
    pyperclip.copy(time_logs)
else:
    print("No filename provided.")
    print("Please use: python3 time_logs.py [CSV filename, e.g. xxx.csv]")
