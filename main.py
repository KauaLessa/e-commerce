from client import User
from client import Admin
from connect import create_connection


def get_input(prompt, min_length=None):
    while True:
        value = input(prompt)
        if value == '0' or value == '-1':
            return None
        if min_length and len(value) < min_length:
            print(f"Input must have at least {min_length} characters!\n")
        else:
            return value

def create_account(connection) -> bool:
    print("Enter [0] to cancel account creation")
    
    user_name = get_input('Enter your name: ', 4)
    if not user_name:
        return False
    
    user_password = get_input('Enter your password: ', 8)
    if not user_password:
        return False
    
    user_email = get_input('Enter your email: ', 1)
    if not user_email:
        return False
    
    new_user = User(name=user_name,password=user_password,email=user_email)
    success = new_user.insert_login(connection, user_email)
    
    return success
    
def login_account(connection):
    print("Enter [0] to cancel account login")
    
    user_email = input("Enter user email: ")
    if user_email == '0':
        return None
    
    user_password = input("Enter user password: ")
    if user_password == '0':
        return None
    
    user = User()
    success = user.login_user(connection, user_email, user_password)
    
    if success:
        return user
    else:
        return None
       
def update_account(connection, user: User):
    password = input("Enter your current password for authentication: ")
    
    if password != user.password:
        print("Invalid pasword!")
        return False
        
    name = input("Enter new user name: ")
    email = input("Enter new user email: ")
    password = input("Enter new user password: ")
    
    success = user.update_login(connection, name, password, None, email)
    
    return success

def get_num(input_msg: str) -> float:
    while True:
        number = input(input_msg)
        
        # Verifica se a entrada está vazia
        if number == '':
            return number
        
        # Tenta converter a entrada para float
        try:
            number = float(number)
        except ValueError:
            print('Invalid input!')
            continue  # Reinicia o loop para pedir a entrada novamente
        
        # Verifica se a entrada é -1
        if number == -1:
            return None
        
        return number  # Retorna o número convertido

def enter_product(connection, admin: Admin) -> bool:
    print("Enter [-1] to cancel product registration")
    
    product_name = get_input("Enter product name: ", 1)
    if not product_name:
        return False
    
    product_cost = get_num('Enter product cost: ')
    if not product_cost:
        return False
    
    product_quantity = get_num('Enter product stock: ')
    if not product_quantity:
        return False
    
    admin.insert_product(connection, product_name, product_cost, product_quantity)
    
    return True

def change_loc_info(connection, user: User) -> bool:
    print("Enter [0] to cancel location update")
    
    country = get_input("Enter your country: ")
    if country != '' and not country:
        return False
    
    state = get_input("Enter your state: ")
    if state != '' and not state:
        return False
    
    city = get_input("Enter your city: ")
    if city != '' and not city:
        return False
    
    district = get_input("Enter your district: ")
    if district != '' and not district:
        return False
    
    street = get_input("Enter your street: ")
    if street != '' and not street:
        return False
        
    return user.update_location(connection,country,state,city,district,street)

def update_item(connection, admin:Admin) -> bool:
    print("Enter -1 to cancel item update")
    
    product_id = get_num('Enter product id: ')
    
    if not product_id:
        return False
    
    new_name = get_input('Enter product new name: ')
    if new_name != '' and not new_name:
        return False
    
    new_cost = get_num('Enter new cost: ')
    if new_cost != '' and not new_cost:
        return False
    
    new_quantity = get_num('Enter new quantity: ')
    if new_quantity != '' and not new_quantity:
        return False
    
    return admin.update_product(connection,new_name,new_cost,new_quantity,product_id)

def del_product(connection, admin: Admin) -> bool:
    pd_id = input('Enter product id: ')
    
    return admin.remove_product(connection, pd_id)

def my_account(connection, user: User):
    print("Your user data:")
    print(user)
    print()
    print("Press [1] to change your account login")
    print("Press [2] to change your account location info")
    
    if user.isAdmin:
        print("Press [3] to insert new product")
        print("Press [4] to update product")
        print("Press [5] to delete product")
        
    print("Press any other key to log out")
    
    option = input()
    
    
    if option == '1':
        print()
        if update_account(connection, user):
            print("Account sucessful updated!\n")
        else:
            print("Error when updating account\n")
            
    elif option == '2':
        print()
            
        if change_loc_info(connection, user):
            print("Location info updated!\n")
        else:
            print("Error when trying to update location\n")
                
    elif option == '3' and user.isAdmin:
        print()
    
        admin = Admin()
            
        if enter_product(connection, admin):
            print("Product registration successful!\n")
        else:
            print("Error when registrating product.\n")
    elif option == '4' and user.isAdmin:
        print()
        
        admin = Admin()
        
        if update_item(connection, admin):
            print("Product update successful!\n")
        else:
            print("Error when updating product\n")
    elif option == '5' and user.isAdmin:
        print()
        
        admin = Admin()
        
        if del_product(connection, admin):
            print("Product successful deleted!")
        else:
            print("Error. Can not find product.")
    else:
        return
    
def main():
    reconfig_conn = input("Reconfig connection? [y/n]: ").upper()
    
    if reconfig_conn == 'Y':
        # entry = input("Enter, in order, password, database, hostname, user: ").split()
        password = input('Enter connection password: ')
        hostName = input('Enter connection hostname: ')
        user = input('Enter connection user: ')
        port = input('Enter connection port: ')
        # password, database, hostName, user = entry
        connection = create_connection(password,port,hostName,user)
    else:
        connection = create_connection()
    
    print()

    
    while(True):
        print("Press [1] to create new account")
        print("Press [2] to log in with existing account")
        print("Press any other key to exit")
        
        select = input()
        
        if select == '1':
            print()
            if create_account(connection):
                print("New account created!\n")
            else:
                print("Email alredy in use!\n")
        elif select == '2':
            print()
            user: User = login_account(connection)
            if user:
                print("Login successful!\n")
                my_account(connection, user)
            else:
                print("Login unsucessful. Check your email and password\n")
                continue
        else:
            break

if __name__ == '__main__':
    main()