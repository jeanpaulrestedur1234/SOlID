list_users={
    1: {"name": "Juan", "email": "juan@example.com", "phone": "123456789", "whatsapp": True},
    2: {"name": "María", "email": "maria.example.com"},
    3: {"name": "Luis", "email": "luis@example.com", "phone": "987654321"},
}

## incorrecto
class User:
    def __init__(self, name, email, phone=None, whatsapp=False) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.whatsapp = whatsapp

    def save_to_database(self):
        # lógica para guardar el usuario en una base de datos
        print(f"Guardando usuario {self.name} en la base de datos")
        pass

    def send_email(self):
        # lógica para enviar un correo al usuario
        print(f"Enviando correo a {self.email}")
        pass
    def send_sms(self):
        # lógica para enviar un SMS al usuario
        print(f"Enviando SMS a {self.phone}")
        pass
    def send_whatsapp(self):
        # lógica para enviar un WhatsApp al usuario
        print(f"Enviando WhatsApp a {self.phone}")
        pass

if __name__ == "__main__":
    for u in list_users.values():
        user= User(u["name"], u["email"], u.get("phone"))
        
        user.save_to_database()
        if user.phone:
            if u.whatsapp:
                user.send_whatsapp()
            else:
                user.send_sms()
        else:
            user.send_email()
        
    
#correcto-----------------------------------------------------------------------------------

class User:
    def __init__(self, name, email, phone=None) -> None:
        self.name = name
        self.email = email
        self.phone = phone

class UserRepository:
    def save(self, user: User) -> None:
        # lógica para guardar el usuario en la base de datos
        print(f"Guardando usuario {user.name} en la base de datos")
        pass

class EmailService:
    def send_email(self, user: User, message: str) -> None:
        # lógica para enviar un correo
        print(f"Enviando correo a {user.email} con el mensaje: {message}")
        pass
class SMSService:
    def send_sms(self, user: User, message: str) -> None:
        # lógica para enviar un SMS
        print(f"Enviando SMS a {user.phone} con el mensaje: {message}")
        pass
class WhatsappService:
    def send_whatsapp(self, user: User, message: str) -> None:
        # lógica para enviar un WhatsApp
        print(f"Enviando WhatsApp a {user.phone} con el mensaje: {message}")
        pass 
  
class NotificationService:
    def __init__(self, email_service: EmailService, sms_service: SMSService, whatsapp_service: WhatsappService):
        self.email_service = email_service
        self.sms_service = sms_service
        self.whatsapp_service = whatsapp_service

    def notify_user(self, user: User, message: str) -> None:
        if user.phone | user.whatsapp:
           self.whatsapp_service.send_whatsapp(user, message)
           return
        if user.phone:
           self.sms_service.send_sms(user, message)
           return
        self.email_service.send_email(user, message)
#Uso ----------------------------------------------------------------
class UserRegistrationService:
    def __init__(self, repo: UserRepository, notify_service: NotificationService):
        self.repo = repo
        self.notify_service = notify_service

    def register_user(self, user: User) -> None:
        self.repo.save(user)
        self.notify_service.notify_user(user, "Welcome to the platform!")
print("--- Correcto ---")       
if True:   
    users = [User(u["name"], u["email"], u.get("phone")) for u in list_users.values()]    
    for u in users:
        UserRegistrationService(UserRepository(), NotificationService(EmailService(), SMSService(), WhatsappService())).register_user(u)
        
        