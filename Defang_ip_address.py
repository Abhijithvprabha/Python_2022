def ip_address(ip_add):
    new_ip_add = ""
    split_add = ip_add.split('.')
    # print(split_add)
    seperator = '[.]'
    new_ip_add = seperator.join(split_add)
    return  new_ip_add


ip = input("Enter the ip address you want to defang? ")

new_ip = ip_address(ip)
print(new_ip)