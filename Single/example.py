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
            if user.whatsapp:
                user.send_whatsapp()
            else:
                user.send_sms()
        else:
            user.send_email()
        
    
#correcto-----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum


# ============================================================================
# MODELS
# ============================================================================

@dataclass
class User:
    """Modelo de usuario con validaciones básicas"""
    name: str
    email: str
    phone: Optional[str] = None
    whatsapp: Optional[str] = None
    


class NotificationPriority(Enum):
    """Prioridades para los canales de notificación"""
    WHATSAPP = 1
    SMS = 2
    EMAIL = 3


# ============================================================================
# INTERFACES (Abstracción)
# ============================================================================

class INotificationChannel(ABC):
    """Interfaz para canales de notificación (Open/Closed Principle)"""
    
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        """Envía una notificación y retorna True si fue exitoso"""
        pass
    
    @abstractmethod
    def can_send_to(self, user: User) -> bool:
        """Verifica si puede enviar al usuario"""
        pass
    
    @property
    @abstractmethod
    def priority(self) -> int:
        """Prioridad del canal (menor = mayor prioridad)"""
        pass


class IUserRepository(ABC):
    """Interfaz para repositorio de usuarios"""
    
    @abstractmethod
    def save(self, user: User) -> bool:
        pass
    

# ============================================================================
# IMPLEMENTACIONES DE CANALES (Single Responsibility)
# ============================================================================

class EmailChannel(INotificationChannel):
    """Canal de notificación por Email"""
    
    def send(self, recipient: str, message: str) -> bool:
        print(f"✉️  Enviando email a {recipient}: {message}")
        # Aquí iría la lógica real (SMTP, API, etc.)
        return True
    
    def can_send_to(self, user: User) -> bool:
        return bool(user.email)
    
    @property
    def priority(self) -> int:
        return NotificationPriority.EMAIL.value


class SMSChannel(INotificationChannel):
    """Canal de notificación por SMS"""
    
    def send(self, recipient: str, message: str) -> bool:
        print(f"📱 Enviando SMS a {recipient}: {message}")
        # Aquí iría la integración con proveedor SMS
        return True
    
    def can_send_to(self, user: User) -> bool:
        return bool(user.phone)
    
    @property
    def priority(self) -> int:
        return NotificationPriority.SMS.value


class WhatsAppChannel(INotificationChannel):
    """Canal de notificación por WhatsApp"""
    
    def send(self, recipient: str, message: str) -> bool:
        print(f"💬 Enviando WhatsApp a {recipient}: {message}")
        # Aquí iría la integración con WhatsApp Business API
        return True
    
    def can_send_to(self, user: User) -> bool:
        return bool(user.whatsapp or user.phone)
    
    @property
    def priority(self) -> int:
        return NotificationPriority.WHATSAPP.value


# ============================================================================
# NOTIFICATION SERVICE (Strategy Pattern + Dependency Inversion)
# ============================================================================

class NotificationService:
    """Servicio de notificaciones escalable con múltiples canales"""
    
    def __init__(self, channels: List[INotificationChannel]):
        # Ordenar canales por prioridad
        self.channels = sorted(channels, key=lambda c: c.priority)
    
    def notify(self, user: User, message: str) -> bool:
        """
        Intenta enviar notificación usando canales en orden de prioridad
        Retorna True si al menos un canal fue exitoso
        """
        for channel in self.channels:
            if channel.can_send_to(user):
                recipient = self._get_recipient(user, channel)
                if channel.send(recipient, message):
                    return True
        
        print(f"⚠️  No se pudo notificar a {user.name}")
        return False
    
    def _get_recipient(self, user: User, channel: INotificationChannel) -> str:
        """Obtiene el destinatario apropiado según el canal"""
        if isinstance(channel, EmailChannel):
            return user.email
        elif isinstance(channel, WhatsAppChannel):
            return user.whatsapp or user.phone
        elif isinstance(channel, SMSChannel):
            return user.phone
        return ""


# ============================================================================
# REPOSITORY IMPLEMENTATION
# ============================================================================

class InMemoryUserRepository(IUserRepository):
    """Implementación en memoria del repositorio (puede ser DB, API, etc.)"""
    
    def __init__(self):
        self._users = {}
    
    def save(self, user: User) -> bool:
        print(f"💾 Guardando usuario: {user.name}")
        self._users[user.email] = user
        return True


# ============================================================================
# USE CASE / APPLICATION SERVICE
# ============================================================================

class UserRegistrationService:
    """Servicio de registro de usuarios (Use Case)"""
    
    def __init__(
        self, 
        repository: IUserRepository, 
        notification_service: NotificationService
    ):
        self.repository = repository
        self.notification_service = notification_service
    
    def register(self, user: User) -> bool:
        """
        Registra un usuario y envía notificación de bienvenida
        Retorna True si el registro fue exitoso
        """
        try:

            
            # Guardar usuario
            if not self.repository.save(user):
                return False
            
            # Notificar
            self.notification_service.notify(user, f"¡Bienvenido {user.name}! Gracias por registrarte.")
            
            return True
            
        except Exception as e:
            print(f"❌ Error al registrar usuario: {e}")
            return False


# ============================================================================
# DEPENDENCY INJECTION CONTAINER (Factory Pattern)
# ============================================================================

class ServiceContainer:
    """Contenedor de dependencias para facilitar la inyección"""
    
    @staticmethod
    def create_notification_service() -> NotificationService:
        """Factory para crear el servicio de notificaciones"""
        channels = [
            WhatsAppChannel(),
            SMSChannel(),
            EmailChannel()
        ]
        return NotificationService(channels)
    
    @staticmethod
    def create_user_repository() -> IUserRepository:
        """Factory para crear el repositorio"""
        return InMemoryUserRepository()
    
    @staticmethod
    def create_registration_service() -> UserRegistrationService:
        """Factory para crear el servicio de registro completo"""
        return UserRegistrationService(
            repository=ServiceContainer.create_user_repository(),
            notification_service=ServiceContainer.create_notification_service()
        )



if __name__ == "__main__":
    
    # Crear servicio usando el contenedor de dependencias
    registration_service = ServiceContainer.create_registration_service()
    
    # Registrar usuarios
    for user_data in list_users.values():
        try:
           user = User(**user_data)
           registration_service.register(user)
        except ValueError as ve:
            print(f"❌ Error de validación para {user_data.get('name', 'desconocido')}: {ve}")
