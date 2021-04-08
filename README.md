# scrapy_pdf

爬取PDF文件
原本目的是抓取校园网内部服务某个文件夹下的所有PDF文件,但是站方了下架所有PDF-_-

使用方法：
在setting中配置
root_link 为需要爬取PDF的根页面
link_start 为下载PDF的地址头部, https://xxxx/
download_local_dir 本地下载目标文件夹

TODO：
模块化为命令行程序
