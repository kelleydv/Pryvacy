from pryvacy import models
import gnupg


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


def get_users_list():
    users = models.User.match_all()
    return [ {'username':x['username'], 'public_key': x['public_key']} for x in users ]

gpg = gnupg.GPG()
gpg.encoding = 'utf-8'

def gen_pgp_key(user_id, username):
    input_data = gpg.gen_key_input(
        key_type="RSA",
        key_length=1024,
        name_real=username
    )
    key = gpg.gen_key(input_data)
    public_key = gpg.export_keys(key.fingerprint)
    models.User.update(
        user_id,
        rsa_fingerprint=key.fingerprint,
        public_key=public_key
    )
    return public_key

def get_key(user_id, username):
    key = models.User.from_id(user_id).get('public_key')
    return key

def encrypt(key, plaintext):
    if not 'PGP PUBLIC KEY' in key:
        #Might be a substitution key
        if not len(key) == 26:
            error = 'A substitution key must be 26 character long'
        else:
            key = key.lower()
            ciphertext = ''
            for ch in plaintext:
                    idx = alphabet.find(ch.lower())
                    if ch == ch.lower():
                        ciphertext = ciphertext + key[idx]
                    else:
                        ciphertext = ciphertext + key[idx].upper()
            return ciphertext
    else:
        #PGP encryption
        recip_fingerprint = gpg.import_keys(key).fingerprints[0]
        return str(gpg.encrypt(plaintext, recip_fingerprint))

def decrypt(key, ciphertext, username):
    message = gpg.decrypt(ciphertext)

    #proceed with massive kludge to get username of pub-key from message
    for x in message.stderr.split('\n'):
        if '@' in x:
            for y in x.split('"'):
                if '@' in y:
                    key_username = y.split()[0]

    if username == key_username:
        return str(message)
    return 'Pryvacy: Failed to Decrypt Message'
