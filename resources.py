from flask.views import MethodView
from flask import jsonify, request
from database import db, PrivilegedAccount

class PrivilegedAccount(MethodView):
    def get(self, account_id):
        account = PrivilegedAccount.query.filter_by(id=account_id).first()
        if not account:
            return {'error': 'Account not found'}, 404

        return jsonify({
            'id': account.id,
            'username': account.username,
            'password': account.password,
            'role': account.role,
            'created_at': account.created_at
        })

    def post(self):
        data = request.get_json()
        account = PrivilegedAccount(**data)
        db.session.add(account)
        db.session.commit()
        return jsonify({'message': 'Account created successfully'}), 201

    def put(self, account_id):
        account = PrivilegedAccount.query.filter_by(id=account_id).first()
        if not account:
            return {'error': 'Account not found'}, 404

        data = request.get_json()
        account.username = data['username']
        account.password = data['password']
        account.role = data['role']
        db.session.commit()
        return jsonify({'message': 'Account updated successfully'})

    def delete(self, account_id):
        account = PrivilegedAccount.query.filter_by(id=account_id).first()
        if not account:
            return {'error': 'Account not found'}, 404

        db.session.delete(account)
        db.session.commit()
        return jsonify({'message': 'Account deleted successfully'})

class PrivilegedAccountList(MethodView):
    def get(self):
        accounts = PrivilegedAccount.query.all()
        result = []
        for account in accounts:
            result.append({
                'id': account.id,
                'username': account.username,
                'password': account.password,
                'role': account.role,
                'created_at': account.created_at
            })

        return jsonify(result)
