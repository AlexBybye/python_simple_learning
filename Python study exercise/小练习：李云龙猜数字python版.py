# # 目前是简单版本(不包括多位玩家姓名成绩及其比较排序等)
# import random
# s_num = random.randint(1, 101)
# time = 0
# name = input("please sign in your name")
# while True:
#     g_num = int(input("please input your guessing number"))
#     time += 1
#     if g_num > s_num:
#         if g_num > s_num+10:
#             print("太大啦！老子当年要是有这么多兵，别说平安县城，就是太原也拿下来啦！")
#         else:
#             print("这炮打高了点，和尚你小子挺厉害嘛！")
#     elif g_num < s_num:
#         if g_num < s_num-10:
#             print("太小啦！我说李旅长，你不能这么偏心眼吧！凭什么人家老靳那么多，到我独立团这就连根毛都不剩啦？")
#         else:
#             print("这炮打稍微矮了，嘿哟！老赵你赶紧调高点，别让山本这小子跑了！")
#     elif g_num == s_num:
#         if time <= 7:
#             print("嘿，你他娘的还真是个天才！")
#             if time <= 3:
#                 print(f"升职连长，原因是仅用{time}招就做掉了山本")
#                 break
#             elif time > 3 & time <= 4:
#                 print(f"结局是：{name}升职排长，原因是仅用{time}招就做掉了山本")
#                 break
#             elif time > 4 & time <= 5:
#                 print(f"结局是：{name}升职班长，原因是仅用{time}招做掉了山本")
#                 break
#             elif time > 5 & time <= 7:
#                 print(f"结局是：{name}仍旧是大头兵，原因是仅用{time}招才做掉了山本")
#                 break
#         if time > 7:
#             print("奶奶的，老子要是靠你，全团人都死炕上了")
#             print(f"结局是：{name}战死沙场，原因是用了一六十三招却反被山本拿着他的M3突突了")
#             break
