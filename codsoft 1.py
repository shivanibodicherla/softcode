# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 20:27:37 2023

@author: shiva
"""

import os
import json

# Function to load contacts from a file
def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file)
    return {}

# Function to save contacts to a file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name : ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")

    contacts[name] = {"phone": phone, "email": email, "address": address}

    save_contacts(contacts)
    print(f"\nContact '{name}' added successfully!\n")

# Function to view all contacts
def view_contacts(contacts):
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

# Function to search for a contact
def search_contact(contacts):
    search_term = input("\nEnter the name or phone number to search: ")

    for name, details in contacts.items():
        if search_term in [name, details["phone"]]:
            print(f"\nContact Found:\nName: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n")
            return

    print("\nContact not found!\n")

# Function to update a contact
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")

    if name in contacts:
        print("\nCurrent Contact Details:")
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}, Address: {contacts[name]['address']}")

        contacts.pop(name)
        add_contact(contacts)
        print(f"Contact '{name}' updated successfully!\n")
    else:
        print("\nContact not found!\n")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")

    if name in contacts:
        contacts.pop(name)
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully!\n")
    else:
        print("\nContact not found!\n")

# Main function
def main():
    contacts = load_contacts()

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("\nExiting Contact Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
