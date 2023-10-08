import logging
import json
import re
from datetime import time
from datetime import datetime
from datetime import date

logger = logging.getLogger('log')

"""
Model Definitions
"""


class Message(object):

    def __init__(self, content, msg_id=None, to_user_name=None, from_user_name=None, create_time=None, msg_type=None):
        self.msg_id = msg_id
        self.msg_type = msg_type
        self.to_user_name = to_user_name
        self.from_user_name = from_user_name
        self.create_time = create_time
        self.content = content


class GetUpData(object):
    nick: str
    get_up_time: time
    get_up_log: str

    def __init__(self, nick: str, get_up_time: time, get_up_log: str):
        self.nick = nick
        self.get_up_time = get_up_time
        self.get_up_log = get_up_log

    def __str__(self):
        return f'nick: {self.nick}, ' \
               f'get_up_time: {self.get_up_time}, ' \
               f'get_up_log: {self.get_up_log}, '

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, GetUpData):
            return self.get_up_time == other.get_up_time
        else:
            raise TypeError("Unsupported types for comparison")

    def __lt__(self, other):
        if isinstance(other, GetUpData):
            return self.get_up_time < other.get_up_time
        else:
            raise TypeError("Unsupported types for comparison")

    def __gt__(self, other):
        if isinstance(other, GetUpData):
            return self.get_up_time > other.get_up_time
        else:
            raise TypeError("Unsupported types for comparison")

    @staticmethod
    def custom_serializer(obj):
        if isinstance(obj, GetUpData):
            return {
                "nick": obj.nick,
                "get_up_time": obj.get_up_time,
                "get_up_log": obj.get_up_log
            }
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif isinstance(obj, time):
            return obj.strftime('%H:%M:%S')
        print(obj)
        raise TypeError("Type [GetUpData] not serializable")


"""
Util Classes
"""


def parse_message_content_without_format(message_content):
    res_dict = {}
    msg_content = message_content

    # If msg_content include `<title>` tag, only remind the contents inside the `<title></title>`
    match = re.search(r'<title>(.*?)<\\/title>', msg_content, re.IGNORECASE)
    if match:
        msg_content = match.group(1)

    index = 1
    index_label = '\n1. '
    # Clean up message head
    pos = msg_content.find(index_label)
    if pos == -1:
        return res_dict
    msg_content = msg_content[pos:]

    # Parse message
    while True:
        msg_content = msg_content[len(index_label):]
        index = index + 1
        index_label = f'\n{index}. '
        pos = msg_content.find(index_label)
        if pos == -1:
            single_record = msg_content
        else:
            single_record = msg_content[:pos]
            msg_content = msg_content[pos:]

        space_pos = single_record.find(' ')
        if space_pos == -1:
            continue
        key = single_record[:space_pos]
        val = single_record[space_pos + 1:]
        if key in res_dict:
            res_dict[key] += '\n' + val
        else:
            res_dict[key] = val

        if pos == -1:
            break

    return res_dict


def parse_first_integer(message_str) -> (int, int, int):
    """
    Return: (start_pos, end_pos, first_num)
    start_pos: The start pos of the first integer in the message_str
    end_pos: The end pos of the first integer in the message_str
    first_num: The value of the first integer in the message_str
    """
    start_pos: int = -1
    end_pos: int = -1
    first_num: int = 0

    find_num = False
    i = 0
    while i < len(message_str):
        c = message_str[i]
        if '0' <= c <= '9':
            if not find_num:
                start_pos = i
            c_num = int(c) - int('0')
            first_num = first_num * 10 + c_num
            find_num = True
        else:
            if find_num:
                break
        i += 1
    if find_num:
        end_pos = i
    return start_pos, end_pos, first_num


def get_pretty_json_get_up_data(data: dict[str, GetUpData]) -> str:
    return json.dumps(data, indent=4, ensure_ascii=False, default=GetUpData.custom_serializer)


def pretty_json_print_get_up_data(data) -> None:
    print(get_pretty_json_get_up_data(data))


"""
Constant Definitions
"""


VALID_LOG_MIN_LEN = 5
GET_UP_LATE_TIME = time(8)

USER_NAME_PLACEHOLDER = '[[USER_NAME_PLACEHOLDER]]'

UNLOG_REMINDER_COPYWRITE_TEMPLATE = "Hi，[[USER_NAME_PLACEHOLDER]]，记得更新今天的早起日志哦 (*^▽^*)"
GET_UP_LATE_REMINDER_COPYWRITE_TEMPLATE = "Hi，[[USER_NAME_PLACEHOLDER]]，今天的起床时间晚于8点呢？是遇到什么困难了嘛 =。=?"
FORMAT_ERROR_REMINDER_COPYWRITE_TEMPLATE = "Hi，[[USER_NAME_PLACEHOLDER]]，昵称识别失败，群里 @Bean 查下哈"

NO_USER_NEED_AT_COPYWRITE_TEMPLATE = '喜大普奔，今日无人可@'

TIME_END_FLAGS = {'\n', '-', '—'}


"""
Service Implementations
"""


class ChainMessageReminderService(object):

    def __init__(self, message: Message):
        self._message = message
        self._get_up_content_dict = {}

    @property
    def get_up_content_dict(self):
        return self._get_up_content_dict

    def get_reminded_msg(self, append_billboard: bool = False) -> str:
        self._get_up_content_dict, format_error_users = self._parse_get_up_time_and_log()
        if append_billboard:
            get_up_time_msg = self._build_get_up_time_billboard(self._get_up_content_dict)
        else:
            get_up_time_msg = ''

        unlog_users = self._get_unlog_users(self._get_up_content_dict)
        get_up_late_users = self._get_get_up_late_users(self._get_up_content_dict)

        unlog_reminder_copywrite = self._build_unlog_reminder_copywrite(unlog_users)
        get_up_late_reminder_copywrite = self._build_get_up_late_reminder_copywrite(get_up_late_users)
        format_error_reminder_copywrite = self._build_format_error_reminder_copywrite(format_error_users)

        return self._build_response_msg(
            unlog_reminder_copywrite,
            get_up_late_reminder_copywrite,
            format_error_reminder_copywrite,
            get_up_time_msg,
        )

    def get_parsed_content_dict(self) -> (dict[str, GetUpData], set):
        self._get_up_content_dict, format_error_users = self._parse_get_up_time_and_log()

        format_error_reminder_copywrite = self._build_format_error_reminder_copywrite(format_error_users)
        if format_error_reminder_copywrite:
            logger.error(format_error_reminder_copywrite)

        return self._get_up_content_dict, format_error_users

    def _parse_get_up_time_and_log(self) -> (dict[str, GetUpData], set):
        get_up_content_dict = {}
        format_error_users = set()

        # Parse the beginning number label
        message_content_dict = parse_message_content_without_format(self._message.content)

        # Parse the get up time and get up log
        # If parse failed, put this user into format_error_users set
        for nick, message in message_content_dict.items():
            hour_res = -1
            minute_res = -1
            log_start = len(message)

            hour_start, hour_end, hour_val = parse_first_integer(message)
            if hour_start != -1:
                nick += f' {message[:hour_start]}'
                nick = nick.strip()

                while hour_end < len(message) and message[hour_end] == ' ':
                    hour_end += 1

                if hour_end == len(message):
                    hour_res = hour_val
                    minute_res = 0
                    log_start = hour_end
                else:
                    hour_min_separaion = message[hour_end]
                    if hour_min_separaion in TIME_END_FLAGS:
                        hour_res = hour_val
                        minute_res = 0
                        log_start = hour_end
                    else:
                        minute_start, minute_pos, minute_val = parse_first_integer(message[hour_end + 1:].strip())
                        if minute_start == 0:
                            hour_res = hour_val
                            minute_res = minute_val
                            log_start = hour_end + 1 + minute_pos
                        else:
                            hour_res = hour_val
                            minute_res = 0
                            log_start = hour_end

            get_up_time = None
            get_up_log = None
            try:
                get_up_time = time(hour_res, minute_res)
                get_up_log = message[log_start:].strip()
            except Exception:
                logger.error(f'ChainMessageReminderService._parse_get_up_time_and_log error, '
                             f'nick: {nick}, message: {message}')

            # Build GetUpData for current user
            if get_up_time:
                data = GetUpData(nick, get_up_time, get_up_log)
                if nick not in get_up_content_dict \
                        or data.get_up_time < get_up_content_dict[nick].get_up_time:
                    get_up_content_dict[nick] = data
            else:
                format_error_users.add(nick)

        return get_up_content_dict, format_error_users

    @staticmethod
    def _get_unlog_users(get_up_content_dict: dict) -> set:
        unlog_users = set()
        for nick, data in get_up_content_dict.items():
            if len(data.get_up_log) < VALID_LOG_MIN_LEN:
                unlog_users.add(nick)
        return unlog_users

    @staticmethod
    def _get_get_up_late_users(get_up_content_dict: dict) -> set:
        get_up_late_users = set()
        for nick, data in get_up_content_dict.items():
            if GET_UP_LATE_TIME < data.get_up_time:
                get_up_late_users.add(nick)
        return get_up_late_users

    @staticmethod
    def _build_unlog_reminder_copywrite(unlog_users: set) -> str:
        if unlog_users:
            users_str = '@' + ' @'.join(unlog_users)
            return UNLOG_REMINDER_COPYWRITE_TEMPLATE.replace(USER_NAME_PLACEHOLDER, users_str)
        else:
            return ''

    @staticmethod
    def _build_get_up_late_reminder_copywrite(get_up_late_users: set) -> str:
        if get_up_late_users:
            users_str = '@' + ' @'.join(get_up_late_users)
            return GET_UP_LATE_REMINDER_COPYWRITE_TEMPLATE.replace(USER_NAME_PLACEHOLDER, users_str)
        else:
            return ''

    @staticmethod
    def _build_format_error_reminder_copywrite(format_error_users: set) -> str:
        if format_error_users:
            users_str = '@' + ' @'.join(format_error_users)
            return FORMAT_ERROR_REMINDER_COPYWRITE_TEMPLATE.replace(USER_NAME_PLACEHOLDER, users_str)
        else:
            return ''

    @staticmethod
    def _build_get_up_time_billboard(get_up_content_dict: dict) -> str:
        get_up_time_arr = []
        get_up_data_sorted_list = sorted(get_up_content_dict.values())
        for i in range(len(get_up_data_sorted_list)):
            item = get_up_data_sorted_list[i]
            get_up_time_arr.append(f'{i + 1}. {item.nick} {item.get_up_time.strftime("%H:%M")}')
        if get_up_time_arr:
            return f'今日打卡人数：{len(get_up_time_arr)}，早起时间日志：\n' + '\n'.join(get_up_time_arr)
        else:
            return ''

    @staticmethod
    def _build_response_msg(*args: str) -> str:
        response_msg_arr = []
        for arg in args:
            if arg:
                response_msg_arr.append(arg)

        if response_msg_arr:
            return '\n\n'.join(response_msg_arr)
        else:
            return NO_USER_NEED_AT_COPYWRITE_TEMPLATE
