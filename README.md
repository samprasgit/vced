<h1 align="center">
	VCED: Video Clip Extraction by description
	<br>

</h1>
<div align="center">
  <a href="https://www.python.org/downloads/" target="_blank"><img src="https://img.shields.io/badge/python-3.9.x-brightgreen.svg" alt="Python supported"></a>
  <a href="https://linklearner.com/"><img src="https://img.shields.io/website?url=https%3A%2F%2Flinklearner.com%2F%23%2F" alt="DataWhale Website"></a>

  <h3 align="center">
    <a href="https://linklearner.com/">Datawhale Website</a>
    <br/>
    <a href="https://linklearner.com/">Docs</a>
    <span> | </span>
    <a href="https://github.com/datawhalechina/vced#%E5%8F%82%E4%B8%8E%E8%B4%A1%E7%8C%AE">Contribute</a>
  </h3>

</div>

----------------------------------------
VCED 可以通过你的文字描述来自动识别视频中相符合的片段进行视频剪辑。该项目基于跨模态搜索与向量检索技术搭建，通过前后端分离的模式，帮助你快速的接触新一代搜索技术。

如果你喜欢本项目欢迎给一个 **⭐ !**

----------------------------------------

[QuickStart](https://github.com/datawhalechina/vced#quickstart) - [项目结构](https://github.com/datawhalechina/vced#%E6%96%87%E6%A1%A3) - [文档](https://github.com/datawhalechina/vced#%E6%96%87%E6%A1%A3) - [Learning Roadmap](https://github.com/SuperSupeng/vced/blob/4387bbeaf7c66cf03532ef64617a8877481dad0d/Roadmap.md) - [反馈](https://github.com/datawhalechina/vced#%E5%8F%8D%E9%A6%88) - [参与贡献](https://github.com/datawhalechina/vced#%E5%8F%82%E4%B8%8E%E8%B4%A1%E7%8C%AE) - [关注我们](https://github.com/datawhalechina/vced#%E5%85%B3%E6%B3%A8%E6%88%91%E4%BB%AC) - [License](https://github.com/datawhalechina/vced#license)

----------------------------

<h2 align="center">
   VCED demo
   <br/>
   <br/>
  <img width="600" src="./pics/demo.gif" alt="VCED">	

</h2>

## QuickStart

### 通过 docker 启动

使用 docker 镜像快速启动本项目:

>在clone好的项目的根目录下，使用终端启动docker

![image-20221115103634904](../../../../Library/Application%20Support/typora-user-images/image-20221115103634904.png)

``` bash
docker-compose build
docker-compose up -d
```

### 通过源代码启动

#### 说明

本项目依赖以下环境，在进行具体的安装之前请确保你的电脑已经安装好这些依赖

1. 创建 python3.9 环境
2. 安装 rust, ffmpeg
3. 安装 clip `pip install git+https://github.com/openai/CLIP.git`

*Jina 暂不支持在 Windows 安装，如需在 Windows 上安装 Jina 请通过 WSL 方式，详情见：[Jina 轻松学 —— Windows中安装Jina](https://blog.csdn.net/Jina_AI/article/details/122820646)*

#### 启动 server

```bash
# 进入 server 文件夹
cd code/service
# 安装相关依赖
pip install -r requirements.txt
# 启动服务端
python app.py
```

#### 启动 web

前端我们通过 [Streamlit](https://streamlit.io/) 搭建。[Streamlit](https://streamlit.io/) 是一个 Python Web 应用框架，但和常规 Web 框架，如 Flask/Django 的不同之处在于，它不需要你去编写任何客户端代码（HTML/CSS/JS），只需要编写普通的 Python 模块，就可以在很短的时间内创建美观并具备高度交互性的界面。

```bash
# 进入 web 文件夹
cd code/web
# 安装相关依赖
pip install -r requirements.txt
# 启动服务端
streamlit run app.py
```

Streamlit默认启动的端口为8501，也可以通过 `localhost:8501` 进行访问

## 项目结构

```
    ├── code/service
        ├── customClipImage (通过 CLIP 模型处理上传的视频)
        ├── customClipText  (通过 CLIP 模型处理输入的文字)
        ├── customIndexer   (创建向量数据的索引)
        ├── videoLoader     (对上传的视频进行处理)
        ├── workspace       (用于存储生成的向量数据)
        ├── app.py          (后端主程序)                                                       
    ├── code/web
        ├── data            (用于存储上传的视频)
        │   ├── videos      (用于存储简介好的视频片段)
        ├── app.py          (前端主程序)  
	  ├── Dockerfile                                                     
    ├── requirements.txt  
```

## 文档

如果你想在本地查阅文档可以通过以下方式实现

1. 将项目下载到本地
2. 用浏览器打开 [docs/build/html/index.html](./docs/build/html/index.html)

如果你对文档内容有修改想要查看最新的内容可以通过以下方式

```bash
# 进入 docs 文件夹
cd docs
# 安装相关依赖
pip install -r requirements.txt
# 编译
make html
```

然后就可以在`public`文件夹下双击`index.html`即可看到文档，如下所示
![homepage](./pics/homepage.png)

## Learning Roadmap

内容学习路线详见：[Roadmap](https://github.com/datawhalechina/vced/blob/main/Roadmap.md)


## License

VCED is licensed under [GNU General Public License v3.0](https://github.com/datawhalechina/vced/blob/21f5f745665abcebbe1556238af8070d6e4f5c2e/LICENSE)
