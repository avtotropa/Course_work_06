from django.core.management import BaseCommand
from django.utils import timezone

from client.models import Client
from mailing.models import Mailing, Message


class Command(BaseCommand):
    """
    Команда для наполнения базы Рассылки, Клиенты, Сообщения
    """

    def handle(self, *args, **options):
        message_list = [
            {'id': 3, 'theme': '!!!2 + 1 = 4!!!',
             'body': 'Четыре товара электроники по цене трех! Не упусти, дружочек.'},
            {'id': 2, 'theme': 'Черная пятница', 'body': 'Все товары в эту пятницу со скидкой до 70 %!!'}
        ]
        message_for_create = []

        for message in message_list:
            message_for_create.append(
                Message(**message)
            )

        Message.objects.bulk_create(message_for_create)

        mailing_list = [
            {'mailing_time': timezone.now(), 'periodicity': 1, 'status': 1, 'massage': Message.objects.get(pk=1)},
            {'mailing_time': timezone.now(), 'periodicity': 2, 'status': 2, 'massage': Message.objects.get(pk=2)},
            {'mailing_time': timezone.now(), 'periodicity': 3, 'status': 1, 'massage': Message.objects.get(pk=1)},
            {'mailing_time': timezone.now(), 'periodicity': 1, 'status': 3, 'massage': Message.objects.get(pk=2)},
            {'mailing_time': timezone.now(), 'periodicity': 2, 'status': 1, 'massage': Message.objects.get(pk=1)},
            {'mailing_time': timezone.now(), 'periodicity': 3, 'status': 3, 'massage': Message.objects.get(pk=2)},
            {'mailing_time': timezone.now(), 'periodicity': 1, 'status': 1, 'massage': Message.objects.get(pk=1)},
            {'mailing_time': timezone.now(), 'periodicity': 1, 'status': 3},
        ]
        mailing_for_create = []

        for mailing in mailing_list:
            mailing_for_create.append(
                Mailing(**mailing)
            )

        Mailing.objects.bulk_create(mailing_for_create)

        client_list = [
            {'first_name': 'Denis', 'last_name': 'Denisov', 'email': 'user1@mail.ru'},
            {'first_name': 'Petr', 'last_name': 'Petrov', 'email': 'user2@mail.ru'},
            {'first_name': 'Andrey', 'last_name': 'Popov', 'email': 'user3@mail.ru'},
            {'first_name': 'Oleg', 'last_name': 'Maslov', 'email': 'user4@mail.ru'},
            {'first_name': 'Anastasia', 'last_name': 'Grekova', 'email': 'user5@mail.ru'},
        ]
        client_for_create = []

        for client in client_list:
            client_for_create.append(
                Client(**client)
            )

        Client.objects.bulk_create(client_for_create)
