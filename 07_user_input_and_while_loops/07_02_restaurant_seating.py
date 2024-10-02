question = input("how many people are eating here today?: ")
question = int(question)
if question > 8:
    print("sorry, you have to wait 15 hours")
else:
    print(f"okay we got a table for {question}")