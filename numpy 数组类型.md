numpy 数组类型:

问题: 
```
float64型 数据无法转化成 Tensor, 并报错如下:
TypeError: can't convert np.ndarray of type numpy.object_. The only supported types are: double, float, float16, int64, int32, and uint8.
```

**double** (即 float64)

 	DoubleTensor



**float** (即 float32)

 	FloatTensor



**float16**

​	HalfTensor
```
	半精度浮点：1位符号，5位指数，10位尾数
```


**float64**

​	DoubleTensor
```
	双精度浮点：1位符号，11位指数，52位尾数
```


**int64**

​	LongTensor
```
	整数（-9223372036854775808 到 9223372036854775807）
```


**int32**

​	IntTensor
```
	整数（-2147483648 到 2147483647）
```
**uint8**

​	ByteTensor
```
	无符号整数（0 到 255）
```