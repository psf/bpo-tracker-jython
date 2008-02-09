from roundup.password import Password

#
# TRACKER INITIAL PRIORITY AND STATUS VALUES
#

issue_type = db.getclass('issue_type')
issue_type.create(name='behaviour', order='1')
issue_type.create(name='security', order='2')
issue_type.create(name='rfe', order='3')
issue_type.create(name='crash', order='4')

component = db.getclass('component')
component.create(name="Any", order="1")
component.create(name="Core", order="2")
component.create(name="Documentation", order="3")
component.create(name="Installer", order="4")
component.create(name="Jythonc compiler", order="5")
component.create(name="Library", order="6")
component.create(name="website", order="7")
component.create(name="zxjdbc", order="8")

version = db.getclass('version')
version.create(name='Deferred', order='1')
version.create(name='Fixed in 2.1a3', order='2')
version.create(name='Fixed in 2.1b1', order='3')
version.create(name='Fixed in 2.1b2', order='4')
version.create(name='Fixed in 2.1final', order='5')
version.create(name='Fixed in 2.2a0', order='6')
version.create(name='targeted for 2.2.1rc1', order='7')
version.create(name='targeted for 2.2beta1', order='8')
version.create(name='targeted for 2.2beta2', order='9')
version.create(name='targeted for 2.2rc1', order='10')
version.create(name='targeted for 2.2rc2', order='11')
version.create(name='targeted for 2.2rc3', order='12')
version.create(name='test failure causes', order='13')

severity = db.getclass('severity')
severity.create(name='critical', order='1')
severity.create(name='urgent', order='2')
severity.create(name='major', order='3')
severity.create(name='normal', order='4')
severity.create(name='minor', order='5')

priority = db.getclass('priority')
priority.create(name='immediate', order='1')
priority.create(name='urgent', order='2')
priority.create(name='high', order='3')
priority.create(name='normal', order='4')
priority.create(name='low', order='5')

status = db.getclass('status')
status.create(name='open', order='1')
status.create(name='closed', order='2')
status.create(name='pending', description='user feedback required', order='3')

resolution = db.getclass('resolution')
resolution.create(name='accepted', order='1')
resolution.create(name='duplicate', order='2')
resolution.create(name='fixed', order='3')
resolution.create(name='invalid', order='4')
resolution.create(name='later', order='5')
resolution.create(name='out of date', order='6')
resolution.create(name='postponed', order='7')
resolution.create(name='rejected', order='8')
resolution.create(name='remind', order='9')
resolution.create(name='wont fix', order='10')
resolution.create(name='works for me', order='11')

keyword = db.getclass("keyword")
# The patch keyword is needed by the importer
keyword.create(name="patch", description="Contains patch")

#
# create the two default users
user = db.getclass('user')
user.create(username="admin", password=adminpw, address=admin_email, roles='Admin')
user.create(username="anonymous", roles='Anonymous')

# and some test users
user.create(username="user", password=Password("user"), roles="User")
user.create(username="developer", password=Password("developer"), roles="User,Developer")
