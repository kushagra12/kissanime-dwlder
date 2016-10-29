import requests
import sys
import os

initial_path = 'D:\Anime'

def download_episode(link, episode_name, series_name):

    directory_series = os.path.join(initial_path, series_name)

    if not os.path.exists(directory_series):
        os.makedirs(directory_series)

    file_name = os.path.join(initial_path,series_name, episode_name)

    print("Downloading %s" % file_name)
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')

    with open(file_name, "wb") as f:

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
                sys.stdout.flush()
