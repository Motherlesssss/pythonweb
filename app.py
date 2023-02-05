from flask import Flask
import config
from exts import db
from buleprints.cms import bp as cms_bp
from buleprints.front import bp as front_bp
from buleprints.user import bp as user_bp
from flask_migrate import Migrate
from models import user
import click
import commands





app = Flask(__name__)

#引入配置，根据环境不同选择
app.config.from_object(config.DevelopmentConfig)

#绑定插件
db.init_app(app)

#注册蓝图
app.register_blueprint(cms_bp)
app.register_blueprint(front_bp)
app.register_blueprint(user_bp)

#创建Migrate对象
migrate = Migrate(app,db)

#添加命令
app.cli.command('create-permission')(commands.create_permission)
app.cli.command('create-role')(commands.create_role)
app.cli.command('my-command')(commands.my_command)
app.cli.command('create-test-user')(commands.create_test_user)
app.cli.command('create-admin'(commands.create_admin))



if __name__ == '__main__':

    app.run()