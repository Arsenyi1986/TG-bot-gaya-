import random
import parser_module_ar
from parser_module_ar import parse_money, parse_money_b
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5912553276:AAHKCbp6bLfgjDiu453JfJ6jQGJno3I3ITo'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
parser_module_ar.chrome_in()


@dp.message_handler(commands=['start'])
async def beg(message: types.Message):
    user_name = message.from_user.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    butt = types.KeyboardButton("Привет!")
    markup.add(butt)
    await message.reply("Привет, " + user_name + "!\n"
                        "Меня зовут Арбот!\n"
                        "Я умею много разных штук, а ещё меня добавят в портфолио.!\n"
                        "Чтобы перейти к моим оснвным функциям - напиши привет!",
                        reply_markup=markup)


@dp.message_handler(content_types=['text'])
async def get_txt_msg(msg: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if msg.text.lower() == 'узнать курс валют!':
        back = types.KeyboardButton("Назад")
        birzh = types.KeyboardButton("Давай")
        markup.add(back, birzh)
        await msg.answer("Вот информация о курсах валют с сайта Центробанка России!")
        await msg.reply(parse_money())
        await msg.answer("Может ещё глянем на биржевой курс?", reply_markup=markup)
        await msg.answer_photo("https://sun9-26.userapi.com/impg/MU1F2niinxw4l3iP2nqGZP32bj_fYc0-x4iKDw/ki0nrJygIOM.jpg?size=1280x720&quality=95&sign=613277fa5294199a1c8c51bb0e990c0e&c_uniq_tag=an85y8aKsDlOFrnbhnPlCaQGZp1dOviMWTMw0L_w3X0&type=album")
    elif msg.text.lower() == "обо мне)":
        back = types.KeyboardButton("Назад")
        markup.add(back)
        await msg.answer("Меня зовут Арбот. Мой создатель - молодой программист,\n"
                         "набирающий себе работы для портфолио. Я умею присылать вам\n"
                         "разные картиночки и стикеры, а ещё я могу взять актуальную\n"
                         "информацию о курсе валют прямиком с сайта ЦБР и РБК.\n"
                         "Я написан с использованием языка Python, на библиотеке aiogram.\n"
                         "Для использования функций парсинга, я использую Selenium.", reply_markup=markup)
    elif msg.text.lower() == 'привет!' or msg.text.lower() == 'привет' or msg.text.lower() == 'назад' or msg.text.lower() == 'к меню':
        b1 = types.KeyboardButton("Узнать курс валют!")
        b2 = types.KeyboardButton("Обо мне)")
        b3 = types.KeyboardButton("Разные разности")
        markup.add(b1, b2, b3)
        await msg.answer("Добро пожаловать в основное меню!\n"
                         "Отсюда вы сможете воспользоваться моими функциями,\n"
                         "а так же узнать немного больше обо мне.", reply_markup=markup)
    elif msg.text.lower() == "разные разности":
        stk = types.KeyboardButton("Стикеры")
        img = types.KeyboardButton("Картинки")
        back = types.KeyboardButton("Назад")
        markup.add(stk, img, back)
        await msg.answer("Какого типа разности вас интересуют?", reply_markup=markup)
    elif msg.text.lower() == "стикеры":
        sticker_list = ["CAACAgIAAxkBAAEInTZkPRs_3Tfuxd9HbMILr7O5TQnZnQAC-QADMNSdEV9oXriavOrNLwQ",
                        "CAACAgIAAxkBAAEInUBkPR1Q0dFvhaIimfLt3emvWEhvpwACGBQAAnl0yUs1azQBhBNYei8E",
                        "CAACAgIAAxkBAAEInUJkPR1oP6jPsknSI__btgIR_2AnsQACTCQAAt21aUvCnrO-C8Dk9y8E",
                        "CAACAgIAAxkBAAEInURkPR17K8HG3JdrcSBnxk8FTjNccgACCAADwDZPE29sJgveGptpLwQ",
                        "CAACAgIAAxkBAAEInUtkPR8tz9LXRD9Q_a2GXT9GUNAZdwACyQMAAn60IAWem6hxRk_zCS8E",
                        "CAACAgUAAxkBAAEInU1kPR9HDIIT_Qo12NzXqlE-oTVhiwAC-gADR5XbAWtSgBKOL_fFLwQ",
                        "CAACAgIAAxkBAAEInU9kPR9eA4raFOKqx4F6eZdIxvTIDwACUhwAAliV-UnDh_kItuXmvC8E",
                        "CAACAgQAAxkBAAEInVFkPR93L70_fBZaAsPZuYJYZsJZNwACfQMAAuJy2QABdqWPKQVZFjAvBA"]
        sticker = random.choice(sticker_list)
        await msg.answer_sticker(sticker)
    elif msg.text.lower() == "картинки":
        img_list = ["https://indonesiaexpat.id/wp-content/uploads/2016/10/image-004-2.jpg",
                    "https://sun3-13.userapi.com/_a394bIithuKY9cHnthLHGFVMETZpXdniO4smg/YeunPVjs3QU.jpg",
                    "https://pbs.twimg.com/media/EPkqZdkWoAAN1SU?format=jpg&name=medium",
                    "https://pics.awwmemes.com/you-made-this-made-this-some-list-sort-some-list-sort-65108485.png",
                    "https://cs12.pikabu.ru/post_img/2021/04/29/5/1619679232190012552.webp",
                    "https://camo.githubusercontent.com/6891147dc023b817471b0ba0acb0f4eff0f9628a05741ebb88ed55c379b236f9/687474703a2f2f696d61676573372e6d656d6564726f69642e636f6d2f696d616765732f55504c4f414445443937332f353936653463393636353065352e6a706567",
                    "https://img2.joyreactor.cc/pics/post/it-%D1%8E%D0%BC%D0%BE%D1%80-geek-5169598.jpeg",
                    "https://ptolmachev.ru/wp-content/uploads/2019/12/%D0%A3%D1%87%D1%83%D1%81%D1%8C-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D0%BD%D0%B0-%D0%BF%D0%B8%D1%82%D0%BE%D0%BD%D0%B5.png",
                    "https://memestatic.fjcdn.com/pictures/Low+paltry+bad+snail_f1b921_8112109.jpg",
                    "https://i.pinimg.com/originals/e7/8c/ba/e78cbab15705f78c52e2c1bed1b977fd.jpg",
                    "https://i.pinimg.com/736x/78/cb/fc/78cbfc3917d9bf65e65d46f84128a2e1.jpg"]
        image = random.choice(img_list)
        await msg.answer_photo(image)
    elif msg.text.lower() == "давай":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Назад")
        markup.add(back)
        await msg.answer("Подождите немного. Запрос к РБК может занять какое-то время...")
        await msg.answer(parse_money_b(), reply_markup=markup)
    else:
        menu_b = types.KeyboardButton("К меню")
        await msg.answer("Я не понял вас.\n"
                         "Если у вас трудности с вводом - вы можете воспользоваться кнопками)")

        
def chrome_in():
    s = Service(ChromeDriverManager().install())

def parse_money():
    driver = webdriver.Chrome(s)
    result = ''
    driver.get("https://cbr.ru/")
    listik = ''
    listik += driver.find_element(By.XPATH,
                                  "//*[@id=\"content\"]/div/div/div/div[1]/div[2]/div/div[5]/div/div[2]/div[2]").text + "\n"
    listik += driver.find_element(By.XPATH,
                                  "//*[@id=\"content\"]/div/div/div/div[1]/div[2]/div/div[5]/div/div[2]/div[3]").text + "\n"
    listik += driver.find_element(By.XPATH,
                                  "//*[@id=\"content\"]/div/div/div/div[1]/div[2]/div/div[5]/div/div[3]/div[2]").text + "\n"
    listik += driver.find_element(By.XPATH,
                                  "//*[@id=\"content\"]/div/div/div/div[1]/div[2]/div/div[5]/div/div[3]/div[3]").text + "\n"
    listik += driver.find_element(By.XPATH,
                                  "//*[@id=\"content\"]/div/div/div/div[1]/div[2]/div/div[5]/div/div[4]/div[2]").text + "\n"
    listik += driver.find_element(By.XPATH,
                                  "//*[@id=\"content\"]/div/div/div/div[1]/div[2]/div/div[5]/div/div[4]/div[3]").text + "\n"

    listik = listik.split('\n')
    result = "Доллар:\n" \
             "Вчера: " + listik[0] + "\n" \
             "Сегодня: " + listik[1] + "\n" \
             "Евро:\n" \
             "Вчера: " + listik[2] + "\n" \
             "Сегодня: " + listik[3] + "\n" \
             "Юань:\n" \
             "Вчера: " + listik[4] + "\n" \
             "Сегодня: " + listik[5] + "\n" \

    driver.close()
    return result


def parse_money_b():
    driver = webdriver.Chrome(s)
    t_res = ''
    res = ''
    driver.get("https://www.rbc.ru/")
    info = driver.find_elements(By.CLASS_NAME, "key-indicators__diff")
    info = info[:6]
    for el in info:
        el = el.text
        res += el + ' '
    res = res.strip()
    res = res.split(' ')
    curr = res[::2]
    grow = res[1::2]
    t_res = "Доллар: " + curr[0] + " (" + grow[0] + ")\n" \
            "Евро: " + curr[1] + " (" + grow[1] + ")\n" \
            "Юани: " + curr[2] + " (" + grow[2] + ")"
    driver.close()
    return t_res

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
