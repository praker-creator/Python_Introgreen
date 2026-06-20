from moviepy import AudioFileClip

audio = AudioFileClip("cutremix.mp3")

cut = audio.subclipped(14, 44)

cut.write_audiofile("remixg.mp3")