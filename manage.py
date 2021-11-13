from app import create_app,db
from flask_script import Manager,Server
import app
from app.models import User
from flask_migrate import Migrate,MigrateCommand, migrate



#creating app instances
app = create_app('production')


app = Manager(app)
Manager.add_command('server',Server)


migrate = migrate(app,db)
Manager.add_command('db',MigrateCommand)
@Manager.command

def test():
    """
    run the unitests
    """
    import unittest
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(test)


@Manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User)


if __name__ == '__main__':
    Manager.run()