SECRET_KEY = "ahjoiiuiijnxchauygg"

# mysql所在的主机名
HOSTNAME = "127.0.0.1"
# mysql监听的端口号，默认3306
PORT = 3306
# 连接mysql的用户名
USERNAME = "root"
# 连接mysql的密码
PASSWORD = "gyla2022"
# mysql上创建的数据库名称
DATABASE = "zhiliaooa_course"

DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "3026715639@qq.com"
MAIL_PASSWORD = "xokijmvyailrdfjb"
MAIL_DEFAULT_SENDER = "3026715639@qq.com"
