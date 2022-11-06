from dependency_injector import containers, providers

from order_repository import OrderRepository


class Container(containers.DeclarativeContainer):
    order_repository_provider = providers.Singleton(
        OrderRepository
    )
