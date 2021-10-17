from pytube import YouTube
from pytube import Playlist

# RESERVED_NAMES_MAP = [
    # { 'Чому саме фізфак? Мирослав Кавацюк' : 1},
    # { 'Чому саме фізфак? Галатюк Тетяна' : 2},
    # { 'Чому саме фізфак? Бондаренко Ольга' : 3},
    # { 'Чому саме фізфак? Анастасія Золотарьова, випускниця 2015 року' : 4},
    # { 'Андрій Наточій | Шлях на Фуджі або навіщо займатись фізикою?' : 5},
    # { 'Почему физфак КНУ, почему кафедра ядерной физики и почему быть физиком круто' : 6},
    # { 'Чому фізичний факультет КНУ імені Т. Шевченка, чому Кафедра Ядерної Фізики?' : 7},
    # { 'Чому саме фізфак? Інна Макаренко та Денис Лонтковський' : 8},
    # { 'Фізичний факультет як квиток у життя' : 11},
    # { 'Звернення до абітурієнтів' : 12}
# ]
#RESERVED_NAMES = []

LINKS = [
    'https://www.youtube.com/watch?v=wN__2xl-SEc&list=PLKFgsOuJ0Bmz3S1_uVWmycZc1bJW3KvkR&index=21',
    'https://www.youtube.com/watch?v=waX1mqMUGNU&list=PLKFgsOuJ0Bmz3S1_uVWmycZc1bJW3KvkR&index=28',
    'https://www.youtube.com/watch?v=cWSLoelfvgc&list=PLKFgsOuJ0Bmz3S1_uVWmycZc1bJW3KvkR&index=33',
    'https://www.youtube.com/watch?v=wN__2xl-SEc&list=PLKFgsOuJ0Bmz3S1_uVWmycZc1bJW3KvkR&index=67',
    'https://www.youtube.com/watch?v=wN__2xl-SEc&list=PLKFgsOuJ0Bmz3S1_uVWmycZc1bJW3KvkR&index=73',
    'https://www.youtube.com/watch?v=wN__2xl-SEc&list=PLKFgsOuJ0Bmz3S1_uVWmycZc1bJW3KvkR&index=18',
    'https://www.youtube.com/watch?v=wN__2xl-SEc&list=PLKFgsOuJ0Bmz3S1_uVWmycZc1bJW3KvkR&index=3',
    'https://www.youtube.com/watch?v=wN__2xl-SEc&list=PLKFgsOuJ0Bmz3S1_uVWmycZc1bJW3KvkR&index=7',
    'https://www.youtube.com/watch?v=wN__2xl-SEc&list=PLKFgsOuJ0Bmz3S1_uVWmycZc1bJW3KvkR&index=53',
    'https://www.youtube.com/watch?v=wN__2xl-SEc&list=PLKFgsOuJ0Bmz3S1_uVWmycZc1bJW3KvkR&index=2'
]

YOUTUBE_URL = 'https://www.youtube.com/playlist?list=PLKFgsOuJ0Bmz3S1_uVWmycZc1bJW3KvkR'
DOWNLOAD_DIR = '../videoPack'

def find_in_reserved_list(name):
    for item in RESERVED_NAMES:
        if item in name: 
            return RESERVED_NAMES_MAP[item]
    return 0

playlist = Playlist(YOUTUBE_URL)

print('Amount videos in playlist ' + str(len(playlist.video_urls)))

# physically downloading the audio track
index = 1
for video in playlist.videos:
    video_name = str(index) + '.mp4'
    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=DOWNLOAD_DIR, filename=video_name)
    index = index + 1

# for link in LINKS:
    # video_name = str(index)
    # video = YouTube(link)
    # video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=DOWNLOAD_DIR, filename=video_name)
    # index = index + 1