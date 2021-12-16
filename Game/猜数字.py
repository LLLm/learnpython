print("欢迎游玩猜数字游戏！")
print("我在1-20之间选中了三个数字，你需要猜中其中一个数字\n如果你猜对了会有奖励，否则就会有惩罚！")
yi=int(input("请输数字"))
if yi == 1 or yi == 18 or yi == 4:
    print("恭喜你！猜中了！\n奖励你一个\n“奖励”")
else:
    print("你猜错啦！没关系，还有两次机会！")
print
er=int(input("请输入数字"))
if er == 1 or er == 18 or er == 4:
    print("恭喜你！猜中了！\n奖励你一个\“奖励”")
else:
     print("你猜错啦！没关系，还有一次机会！")
san=int(input("请输入数字"))
if san == 1 or yi == 18 or yi == 4:
    print("恭喜你！猜中了！\n奖励你一个\“奖励”")
else:
    print("你猜错啦！接受惩罚吧！")
    print("你已经遭受了惩罚了，游玩这个游戏浪费了你宝贵的生命（O v O）")