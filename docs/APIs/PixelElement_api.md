# PixelElement
## 属性

---

| 属性名        | 类型         | 介绍     |
| ------------- | ------------ | -------- |
| shape         | tuple(2)     | 元素大小 |
| element_mask  | numpy.matrix | 元素掩膜 |
| color_style   | numpy.matrix | 颜色样式 |
| element_style | numpy.matrix | 元素样式 |

## 方法

---

<div style='font-size: 25px;font-weight:700'>

?> __init__()

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

?> get_element_style()

</div>


##### 介绍

- 获取元素样式

##### 参数

- 无

##### 返回

- 无