from service import login, register, logout, todo_list, todo_add, login_required, is_admin,make_admin, todo_update, todo_delete


def menu():
    print('Login => 1')
    print('Register => 2')
    print('Logout => 3')
    print('Todo List => 4')
    print('Todo Add => 5')
    print('Make Admin => 6')
    print('Update todo=> 7')
    print('Delete todo => 8')
    print('Quit => q')
    return input('say ...')



def login_response():
    username = input('Username : ')
    password = input('Password : ')
    response = login(username,password)
    print(response.message)
    

def register_response():
    username = input('Username : ')
    password = input('Password : ')
    response = register(username,password)
    print(response.message)
    

def logout_response():
    response = logout()
    print(response.message)
    

@login_required
@is_admin  
def create_todo():
    title = input('Title : ')
    user_id = int(input('USER ID : '))
    response = todo_add(title,user_id)
    return response


def make_admin_response():
    username = input("Admin qilish uchun foydalanuvchi nomini kiriting: ")
    response = make_admin(username)
    print(response.message)


def update_todo_response():
    todo_id = int(input("Todo ID kiriting: "))
    new_title = input("Yangi sarlavha: ")
    response = todo_update(todo_id, new_title)
    print(response.message)

def delete_todo_response():
    todo_id = int(input("Todo ID kiriting: "))
    response = todo_delete(todo_id)
    print(response.message)    

    

def run():
    while True:
        choice = menu()
        if choice == '1':
            login_response()
        
        elif choice == '2':
            register_response()
        
        elif choice == '3':
            logout_response()
        
        elif choice == '4':
            todo_list()
        
        elif choice == '5':
            response = create_todo()
            print(response.message)

        elif choice == '6':
            make_admin_response()

        elif choice == '7':
            update_todo_response()

        elif choice == '8':
            delete_todo_response()

        elif choice == 'q':
            break
        
        
if __name__ == '__main__':
    run()   