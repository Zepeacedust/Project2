from dependency_injector import containers, providers

from order_repository import OrderRepository
from event_sender import EventSender

class Container(containers.DeclarativeContainer):
    order_repository_provider = providers.Singleton(
        OrderRepository
    )
    event_sender_provider = providers.Singleton(
        EventSender
    )
