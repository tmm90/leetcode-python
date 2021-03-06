---
title: "Alibaba Interview"
date: 2020-09-11
---

#### 1. 用你最熟悉的语言协议到计算器程序，输入是需要计算的表达式，输出是表达式的结果

有现成的不去自己实现功能。

可以沟通一下是否可以这么是用，还是要实现具体细节。

```python
# #表示注释别抄
expression = raw_input("Enter your expression: ") # raw_input 是获取原始的输入，跟input的区别是input会计算完才作为输入
print(eval(expression)) # eval 函数是执行一个表达式
```

#### 2. 有两个人，一个人只说真话，一个人只说假话。如何质问其中一个人一句话，就能分辨出谁是说真话的。

问题是：你们两根人中是不是只有一个说真话的？

- 只说真话的会回答：是的
- 只说假话的会回答：不是

**结题思路：需要充分地利用信息。**

不可能只问关于一个人的问题（一个bit位）。因为发生在一个人身上是真，另外一个人身上是假，而`真话人说的真话`和`假话人说的假话`是一样的。

|      问题      | 真话人的答案 | 假话人的答案 |
| :------------: | :----------: | :----------: |
|   你只说真话   |      对      |      对      |
|   你只说假话   |      错      |      错      |
| 你有时候说真话 |      对      |      对      |
| 你有时候说假话 |      错      |      错      |

必须得问关于两个人的问题，才能有更多的信息（两个bit位）

|        问题        | 真话人的答案 | 假话人的答案 |
| :----------------: | :----------: | :----------: |
|    你们都说真话    |      错      |      对      |
|    你们都说假话    |      错      |      对      |
| 你们只有一个说真话 |      对      |      错      |

#### 3. 10个人分3组，总共有多少种可能性

每次抽三个人出来，但是因为是没有顺序的分组，所以需除掉三组的排序。

$$ \frac{C_{10}^{3} * C_{7}^{3} * C_{4}^{3}} { A_{3}^{3} } = 2800$$

#### 4. 给当前目录aaa加上读写权限

注意会用`-R`表示递归所有子目录

```bash
chmod a+rwx -R aaa # 为所有的人加
chmod +rwx -R aaa  # 为所有者加
```

#### 5. SQL语句：A表和B表中分别有A.1, A.2, A.3; B.1, B.2, B.3 找出 A.1 = B.1 关联的A.3 和 B.3

考察表的连接

```sql
SELECT A.3, B.3 FROM A LEFT JOIN B ON A.1=B.1;
```

#### 6. 从文件a.xsl表格中找出列名ABCDE且该表格中内容中纯数值的内容总和

考察使用Excel的技巧，常用函数`SUM`

```
=SUM(A:E)
```


#### 7. 用例设计题 滴滴打车计价系统

```
1) 起步3公里10元
2) 每超过1公里，额外收费2元
3) 额外里程费晚上是白天1.2倍
4) 晚上22:00-6:00，其他时间为白天
5) 堵车低速行驶，每3分钟1元
6) 深圳宝安、南山、福田区域，可以调度车辆小于10，则总价1.1倍
7) 去机场、火车站额外收费10元
```
测试用例设计是为了覆盖所有分支的。

分清互斥关系。互斥的条件需要相乘。


```python
# -*- encoding: utf-8 -*-
import itertools
c1 = [True, False]  # 是否产生调度费用
c2 = [True, False]  # 是否小于3公里
c3 = [0, 1, 2, 3]  # 全程白天、全程夜间、白天到夜间、夜间到白天
c4 = [True, False]  # 去机场、不去机场
c5 = [True, False]  # 发生堵车、未发生堵车

ret = c1

all_cases = list(itertools.product(c1, c2, c3, c4, c5))


def print_case(x):
    print(("产生了" if x[0] else "未产生") + "调度费用"),
    print(("小于等于" if x[1] else "大于") + "3公里"),
    print({
        0: "白天开始白天结束",
        1: "夜间开始夜间结束",
        2: "白天开始夜间结束",
        3: "夜间开始白天结束",
    }[x[2]]),
    print(("产生" if x[1] else "未产生") + "高速费用"),
    print(("发生" if x[1] else "发生") + "发生堵车")


for case in all_cases:
    print "===="
    print_case(case)
```




