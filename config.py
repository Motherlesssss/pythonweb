#任何环境下都相同的配置
class BaseConfig:
  SECRET_KEY = '569889'
  SQLALCHEMY_TRACK_MODIFICATIONS = False


#开发环境
class DevelopmentConfig():
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:569889@127.0.0.1:3306/xiangmushizhan?charset=utf8mb4'

#测试环境
class Testingconfig():
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:569889/test_db?charset=utf8mb4'

#生产环境
class ProductionConfig():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:569889/test_db?charset=utf8mb4'