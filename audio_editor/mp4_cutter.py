from moviepy.editor import *

time_list = [
    "00:00",
    "19:36",
    "47:48",
    "1:10:25",
    "1:33:33",
    "1:48:38",
    "2:06:39",
    "2:24:50",
    "2:34:09",
    "2:53:43",
    "3:12:15",
    "3:29:29",
    "3:39:03",
    "3:56:49",
    "4:11:15",
    "4:24:54",
    "4:46:08",
    "5:04:38",
    "5:16:26",
    "5:38:17",
    "5:52:34",
    "6:11:34"
]
name_list = [
    "Atomic Habits - Introduction",
    "Atomic Habits - Ch1 - The surprising power of atomic habits",
    "Atomic Habits - Ch2 - How your habits shape your identity (and vice versa)",
    "Atomic Habits - Ch3 - How to build better habits in 4 simple steps",
    "Atomic Habits - Ch4 - The man who didn't look right",
    "Atomic Habits - Ch5 - The best way to start a new habit",
    "Atomic Habits - Ch6 - Motivation is overrated; Environment often matters more",
    "Atomic Habits - Ch7 - The secret to self control",
    "Atomic Habits - Ch8 - How to make a habit irresistible",
    "Atomic Habits - Ch9 - The Role of Family and Friends in Shaping Your Habits",
    "Atomic Habits - Ch10 - How to Find and Fix the Causes of Your Bad Habits",
    "Atomic Habits - Ch11 - Walk Slowly, but Never Backward",
    "Atomic Habits - Ch12 - The Law of Least Effort",
    "Atomic Habits - Ch13 - How to Stop Procrastinating by Using the Two-Minute Rule",
    "Atomic Habits - Ch14 - How to Make Good Habits Inevitable and Bad Habits Impossible",
    "Atomic Habits - Ch15 - The Cardinal Rule of Behaviour Change",
    "Atomic Habits - Ch16 - How to Stick with Good Habits Every Day",
    "Atomic Habits - Ch17 - How an Accountability Partner Can Change Everything",
    "Atomic Habits - Ch18 - The Truth About Talent (When Genes Matter and When They Don’t)",
    "Atomic Habits - Ch19 - The Goldilocks Rule How to Stay Motivated in Life and Work",
    "Atomic Habits - Ch20 - The Downside of Creating Good Habits",
    "Atomic Habits - Conclusion"
]


def time_to_seconds(time_str):
    parts = time_str.split(':')
    # 根据时间字符串的部分数量，将其转换为秒
    if len(parts) == 3:  # HH:MM:SS格式
        hours, minutes, seconds = parts
        return int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    elif len(parts) == 2:  # MM:SS格式，或假定的HH:MM格式
        # 如果时间字符串表示的是超过1小时的时间（例如"47:48"），但格式为MM:SS
        minutes, seconds = parts
        return int(minutes) * 60 + int(seconds)
    else:
        raise ValueError("Invalid time format")


# 加载视频
audio = AudioFileClip("Atomic Habits.mp4")
# for i in range(0, len(time_list)):
for i in [19]:
    start = time_to_seconds(time_list[i])
    if i < len(time_list) - 1:
        end = time_to_seconds(time_list[i+1])
    else:
        end = audio.end
    ele = audio.subclip(start, end)

    # 保存为MP3
    ele.write_audiofile(name_list[i] + ".mp3")

# 关闭视频和音频对象以释放资源
audio.close()
print("Finished")
