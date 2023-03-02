import argparse

parser = argparse.ArgumentParser()
parser.add_argument("memberList", help="the name list to greet", type=list)
args = parser.parse_args()

greeting = ""
if args.memberList:
    for item in memberList:
        greeting += "Member No. " + item[0] + " " + item[1] + " " + item[2] + " is " + item[3] + " years old. \n"

print(greeting)
