# Color

请import renderer包下color文件中所有方法来使用。

```python
from renderer.color import *
```

## 定义

<div style='font-size: 25px;font-weight:700' id="hex_color">

?> hex color

</div>

hex color为PixelDisplay显示内部颜色类型，为uint32类型，由高至底每8位分别为白色、红色、绿色、蓝色

---

<div style='font-size: 25px;font-weight:700' id="opacity_color">

?> opacity color

</div>

Opacity color为PixelRenderer中自定义的具有不透明度的颜色，为uint32类型。由高至底每8位分别为不透明度、红色、绿色、蓝色

## 方法

---

<div style='font-size: 25px;font-weight:700' id="get_hex_color">

?> get_hex_color()

</div>


##### 介绍

- 获取用于PixelDisplay显示的颜色

!> 内部方法，请勿在自定义效果器中使用该方法！效果器中请使用[get_opacity_color](#get_opacity_color)。

##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
|red|是|uint8|无|红色值|
|green|是|uint8|无|绿色值|
|blue|是|uint8|无|蓝色值|
|white|否|uint8|0|白色值|

##### 返回

- [hex color](#hex_color),PixelDisplay显示的颜色

---

<div style='font-size: 25px;font-weight:700' id="get_opacity_color">

?> get_opacity_color()

</div>

##### 介绍

- 生成一个具有不透明度的颜色

##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
|red|是|uint8|无|红色值|
|green|是|uint8|无|绿色值|
|blue|是|uint8|无|蓝色值|
|opacity|否|uint8|0|不透明度|

##### 返回

- 具有不透明度的颜色

---

<div style='font-size: 25px;font-weight:700'>

?> get_RGB_color()

</div>

##### 介绍

- 从Hex color 获取RGB通道值

!> 内部方法，请勿在自定义效果器中使用该方法！效果器中请使用[get_opacity_color](#get_opacity_color)。


##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
|hex_color|是|[hex color](#hex_color)|无|hex color|

##### 返回

- red, green, blue

---


<div style='font-size: 25px;font-weight:700'>

?> get_color_opacity()

</div>

##### 介绍

- 获取颜色不透明度

##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
|opacity_color|是|[opacity color](#opacity_color)|无|不透明度Color|

##### 返回

- 颜色不透明度

---


<div style='font-size: 25px;font-weight:700'>

?> set_color_opacity()

</div>

##### 介绍

- 设置颜色不透明度

##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
| opacity_color | 是   | [opacity color](#opacity_color) | 无     |不透明度Color|
|opacity|是|uint8|无|不透明度|

##### 返回	

- [opacity color](#opacity_color)

---

<div style='font-size: 25px;font-weight:700'>

?> get_random_color_style()

</div>

##### 介绍

- 生成用于初始化Element的随机颜色样式

##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
|shape|是|tuple(2)|无|样式大小|

##### 返回

- shape大小的numpy.matrix随机颜色矩阵

---


<div style='font-size: 25px;font-weight:700'>

?> get_color_style()

</div>

##### 介绍

- 生成用于初始化Element的指定颜色样式

##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
|shape|是|tuple(2)|无|样式大小|
|color|是|[opacity color](#opacity_color)|无|单色颜色值|

##### 返回

- shape大小的numpy.matrix指定颜色矩阵

---



<div style='font-size: 25px;font-weight:700'>

?> 

</div>

##### 介绍

- 

##### 参数

|参数名|必须|类型|默认值|介绍|
|:---|:----|:---|---|---|
||||||

##### 返回

- 无

---
