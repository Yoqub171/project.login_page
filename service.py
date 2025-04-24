from session import Session
from models import User, UserRole
from utils import Response,match_password, hash_password
from database import cursor,commit


session = Session()

@commit
def login(username:str,password:str):
    user : Session | None = session.check_session()
    if user:
        return Response(message='You already logged in',status_code=401)
    get_user_by_username_query = '''
        select * from users where username = %s;
    '''
    data = (username,)
    cursor.execute(get_user_by_username_query,data)
    user_data = cursor.fetchone()
    if not user_data:
        return Response('User not Found',status_code=404)
    
    user = User.from_tuple(user_data)
    if not match_password(password,user.password):
        update_login_try_count_field = '''
            UPDATE users set login_try_count = login_try_count + 1
            where username = %s;
        '''
        cursor.execute(update_login_try_count_field,data)
        return Response('Password did not match')
    session.add_session(user)
    return Response('You successfully logged in ✅✅✅')
    

# response = login('ADMIN','admin1234')
# print(response.message)


@commit
def register_user(username: str, password: str, email: str = None):
    user: Session | None = session.check_session()
    if user:
        return Response(message='You are already logged in', status_code=401)

    check_user_query = '''
        SELECT * FROM users WHERE username = %s;
    '''
    cursor.execute(check_user_query, (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        return Response(message='Username already exists', status_code=400)

    hashed_password = hash_password(password)

    insert_user_query = '''
        INSERT INTO users (username, password, email, role, login_try_count)
        VALUES (%s, %s, %s, %s, 0);
    '''
    cursor.execute(insert_user_query, (
        username,
        hashed_password,
        email,
        UserRole.USER.value
    ))

    return Response(message='User registered successfully ✅')


def register():
    print("Ro'yxatdan o'tish")
    username = input("Foydalanuvchi nomi: ")
    password = input("Parol: ")
    email = input("Email: ") or None

    response = register_user(username, password, email)
    print(response.message)


register()
