# RhyVFX ChaEdt
## RhyVFX chart editor

[中文简体自述](README_cn.md)

### How to use?

#### Install libs

ChaEdt need ursina engine  
`pip install ursina`

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


