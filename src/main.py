import asyncio
import os
import shutil
from torrentp import TorrentDownloader
import random


# Read magnet from environment variable
# download the torrent then delete the file after download

async def download_delete():
    magnet = os.environ.get('MAGNET')
    random_name = str(random.randint(0, 1000))
    torrent = TorrentDownloader(magnet, 'downloads/' + random_name)
    await torrent.start_download()
    # Delete the file after download
    shutil.rmtree('downloads/' + random_name)

def main():
    asyncio.run(download_delete())


if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=main)
        processes.append(p)
        p.start()
    for p in processes:
        p.join()



