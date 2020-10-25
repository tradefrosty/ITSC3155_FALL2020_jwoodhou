# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.
def array_2_dict(emails, contacts):
    d = {}
    if not emails:
        for x in contacts:
            d[x] = ""
        return d
    d = dict(zip(contacts,emails))
    return d
# # Part B.
def array2d_2_dict(contact_info, contacts):
    d = {}
    info = {}
    title = {'email': '', 'phone': ''}
    if not contact_info:
        for x in contacts:
            d[x] = ""
        return d
    if not contact_info[0]:
        for x in contacts:
            d[x] = ""
        return d

    for x in contacts:
            d[x] = ""
    k = 0
    for key in d:
        j = 0
        title = {'email': '', 'phone': ''}
        for t in title:
            title[t] = contact_info[k][j]
            j += 1
        d[key] = title
        k += 1
    return d

# # Part C.
def dict_2_array(contacts):
    empty = [[], [], []]
    res = not bool(contacts)
    values1 = []
    values2 = []
    numbers = []
    names = []
    emails = []
    if res == True:
        return empty

    for key in contacts:
        names.append(key)

    for value in contacts.values():
        values1.append(value)

    y = 0
    for x in values1:
        for val in values1[y].values():
            values2.append(val)
        y = y + 1
    j = 0
    for x in values2:
        k = j % 2
        if k == 0 :
            emails.append(x)
        else:
            numbers.append(x)
        j = j + 1
    final = [emails, numbers, names]
    return final
