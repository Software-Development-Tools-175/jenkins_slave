import argparse

parser = argparse.ArgumentParser()
parser.add_argument("memberList", nargs="?", type=list, help="the name list to greet")
args = parser.parse_args()

print(args.memberList)

# greeting = ""
# if args.memberList:
#     for item in convertStr:
#         greeting += "Member No. " + item[0] + " " + item[1] + " " + item[2] + " is " + item[3] + " years old. \n"

# print(greeting)
