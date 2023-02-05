import email
from pydoc import cli
from models.user import PermissionEnum,PermissionModel,RoleModel, UserModel
import click
from exts import db

#自定义命令示意
#@app.cli.command('my-command')
def my_command():
    click.echo('这是我的命令')

#创建权限数据命令
#@app.cli.command('create-permission')
def create_permission():
    for permission_name in dir(PermissionEnum):
        if permission_name.startswith('__'):
            continue
        permission = PermissionModel(name=getattr(PermissionEnum,permission_name))
        db.session.add(permission)
    db.session.commit()
    click.echo('权限添加成功!')

#添加角色命令
#@app.cli.command('create-role')
def create_role():
    #稽查
    inspector = RoleModel(name='稽查',desc='负责审核帖子和评论是否合法合规！')
    inspector.permissions = PermissionModel.query.filter(PermissionModel.name.in_([PermissionEnum.POST,PermissionEnum.COMMENT])).all()

    #运营
    operator = RoleModel(name='运营',desc='负责网站持续正常运营！')
    operator.permissions = PermissionModel.query.filter(PermissionModel.name.in_([
        PermissionEnum.POST,
        PermissionEnum.COMMENT,
        PermissionEnum.BOARD,
        PermissionEnum.FRONT_USER,
        PermissionEnum.CMS_USER
    ])).all()

    #管理员
    administrator = RoleModel(name='管理员',desc='负责整个网站的所有工作！')
    administrator.permissions = PermissionModel.query.all()

    db.session.add_all([inspector,operator,administrator])
    db.session.commit()
    click.echo('角色添加成功！')

#创建测试用户
def create_test_user():
    admin_role = RoleModel.query.filter_by(name='管理员').first()
    Jinhui_Xu = UserModel(username='许金辉',email='1169153079@qq.com',password='666666',is_staff=True,role=admin_role)

    operator_role = RoleModel.query.filter_by(name='运营').first()
    Mengsheng_Wang = UserModel(username='王蒙圣',email='2319133140@qq.com',password='666666',is_staff=True,role=operator_role)

    inspector_role = RoleModel.query.filter_by(name='稽查').first()
    Xulin_Yao = UserModel(username='姚旭麟',email='1819204226@qq.com',password='666666',is_staff=True,role=inspector_role)

    db.session.add_all([Jinhui_Xu,Mengsheng_Wang,Xulin_Yao])
    db.session.commit()
    click.echo('测试用户添加成功！')

#创建管理员
@click.option('--username','-u')
@click.option('--email','-e')
@click.option('--password','-p')
def create_admin(username,email,password):
    admin_role = RoleModel.query.filter_by(name='管理员').first()
    admin_user = UserModel(username=username,email=email,password=password,is_staff=True,role=admin_role)
    db.session.add(admin_user)
    db.session.commit()
    click.echo('管理员创建成功！')