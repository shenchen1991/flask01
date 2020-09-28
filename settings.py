# 配置文件
ENV = 'development'
DEBUG = True

DIALCT = 'mysql'
DRIVER = "pymysql"
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DBNAME = 'bigodds'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DBNAME)
SQLALCHEMY_TRACK_MODIFICATIONS = True  # 没有此配置会导致警告
