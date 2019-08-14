import base64
import zlib


class StringZipper:

    @staticmethod
    def zip(str):
        zip_str = zlib.compress(str)
        return zip_str

    @staticmethod
    def unzip(str):
        return zlib.decompress(str)

    @staticmethod
    def b64encode(str):
        b64_str = base64.b64encode(str)
        return b64_str

    @staticmethod
    def b64decode(str):
        return base64.b64decode(str)
