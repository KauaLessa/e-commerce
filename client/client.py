'''from .models import Logins
from .models import Locations
from products.models import Products
from django.core.exceptions import ValidationError
from decimal import Decimal
from decimal import getcontext

class User():
    
    isAdmin = False
    
    def __init__(self, user_id: int = None, name: str = None, email:str = None, password:str = None):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.email = email
        self.country = None
        self.state = None
        self.city = None
        self.district = None
        self.street = None
        
    @staticmethod    
    def sign_in(myEmail: str, myPassword: str):
        try:
            # Autenticação de login e senha
            userData = Logins.objects.get(email=myEmail, password=myPassword)
        except Logins.DoesNotExist as e:
            print(e)
            return None
        try:
            # Verifica se existem informações de localização
            location = Locations.objects.get(user=userData.user_id)
        except Locations.DoesNotExist:
             # Se nao existir, crie um usuario sem localização
            return User(userData.user_id,userData.name,userData.email,userData.password)
        else:
            # Se existir, crie um usuário e atribua a localização
            myUser = User(userData.user_id,userData.name,userData.email,userData.password)
            myUser.country = location.country
            myUser.state = location.state
            myUser.city = location.city
            myUser.district = location.district
            myUser.street = location.street
            return myUser
            
    def insert_login(self) -> bool:
        # confere
        if Logins.objects.filter(email=self.email):
            return False
        
        Logins.objects.create(name=self.name, email=self.email,password=self.password,admin=False)
        return True
    
    def update_login(self,new_name=None, new_password=None, new_email=None):
        try:
            # Se o login não existir, levantamos uma exceção
            login = Logins.objects.get(user_id=self.user_id)
        except Logins.DoesNotExist as e:
            print(e)
            raise
        if Logins.objects.filter(email=new_email):
            return False
        else:
            #Primeiro redefinimos os campos da instancia
            login.name = self.name = new_name or self.name
            login.password = self.password = new_password or self.password
            login.email = self.email = new_email or self.email
            login.save()
            return True
        
    def insert_location(self, inCountry: str, inState: str, inCity: str, inDistrict: str, inStreet: str):
        # confere
        u = Logins.objects.get(user_id=self.user_id)
        if Locations.objects.filter(user=u):
            return False
        
        # Primeiro insiro a localização no banco de dados
        Locations.objects.create(user=u, country=inCountry, state=inState, city=inCity, district=inDistrict, street=inStreet)
        
        # Agora atualizo os campos da instância
        self.country= inCountry
        self.city = inCity
        self.state = inState
        self.district = inDistrict
        self.street = inStreet
        return True
            
    def update_location(self, new_country=None, new_state=None, new_city=None, new_district=None, new_street=None):
        try:
            # Se a localização não existir, levantamos uma exceção
            u = Logins.objects.get(user_id=self.user_id)
            location = Locations.objects.get(user=u)
        except Locations.DoesNotExist as e:
            print(e)
            raise
        else:
            # Atualiza a instância caso o argumento seja fornecido
            location.country = self.country = new_country or self.country
            location.state = self.state = new_state or self.state
            location.city = self.city = new_city or self.city
            location.district = self.district = new_district or self.district
            location.street = self.street = new_street or self.street
            location.save()
            
    def show_location(self) -> str:
        return f'Country: {self.country}\nState: {self.state}\nCity: {self.city}\nDistrict: {self.district}\nStreet: {self.street}'
    
    def __str__(self):
        return f'Name: {self.name}\nEmail: {self.email}\nPassword: {self.password}'

class Admin(User):
    
    isAdmin = True
    
    @staticmethod
    def sign_in(myEmail: str, myPassword: str):
        try:
            # Autenticação de login e senha
            userData = Logins.objects.get(email=myEmail, password=myPassword)
        except Logins.DoesNotExist as e:
            print(e)
            return None
        if not userData.admin:
            return None
        try:
            # Verifica se existem informações de localização
            location = Locations.objects.get(user=userData.user_id)
        except Locations.DoesNotExist:
            # Se nao existir, crie um usuario sem localização
            return Admin(userData.user_id,userData.name,userData.email,userData.password)
        else:
            # Se existir, crie um usuário e atribua a localização
            myUser = Admin(userData.user_id,userData.name,userData.email,userData.password)
            myUser.country = location.country
            myUser.state = location.state
            myUser.city = location.city
            myUser.district = location.district
            myUser.street = location.street
            return myUser      
    
    @staticmethod
    def insert_product(pd_name:str, pd_cost:float, pd_quantity:int):
        Products.objects.create(product_name=pd_name, cost=pd_cost, quantity=pd_quantity)
    
    def update_product(self, pd_id: int, new_name = None, new_cost = None, new_stock = None):
        product = Products.objects.get(product_id=pd_id)
        
        product.product_name = new_name or product.product_name
        product.cost = new_cost or product.cost
        product.quantity = new_stock or product.quantity
        product.save()
                
    def delete_product(self, pd_id: int):
        Products.objects.get(product_id=pd_id).delete()
        
    @staticmethod
    def set_discount(id: int, discount: float):
        # Obtenha o produto
        pd = Products.objects.get(product_id=id)
        
        # Configuração de precisão decimal
        getcontext().prec = 4
        discount = Decimal(discount)  # Converta o desconto para Decimal
        _1 = Decimal(1)
        
        if pd.discount is not None:  
            # Se já existe um desconto, combine com o novo desconto
            pd.discount = _1 - ((_1 - pd.discount) * (_1 - discount))
        else:
            # Caso contrário, defina o desconto diretamente
            pd.discount = discount
        
        try:
            pd.full_clean()
        except ValidationError as e:
            print(e.message_dict)
            return False
        else:
            pd.cost = pd.cost * (_1 - pd.discount)
            pd.save()
            return True
        
    @staticmethod
    def full_price(id: int):
        pd = Products.objects.get(product_id=id)
        
        getcontext().prec = 4
        
        if pd.discount == None:
            return False
        
        pd.cost = pd.cost/(Decimal(1) - pd.discount)
        pd.discount = None
        pd.save()
        return True
'''