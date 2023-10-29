from moviepy.editor import *

# 加载视频
audio = AudioFileClip("How-AI-Could-Empower-Any-Business_Andrew-Ng_TED_Part-1.mp3").subclip(0, 30)

# 保存为MP3
audio.write_audiofile("How-AI-Could-Empower-Any-Business_Andrew-Ng_TED_Part-1_0-30.mp3")

# 关闭视频和音频对象以释放资源
audio.close()
