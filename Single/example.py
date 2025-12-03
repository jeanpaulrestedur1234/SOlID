## incorrecto
class User:
    def __init__(self, name, email, phone=None) -> None:
        self.name = name
        self.email = email

    def save_to_database(self):
        # lógica para guardar el usuario en una base de datos
        pass

    def send_email(self):
        # lógica para enviar un correo al usuario
        pass
    def send_sms(self):
        # lógica para enviar un SMS al usuario
        pass

if __name__ == "__main__":
    user = User("Carlos Pérez", "carlos@example.com")
    user.save_to_database()
    user.send_email()
    
    users= []
    users.append(user)
    user2 = User("Ana Gómez", "ass")
    users.append(user2)
    for u in users:
        u.save_to_database()
        if u.phone:
            u.send_sms()
        else:
            u.send_email()
        
    
#correcto-----------------------------------------------------------------------------------

class User:
    def __init__(self, name, email, phone=None) -> None:
        self.name = name
        self.email = email
        self.phone = phone

class UserRepository:
    def save(self, user: User) -> None:
        # lógica para guardar el usuario en la base de datos
        pass

class EmailService:
    def send_email(self, user: User, message: str) -> None:
        # lógica para enviar un correo
        pass
class SMSService:
    def send_sms(self, user: User, message: str) -> None:
        # lógica para enviar un SMS
        pass
    
class NotificationService:
    def __init__(self, email_service: EmailService, sms_service: SMSService):
        self.email_service = email_service
        self.sms_service = sms_service

    def notify_user(self, user: User, message: str) -> None:
        if user.phone:
            self.sms_service.send_sms(user, message)
        else:
            self.email_service.send_email(user, message)
#Uso ----------------------------------------------------------------
class UserRegistrationService:
    def __init__(self, repo: UserRepository, email_service: EmailService):
        self.repo = repo
        self.email_service = email_service

    def register_user(self, user: User) -> None:
        self.repo.save(user)
        self.email_service.send_email(user, "Welcome to the platform!")
            
if __name__ == "__main__":
    user = User("Carlos Pérez", "carlos@example.com")
    repo = UserRepository()
    repo.save(user)
    email_service = EmailService()
    email_service.send_email(user, "hello")
    registration = UserRegistrationService(repo, email_service)

    registration.register_user(user)
    
    
    users= []
    
    
    users.append(user)
    user2 = User("Ana Gómez", "ass")
    users.append(user2)
    
    for u in users:
        UserRepository().save(u)
        NotificationService(EmailService(), SMSService()).notify_user(u, "Hello!")      
        UserRegistrationService(UserRepository(), EmailService()).register_user(u)
        
        