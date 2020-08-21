# Leetcode Python

[![Travis Build Status][travis-image]][travis-url]

本项目是个人在刷Leetcode时的代码和总结。

- 使用pylint检查代码格式。
- 使用[pytest](https://github.com/pytest-dev/pytest)执行测试用例。
- 使用travis CI执行进行代码检查与测试用例的执行。

## 目录说明

- `src/` 为题目的解答和测试用例
- `docs/` 为题目相关的总结
- `tools/` 中存放CI及其他功能的工具
- `.travis.yml` 为TravisCI的配置文件

## 代码规范说明

### 文件命名说明

文件命名格式 `{4位补0题号}_{题目说明}.py`，比如第一题两数之和的链接为:

<https://leetcode.com/problems/two-sum/>

我们则取题号1补0得到`0001`，题目说明及URL中最后一部分`two-sum`，所以第一题的命名应为`0001_two-sum.py`。

### 代码内容说明

代码分为两部分：

1. 可以直接提交Leetcode的类的定义。
2. 使用`test_{4位补0题号}`作为函数名的测试函数，需要包含完整的测试用例

### 使用pylint工具

使用pylint作为检查代码，`pylintrc` 为pylint的配置文件，主要为了忽略几种Leetcode相关的错误。包括：

- 忽略模块、方法名称风格检查
- docstring的检查
- 忽略类方法太少的警告
- 忽略类成员方法内不使用self的警告
- 忽略继承object的警告

### alias工具

为简单方便，本项目中提供了快捷工具。

#### 一次性添加配置

```bash
# 跳转到本项目的根目录
cd $PROJECT_ROOT  

# 将source alias的脚本加入到bashrc中
echo "source $PWD/tools/alias.sh" >> ~/.bashrc

source ~/.bashrc
```

#### `lco` 根据题号创建并打开文件

如执行`lco 1`会自动打开`src/0001_two-sum.py`文件。

- 如果文件存在，直接打开
- 如果文件不存在，会拉取题号对应的题目名称，创建文件并打开


## 参考
pylintrc 参考自 https://gist.github.com/xen/6334976

<https://dev.to/edeediong/using-travisci-to-write-better-python-codes-27kg>

[travis-image]: https://travis-ci.org/tmm90/leetcode-python.svg?branch=master
[travis-url]: https://travis-ci.org/tmm90/leetcode-python


