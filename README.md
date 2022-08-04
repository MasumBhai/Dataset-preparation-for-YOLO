### Installation

1. Clone this repository 
```bash
https://github.com/MasumBhai/Dataset-preparation-for-YOLO.git
```
2. Requirement installation

```bash
pip3 install -r requirements.txt
```

### Where to get labeled image dataset
<a href="https://storage.googleapis.com/openimages/web/index.html" target="_blank">Open Image Dataset</a>

### How to download those labeled image dataset
For Single Class Download to train & validation
```bash
python main.py downloader --classes "Missile" --type_csv train --limit 300
python main.py downloader --classes "Missile" --type_csv validation --limit 300
```
For Multiple Class Download to train & validation
```bash
python main.py downloader --classes "Ball" "Football" "Golf_ball" "Cricket_ball" "Tennis_ball" --type_csv train --limit 500
python main.py downloader --classes "Ball" "Football" "Golf_ball" "Cricket_ball" "Tennis_ball" --type_csv validation --limit 300
```
### How to Annotate those downloaded images
```bash
python convert_annotations.py
```
#### Now, just remove label folder from each classes inside OID -> Dataset -> train & validation folder for YOLO processing

### Acknowledgement
these two awesome repositories <br/>
##### 1. <a href="https://github.com/theAIGuysCode/OIDv4_ToolKit.git" target="_blank">theAIGuysCode / OIDv4_ToolKit</a> <br/>
##### 2. <a href="https://github.com/EscVM/OIDv4_ToolKit.git" target="_blank">EscVM / OIDv4_ToolKit</a>

## Feedback

If you have any feedback, please reach out to me at abdullahmasum6035@gmail.com

| <a href="https://github.com/MasumBhai"><img alt="Abdullah Al Masum's Github Stats" src="https://github-readme-stats.vercel.app/api?username=masumBhai&show_icons=true&count_private=true&theme=great-gatsby" width=500></a> | <a href="https://github.com/MasumBhai"><img alt="Abdullah Al Masum's Github Streak" src="https://github-readme-streak-stats.herokuapp.com?user=MasumBhai&theme=vision-friendly-dark&fire=DD2727&sideNums=CD5CDD" width=500></a> |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|