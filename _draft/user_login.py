
    username = request.json['username']
    password = request.json['password']
    user = User.query.filter_by(username=username).first()
    if user is None or not bcrypt.check_password_hash(user.password, password):
        abort(400)
    login_user(user)
    return jsonify({'username': user.username})


#----------

    if not request.json or not 'username' in request.json or not 'password' in request.json:
           abort(400)
        username = request.json['username']
        password = request.json['password']
        user = User.query.filter_by(username=username).first()
        if user is None or not bcrypt.check_password_hash(user.password, password):
            abort(400)
        login_user(user)
        return jsonify({'username': user.username})
    