import card_tools

'''
名片管理系统，
1，新增名片
2，显示全部
3，查找名片
   3.1，修改名片
   3.2，删除名片

'''
while True:
    print("*" * 50)
    print("欢迎使用 【名片管理系统】v1.0")
    card_tools.show_menu()
    print("*" * 50)

    button = input("请选择菜单：")
    print("您选择的菜单是【%s】" % button)

    if button in ["1","2","3"]:
        if button == "1":
           card_tools.card_add()
        if button == "2":
           card_tools.card_show()
        if button == "3":
           card_tools.card_check()
    elif button == "0":
        print("您退出了程序，欢迎再次使用")
        break
    else:
        print("请您输入正确的选择")

