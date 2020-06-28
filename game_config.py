import os

IMAGE_SIZE = 128
SCREEN_SIZE = 512
NUM_TILES = 4
NUM_TILES_TOTAL = 16
MARGIN = 4

ASSET_DIR = 'assets'
ASSET_FILES = [assetFile for assetFile in os.listdir(ASSET_DIR) if assetFile[-3:].lower() == 'png']

assert len(ASSET_FILES) == 8
