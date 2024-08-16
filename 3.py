marital_status_dict={
    'John':'married',
    'Alice':'single',
    'Bob':'divorced'
}


def marital_status(name):
    return marital_status_dict.get(name,'unknown')

print(marital_status("alice"))