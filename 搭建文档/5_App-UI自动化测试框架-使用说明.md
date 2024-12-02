# 5_App-UI自动化测试框架-使用说明
第3、4为我在博客上的相关问题分享文章，故未放在此处
- [5\_App-UI自动化测试框架-使用说明](#5_app-ui自动化测试框架-使用说明)
  - [框架结构说明](#框架结构说明)
    - [1. **cases/** 文件夹](#1-cases-文件夹)
    - [2. **config/** 文件夹](#2-config-文件夹)
    - [3. **logs/** 文件夹](#3-logs-文件夹)
    - [4. **page/** 文件夹](#4-page-文件夹)
    - [5. **tools/** 文件夹](#5-tools-文件夹)
    - [6. **项目根目录文件**](#6-项目根目录文件)
  - [使用说明](#使用说明)
    - [修改配置](#修改配置)
    - [连接设备](#连接设备)
    - [创建用例](#创建用例)
    - [调试、运行代码](#调试运行代码)

## 框架结构说明

```bash
AUTO-TEST/
│
├── case/                   # 测试用例目录
│   ├── testCheckin/          # 示例测试用例模块
│       ├── test_test_setup.py
│       └── __init__.py
│
├── config/                  # 配置文件目录
│   ├── cookies.json
│   ├── db_config.json
│   └── test_paths.json
│
├── logs/                    # 日志目录
│
├── page/                    # 页面对象目录 (Page Object Model)
│   ├── po_chufang.py  # 工具类
│   └── base.py    # 基类，所有用例都要继承
│
├── base/                   # 工具模块
│   ├── cleanup_utils.py
│   ├── database_utils.py
│   └── sl_cookies.py
│
├── LICENSE                  # 许可证
├── main.py              # 测试运行入口
├── pytest.ini               # pytest 配置
├── README.md                # 项目说明文档
├── requirements.txt         # 项目依赖
└── suites.py                # 测试套件
```

### 1. **cases/** 文件夹

   **作用**：该文件夹存放各种测试用例，通常包含针对不同功能或模块的自动化测试脚本。测试用例是项目的核心，直接验证被测系统的功能是否符合预期。

- **示例文件夹：testCheckin/**
  - **作用**：存放与“签到”功能相关的测试用例。每个子文件夹对应一个功能模块，帮助组织和管理不同模块的测试。
  - **`test_test_setup.py`**：通常用于测试初始化或设置一些通用的测试前置条件，比如清理环境、准备测试数据等。
  - **`__init__.py`**：让 `testCheckin/` 目录成为一个 Python 包，便于模块化导入和使用。

### 2. **config/** 文件夹

   **作用**：存放项目的各种配置文件。将配置项从代码中分离出来，便于维护、修改和重用。

- **cookies.json**：存储登录状态或特定操作所需的 Cookie 信息，用于在自动化测试中模拟用户登录状态，避免频繁重新登录。
- **db_config.json**：数据库配置文件，可能存储数据库的连接信息（例如主机、端口、用户名、密码等），用于测试用例中涉及的数据库操作。
- **test_paths.json**：路径配置文件，可能用于存放测试相关文件或 API 的路径，确保路径可灵活配置，不需硬编码在测试脚本中。

### 3. **logs/** 文件夹

   **作用**：用于存放测试运行过程中生成的日志文件。日志能够记录测试执行的详细信息，包括哪些测试通过、哪些失败，以及失败的详细原因，便于调试和排查问题。

### 4. **page/** 文件夹

   **作用**：该目录遵循**页面对象模型（Page Object Model，POM）**，通过封装页面操作逻辑，将页面元素的定位和交互独立出来，提高代码复用性和可维护性。

- **app_kaichufang_page.py**：封装与“开处方”页面相关的操作，定义该页面的所有元素及其操作方法。每个页面对象类通常包含页面元素的定位符（例如 XPath、CSS 选择器）以及对这些元素的操作（如点击、输入文本、获取文本等）。
- **base_page.py**：基础页面对象类，封装了所有页面共用的操作，比如点击、输入、等待页面加载等。其他页面对象类可以继承这个类，避免重复代码，提升代码的可维护性。

### 5. **tools/** 文件夹

   **作用**：存放辅助测试的工具模块。通常用于简化测试中的常见操作或提供额外功能。

- **cleanup_utils.py**：用于清理测试数据或环境的工具模块。例如，测试运行前或运行后清除一些无效数据，确保每次测试运行在一个干净的环境中。
- **database_utils.py**：数据库工具模块，可能包含用于连接数据库、执行 SQL 查询、获取数据等常见操作，避免在每个测试用例中重复编写数据库连接逻辑。
- **sl_cookies.py**：与 Cookie 相关的工具模块，可能用于管理（如获取、设置、保存或删除）测试中的 Cookie，帮助在自动化测试中处理用户会话。

### 6. **项目根目录文件**

- **LICENSE**：项目的许可证文件，规定了该项目的使用和分发权限。常见的开源许可证包括 MIT、Apache、GPL 等。
- **main_run.py**：测试运行的主入口文件。通常用来配置和启动整个测试流程。可能包含设置测试环境、加载测试用例并执行、输出结果等逻辑。
- **pytest.ini**：pytest 的配置文件。pytest 是一个流行的 Python 测试框架，`pytest.ini` 允许你自定义 pytest 的一些行为，例如并行执行测试、指定测试文件夹、报告格式等。
- **README.md**：项目的说明文档，通常包含项目的简要介绍、安装步骤、使用方法等，是供开发者或用户快速了解和上手项目的重要文档。
- **requirements.txt**：项目依赖文件，列出该项目运行所需的所有 Python 包及其版本。通过 `pip install -r requirements.txt` 可以安装这些依赖。
- **suites.py**：测试套件文件，可能用于将多个测试用例组合起来，形成一个完整的测试套件。测试套件可以批量执行相关的测试用例，便于进行全面测试。

---

## 使用说明

### 修改配置

先在config下创建文件`dev_paths.json`

![20241011173419](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/5_App-UI自动化测试框架-使用说明/20241011173419.png)

然后将`test_paths.json`里的代码复制进去，对应修改相应的配置

![20241011175212](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/5_App-UI自动化测试框架-使用说明/20241011175212.png)

ADB连接的端口，以MuMu模拟器举例，可以到多开器里查看：

![20241011175500](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/5_App-UI自动化测试框架-使用说明/20241011175500.png)

可以顺便把模拟器的分辨率改成720p（因为我的代码是以720p写的）

![20241011175910](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/5_App-UI自动化测试框架-使用说明/20241011175910.png)

然后进入`page\base_page.py`修改这个代码来修改环境，因为我们要开发，所以就把这个改成`dev_paths`，**要注意commit代码的时候不要加上这个文件**，或者把这个环境修改回去，因为服务器用的是测试环境，你用的是开发环境，你把代码合上去会出现服务器无法运行的情况

![20241011180454](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/5_App-UI自动化测试框架-使用说明/20241011180454.png)

### 连接设备

通过adb命令来连接设备，打开cmd输入命令：

![20241012114254](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/5_App-UI自动化测试框架-使用说明/20241012114254.png)

记得修改对应端口成你自己的

连接完可以用`adb devices`查看已连接设备

然后运行`appium`启动appium服务

![20241012114441](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/5_App-UI自动化测试框架-使用说明/20241012114441.png)

### 创建用例

在cases创建功能模块和用例

![20241012100735](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/5_App-UI自动化测试框架-使用说明/20241012100735.png)

然后开始写用例代码

![20241012102538](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/5_App-UI自动化测试框架-使用说明/20241012102538.png)

图中的wait and click方法是我自己写的一个方法，防止出现元素还没加载出来导致报错。正常的点击是`driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().className(\"android.view.ViewGroup\").instance(37)").click()`,然后value就是你想定位的元素，要获取这个，就需要用到Appium Inspector这个工具

![20241012113945](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/5_App-UI自动化测试框架-使用说明/20241012113945.png)

填完信息后点击 启动会话

![20241012115111](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/5_App-UI自动化测试框架-使用说明/20241012115111.png)

目前我的代码里增加了一些基本方法，可以去Base类看注释，这里不再过多赘述

如果遇到一些用例涉及逻辑判断或者其他需要增加方法，我个人倾向将方法放到这些位置：

- 所有用例都可以用到的方法——放到`page\base_page.py`
- 相应模块才能用的方法，比如说把页面往下滑动的同时查找特定元素，找到元素时停止滑动。这种就只有能滑动的页面采用得到，就在`page\`下面创建一个专用的模块。
- 用一次就丢的方法，没有任何通用性，比如一个找到页面中所有的2024年10月的时间元素，并点击时间最晚的元素。这种就基本没什么复用性，把方法放到用例文件里就行。

### 调试、运行代码

可以使用`pytest cases\testTest\test_test_setup.py`来执行单个文件，“cases\testTest\test_test_setup.py”是你的用例文件的相对路径。

调试完后在根目录下suites文件配置测试套件，就是将用例组合起来。例如我有三个用例，注册、登录、退出登录。我就可以把这些组合成{登录}、{注册并登录}、{退出登录并登录}、{退出登录并注册再登录}等等排列组合。按照文件里现有的格式添加就行。

![20241012121438](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/5_App-UI自动化测试框架-使用说明/20241012121438.png)

用`python main_run.py`命令，运行在all_suites字典里添加的套件。这个文件也是主入口，服务器只需运行main run文件就可以运行用例。

那如果我不想运行所有的，只想运行其中几个怎么办?

也可以运行`python main_run.py testf moban`，这条命令就是在后面加上你想运行的套件。testf和moban都是上图中all suites字典里冒号前面的key，你想运行哪些套件就按照这个格式在后面加就行了。这样的好处是比如使用Jenkins运行的时候，我可以创建不同的job来运行不同的套件，不需要更改代码，也不需要切分支，对多个分支进行维护。
