# Pglint - 用于批改网的英语写作分析工具 | www.pigai.org
**不止是一个烦人的语法检查工具！**  

Pglint 是一个英语写作分析工具，它将帮你找出语法错误，加强语义表达，分析逻辑谬误并提供简单的、建设性的建议。


## 一般使用：

1. 下载 **pglint.exe** 到本地。

2. 点击 **pglint.exe** 或打开控制台，输入pglint启动。

3. 启动成功后，即可通过快捷键控制输入。

更多指令请见 **使用提示**

   | 快捷键  | 功能                                                         | 名称    |
   | ------- | ------------------------------------------------------------ | ------- |
   | \       | 开启/关闭**自动输入模式**——在此模式下所有字符输入都将被替换为文章 | switch  |
   | [       | 定位至文章开头                                               | reset   |
   | ]       | 从当前位置起输完全文                                         | all     |
   | -       | 输入下一个单词/输完当前单词                                  | next    |
   | =       | 输入下一句句子/输完当前句子                                  | forward |
   | Alt + - | 定位至当前单词的起始位置                                     | before  |
   | Alt + = | 定位至下一个单词的起始位置                                   | after   |
   | Alt + [ | 定位至当前句的起始位置                                       | behind  |
   | Alt + ] | 定位至下一句的起始位置                                       | ahead   |
   | Esc     | 退出Pglint kernel                                            | stop    |

## 使用提示：

1. 灵活使用"Alt + ..."调位：e.g. 若要求从语段中间某句话开始输入，则使用 "Alt + ]" 可快速定位至该位置。
2. 在**自动输入模式**下，若输入速度过快可能造成错位。
3. 请勿使用中文输入法。

命令列表：
-----------------------------------

```shell
options:
  -h --help                   Show help.
  -a --all                    Show all available remote sources.
  -k --keys                   Show keyboard config.
  -s --save                   Save text to local file __answer__.txt
  -c --channel <url>          Get text from remote source and start.
  -f --file <path>            Get text from local file and start.
  -t --text <text>            Get text from console.
  -o --option <string>        Customize keyboard config.
```

### 查看可用在线资源

```shell
pglint -a

示例：
  pglint -a
输出：
  Showing all available texts below
  ---- 基础英语 | test-1: https://raw.githubusercontent.com/yanglinshu/pglint/master/answers/answer1-test.txt

* 往往结合 "pgurl -c <url>" 使用
```

### 加载在线资源并启动

```shell
pgurl -c <url> [-s]

参数：
  <url>  在线资源的网址
  [-s]    保存至本地为__answer__.txt

示例：
  pgurl -c https://raw.githubusercontent.com/yanglinshu/pglint/master/answers/answer1-test.txt
输出：
  SUCCESS Get text from remote source successfully.
  SUCCESS Pglint kernel is now activated
  ...
```

### 加载本地资源并启动

```
pglint -f <path>

参数：
  <path>  本地文本的绝对路径或相对路径

实例：
  pglint -f test.txt
输出：
  SUCCESS Get text from local file successfully.
  SUCCESS Pglint kernel is now activated
  ...
```

### 将指定字符串作为输出源启动

```
pglint -t "<text>"

参数
  <text>  输出源字符串
  
实例：
  pglint -t 
输出：
  SUCCESS Get text from console successfully.
  SUCCESS Pglint kernel is now activated
  ...
```
注意在输入包含空格的文本时，请用引号括住该文本。

### 查看快捷键定义

    pglint -k
    
    示例：
      pglint -k
    输出：
      Showing keyboard config below
      ---- c: esc
      ---- switch: \
      ---- reset: [
      ---- all: ]
      ---- next: -
      ---- forward: =
      ---- before: alt+-
      ---- after: alt+plus
      ---- behind: alt+[
      ---- ahead: alt+]

### 自定义快捷键

```
pglint -o "<name> <key(s)>"

参数：
  <name>    以上10种操作(c,switch,reset,all,next,forward,before,after,behind,ahead)的任意一个
  <key(s)>  单个按键或组合键如ctrl+m

示例：
  pglint -o "switch ctrl+m"
输出：
  SUCCESS Update keyboard config successfully
```
注意你的快捷键应当以单个合法字母结尾（退出除外），如ctrl+m、ctrl+alt+p，且不应与windows、浏览器或pglint已有快捷键重叠。
同时对于" ", "+"和","，请使用"space", "plus"和"comma"代替。
注意在输入包含空格的文本时，请用引号括住该文本。

## FAQ

Q: "如何打开控制台？"

A: "打开所在文件夹，按住Shift后右键，单击 “**在此处打开 Powershell 窗口**” 或在地址栏输入cmd。"


Q: "pglint : 无法将“pglint”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的拼写，如果包括路径，请确保路径正确，然后再试一次。"

A: "请检查你是否与pglint处于同一文件夹下。如果在，且你正在使用powershell启动pglint，请尝试输入.\pglint"