# calculator程序说明

> - 用Python3.0及以上解释器运行calculator.py，运行环境保证编码为UTF-8
> - 系统实现自定义四则混合运算公式计算
> - 系统采用3步计算，先去括号，然后算乘除，再加减
> - 去括号采用正则匹配获取最小括号单位，计算括号内值后替换公式原值，重复计算，直至没有括号，去括号时会遇到“-”问题，把值放入原公式后，进行“-”的提取，使公式符合规范，再进行下一次计算
> - 计算乘除为一次性计算，从左往右依次计算
> - 加减计算和乘除一样，从左往右，如公式开头带“-”，则视为负数计算
> - 具体测试用例见test.md
