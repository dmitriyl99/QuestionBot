from application import telegram_bot
from application.core.models import Test
from application.resources import strings, keyboards
import os


def publish_rating():
    pass


def publish_test(test_id: int):
    test = Test.get_by_id(test_id)
    channel_chat_id = test.quiz.channel.chat_id
    test_message = strings.from_test(test)
    keyboard = keyboards.from_test_options(test.options.all())
    if test.file_path:
        file = open(test.file_path, 'r')
        _, file_ext = os.path.splitext(test.file_path)
        if file_ext in ['.jpg', '.png']:
            telegram_bot.send_photo(channel_chat_id,
                                    file,
                                    caption=test_message,
                                    reply_markup=keyboard, parse_mode='HTML')
        else:
            telegram_bot.send_document(channel_chat_id,
                                       file,
                                       caption=test_message,
                                       reply_markup=keyboard, parse_mode='HTML')
    else:
        telegram_bot.send_message(channel_chat_id, test_message, reply_markup=keyboard, parse_mode='HTML')