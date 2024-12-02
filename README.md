# [跨平台UI与API自动化测试框架](/)

## [概况](/)

**该项目是本人为了求职所建，用例仅用作展示本人代码，因为浏览器Token一定是不能用的的，所以并不能直接运行，需要修改config里的对应配置文件，同时需要参考我的代码写自己的用例**

主要提供一个思路，每个项目适合的测试框架结果也不相同。希望能帮助看到该项目的人

该框架集成了App和Web端的UI测试以及API测试。利用Python和Pytest，结合Selenium和Appium实现跨平台UI自动化测试，并通过Requests库实现API自动化测试。框架采用页面对象（PO）模式进行UI测试，并支持数据驱动的接口测试，确保了测试的全面性和业务需求的符合性。

- UI自动化：基于Selenium和Appium，采用页面对象（PO）模式设计，将页面元素及操作封装为独立对象模块，提升代码的复用性和可读性，便于后续的维护和扩展。

- API自动化：基于Requests库实现API自动化，通过Pytest的parametrize功能管理测试数据，数据存储在JSON或CSV文件中，实现数据驱动的接口测试，减少重复代码。框架设计采用分层结构，将接口请求、业务逻辑还有数据层分离，确保模块化和逻辑清晰。

- UI与API自动化集成：将UI自动化和接口自动化测试集成，通过Pytest实现统一执行，支持不同测试模块间的协同运行，提升框架的兼容性和灵活性。

- 持续集成与报告生成：通过Git管理代码，利用Jenkins触发自动化测试，结合Allure生成详尽的可视化报告，便于分析测试结果和追踪缺陷，提高了测试效率和稳定性。

## [项目结构](/)

### 目录结构概览

以下是整个测试框架的目录结构概览：

```bash
.
│  .gitignore                
│  LICENSE               
│  suites.py 				 # 测试套件存放文件
│  pytest.ini 				
│  conftest.py               # pytest 全局fixture存放
│  main.py                   # 主程序入口
│  README.md                 
│  requirements.txt          # 项目依赖包列表
│
├─case                       # 测试用例目录
│  ├─apicase                 # API相关测试用例
│  │  ├─business             
│  │  │  └─patient          
│  │  │      test_getpatientbyid.py  # /business/patient/getPatientById接口的测试
│  │  │      test_list.py            
│  │  └─medical_report      
│  │          test_upload.py         # /follow-up/medical-report/upload接口的测试
│  │
│  ├─appcase                 # APP端测试用例
│  │  └─testChuFang          # 处方相关测试集合
│  │          test_im_kai_chu_fang.py  
│  │          test_jie_tu_wen.py       
│  │          test_shenfang.py         # 审方模块测试用例（所有审方的用例放在这个模块
│  │          test_yong_yao_yu_ding_dan.py  
│  │
│  ├─testDB                  # 数据库相关测试
│  │      test_fetch_sms_record.py     # 获取验证码
│  │
│  └─webcase                 # Web端测试用例
│      └─testDemo            # 测试集合
│         test_mo_ban_she_zhi.py       # 配置项模板设置相关用例模块
│
├─common                     # 公共工具模块
│      api_client.py         # API客户端封装
│      app_driver.py         # 移动应用驱动配置
│      basepage.py           # 页面对象基类
│      cleanup_utils.py      # 清理工具函数
│      database_utils.py     # 数据库工具函数
│      load_data_from_file.py # 数据加载工具
│      logging_config.py     # 日志配置
│      sl_cookies.py         # Cookie管理
│      web_driver.py         # Web驱动配置
│
├─data                       # 数据文件
│  ├─api                     # API测试数据
│  │  ├─business           
│  │  │  └─patient         
│  │  │      getPatientById_get.csv # /business/patient/getPatientById接口get用例数据     
│  │  ├─follow-up          
│  │  │  └─medical_report    
│  │  │      upload_post.csv   		# /follow-up/medical-report/upload接口post用例数据
│  │  │      upload_post.json      
│  │ 
│  ├─tempdata                     # 临时数据存放
│  │ 
│  └─config                 # 配置文件
│          api_cookies.json      # API cookies配置
│          cookies.json          # 通用cookies配置
│          db_config.json        # 数据库配置
│          test_paths.json       # 测试环境配置文件
│
├─output               		 # allure，log，截图等输出文件
│
├─pagelocators               # 页面定位符
│  ├─doc                     # 医生App端页面定位符
│      pl_index.py           # 主页元素定位
│
│  └─med                     # 药师app端相关页面定位符
│
└─pageobject                 # 页面对象模型
   ├─doc                     # 医生App端页面对象
       po_chufang.py         # 处方页面对象
       po_im.py              # 即时通信页面对象
       po_index.py           # 主页页面对象
 
   └─med                     # 药师app端相关页面对象
```

### 项目结构说明

- `main.py` 程序的主运行入口，用于运行所有用例和运行指定的用例套件，在`suites.py`中编辑测试套件
- `test_paths.json`测试环境配置文件,可根据需要添加开发环境或生产环境配置文件，然后在`main.py`文件中更改
- `case`：存放所有测试用例，包括 API、APP 和 Web 各端的测试逻辑。
- `common`：公共工具模块，封装了测试所需的API客户端、驱动配置、数据库操作、日志和清理工具等。
- `data`：测试数据和配置信息，分模块存放API、业务数据和配置文件。
- `output`：存放测试输出结果，如日志、截图和 Allure 报告。
- `pagelocators`：页面元素的定位文件，分模块组织，帮助页面对象直接引用元素位置。
- `pageobject`：页面对象模型，以模块划分实现不同页面的操作封装，提高测试复用性和可维护性。

## [编码规范](/)

- 统一使用python 3.8
- 编码使用`coding:utf8`,且不指定解释器
- 类/方法的注释均写在class/def下一行，并且用三个双引号形式注释
- 局部代码注释使用#号
- 所有中文都直接使用字符串，不转换成Unicode，即不是用【u'中文'】编写
- 在各个用例目录（如接口测试的case/appcase/）下的测试包以testModuleName小驼峰命名，用于存放不同分类的模块
- case/apicase下的接口用例使用接口进行分类：如`/business/patient/getPatientById`这个接口就放在`case/apicase/business/patient/test_getpatientbyid.py`这个路径下，同一个接口的不同请求如get和post或delete等都放在一个模块文件里，以一个测试类的不同测试用例存在。
- 接口测试的测试数据根据接口名字放在data/api文件夹下，如：上一条的接口的测试数据就放在`data/api/business/patient/getPatientById_get.csv
- 所有的测试模块文件都以test_module_name.py命名，所有跟这个模块相关的用例都放在一个模块文件内
- 所有的测试类都以Test开头，大驼峰命名，类中方法(用例)都以test_开头，同时非测试类和方法请勿按照这个格式命名，否则会被识别为测试用例，测试类名字最好和模块文件相同
- 每一个模块中测试用例如果有顺序要求【主要针对ui自动化测试】，则自上而下排序，pytest在单个模块里会自上而下按顺序执行
- 需要同时运行多个模块时，在`suites.py`中添加套件后到`main.py`中增加套件名字，并使用`python main.py suitename1 suitename2`来运行
- 单独运行某个模块，使用`pytest path/to/your/module`来执行单个模块文件。

## [项目部署](/)

### 本项目使用了以下包

#### 1. **测试框架和报告**
   - **`pytest`**：主要测试框架，用于运行测试。
   - **`allure-pytest`** 和 **`allure-python-commons`**：用于生成测试报告的工具。
   - **`pytest-html`**：生成 HTML 格式的测试报告。
   - **`pytest-metadata`**：提供测试元数据功能。
   - **`pytest-order`**：控制测试用例的执行顺序。

#### 2. **自动化和 App 操作**
   - **`Appium-Python-Client`**：用于移动端自动化测试的 Appium 客户端。
   - **`selenium`**：用于 Web 自动化测试的 Selenium 库。
   - **`PyAutoGUI`**、**`MouseInfo`**、**`PyGetWindow`**、**`PyMsgBox`**、**`PyScreeze`**、**`PyRect`**：自动化 GUI 操作的库，主要用于模拟鼠标、键盘等操作。

#### 3. **HTTP 请求和网络**
   - **`requests`**：HTTP 请求库，用于发送网络请求。
   - **`urllib3`**、**`urllib3-secure-extra`**、**`idna`**、**`certifi`**：与 HTTP 请求相关的底层依赖。
   - **`pyOpenSSL`**、**`PySocks`**、**`websocket-client`**、**`wsproto`**：用于安全连接和 WebSocket 的支持。

#### 4. **并发和异步操作**
   - **`trio`** 和 **`trio-websocket`**：异步编程库，用于异步 WebSocket 操作。
   - **`sniffio`**、**`outcome`**：辅助并发操作的库。

#### 5. **数据库**
   - **`PyMySQL`**：用于 MySQL 数据库连接和操作。

#### 6. **其他辅助库**
   - **`attrs`**、**`iniconfig`**、**`pluggy`**、**`sortedcontainers`**、**`typing_extensions`**：提供属性管理、配置管理、插件支持、类型扩展等功能。
   - **`colorama`**：提供终端字符的着色功能。
   - **`cryptography`** 和 **`cffi`**：提供加密支持。
   - **`packaging`**：用于处理版本号和依赖关系。
   - **`pytweening`**：提供动画的缓动函数。
   - **`pillow`**：图像处理库，处理图片格式和操作。

#### 7. **模板和字符处理**
   - **`Jinja2`** 和 **`MarkupSafe`**：用于生成动态 HTML 模板。
   - **`charset-normalizer`**：处理字符编码。
   - **`pyperclip`**：提供剪贴板操作功能。

## 快速部署

### 环境配置

1. 克隆项目到本地
2. 安装项目依赖：`pip install -r requirements.txt`
3. app端需要安装appium服务，请自行Google
4. 进入`data/config/test_paths.json`文件，按照下列进行修改

   1. chrome_testing_path : chrome路径
   2. chromedriver_path : chromedriver路径
   3. chrome_user_data_dir ：chrome用户数据文件夹，一般为："C:\\Users\\Username\\AppData\\Local\\Google\\Chrome for Testing\\User Data"将username修改为自己的用户名。有些使用token来保存登陆状态的网站我选择直接读取用户数据来保证测试时的登陆状态
   4. test_doc_port/test_med_port ：我需要测试的app端分为两个app，这是使用adb连接安卓模拟器的端口，本项目的配置只支持模拟器，且为安卓12，想用真机请自行查询如何使用adb连接真机，然后去common/app_driver.py里修改对应的appium启动参数deviceName和udid
   5. appPackage：需要启动的app包名，自行查询怎么获得
   6. appActivity：需要启动的app的Activity，自行查询怎么获得
   7. BASE_URL：接口测试的域名
