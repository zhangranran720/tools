### 日常使用的小脚本
#### 1. MAC终端连接脚本 connect_host.py
    host文件: 存放连接信息
    .zshrc: 设置lshost别名  alias lshost='python connect_host.py'
    connect_host.py: 主脚本
    使用ssh-copy-id与被连接主机做SSH密钥认证,免密连接.  
    执行lshost命令选择要连接的主机即可.
    
