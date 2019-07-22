#显示全部菜单
def show_menu():
    print("1,新增名片")
    print("2,显示全部")
    print("3,查询名片")
    print("")
    print("0,退出程序")

cardList = []
def card_add():

    name_str = input("姓名:")
    phoneNumber_str = input("电话号码:")
    email_str = input("邮箱:")

    cardDict = {"name":name_str,"phoneNumber":phoneNumber_str,"email":email_str}
    cardList.append(cardDict)

    print("您成功添加了一个 %s 用户" % cardDict["name"])

def card_show():

    #TODO（钱昆）显示全部用户
    if len(cardList) == 0:
       print("本系统中还没有名片")
       return
    print("姓名\t电话号码\t邮箱\t")
    print("-" * 50)
    for users in cardList:
        print("%s\t%s\t%s\t" %(users["name"],users["phoneNumber"],users["email"]))

def card_check():

    name = input("请输入您要查找的姓名:")

    count = 0
    for user in cardList:

        if user["name"] == name:
            count += 1
            print("姓名\t电话号码\t邮箱\t")
            print("-" * 50)
            print("%s\t%s\t%s\t" % (user["name"],user["phoneNumber"],user["email"]))

            card_caozuo(user,cardList)

    if count == 0:
        print("您要查找的姓名不存在")

def card_caozuo(user,cardDict):
    print("请选择您要对该人物的操作")
    mune = input("【0】删除 【1】修改 【2】返回")

    if mune in ["0", "1"]:
        if mune == "0":
            u = cardList.pop()
            print("成功删除 %s" % u["name"])
        else:
            name_str = input("姓名:")
            phoneNumber_str = input("电话号码:")
            email_str = input("邮箱:")

            user["name"] = name_str
            user["phoneNumber"] = phoneNumber_str
            user["email"] = email_str
    elif mune == "2":
        return
    else:
        print("请您输入正确的选项")