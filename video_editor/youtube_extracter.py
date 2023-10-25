# from pytube import YouTube
#
# # 视频URL
# video_url = 'https://www.youtube.com/watch?v=reUZRyXxUs4'  # 替换为你想下载的视频链接
#
# # 使用YouTube类来创建一个视频对象
# yt = YouTube(video_url)
#
# # 获取视频对象中的最高分辨率的流（通常是mp4格式的视频流）
# video_stream = yt.streams.get_audio_only()
#
# # 下载视频到当前目录
# video_stream.download()
#
# print(f"Downloaded {yt.title} successfully!")


from moviepy.editor import *

# 加载视频
video = VideoFileClip("How AI Could Empower Any Business  Andrew Ng  TED.mp4")

# 提取1-3分钟的音频
audio = video.subclip(4, 63).audio  # 参数为秒

# 保存为MP3
audio.write_audiofile("How-AI-Could-Empower-Any-Business_Andrew-Ng_TED_Part-1.mp3")

# 关闭视频和音频对象以释放资源
audio.close()
video.close()
