# API手册
## PixelCanvas
### 属性

|属性名      |类型|     介绍   |
|:----     	 |:---- |   :-:   |
|show_tool|PixelDisplay|暂不支持指定显示工具|
|shape|tuple(2)|画布大小|
|canvas_style|numpy.matrix|画布样式，存储了当前画布样式|
|layer_sum|int|画布层数，默认为4层|
|elements|Dirt|画布当前元素|
|element_diff|List|当前未渲染差异|
|renderer|[PixelRenderer](#pixelelement)|画布对应的渲染器，不支持指定|
|auto_renderer|bool|自动渲染状态|

### 方法

> #### __init__()

##### 介绍

- __init__方法

##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|:---|:---:|
|shape   |是  |tuple(2) |无 |画布形状|
|background|否|opacity color|0x0|背景色|
|layer_sum |否|int|4|层数 |

##### 返回

- 无

---

<div style='font-size: 20px;font-weight:600'>

?> put_element()

</div>

##### 介绍

- 在画布上放置一个元素
##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|----|
| element_name | 是 | str | 无 |元素名|
| element | 是 | PixelElement | 无 |元素对象|
| layer | 否 | int | 1 |元素所在层|
| position | 否 | tuple(2) | (0,0) |元素位置|
| effector_name | 否 | str | Fade |效果器名称|

##### 返回
- 无

---

<div style='font-size: 20px;font-weight:600'>

?> remove_element

</div>

##### 介绍

- 移除元素

##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
| element_name | 是 | str | 无 |元素名|
| effector_name | 否 | str | Fade |效果器名称|

##### 返回
- 无

---

<div style='font-size: 20px;font-weight:600'>

?> change_element_position

</div>

##### 介绍

- 改变元素位置

##### 参数
|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
| element_name | 是 | str | 无 |元素名|
| new_position | 是 | tuple(2) | 无 |元素新位置|
| effector_name | 否 | str | Default |效果器名称|

##### 返回
- 无

---

<div style='font-size: 20px;font-weight:600'>

?> switch_element_style

</div>

##### 介绍

- 切换元素样式

##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
| element_name | 是 | str | 无 |元素名|
| new_element | 是 | PixelElement | 无 |新的元素样式|
| effector_name | 否 | str | Fade |效果器名称|

##### 返回

- 无

---

<div style='font-size: 20px;font-weight:600'>

?> render_canvas

</div>

##### 介绍

- 进行一次渲染

##### 参数

- 无

##### 返回

- 无

---

<div style='font-size: 20px;font-weight:600'>

?> auto_renderer_open

</div>

##### 介绍

- 打开自动渲染并进行一次渲染


##### 参数

- 无

##### 返回

- 无

---

<div style='font-size: 20px;font-weight:600'>

?> auto_renderer_close

</div>

##### 介绍

- 关闭自动渲染

##### 参数

- 无

##### 返回

- 无

---

<div style='font-size: 20px;font-weight:600'>

?> auto_renderer_switch

</div>


##### 介绍

- 切换自动渲染状态

##### 参数

- 无

##### 返回

- 无

---

## PixelElement
### 属性

| 属性名        | 类型         | 介绍     |
| ------------- | ------------ | -------- |
| shape         | tuple(2)     | 元素大小 |
| element_mask  | numpy.matrix | 元素掩膜 |
| color_style   | numpy.matrix | 颜色样式 |
| element_style | numpy.matrix | 元素样式 |

### 方法

<div style='font-size: 20px;font-weight:600'>

?> __init__

</div>

##### 介绍

- PixelElement类__init__方法

##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
| element_type | 是 | int | 无 |1：掩膜+颜色样式	2：元素样式	3：颜色+纯色|
| color_style | element_type为1或2时 | numpy.matrix | None |颜色样式|
| element_mask | element_type为1时 | numpy.matrix | None |掩膜|
| color | element_type为3时 | opacity color | 0xffffffff |纯色样式时指定颜色|

##### 返回

- 无

---

<div style='font-size: 20px;font-weight:600'>

?> get_element_style

</div>


##### 介绍

- 获取元素样式

##### 参数

- 无

##### 返回

- 无



## Color

请import renderer包下color文件中所有方法来使用。

```python
from renderer.color import *
```

### 方法


<div style='font-size: 20px;font-weight:600'>

?> get_hex_color

</div>


##### 介绍

- 获取用于PixelDisplay显示的颜色

!> 内部方法，请勿在自定义效果器中使用该方法！效果器中请使用get_opacity_color

##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
||||||

##### 返回

- 无

---

<div style='font-size: 20px;font-weight:600'>

?>

</div>

##### 介绍

- 获取元素样式

##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
||||||

##### 返回

- 无

---
