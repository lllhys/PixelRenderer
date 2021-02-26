# 效果器开发
## 概述
PixelRenderer提供了自定义效果器的能力。您只需要一些基础numpy的使用知识就可以开发自己想要的过渡效果了。

## 介绍
我们提供了两种不同的效果器实现，他们分别是AbstractEffector和AbstractThreadingEffector（多线程）。当您需要开发一个效果器时，您只需要写一个类命名为Effector并实现这两个类的抽象方法就完成了一个效果器的开发。

下面我们看一个简单的例子吧。
```python
from renderer.abstract_effectors.abstract_effector import AbstractEffector

# 定义一个Effector，继承自AbstractEffector
class Effector(AbstractEffector):
    # 效果器名称
    _name_ = "My first effector"
    # 效果器支持的操作
    _func_ = ['show']
    
    #实现show方法
    def show(self):
        # 请在此实现过渡效果
        return 
```
您只需要在show中进行您需要的效果生成。这样一个支持show操作的名为My first effector的效果器就完成啦！

别忘了将它放置在renderer/effectors目录下。下次运行渲染引擎就会自动检测到它了。
