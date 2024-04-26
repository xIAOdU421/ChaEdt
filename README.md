# RhyVFX ChaEdt
## RhyVFX chart editor

[English readme](README_en.md)

### 如何使用？

#### 安装依赖库

ChaEdt需要ursina才能正常运行
`pip install ursina`

#### 运行
下载github上的源代码
*(懒得打包。。。)*

使用python来运行
`python main.py`



#### 操作
鼠标上下滚动查看

上箭头摄像机置顶

右键Note长按拖动更改长按时间

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


