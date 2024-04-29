
print ("How may I help you today?")


responses= { "hello" : "Hi there!",
            "i lost my debit card" : "I've ordered a new one for you",
            "i can't get into my account" : "You can reset your password under the Forgot Password section on the login page",
            "my card has been stolen" : "I have cancelled that card and ordered a new one for you",
            "how do i check the funds in my account" : "You may either come into one of our locations or download our banking app",
            "can i speak to a sales representitive" : "Sure let me forward you to a representitive now",
            "how do i transfer funds from my account" : "You will need to use our app for a transfer",
            "how do i open a savings account" : "you will need to talk to an associate. I'll forward you now",
            "how do i open a checking account" : "you will need to talk to an associate. I'll forward you now",
            "is there any suspicios activity on my account" : "you can either check the My Transactions section on the app or I can forward you to an associate",
            "can i talk to an associate" : "I'll forward you now",
            "what is my account balance" : "You can check your available balance by checking the My Balance secton of the app or you can visit one of our locations",
            "can i put my account on hold?" : "Certaintly! I'll take care of it for you",
            "i would like to setup an account for a child" : "You will need to bring your child to one of our locations in order to set that up",
            "what is te annual fee on my credit card" : "The annual fee for all of our cards is $450",
            "how do i cash a check" : "You can cash a check through our app or you can visit one of our locations",
            "what is my withdrawal limit" : "Your withdraw limit is automatically set to $1000 but if you would like to increase it then we can forward you to an associate",
            "What are all of your locations" : "We have several locations all over the US if you would like to find a location feel free to visit our website or give us a search on your smart phone maps",
            "how do i check my credit score" : "You will need to download our app. You can view your score under the MY SCORE section of the app.",
            "why aren't charges going through on my card" : "You maybe have a hold on your card. You can talk to an associate for better assistance.",
            "how do i transfer from your checking account to my savings account" : "You will need to open the transfer section of our app to move funds from your checking account to your savings.",
            "hello" : "Hi there!",
            "hello" : "Hi there!",
            }

response = input("> ")
if response in responses : 
    print (responses[response])
