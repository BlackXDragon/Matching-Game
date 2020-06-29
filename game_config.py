import os
import sys

IMAGE_SIZE = 128
SCREEN_SIZE = 512
NUM_TILES = 4
NUM_TILES_TOTAL = 16
MARGIN = 4

ASSET_DIR = '.'
OTHER_ASSETS_DIR = '.'
FONT_DIR = '.'
if not getattr(sys, 'frozen', False):
	ASSET_DIR = 'assets'
	OTHER_ASSETS_DIR = 'other_assets'
	FONT_DIR = 'fonts'
ASSET_FILES = [assetFile for assetFile in os.listdir(ASSET_DIR) if assetFile[:5].lower() == 'anim_']

assert len(ASSET_FILES) == 8
