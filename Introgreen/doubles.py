from moviepy import AudioFileClip, concatenate_audioclips

audio = AudioFileClip("cinder.mp3")

long_audio = concatenate_audioclips([
    audio,
    audio
])

long_audio.write_audiofile("cinder1.mp3")