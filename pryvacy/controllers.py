from pryvacy import models


def authenticate_user(username, password):
    """
    Authenticate and return user document from
    database, None on failed auth.  Prepare for
    use as session data.
    """
    user = models.User.auth(username, password)
    if not user:
        return
    user['_id'] = str(user['_id']) # For session data
    return user


def signup(username, password, password2):
    """Register the user, return error or None."""
    if models.User.match(username=username):
        error = 'This username is taken'
    elif not password:
        error = 'You have to enter a password'
    elif password != password2:
        error = 'The two passwords do not match'
    else:
        # Insert user into database.
        models.User.create(
            username,
            password
        )
        return
    return error
