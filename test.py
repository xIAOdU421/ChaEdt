from ursina import *

class ClickableEntity(Entity):
  def __init__(self, **kwargs):
    super().__init__(
      model='cube',
      color=color.orange,
      scale=(1, 1, 1),
      collider='box',
      **kwargs
    )

  def input(self, key):
    if key == 'right mouse down' and mouse.hovered_entity == self:
      print(f'右键点击了实体 {self}')

app = Ursina()
window.borderless = False

# 创建可点击的实体
entity1 = ClickableEntity(position=(-2, 0, 0))
entity2 = ClickableEntity(position=(2, 0, 0))

app.run()
