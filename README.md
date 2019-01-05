本项目含有整个前后端文件以及iView echarts等插件及其示例。示例用法请在HelloWorld.vue查看。
本项目用法：
首先请安装venv环境。步骤如下：File->Setiings->Project:myproject(或者是你自己的工程名)，在右边的Project Interpreter中选择pull或者clone下来的venv环境
然后开发django的人员请在项目文件夹下输入pip install -r requirements.txt安装依赖
如果右上的"myproject"有红X，请点开edit configurations，点击下面的fix配置django文件。
之后请修改myproject->myproject下的settings.example.py文件，名字改为settings.py然后改写为自己的数据库等内容
django project root选择myproject文件夹，Settings选择settings.py文件
开发前端的人员可以进入frontend下载依赖进行开发。

请注意！！！
开发前端的人员尽量不要下载django依赖，开发后端的人员请不要下载frontend依赖以避免麻烦！！！

