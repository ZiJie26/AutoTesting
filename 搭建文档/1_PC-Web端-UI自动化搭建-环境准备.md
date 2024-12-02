
# PC Web端 UI自动化搭建（1）本地环境准备

- [PC Web端 UI自动化搭建（1）本地环境准备](#pc-web端-ui自动化搭建1本地环境准备)
  - [脚本编写环境准备](#脚本编写环境准备)
    - [Git](#git)
    - [Anaconda](#anaconda)
    - [Pycharm](#pycharm)
  - [其余工具](#其余工具)
    - [Chrome for Testing \& ChromeDriver](#chrome-for-testing--chromedriver)
    - [Selenium IDE](#selenium-ide)
    - [allure](#allure)

## 脚本编写环境准备

### Git

> 版本控制工具

这里<https://git-scm.com/downloads>下载安装就好

### Anaconda

> python 环境管理软件

[下载地址](https://www.anaconda.com/download/success)

![2](https://i-blog.csdnimg.cn/direct/5568383bedc448a1b3c14b450d543b31.png)

**把自己的安装路径记下来！后面要用。**

![1](https://i-blog.csdnimg.cn/direct/ebc0bc7229f942ee969c83097bf88f18.png)

这里懒得设环境变量建议全选

![1](https://i-blog.csdnimg.cn/direct/19fc94207a3744acb6cba5d98fb2da66.png)

安装完之后不用打开，可以在cmd检查一下是否添加到环境变量

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/453f5eee6b3e4306b7783fb9b25ab77a.png)

### Pycharm

> python 脚本编写调试工具

[点击这里](https://www.jetbrains.com/pycharm/download/?section=windows)下载
Pycharm社区版

![社区版](https://i-blog.csdnimg.cn/direct/b78612139adc4ecebcd6846ba0f04c85.png)

安装过程不再赘述

## 其余工具

### Chrome for Testing & ChromeDriver

> 谷歌推出的专用于测试的浏览器和驱动

[下载地址](https://googlechromelabs.github.io/chrome-for-testing/#stable)
把这两个链接粘贴到地址栏下载得到两个压缩包

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/c3d5e90c206148f1bbb644c989381f37.png)

把chrome解压到任意地址（但是最好是C盘下面，因为这个项目配置的是C盘下面的地址）：

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e27a329144944b89bfd283449ad6ecf0.png)

**！记住这个地址！**

然后把chromedriver压缩包里的这三个文件解压到这个文件夹

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/aaedb20e56e44fb7bc20d6b4293712b1.png)

### Selenium IDE

>用于录制操作，快速生成脚本，减少工作量

双击这个打开测试浏览器,下面的操作都在测试浏览器里进行

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/fced8391e1b04e13bbe8832bf5802888.png)

有梯子去这里<https://chromewebstore.google.com/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd?hl=zh-CN>安装

没梯子去这里<https://www.chajianxw.com/developer/30773.html>安装

### allure

>本地部署的allure，用于本地查看生成的allure报告
>>allure可以生成比较明了的执行报告，后面部署到Jenkins上时会用到allure插件，这个可以使本地调试的时候查看allure报告

这里（<https://github.com/allure-framework/allure2/releases/tag/2.30.0>）下载：

![20240828165932](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828165932.png)

解压放到你能记住的路径

![20240828173432](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828173432.png)

双击打开`allure.bat`

![20240828173538](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828173538.png)

然后去系统变量添加这个bin文件夹：

![20240828173728](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828173728.png)

确定完可以去cmd确认一下是否添加成功：

![20240828175224](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828175224.png)
