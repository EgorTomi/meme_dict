
import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin, random_number_Game, random_number, True_Or_False
from telebot.types import ReactionTypeEmoji
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("")
# Замени 'TOKEN' на токен твоего бота


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Это группвой бот помощник. Напиши команду /help, чтобы узнать больше о моих возможностях.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Привет! Это чат-бот, он, что то типо игрового бота, он может сгенерировать пароль, эмодзи, подбросить монетку, сыграть в игру с угадыванием числа от 1 до 10, создать опрос, задать вопрос магическому шару. Для большей навигации используй: /help_Comm")

@bot.message_handler(commands=['help_Comm'])
def send_help_Comm(message):
    bot.reply_to(message, "Команды бота:\n /hi - Приветствие\n /bye -  Прощание\n /pass - Генерация пароля\n /emodji - Генерация эмодзи\n /coin - Подбросить монетку\n /randomNumber - Сгенерировать случайное число от 1 до 10\n /randomNumberGame - Игра с угадыванием числа от 1 до 10\n /poll - Создать опрос\n /MagicSphere - Задать вопрос магическому шару\n /help_Comm - Помощь по командам бота\n /help - Общая помощь по боту")
    bot.reply_to(message, "О комманде /poll и /MagicSphere, бот сырой и поэтому используй ее в ручную. Пример: /poll | Вам нравятся фильмы?, Помни, что отступ после команды обязателен, но вот разделение ты можешь выбирать сам будь это |, /, -, ! или прочий символ ")
@bot.message_handler(commands=['hi'])
def send_hello(message):
    bot.reply_to(message, "Привет! Рад видеть тебя в нашей группе, как твои дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, {emodji})

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"выпало: {coin}")


@bot.message_handler(commands=['randomNumberGame']) #Не работает 
def send_random_number_Game(message):
    bot.reply_to(message, "Загадай число от 1 до 10")
    if message.text.isdigit():
        Num_Game = random_number()
        if message.text == Num_Game:
            bot.reply_to(message, "Ты угадал!")
        else:
            bot.reply_to(message, f"Ты не угадал, я загадал число {Num_Game}")

@bot.message_handler(commands=['randomNumber'])
def send_random_number(message):
    R_Num = random_number()
    bot.reply_to(message, f"Число: {R_Num}" )
    
@bot.message_handler(commands=['MagicSphere'])
def send_True_Or_False(message):
    T_Or_f = True_Or_False()
    if T_Or_f == 1:
        bot.reply_to(message, "Правда")
    if T_Or_f == 2:
        bot.reply_to(message, "Ложь")
    if T_Or_f == 3:
        bot.reply_to(message, "Возможно")
    if T_Or_f == 4:
        bot.reply_to(message, "Наверное")
    if T_Or_f == 5:
        bot.reply_to(message, "Скорее всего")
    if T_Or_f == 6:
        bot.reply_to(message, "Скорее нет")

    

@bot.message_handler(commands=["poll"])
def create_poll(message):
    bot.send_message(message.chat.id, "Напиши вопрос для опроса, пример: /poll | Вам нравится дождь?")
    answer_options = ["Да", "Нет", "Возможно"]

    bot.send_poll(
        chat_id=message.chat.id,
        question = message.text,
        options=answer_options,
        type="quiz",
        correct_option_id=2,
        is_anonymous=False,
    )


@bot.poll_answer_handler()
def handle_poll(poll):
    # This handler can be used to log User answers and to send next poll
    pass
        
@bot.message_handler(commands=['mem'])
def send_mem(message):
    files_Meme = 'images'
    all_meme = os.listdir(files_Meme)
    random_meme = random.choice(all_meme)  
    with open(f'images/{random_meme}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['Mem_Animals'])
def mem_animals(message):
    Animals_Meme_files = 'Mem_Animals'
    Animals = os.listdir(Animals_Meme_files)
    Rarity = [10, 65, 30, 5]  
    Choise_itom = random.choices(Animals, weights=Rarity, k=1)
    chosen_filename = Choise_itom[0]
    full_path = os.path.join(Animals_Meme_files, chosen_filename)
    with open(full_path, 'rb') as f:
        bot.send_photo(message.chat.id, f)

bot.infinity_polling()
