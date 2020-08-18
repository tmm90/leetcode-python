## 算法要点

### 二分法查找

- 将二分法的线性坐标映射到二维坐标
- 左闭右开
- 区间更新：因为左闭右开，所以value[mid]不符合时，需要将left=mid+1或者right=mid，仍然下次的左闭右开
- 终止条件：因为left会变成mid+1，一定能够达到left>=right（等号是当left=right时，左闭右开的区间[n,n)为空）


## Python知识点

### 整数除法

"/"可以用于float除法，"//"用于整除法

```python
>>> type((1+2)/2)
<class 'float'>

>>> type((1+2)//2)
<class 'int'>
```

**注意: 24行的`mid`计算时，要使用`(left + right) // 2`**


### 链式比较

因为这里要根据下标取值，所以要满足`line_index`在有效的范围内，使用以下连续大于、等于、小于符号判断其范围。

```python
assert 0 <= line_index < self.total_len
```
