

def view_my_own_customers(args):
    print("running permisionn hook check.....")
    print(args)
    if str(args) in ['12','13']:
        print("访问自己创建的用户,允许")
        return True
    else:
        return False