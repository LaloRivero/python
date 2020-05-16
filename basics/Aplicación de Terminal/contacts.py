# -*- coding: utf-8 -*-
import csv


class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
            break
        else:
            self._not_found()

    def update(self, name, update_data):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                if update_data == 'name':
                    new_name = str(
                        raw_input('Escribe el nuevo nombre del contacto: '))
                    contact.name = new_name
                elif update_data == 'phone':
                    new_phone = str(
                        raw_input('Escribe el nuevo telefono del contacto: '))
                    contact.phone = new_phone
                elif update_data == 'email':
                    new_email = str(
                        raw_input('Escribe el nuevo email del contacto: '))
                    contact.email = new_email
            break
        else:
            self._not_found()
        self._save()

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * --- * --- *')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Correo: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * --- * --- *')

    def _not_found(self):
        print('**********************')
        print('¡No encontrado!')
        print('**********************')


def run():

    new_contact_book = ContactBook()
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if(idx) == 0:
                continue
            new_contact_book.add(row[0], row[1], row[2])
    while True:
        command = str(raw_input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(raw_input('Escribe el nombre del contacto: '))
            phone = str(raw_input('Escribe el telefono del contacto: '))
            email = str(raw_input('Escribe el email del contacto: '))
            new_contact_book.add(name, phone, email)

        elif command == 'ac':
            name = str(raw_input('Escribe el nombre del contacto: '))
            update_data = str(raw_input('''
            ¿Qué deseas actualizar?

            [n]ombre de contacto
            [t]eléfono de contacto
            [e]mail de contacto
            '''))
            if update_data == 'n':
                new_contact_book.update(name, 'name')
            elif update_data == 't':
                new_contact_book.update(name, 'phone')
            elif update_data == 'e':
                new_contact_book.update(name, 'email')
            else:
                break
        elif command == 'b':
            name = str(raw_input('Escribe el nombre del contacto: '))
            new_contact_book.search(name)

        elif command == 'e':
            name = str(raw_input('Escribe el nombre del contacto: '))
            new_contact_book.delete(name)

        elif command == 'l':
            new_contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('AGENDA PERSONAL')
    run()
