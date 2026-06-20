from moviepy import *
from moviepy.video.fx import FadeIn
import math
import random
import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

open_eye = (
    ImageClip("g1.png")
    .resized(width=WIDTH, height=HEIGHT)
    .with_duration(1.8)
)

open_eye_end = (
    ImageClip("g1.png")
    .resized(width=WIDTH, height=HEIGHT)
    .with_duration(1)
)

close_eye = (
    ImageClip("g2.png")
    .resized(width=WIDTH, height=HEIGHT)
    .with_duration(0.7)
)

video = concatenate_videoclips([
    open_eye_end,
    close_eye,
    open_eye,
    open_eye_end,
    close_eye,
    open_eye,
    open_eye_end
])


winds = []

for i in range(10):
    winds.append([
        random.randint(0, WIDTH),
        random.randint(100, 600),
        random.randint(5, 15)
    ])

for frame in range(10):

    screen.fill((0,0,0))

    for w in winds:

        pygame.draw.line(
            screen,
            (255,255,255),
            (w[0], w[1]),
            (w[0]-50, w[1]),
            2
        )

        w[0] -= w[2]

        if w[0] < -100:
            w[0] = WIDTH + 100

    pygame.image.save(
        screen,
        f"frames/frame_{frame:04d}.png"
    )

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

wind_video = ImageSequenceClip(
    [f"frames/frame_{i:04d}.png" for i in range(10)],
    fps=30
)

video = concatenate_videoclips([video] * 4)
video = video.subclipped(0, 30)

texts = []

for start in [0, 8, 16, 24]:

    texts.append(
    TextClip(
        text="Wait...",
        font_size=70,
        font="angsana.ttc",
        color="yellow",
        margin=(20, 40),
        stroke_color="black",
        stroke_width=3
    )
    .with_start(start+0.5)
    .with_duration(3)
    .with_position((100, 330))
    .with_effects([FadeIn(0.5)])
    .with_position(
    lambda t: (
        100,
        330 + 5 * math.sin(t * 3)
    )
)
    .resized(
    lambda t: 1 + 0.05 * math.sin(t * 3))
)

    texts.append(
    TextClip(
        text="Python Can Do THIS?!",
        font_size=70,
        font="angsana.ttc",
        color="yellow",
        margin=(20, 40),
        stroke_color="black",
        stroke_width=3
    )
    .with_start(start+1.5)
    .with_duration(2)
    .with_position(("center", 430))
    .with_effects([FadeIn(0.5)])
)

    texts.append(
    TextClip(
        text="Python ทำ Intro ได้ด้วยหรือ?!",
        font_size=60,
        font="angsana.ttc",
        color="yellow",
        margin=(20, 40),
        stroke_color="black",
        stroke_width=3
    )
    .with_start(start+3.5)
    .with_duration(4.5)
    .with_position(("center", 430))
    .with_effects([FadeIn(0.5)])
    .with_position(
    lambda t: (
        100,
        430 + 5 * math.sin(t * 3)
    )
)
    .resized(
    lambda t: 1 + 0.05 * math.sin(t * 3)
)
)

video = video.resized(
    lambda t: 1 + 0.01 * math.sin(t*2)
)

videoe = CompositeVideoClip(
    [
        video,
        wind_video.with_opacity(0.4)
    ] + texts
).with_duration(30)

# videoe.write_videofile(
#     "itg6.mp4",
#    fps=30
# )
