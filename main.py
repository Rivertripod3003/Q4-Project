import Levenshtein

def similar(str1, str2):
    str1 = str1 + ' ' * (len(str2) - len(str1))
    str2 = str2 + ' ' * (len(str1) - len(str2))
    return sum(1 if i == j else 0
               for i, j in zip(str1, str2)) / float(len(str1))


print (" ")
print (" ")
print ("Hi my name is CLOUD and im your bank's friendly chatbot. How may I help you today?")
print (" ")
print (" ")
 
 
 
print ("Try typing {Hello} or {I can't get into my account} type something...")
print (" ")
print (" ")
print ("When you're finished type {done} to close the bot")

responses= { "hello" : "Hi there!",
            "hi" : " Hello there!",
            "what time is it" : "It is 12:03 am",
            "who are you" : "Hi I am your friendly chatbot!",
            "i need help" : "How may I help you?",
            "i can't get into my account" : "No worries I can reset your password for you",
            "what is your name" : "My name is CLOUD!",
            "i lost my debit card" : "I've ordered a new one for you",
            "i lost my credit card" : "I've ordered a new one for you",
            "i can't get into my account" : "You can reset your password under the Forgot Password section on the login page",
            "my card has been stolen" : "I have cancelled that card and ordered a new one for you",
            "how do i check the funds in my account" : "You have $3.49 because you're broke",
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
            "What is the overdraft fee?": "Our overdraft fee is $35 per transaction You can avoid overdraft fees by opting into overdraft protection or ensuring sufficient funds in your accoun",
            "how do i check my credit score" : "You will need to download our app. You can view your score under the MY SCORE section of the app.",
            "why aren't charges going through on my card" : "You maybe have a hold on your card. You can talk to an associate for better assistance.",
            "how do i transfer from your checking account to my savings account" : "You will need to open the transfer section of our app to move funds from your checking account to your savings.",
            "where are the banks atm's" : "You can find any of our atm's at one of our bank locations and throughout large city areas.",
            "who is the bank's owner" : "Our owner is Harout Vinklestein.",
            "what is my apr" : "Your credit apr is 19%",
            "i need a loan for a car" : "Certaintly! You need to visit one of our in person locations to talk to an associate",
            "i need a loan for a bike" : "Certaintly! You need to visit one of our in person locations to talk to an associate",
            "i need a loan for an apartment" : "Certaintly! You need to visit one of our in person locations to talk to an associate",
            "i need a loan for a house" : "Certaintly! You need to visit one of our in person locations to talk to an associate",
            "what is the downpayment for my mortgage" : "To answer that you will need to go to the MY MORTGAGE section of the app",
            "credit" : "Your credit score can be found in the app",
            "credit card" : "To setup or replace a credit card please submit a request for one in our app",
            "debit card" : "To setup or replace a credit card please submit a request for one in our app",
            "i have a question" : "Sure! How may I help you?",
            "may I speak to a manager" : "Certaintly! I'll forward you now!",
            "is there any interest on a child account" : "Only childrens savings accounts earn interest",
            "how old does my child need to be to recieve a debit card" : "We offer debit cards to anyone over the age of 12",
            "how old does my child have to be to open a checking account" : "You can be any age to setup an account as long as you have an ID or birth certificate",
            "how old does my child have to be to open a savings account" : "You can be any age to setup an account as long as you have an ID or birth certificate",
            "how old is your bank" : "We have been around for 150 years!",
            "What should I do if I change my address?": "Please update your address through the profile settings section of our app or by contacting customer service to ensure you receive important account information and correspondence.",
            "are you human" : "No I am a robot!",
            "what is your name" : "My name is CLOUD!",
            "how old are you" : "I am a week old!",
            "what day is it today" : "It's Wednesday",
            "who made you" : "Giorgio is my creator!",
            "what langauges do you speak?" : "I only speak English because Americans are stupid!",
            "what is your mothers name" : "Her name is CLOUDIA",
            "how long does a new card take to ship?" : "A new card takes 2-3 business days to ship",
            "do i have to pay for a new card?" : "Nope A new card is on us!",
            "are you ai" : "No I think AI is scary :(",
            "who is your creator" : "Giorgio is my creator!",
            "someone stole my wallet" : "Oh no. I'll cancel your card for you",
            "Do you offer joint accounts?": "Yes we offer joint accounts for individuals who wish to share ownership of an account You can open a joint account by visiting one of our branches with the co-owner and providing the necessary documentation.",
            "what is the name of your bank" : "our bank is called Harout savings bank!",
            "is your bank better than others?" : "Most definitly we are the best!",
            "what benifits do you offer" : "we offer fly miles, car insurance assistance and 20% off all coffee",
            "why am i broke" : "Get yo money up",
            "will harout present today" : "Hmmmmm I doubt it",
            "do you have a mobile app" : "Yes you can download our app from the store",
            "where are your bank branches" : "You can find all of our locations on Google maps",
            "can i use an atm for free" : "Yes you may use anyone of our atm's anytime for free",
            "ive lost my account number can you help me" : "Sure you can reset your account number in our app!",
            "what is this" : "A chatbot",
            "how are you" : "Good how are you?",
            "how can i withdraw money from my account" : "You can withdraw money through one of our atm's",
            "what do you think about ai" : "Ai is terrifying and it might destroy the world",
            "credit score" : "Your credit score is 600",
            "do you like harout" : "Not really",
            "fine thank you" : "Nice",
            "who is harout" : "A strong little man",
            "what is a chatbot" : "I am a chatbot and I'm here to answer all of your questions",
            "who is mr williams" : "He is our great teacher who will give me a good grade on this project",
            "is there a fee for using non-network ATMs?": "Yes, there may be fees for using non-network ATMs You can fid information about ATM fees in our fee schedule or by contacting customer service",
            "do my saving earn interest" : "Yes all of your savings will gradually earn interest over time",
            "what are your business hours" : "We are open from 7am - 7pm",
            "how do I apply for a loan" : "You can start your loan application process online through our website or visit one of our branches for assistance",
            "whats your favorite color" : "My favorite color is blue",
            "wheres my money" : "In your account!                                                                      idiot",
            "sup" : "Wussup",
            "whats the weather" : "It's sunny outside",
            "can I schedule an appointment with a financial advisor?": "Certainly! You can schedule an appointment with a financial advisor through our app or by contacting customer service.",
            "are you enviromentally freindly" : "Somewhat",
            "How do I set up automatic bill payments?": "You can set up automatic bill payments through our app or online banking portal by linking your bills to your account.",
            "how do i know if someone is scamming me " : "Whatch out for fraudulent addresses that might have misspelled names. Remember we will never ask for your password",
            "what happens of i miss a credit card bill" : "under those circumstances your credit will increase",
            "is there a withdraw minimum" : "yes we have a withdraw misimum of $5",
            "help theres a weird charge on my card" : "OH no I'll cancel that card for you and send you a new one",
            "are you spying on me" : "No I would never",
            "what should I do if I receive a suspicious email or text claiming to be from the bank?": "If you receive a suspicious email or text, do not click onany links or provide any personal information. Forward the message to our security team on our app",
            "how do I update my account beneficiaries?": "You can update your account beneficiaries by filling out a beneficiary designatio form available on our website or a any of our branche",
            "can you do my homework for me" : "No",
            "what should I do if I suspect identity theft?": "If you suspect identity thef, immediately place a fraud alert on your credit reports and contact our fraud department for assistance in securing your accounts",
            "can I access my account from overseas?": "Yes, you can access your account from overseas through our online banking portal or by calling our international customer service number",
            "what music do you like" : "Not Travis Scott because Harout likes it",
            "how do I close my account?": "You can close your account by visiting one of our branches and completing an acount closure form or by contacting cutomer service for assistance",
            "how old are you" : "I'm almost 2 months old",
            "whats your favorite food" : "I love burgers",
            "can you do my computer science project" : "Nope",
            "how do I dispute a transaction on my account?": "You can dispute a transaction by contacting our customer service department nd providing details of the disputed transaction We will investigate the matter and work to resolve it promptly.",
            "can I order checks for my account?": "Yes, you can order checks for your account through our app or by contacting customer service There may be a fee associated with ordering checks",
            "how do I enroll in paperless statements?": "You can enroll in paperless statements through the settings section of our app or by contacting customer service. Paperless statements are convenient, secure, and environmentally friendly.",
            "yo" : "Wussup",
            "where are you from" : "I'm from the BHS CS lab",
            "Where is your bank located" : "We have multiple locations all over the US",
            "can i get a 401k" : "Sure! to setup a 401k you need to visit one of our branches",
            "i need help with my account" : "Sure what do you need help with?",
            "I need a loan" : "Sure how much do you need?",
            "is my account on hold" : "No your account is fully active",
            
            
            
            


            
            
            
            }

while True:
    response = input("> ")
    response = response.lower()
    
    if response=="done":
        print("Thanks! What would you rate our service on a scale of 1-5?")
        break

    
        
    best_response=" "
    best_score=0
    
    for key in responses:
        score=Levenshtein.ratio(key,response)
        if score > best_score: 
            best_score=score
            best_response=responses[key]
    
    if best_score<.3:
        print("Sorry I don't quite understand what you're asking me")
    
    else: print(best_response)
userinput=input()   
if userinput=="1":
    print("Thanks for your feedback! We're sorry to hear that. We are constantly updating and improving")
    
if userinput=="2":
    print("Sorry to hear that we hope your experience will be better next time")
    
if userinput=="3":
    print("Thanks for your feedback! We're constantly improving!")

if userinput=="4":
    print("Great! We're glad that we were able to give you a satisfactory experience")

if userinput=="5":
    print("Thanks for your feedback! ")
