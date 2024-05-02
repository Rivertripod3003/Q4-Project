import Levenshtein

def similar(str1, str2):
    str1 = str1 + ' ' * (len(str2) - len(str1))
    str2 = str2 + ' ' * (len(str1) - len(str2))
    return sum(1 if i == j else 0
               for i, j in zip(str1, str2)) / float(len(str1))



print ("Hi my name is CLOUD and im your bank's friendly chatbot. How may I help you today?")
print (" ")
print (" ")
 
 
 
print ("Try typing Hello or I can't get into my account type something...")


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
            "what is the name of your bank" : "our bank is called Harout savings bank!",
            "is your bank better than others?" : "Most definitly we are the best!",
            "what benifits do you offer" : "we offer fly miles, car insurance assistance and 20% off all coffee",
            "why am i broke" : "Get yo money up",
            
            
            
            
            }


response = input("> ")
response = response.lower()

    
best_response=" "
best_score=0

for key in responses:
    score=Levenshtein.ratio(key,response)
    if score > best_score: 
        best_score=score
        best_response=responses[key]
        
print(best_response)
        
print( similar("what is your name", "what's your name") )
