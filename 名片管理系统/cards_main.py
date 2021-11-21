while True:
    # TODO(ALEX) 显示功能菜单

    action_str = input("请选择需要执行的操作：")

    print("您选择的是：【%s】" % action_str)

    # 如果输入1，2，3 ，进入功能选择
    if action_str in ["1", "2", "3"]:
        # 新增用户
        if action_str == "1":
            pass
        # 修改用户
        elif action_str == "2":
            pass
        # 删除用户
        else:
            pass
    # 如果输入0，程序退出
    elif action_str == "0":
        print("欢迎再次使用！再见。")
        break
    # 如果输入其他，提示输入错误
    else:
        print("输入错误，请重新输入！！")
