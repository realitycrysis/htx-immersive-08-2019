phonebook_dict = {
    'Alice': '703-444-2241',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

phonebook_dict['Elizabeth']
print(phonebook_dict.get('Elizabeth'))

phonebook_dict.update({'Kareem': '938-489-1234'} )
print(phonebook_dict)

phonebook_dict.pop('Alice')
print(phonebook_dict)

phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)