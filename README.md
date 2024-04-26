# RhyVFX ChaEdt
## RhyVFX chart editor

[English readme](README_en.md)

### 如何使用？

#### 安装依赖库

ChaEdt需要ursina才能正常运行(必须为ursina6.1.2)
`pip install ursina==6.1.2`

#### 运行
下载github上的源代码
*(懒得打包。。。)*

使用python来运行
`python main.py`



#### 操作
鼠标上下滚动查看

上箭头摄像机置顶

右键Note长按拖动更改长按时间

### 要求文件
#### 文件夹
MapAssets/charts/backups为谱面文件备份

MapAssets/song/song.ogg存放的曲子(ogg格式)



#### Sets
"settings.json"是ChaEdt的设置文件

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

`keys` 键位设置.

`render_range` 为了优化，会使看不见的note设置为不可见.


