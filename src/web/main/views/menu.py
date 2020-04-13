import exceptions

from django.contrib.auth.models import User, AnonymousUser


def get_menu_context() -> list:
    """Генератор контекста навигационной панели

    :return: Контекст навигационной панели
    :rtype: list
    """
    return [
        {"url_name": "index", "name": "Главная"},
        {"url_name": "time", "name": "Текущее время"},
    ]


def get_user_menu_context(user: User) -> list:
    """Генератор контекста навигационной панели пользователя

    :param user:
    :return:
    """
    if not (isinstance(user, User) or isinstance(user, AnonymousUser)):
        raise exceptions.ArgumentTypeException()
    return [
        {"url": f"profile/{user.id}/", "name": "Профиль"},
        {"url_name": "logout", "name": "Выйти"},
    ] if user.is_authenticated else [
        {"url_name": "registration", "name": "Регистрация"},
        {"url_name": "login", "name": "Войти"},
    ]
