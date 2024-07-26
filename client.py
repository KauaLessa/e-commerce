# TODO: Mudar queries
# TODO: Garantir que não ocorram erros de inserção/update de instancias

class User():
    def __init__(self, user_id: int = None, name: str = None, email:str = None, password:str = None, admin:bool = False):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.isAdmin = admin
        self.email = email
        self.country = None
        self.state = None
        self.city = None
        self.district = None
        self.street = None
        # self.locationStatus = False
        
    def insert_login(self, conn, email: str) -> bool:
        cursor = conn.cursor()
        
        cursor.execute('USE ec_users;')
        
        # executa consulta para verificar se este login ja existe
        cursor.execute( 
            f'''SELECT*
            FROM logins
            WHERE email = "{email}";'''
        )
        exists = cursor.fetchone()
        
        if exists:
            cursor.close()
            return False
        else:
            cursor.execute(
                f'''INSERT INTO logins (name, email, password, admin)
                VALUES("{self.name}", "{self.email}", "{self.password}", {self.isAdmin});'''
            )
            conn.commit()
            
            cursor.execute('SELECT LAST_INSERT_ID()')
            self.user_id = cursor.fetchone()[0]
            
            cursor.close()
            return True
        
    def update_login(self, conn,new_name=None, new_password=None,new_admin_status=None, new_email=None) -> bool:
        cursor = conn.cursor()
        
        cursor.execute('USE ec_users;')
        cursor.execute(f'''SELECT* FROM logins WHERE user_id={self.user_id};''')
        exists = cursor.fetchone()
        
        if exists:
            self.name = new_name or self.name
            self.password = new_password or self.password
            self.isAdmin = new_admin_status or self.isAdmin
            self.email = new_email or self.email
        
            cursor.execute(
                f'''UPDATE logins
                SET name = "{self.name}",
                password = "{self.password}",
                admin= {self.isAdmin},
                email="{self.email}"
                WHERE user_id={self.user_id};''')
            
            conn.commit()
            cursor.close()
            return True
        else:
            cursor.close()
            return False
        
    def insert_location(self, conn, in_country: str, in_state: str, in_city: str, in_district: str, in_street: str) -> bool:
        cursor = conn.cursor()
        
        cursor.execute('USE ec_users;')
        cursor.execute(f'''SELECT* FROM locations WHERE user_id="{self.user_id}";''')
        exists = cursor.fetchone()
        
        if exists:
            cursor.close()
            return False
            
        cursor.execute(
            f'''INSERT INTO locations (user_id, country, state, city, district, street)
            VALUES("{self.user_id}","{in_country}","{in_state}", "{in_city}", "{in_district}","{in_street}");
            '''
        )
        conn.commit()
        cursor.close()
        return True
    
    def update_location(self, conn, new_country:None, new_state:None, new_city:None, new_district:None, new_street:None):
        cursor = conn.cursor()
        
        cursor.execute('USE ec_users;')
        cursor.execute(f'''SELECT* FROM logins WHERE user_id = {self.user_id};''')
        isUser = cursor.fetchone()
        
        if isUser:
            self.country = new_country or self.country
            self.state = new_state or self.state
            self.city = new_city or self.city
            self.district = new_district or self.district
            self.street = new_street or self.street
        
            cursor.execute(f'SELECT* FROM locations WHERE user_id = {self.user_id}')
            location_data = cursor.fetchone()

            if location_data:
                cursor.execute(
                    f'''UPDATE locations
                    SET country="{self.country}",
                    state="{self.state}",
                    city="{self.city}",
                    district="{self.district}",
                    street="{self.street}"
                    WHERE user_id = {self.user_id};'''
                )
                # self.locationStatus = True
            else:
                cursor.execute(
                f'''INSERT INTO locations (user_id, country, state, city, district, street)
                VALUES("{self.user_id}","{self.country}","{self.state}", "{self.city}", "{self.district}","{self.street}");
                ''')
                
            conn.commit()
            cursor.close()
            return True
        else:
            cursor.close()
            return False
        
    def delete_user(self, conn, password):
        cursor = conn.cursor()
        
        cursor.execute('USE ec_users;')
        cursor.execute(f'''SELECT* FROM logins WHERE password = "{password}" AND user_id = {self.user_id};''')
        exists = cursor.fetchone()
        
        if exists:
            cursor.execute(f'''DELETE FROM logins WHERE user_id={self.user_id};''')
            conn.commit()
            cursor.close()
            return True
        else:
            cursor.close()
            return False
        
    def login_user(self, conn, email: str, user_password: str) -> bool:
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute('USE ec_users;')
        cursor.execute(f'''SELECT * FROM logins WHERE email = "{email}" AND password = "{user_password}";''')
        user_data = cursor.fetchone()
            
        if user_data:
            self.user_id = user_data['user_id']
            self.name = user_data['name']
            self.password = user_data['password']
            self.isAdmin = user_data['admin']
            self.email = user_data['email']
            
            cursor.execute(f'''SELECT * FROM locations WHERE user_id = "{self.user_id}";''')
            location_data = cursor.fetchone()    
            
            if location_data:
                self.country = location_data['country']
                self.state = location_data['state']
                self.city = location_data['city']
                self.district = location_data['district']
                self.street = location_data['street']
                # self.locationStatus = True
                
            cursor.close()
            return True
        else:
            cursor.close()
            return False
        
    def show_basic_info(self):
        return f'Name: {self.name}\nEmail: {self.email}'
    
    def show_location_info(self):
        return f'Country: {self.country}\nState: {self.state}\nCity: {self.city}\nDistrict: {self.district}\nStreet: {self.street}'
    
    def __str__(self):
        return self.show_basic_info()+'\n'+self.show_location_info()
    
class Admin(User):
    
    @staticmethod
    def update_product(conn,pd_name: str, pd_cost:None, pd_quantity:None, pd_id: int):
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute('USE ec_inventory;')
        cursor.execute(f'''SELECT* FROM products WHERE product_id = {pd_id};''')
        product = cursor.fetchone()
        
        if product:
            new_name =  pd_name or product['product_name']
            new_cost = pd_cost or product['cost']
            new_quantity = pd_quantity or product['quantity']
        
            cursor.execute(
                f'''UPDATE products
                SET product_name="{new_name}",
                cost={new_cost},
                quantity={new_quantity}
                WHERE product_id = {pd_id};'''
            )
            conn.commit()
            cursor.close()
            return True
        else:
            cursor.close()
            return False
        
    @staticmethod
    def remove_product(conn, product_id: int):
        cursor = conn.cursor()
        
        cursor.execute("USE ec_inventory;")
        cursor.execute(f'''SELECT* FROM products where product_id = {product_id}''')
        
        product = cursor.fetchone()
        
        if product:
            cursor.execute(f'''DELETE from products where product_id = {product_id}''')
            conn.commit()
            cursor.close()
            return True
        else:
            cursor.close()
            return False
    
    @staticmethod
    def insert_product(conn, prd_name: str, prd_cost: float, prd_quantity: int):
        cursor = conn.cursor()
        
        cursor.execute('USE ec_inventory;')
        
        cursor.execute(
            f'''INSERT INTO products (product_name, cost, quantity)
            VALUES("{prd_name}", {prd_cost}, {prd_quantity});'''
        )
        conn.commit()
        cursor.close()
        
        