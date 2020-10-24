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
    # YOUR CODE HERE

    return

# # Part C.
def dict_2_array(contacts):
    # YOUR CODE HERE

    return
