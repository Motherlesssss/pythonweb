#任何环境下都相同的配置
class BaseConfig:
  SECRET_KEY = '569889'
  SQLALCHEMY_TRACK_MODIFICATIONS = False


#开发环境
class DevelopmentConfig():
  #链接数据库
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:569889@127.0.0.1:3306/xiangmushizhan?charset=utf8mb4'
  #邮件配置
  MALL_SERVER = 'smtp.163.com'
  MALL_USE_SSL = True
  MALL_PORT = 465
  MALL_USERNAME = 'xjh20190601@163.com'
  MALL_PASSWORD = 'LITKBLGXTEZGMXIW'
  MALL_DEFAULT_USER = 'xjh20190601@163.com'
  #缓存配置
  CACHE_TYPE = 'RedisCache'
  CACHE_REDIS_HOST = '127.0.0.1'
  CACHE_REDIS_PORT = 6379
  #任务调度框架Celery
  #格式：redis://:password@hostname:port/db_number
  CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
  CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'


#测试环境
class Testingconfig():
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:569889/test_db?charset=utf8mb4'

#生产环境
class ProductionConfig():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:569889/test_db?charset=utf8mb4'