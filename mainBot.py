spendedForFood = 0
spendedForHobbie = 0
spendedForTransport = 0
spendedForHealth = 0
choosedAction = 'none'


# Test variable
addTo = 0


import telebot
from secureKeyChain import botApiToken


from languageRu import RuAddButtonText, RuRemoveButtonText, RuLookButtonText, RuFoodButtonText, RuHobbieButtonText, RuTransportButtonText, RuHealthButtonText, RuCancelButtonText
from languageEn import EnAddButtonText, EnRemoveButtonText, EnLookButtonText, EnFoodButtonText, EnHobbieButtonText, EnTransportButtonText, EnHealthButtonText, EnCancelButtonText


bot = telebot.TeleBot(botApiToken)
    


ChoosedAddButtonText = EnAddButtonText
ChoosedRemoveButtonText = EnRemoveButtonText
ChoosedLookButtonText = EnLookButtonText
ChoosedFoodButtonText = EnFoodButtonText
ChoosedHobbieButtonText = EnHobbieButtonText
ChoosedTransportButtonText = EnTransportButtonText
ChoosedHealthButtonText = EnHealthButtonText
ChoosedCancelButtonText = EnCancelButtonText







@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hallo. Welcome back", reply_markup=keyboardMain)
    """
@bot.message_handler(commands=['en'])
def changing_languageEnglish(message):
    global ChoosedAddButtonText
    global ChoosedRemoveButtonText
    global ChoosedLookButtonText
    global ChoosedFoodButtonText
    global ChoosedHobbieButtonText
    global ChoosedTransportButtonText
    global ChoosedHealthButtonText
    global ChoosedCancelButtonText


    ChoosedAddButtonText = RuAddButtonText
    ChoosedRemoveButtonText = RuRemoveButtonText
    ChoosedLookButtonText = RuLookButtonText
    ChoosedFoodButtonText = RuFoodButtonText
    ChoosedHobbieButtonText = RuHobbieButtonText
    ChoosedTransportButtonText = RuTransportButtonText
    ChoosedHealthButtonText = RuHealthButtonText
    ChoosedCancelButtonText = RuCancelButtonText
    bot.send_message(message.chat.id, "Keyboard Hidded press /sk to show it", reply_markup=keyboardHidded)
    print('change to English')

@bot.message_handler(commands=['ru'])
def changing_languageRussian(message):
    global ChoosedAddButtonText
    global ChoosedRemoveButtonText
    global ChoosedLookButtonText
    global ChoosedFoodButtonText
    global ChoosedHobbieButtonText
    global ChoosedTransportButtonText
    global ChoosedHealthButtonText
    global ChoosedCancelButtonText


    
    ChoosedAddButtonText = RuAddButtonText
    ChoosedRemoveButtonText = RuRemoveButtonText
    ChoosedLookButtonText = RuLookButtonText
    ChoosedFoodButtonText = RuFoodButtonText
    ChoosedHobbieButtonText = RuHobbieButtonText
    ChoosedTransportButtonText = RuTransportButtonText
    ChoosedHealthButtonText = RuHealthButtonText
    ChoosedCancelButtonText = RuCancelButtonText
    bot.send_message(message.chat.id, "Keyboard Hidded press /sk to show it", reply_markup=keyboardHidded)
    print('change to Russian')
"""



keyboardMain = telebot.types.ReplyKeyboardMarkup()
keyboardMain.row(ChoosedAddButtonText, ChoosedRemoveButtonText, ChoosedLookButtonText)
keyboardMainRu = telebot.types.ReplyKeyboardMarkup()
keyboardMainRu.row(RuAddButtonText, RuRemoveButtonText, RuLookButtonText)


keyboardAdd = telebot.types.ReplyKeyboardMarkup()
keyboardAdd.row(ChoosedFoodButtonText, ChoosedHobbieButtonText, ChoosedTransportButtonText, ChoosedHealthButtonText)
keyboardGoToMain = telebot.types.ReplyKeyboardMarkup()
keyboardGoToMain.row(ChoosedCancelButtonText)
keyboardHidded = telebot.types.ReplyKeyboardRemove()







@bot.message_handler(commands=['check'])
def check_message(message):
    if addTo == 1:
        bot.send_message(message.chat.id, "Changed", reply_markup=keyboardMain)
        print(addTo)
    else:
       bot.send_message(message.chat.id, "dont", reply_markup=keyboardMain) 
       print(addTo)


@bot.message_handler(commands=[ChoosedRemoveButtonText])
def remove_button(message):
    global choosedAction
    choosedAction = "Remove"

    bot.send_message(message.chat.id, "You cannot remove anything", reply_markup=keyboardMain)






@bot.message_handler(content_types=['text'])

def send_text(message):
    global choosedAction
    global moneyAdded
    global spendedForFood
    global spendedForHobbie
    global spendedForTransport
    global spendedForHealth
    global realUserName
    global realUserId
    global realUserFirstName
    if choosedAction == 'none' and message.text == 'Add':
        print('AddButtonWorking')
        bot.send_message(message.chat.id, "How many do you spend? ", reply_markup=keyboardHidded)
        choosedAction = "Add"
    
    elif choosedAction == 'Look' and message.text == "Cancel":
        bot.send_message(message.chat.id, "What do u want?", reply_markup=keyboardMain)
        choosedAction = "none"



    
    elif choosedAction == "Add" and message.text != "": # First stage of adding - Getting summ

        moneyAdded = ''.join(filter(str.isdigit, message.text))
        
        print(moneyAdded)
        choosedAction = "Add2" # Second stage of adding 
        bot.send_message(message.chat.id, "You pay it for?", reply_markup=keyboardAdd)

    elif message.text == ChoosedLookButtonText:
        
        realUserName = message.from_user.username
        realUserId = message.from_user.id
        realUserFirstName = message.from_user.first_name
        totalSpended = int(spendedForHobbie + spendedForFood + spendedForTransport + spendedForHealth)
        print("FirstName: {}, UserName: {}, UserId: {} Showing Look menu. Food: {}, Hobbies: {}, Transport: {}, Health: {}. Its {} in total.".format(realUserFirstName,realUserName,realUserId,spendedForFood,spendedForHobbie,spendedForTransport,spendedForHealth,totalSpended))
        
        choosedAction = "Look"
        bot.send_message(message.chat.id, "You spend: ", reply_markup=keyboardGoToMain)
        bot.send_message(message.chat.id, "{} for Food".format(spendedForFood))
        bot.send_message(message.chat.id, "{} for Hobbies".format(spendedForHobbie))
        bot.send_message(message.chat.id, "{} for Transport".format(spendedForTransport))
        bot.send_message(message.chat.id, "{} for Health".format(spendedForHealth))
         
        bot.send_message(message.chat.id, "Total: {}".format(totalSpended))


    elif message.text == ChoosedFoodButtonText and choosedAction == "Add2":
        print("Category: Food")
        spendedForFood = int(spendedForFood) + int(moneyAdded) # collecting spended for Food
        choosedAction = "none"
        bot.send_message(message.chat.id, "You added {} in Food".format(spendedForFood), reply_markup=keyboardMain)
    
    elif message.text == ChoosedHobbieButtonText and choosedAction == "Add2":
        print("Category: Hobbie")
        spendedForHobbie = int(spendedForHobbie) + int(moneyAdded) # collecting spended for Hobbies
        choosedAction = "none"
        bot.send_message(message.chat.id, "You have added {} in Hobbies".format(spendedForHobbie), reply_markup=keyboardMain)
    
    elif message.text == ChoosedTransportButtonText and choosedAction == "Add2":
        print("Category: Transport")
        spendedForTransport = int(spendedForTransport) + int(moneyAdded) # collecting spended for Transport
        choosedAction = "none"
        bot.send_message(message.chat.id, "You have added {} in Transport".format(spendedForTransport), reply_markup=keyboardMain)
    
    elif message.text == ChoosedHealthButtonText and choosedAction == "Add2":
        print("Category: Health")
        spendedForHealth = int(spendedForHealth) + int(moneyAdded) # collecting spended for Health
        choosedAction = "none"
        bot.send_message(message.chat.id, "You have added {} in Health".format(spendedForHealth), reply_markup=keyboardMain)
    




bot.polling()