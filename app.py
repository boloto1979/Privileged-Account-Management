from flask import Flask
import datetime
from database import db
from resources import PrivilegedAccount, PrivilegedAccountList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<user>:<password>@<host>/database.py'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# adicionando as rotas
app.add_url_rule('/api/v1/accounts', view_func=PrivilegedAccountList.as_view('account_list'))
app.add_url_rule('/api/v1/accounts/<int:account_id>', view_func=PrivilegedAccount.as_view('account'))

if __name__ == '__main__':
    app.run(debug=True)
