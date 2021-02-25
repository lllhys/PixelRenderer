# 功能
本章节将演示PixelRenderer所提供的所有功能。通过本章节的阅读，您将对PixelRenderer有更全面的了解。
## 画布
### 概念
在PixelRenderer中画布是元素的容器，用于装载不同的元素。PixelRenderer中的画布提出了层的概念。
每一个元素被放置在画布上时，应当指出画布所在的层与位置。然后画布将交由渲染器进行渲染后显示。
### 功能
#### 初始化
画布初始化时需要指定画布的大小，同时还有两个可选参数：画布层数与画布颜色。画布颜色定义在第0层，所以当其他元素放置时应尽量避开第0层。
```python
# 详细用法请参阅API手册
pixel_canvas = PixelCanvas((8,32),background=0x0,layer_sum=4)
```
#### 放置元素
我们可以在画布上放置一个元素，放置元素时应当指出元素名（唯一索引）、元素的样式（PixelElement类的对象）、元素所在层、元素的位置以及所使用的效果器。
放置元素默认使用Fade效果器（在效果器一部分您将更全面的了解）。然后我们会自动调用渲染器进行一次渲染，您将实时看到您所作的变更。
```python
# 详细用法请参阅API手册
pixel_canvas.put_element(element_name='3', element=element, layer=1, position=(1, 12))
```
#### 移动元素
我们可以对在画布上放置的元素进行移动，还记得上面提到的元素名吗？移动元素时我们只需要指出元素名与元素的新位置。请注意，移动渲染默认使用Default效果器，且部分内置效果器不支持移动效果。
```python
# 详细用法请参阅API手册
pixel_canvas.change_element_position(element_name='3', new_position=(2, 15))
```
#### 改变元素样式
每个元素的样式并不是一尘不变的，所以我们提供了元素样式变更的功能。当元素需要变更时只要指定元素名与新的元素（新的PixelElement对象）就可以改变元素样式了。
```python
# 详细用法请参阅API手册
new_element = PixelElement(1, color_style_2, static_font.num_5_mask)
pixel_canvas.switch_element_style(element_name='5',new_element=new_element)
```
#### 删除元素
当元素不再需要时，可以通过元素名将其删除。
```python
# 详细用法请参阅API手册
pixel_canvas.remove_element('3')
```
#### 自动渲染
为了尽可能简便地操作画布，PixelRenderer默认开启了画布自动渲染。每当画面发生变更时渲染器都会自动对画面进行渲染。但是某些时候画面可能同时需要多处变更，所以我们提供了自动渲染的开关。
```python
# 详细用法请参阅API手册
# 关闭自动渲染
pixel_canvas.auto_renderer_close()
# 打开自动渲染，并会进行一次渲染
pixel_canvas.auto_renderer_open()
# 切换开关状态
pixel_canvas.auto_renderer_switch()
```
## 元素
元素是PixelRenderer中可操作的最小对象。我们提供了3种初始化元素的方式。
### 1. 使用掩膜+颜色样式初始化（推荐）
使用元素掩膜以及每个像素的颜色初始化一个元素。
```python
# 定义一个掩膜
num_3_mask = numpy.array([
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0]
])
# 定义颜色样式
color_style = get_random_color_style((5, 5))
# 初始化一个元素
element = PixelElement(element_type=1, element_mask=num_3_mask, color_style=color_style)
```
### 2. 使用颜色样式初始化
当元素为规则图形时，应使用颜色样式初始化。
```python
# 定义颜色样式
color_style = get_random_color_style((5, 5))
# 初始化一个元素
element = PixelElement(element_type=2, color_style=color_style)
```
### 3.使用掩膜+颜色初始化（推荐）
当元素为单色时，应使用该方式初始化一个元素。
```python
# 定义一个掩膜
num_3_mask = numpy.array([
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0]
])
# 初始化一个元素
element = PixelElement(element_type=1, element_mask=num_3_mask, color=0xff00ff00)
```

## 效果器
效果器决定了画布上元素发生变化时，您所看到的画面过渡。效果器目前提供了两个内置效果器，分别是Fade和Default效果器，在对画布元素操作时，可以通过指定效果器名称来使用他们。若您需要其他效果器，可以参阅自定义效果器章节，开发属于您自己的效果器。
### Default效果器
Default效果器实现了抽象类AbstractEffector。Default效果器支持显示、移除、位移、与切换样式的效果。但是样式效果较为单调，您可以尝试使用Default效果器查看效果。当您指定的其他效果器无效或您指定的效果器不支持对应方法时，PixelRenderer将自动切换使用Default效果器。
### Fade效果器
Fade效果器提供淡入淡出的显示效果。Fade效果器实现了抽象类AbstractThreadingEffector，所以Fade效果器支持多线程渲染（您可以在自定义效果器部分学习更多有关效果器的内容）。但是需要注意的是，Fade效果器不支持元素移动时效果。所以除了元素移动效果使用Default外，其他所有效果都默认使用Fade效果器进行渲染。