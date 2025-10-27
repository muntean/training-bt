from xmlrpc import client

# url = 'https://bisstech-training-bt-branko-training-2022-4952715.dev.odoo.com'
url = 'http://localhost:8069'
# db = 'bisstech-training-bt-branko-training-2022-4952715'
db = 'odoo_training_2022_05'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))
model_access = models.execute_kw(db, uid, password, 'academy.book', 'check_access_rights', ['write'], {'raise_exception': False})
print(model_access)
books = models.execute_kw(db, uid, password, 'academy.book', 'search_read', [[['genre', 'in', ['fantasy']]]])
print(books)
