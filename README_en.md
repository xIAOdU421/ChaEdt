# RhyVFX ChaEdt
## RhyVFX chart editor

[中文简体自述](README_cn.md)

### How to use?

#### Install libs

ChaEdt need ursina engine(Must ursina6.1.2)
`pip install ursina==6.1.2`

#### Running
Download source code.
Then you can run "main.py"  
`python main.py`



#### Operations
Mouse scroll up camera will going up. 

Mouse scroll down camera will going down. 

Press up arrow can return to origin. 

Right mouse button click chart can edit chart tail. 


### Require files
#### Folders
MapAssets/charts/backups for chart file backups

MapAssets/song/song.ogg for song




#### Sets
"settings.json" is ChaEdt set file.

```json
{
  "keys": [
    "s",
    "d",
    ";",
    "'"
  ],
  "render_range": 1000
}
```

`keys` Keys sets.

`render_range` For the performance,it will set some charts invisible.


