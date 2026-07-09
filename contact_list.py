class ContactList:
    def __init__(self, name: str, contacts: list = None)
        self.name = name
        self.contacts = contacts if contacts is not None else []
        self._sort_contacts()
    
    def _sort_contacts(self):
        self.contacts.sort(key=lambda x: x ['name'])
    
    def add_contact(self, new_contact: dict):
        self.contacts.append(new_contact)
        self._sort_contacts()
    
    def remove_contact(self, name: str):
        self.contacts = [c for c in self.contacts if c['name'] != name]
    
    def find_shared_contacts(self, other_contact_list: 'ContactList') -> 'ContactList':
        shared_contacts_list = []
        
        for contact in self.contacts:
            if contact in other_contact_list.contacts:
                shared_contacts_list.append(contact)
        
        return ContactList(f"Shared between {self.name} and {other_contact_list.name}", shared_contacts_list)
    

