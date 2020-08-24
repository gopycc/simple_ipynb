from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

print('root: %s' % BASE_DIR)