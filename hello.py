import argparse
import logging
# 1.
print("Hello World!, Devops")

# 2.
inName = input("Give me your name! ")
print(f"Hello, {inName}, welcome to devops!")

# 3.
parse = argparse.ArgumentParser()
parse.add_argument('--name', type=str, help='Ten cua ban')
args = parse.parse_args()

greeting = f"My name is {args.name}"
print(greeting)

# 4.
with open ('greeting.txt', 'w', encoding='utf-8') as file:
    file.write(greeting)

# 5.
logging.basicConfig(filename='devops_log.txt', filemode='a', level=logging.INFO, format='%(asctime)s + %(levelname)s')
logging.info(greeting)