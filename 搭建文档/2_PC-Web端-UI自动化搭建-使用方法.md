# 2_PC-Web端-UI自动化搭建-使用方法

- [2\_PC-Web端-UI自动化搭建-使用方法](#2_pc-web端-ui自动化搭建-使用方法)
  - [拉取代码](#拉取代码)
  - [框架使用](#框架使用)
    - [项目结构说明](#项目结构说明)
    - [测试浏览器路径设置](#测试浏览器路径设置)
    - [数据库设置](#数据库设置)
    - [使用Selenium IDE录制脚本](#使用selenium-ide录制脚本)
    - [运行用例集](#运行用例集)
    - [主运行文件](#主运行文件)
  - [拉取代码！！！很重要，每次修改代码之前都要拉取一下](#拉取代码很重要每次修改代码之前都要拉取一下)
  - [提交代码](#提交代码)
  - [测试人员后面的可以不用看](#测试人员后面的可以不用看)
    - [配置Jenkins](#配置jenkins)
    - [创建job](#创建job)

## 拉取代码

打开Pycharm

按照下图点击

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/ee2b0a693d904efc96b0e45c25f95957.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/3206214a96b84a7094f767033a702261.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/6242a257e46c4f7982e24b8f67ef08aa.png)

我们创建一个新的环境

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/aeb6476fe3fa43a2aaa51a081e87e523.png)

点击确定

再回到主页面

![20240904093821](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904093821.png)

这里先拉取代码仓库

`https://devops.szpuree.com/aidmed/%E4%BA%92%E8%81%94%E7%BD%91%E5%8C%BB%E9%99%A2/_git/auto-test`

![alt text](2_PC-Web端-UI自动化搭建-使用方法/image.png)

注意这里要选中你刚刚创建的环境：

![20240904094721](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904094721.png)

然后打开控制台，输入：`pip install -r requirements.txt`

![20240904095524](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904095524.png)

安装完后可以输入`pip list`查看是否安装成功。

## 框架使用

拉下来的代码目录结构是这样的：

```cmd
.
│  conftest.py          # pytest的全局配置文件，可以在此定义测试的前置/后置操作、hook函数等
│  main_run.py          # 主入口文件，用于启动整个测试项目的执行
│  pytest.ini           # pytest配置文件，用于配置pytest的运行参数，如测试路径、插件配置等
│  README.md            # 项目说明文档，介绍项目的背景、使用方法及结构说明
│  requirements.txt     # 项目所需的依赖库列表，用于通过pip安装依赖
│
├─cases
│  │  __init__.py       # 表示该目录为Python包，可用于初始化相关配置或依赖
│  │
│  ├─data
│  │      test_data.json # 测试数据文件，存储各个测试用例所需的数据，通常以JSON格式保存
│  │
│  └─testFeature
│          test_test1.py # 第一个测试用例文件，使用pytest框架，定义UI自动化测试的具体场景
│          test_test2.py # 第二个测试用例文件，包含另一组自动化测试场景
│          __init__.py   # 初始化文件，标记此目录为Python包，便于模块导入
│
├─config
│      cookies.json      # 登录或其他需要的cookies配置文件，保存登录后使用的cookie信息
│      db_config.json    # 数据库配置文件，存储数据库连接信息和参数
│      dev_paths.json    # 开发环境路径配置文件，包含项目在开发环境下的URL或路径信息
│      test_paths.json   # 测试环境路径配置文件，包含项目在测试环境下的URL或路径信息
│
├─page
│      base_page.py      # 页面基础类，封装常用的页面操作，如点击、输入文本等，是其他页面类的父类
│      __init__.py       # 标记page目录为Python包，便于模块导入
│
├─suites
│      suit1.py          # 测试套件1，组合多个测试用例，作为一组执行
│      suit2.py          # 测试套件2，定义另一组测试用例的组合
│      __init__.py       # 标记此目录为Python包，便于模块导入
│
├─tools
│      cleanup_utils.py  # 工具文件，包含清理测试环境或其他清理任务的工具函数
│      database_utils.py # 数据库工具文件，提供操作数据库的函数，如增删查改等操作
│      sl_cookies.py     # 与cookie相关的工具函数，用于cookie的读取、写入或删除操作
│      webdriver_setup.py# WebDriver配置工具文件，用于配置和启动WebDriver
│      __init__.py       # 标记tools目录为Python包，便于模块导入
```

### 项目结构说明

- **根目录文件**
  - `conftest.py`：这是pytest的全局配置文件，用于定义测试的前置/后置操作、fixture等通用的配置信息。
  - `main_run.py`：项目的主运行文件，用来配置测试的启动逻辑，可以控制执行哪些测试套件或具体的用例。
  - `pytest.ini`：用于pytest的配置，可以在这里设置一些pytest运行时的参数，比如测试路径、插件设置等。
  - `README.md`：文档文件，用于说明项目的目的、安装步骤、如何运行等信息。
  - `requirements.txt`：Python项目的依赖文件，列出了所有运行该项目所需的库和版本信息。

- **cases目录**
  - `cases/__init__.py`：标记`cases`目录为Python包，允许从外部导入包中的模块。
  - `cases/data/test_data.json`：存放测试用例所需的数据，方便测试用例动态使用不同的数据集。
  - `cases/testFeature/`：用于存放测试用例的具体文件，如`test_test1.py`和`test_test2.py`，这些文件中通常会使用pytest框架定义具体的测试场景。

- **config目录**
  - 用于存放项目运行环境相关的配置文件，如数据库连接信息（`db_config.json`）、测试环境路径（`test_paths.json`）等。不同的环境会有不同的配置文件。

- **page目录**
  - `base_page.py`：封装了常见的页面操作和元素查找方法，其他页面类会继承自这个基础类，用于简化代码复用。
  - `__init__.py`：标记`page`目录为Python包，便于模块之间的引用。

- **suites目录**
  - 存放测试套件文件，测试套件是多个测试用例的集合，便于按照不同的功能或模块进行批量测试执行。

- **tools目录**
  - 存放一些辅助工具文件，例如清理工具（`cleanup_utils.py`）、数据库操作工具（`database_utils.py`）、WebDriver配置工具（`webdriver_setup.py`）等。

### 测试浏览器路径设置

在config\test_paths.json文件里设置chrome for testing的路径

![20240904114403](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904114403.png)

### 数据库设置

有时候会需要读取数据库的一些数据来验证，比如说测试登录信息是否存储到数据库中

在config\db_config.json文件里输入要连接的数据库信息

![20240904115831](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904115831.png)

### 使用Selenium IDE录制脚本

安装完之后可以把它固定显示

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b5fe196bc27c4d429e80ab9c2c9f2715.png)

点击上图3号箭头打开下图页面，点第三个选项新建一个Project

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/608c9bcc1ca04b7cbe3ce04e735d8c53.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a980584d96ae4829925d7b1c7f2c524f.png)

点击录制之后会弹出被测网站的新窗口，在那个窗口进行你的测试操作（**建议不要有多余操作**）

下图就是在百度首页输入“hi”然后回车后录制下来的内容：

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/ecdba1e1479541cd8a78a1c578a17dcf.png)
**注意！有些情况下这个插件并不能成功复现你的操作，是插件的问题，这时候就需要导出成脚本在本地运行了**

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e46a90e1db0143fc812bbe73f980647e.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/887db633edd74bf485cf83d50f2ae4b4.png)

点击export导出py脚本

把导出之后的文件放到项目的case/testFeature下（testFeature文件夹类似于存放某个功能模块的用例的文件夹，例如你可以在case文件夹下创建Login文件夹，然后在里面放所有和登录有关的用例）

![20240904110455](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904110455.png)

将代码修改一下，让其继承Base类，Base类里已经包含了启动和结束时的处理，所以我们把setup和teardown method方法给删掉。然后在用例方法前面打上demo标记，因为我们在`pytest.ini`文件里设置了仅运行demo或者smoke标记的测试

然后在终端里输入`pytest .\cases\testFeature\test_untitled.py`运行该脚本

![20240904112153](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904112153.png)

可以看到运行成功的信息和生成的html报告位置：

![20240904112435](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904112435.png)

可以直接点击打开，是这样的：

![20240904112510](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904112510.png)

这个本地报告可以方便对代码调试，更快速的看到是哪个用例出了问题。

同时每次运行过后都会在logs文件夹下打印出日志，如果报错的话会把报错信息也打印出来，同样方便对代码进行调试

![20240904112753](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904112753.png)

还可以输入`allure serve .\report\allure-results`查看本次运行的allure报告（一般用不到，本地的allure无法显示结果趋势，要在Jenkins上才能发挥全部能力）

### 运行用例集

除了使用`pytest`命令运行单个文件之外，还可以运行集合数个用例的用例套件，落实到业务需求的话，举个例子：你可以创建一个auth_suit.py，里面放登录注册注销等用户认证相关的用例。

我这里就在suites文件夹下面创建用例套件`suit1.py`，然后在里面添加想要了我想执行的用例：

![20240904143148](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904143148.png)

可以运行`pytest .\suites\suit1.py`命令来执行这个套件，但是一般也只是本地调试的时候可以更灵活的执行用例，真正部署到Jenkins上自动执行的时候都是执行`main_run.py`这个主运行文件。

### 主运行文件

根目录下的`main_run.py`就是整个程序的主运行文件，在这里可以配置需要运行的测试套件，我这里就是运行suit1和suit2并把这两个套件命名为test1和test2

![20240904144432](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904144432.png)

一般直接运行该文件`python main_run.py`就可以运行这里面的所有套件，当然也可以选择其中几个套件运行，比如说我新添加了suit3，但只想执行suit1和suit2，就执行`python main_run.py test1 test2`，和前面pytest的方法的区别是，这个只需要一次命令可以执行多个套件。

## 拉取代码！！！很重要，每次修改代码之前都要拉取一下

第一次从仓库拉下代码的时候要创建一个新分支（**创建分支只要做一次！只要确保你的分支不是master就行**）

![alt text](2_PC-Web端-UI自动化搭建-使用方法/image-2.png)

![alt text](2_PC-Web端-UI自动化搭建-使用方法/image-3.png)

**之后每次对代码进行修改之前都要确认左上角切换到对应分支，再从master分支拉取最新代码，然后才可以开始修改代码。**

![alt text](2_PC-Web端-UI自动化搭建-使用方法/image-4.png)

![alt text](2_PC-Web端-UI自动化搭建-使用方法/image-5.png)

## 提交代码

当你编写完新的用例脚本的时候，可以在Pycharm里推送代码

修改完后可以按照下图提交代码，提交完之后需要告诉仓库管理人将代码合到master分支才能在服务器上运行

![alt text](2_PC-Web端-UI自动化搭建-使用方法/image-1.png)

## 测试人员后面的可以不用看

>这里使用Jenkins作为持续集成工具，可以在代码构建完之后执行我们的自动化测试，这里用作笔记给楚梓杰之后部署查看，

### 配置Jenkins

![20240904151121](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904151121.png)

找到这里，填上你的jdk目录

![20240904151323](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904151323.png)

然后这里修改为所安装的git的目录

![20240904151423](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904151423.png)

这里让它自动安装就行

![20240904151517](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904151517.png)

点击应用保存。

然后点击这里配置环境变量，建议把你能想到的目录都加上去

![20240904151609](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904151609.png)

![20240904151948](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904151948.png)

不知道conda目录去设置里找，记得把目录下Scripts也要加上

![20240904152357](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904152357.png)

配置完环境变量之后保存，回到主页

### 创建job

![20240904155254](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904155254.png)

![20240904155325](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904155325.png)

这里的仓库链接请不要使用这里的

![20240904155721](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904155721.png)

![20240904155840](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904155840.png)

![20240904155931](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904155931.png)

![20240904160000](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904160000.png)

![20240904160511](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904160511.png)

![20240904160545](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904160545.png)

搞完应用保存，就部署完了。

可以点击这里开始执行脚本

![20240904160925](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904160925.png)

执行完后

![20240904161718](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/2_PC-Web端-UI自动化搭建-使用方法/20240904161718.png)

至此搭建全部完毕
