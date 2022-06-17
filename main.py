from sys import exit
from textwrap import dedent
from modules.parser import *
from modules.utils import *
from modules.downloader import *
from modules.show import *
from modules.csv_downloader import *
from modules.bounding_boxes import *
from modules.image_level import *

ROOT_DIR = ''
DEFAULT_OID_DIR = os.path.join(ROOT_DIR, 'OID')

if __name__ == '__main__':

    args = parser_arguments()

    if args.command == 'downloader_ill':
        image_level(args, DEFAULT_OID_DIR)
    else:
        bounding_boxes_images(args, DEFAULT_OID_DIR)

'''
python main.py downloader --classes "Ball" "Football" "Golf_ball" "Cricket_ball" "Tennis_ball" --type_csv train --limit 500
python main.py downloader --classes "Ball" "Football" "Golf_ball" "Cricket_ball" "Tennis_ball" --type_csv validation --limit 300
python convert_annotations.py

python main.py downloader --classes "Missile" --type_csv train --limit 300
python main.py downloader --classes "Missile" --type_csv validation --limit 300
python convert_annotations.py

python main.py downloader --classes "Tennis_ball" --type_csv train --limit 300
python main.py downloader --classes "Tennis_ball" --type_csv validation --limit 300
python convert_annotations.py

now,have to remove label folder from each classes inside OID -> Dataset -> train & validation folder
'''
