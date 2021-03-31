# 更新日志

## 2021.3.29 Pre-V2.0.0
重构整个渲染引擎，对元素、画布、渲染引擎进一步解耦。
### 新特性
 - 元素支持无限动画。
 - fade效果器支持switch方法。
 - 颜色新增RGBA颜色类，更易于定义PixelRenderer中使用的颜色。(*RGBA仅面向PixelBlock App开发者*。
   基于性能考虑，PixelRenderer中存储数据数据仍为32bit自定义ORGB颜色数据。故自定义效果器，仍需操作ORGB数据。)
### 兼容性影响
 - 由于GIL锁，且基于性能考虑，移除AbstractThreadingEffector。重写fade效果器实现
AbstractEffector。与旧版本不再兼容。
 - 基于实际语义，重命名效果器方法，show重命名为appear，hide重命名为disappear。
 - 重命名效果器名，原有Default与Fade改为default与fade。
 - element重写后与原有element不再兼容