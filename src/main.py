import os
import urllib.request

from scrypted_sdk import ScryptedDeviceBase, Settings, Setting


ffmpeg_download = "https://github.com/scryptedapp/rockchip-essentials/releases/download/ffmpeg-6.0.1-0/ffmpeg"


class RockchipEssentials(ScryptedDeviceBase, Settings):

    def __init__(self) -> None:
        self.file = self.downloadFile(ffmpeg_download, 'ffmpeg')
        os.chmod(self.file, 0o755)

        print("Set the following environment variable to use ffmpeg with Rockchip hardware acceleration:")
        print(f"SCRYPTED_FFMPEG_PATH={self.file}")

    def downloadFile(self, url: str, filename: str):
        try:
            filesPath = os.path.join(os.environ['SCRYPTED_PLUGIN_VOLUME'], 'files')
            fullpath = os.path.join(filesPath, filename)
            if os.path.isfile(fullpath):
                return fullpath
            tmp = fullpath + '.tmp'
            print("Creating directory for", tmp)
            os.makedirs(os.path.dirname(fullpath), exist_ok=True)
            print("Downloading", url)
            response = urllib.request.urlopen(url)
            if response.getcode() < 200 or response.getcode() >= 300:
                raise Exception(f"Error downloading")
            read = 0
            with open(tmp, "wb") as f:
                while True:
                    data = response.read(1024 * 1024)
                    if not data:
                        break
                    read += len(data)
                    print("Downloaded", read, "bytes")
                    f.write(data)
            os.rename(tmp, fullpath)
            return fullpath
        except:
            print("Error downloading", url)
            import traceback
            traceback.print_exc()
            raise

    async def getSettings(self) -> list[Setting]:
        return [
            {
                "key": "ffmpeg_path",
                "title": "FFmpeg Path",
                "value": self.file,
                "readonly": True,
            }
        ]

    async def putSetting(self, key: str, value: str) -> None:
        pass


def create_scrypted_plugin():
    return RockchipEssentials()