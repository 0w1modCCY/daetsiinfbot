from telegram.ext import Updater, CommandHandler, ConversationHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def start(update, context):
    IG = InlineKeyboardButton(text='Instagram', url='https://instagram.com/daetsiinf?igshid=izw8yg1qzpq3')
    TW = InlineKeyboardButton(text='Twitter', url='https://twitter.com/daetsiinf?s=20')
    WA = InlineKeyboardButton(text='WhatApp +34 910 67 27 19')
    #CE = InlineKeyboardButton(text='Correo electronico', url='comunicacion.da@fi.upm.es')

    update.message.reply_text(text='😀 Hola. ¡Bienvenido al bot oficial de Telegram de la Delegación de Alumnos de la E.T.S. Ingenieros Informáticos!\n\nAverigua la lista de cosas que puedo hacer por ti ejecutando /help.\n\nEn caso de no resolver tu duda, nuestro equipo de comunicación estará encantado de ayudarte por nuestros medios de comunicación.\n\nDime. ¿en qué te puedo ayudar?',
                              reply_markup=InlineKeyboardMarkup([
                                    [IG],
                                    [TW],
                                    [WA],

                                ])
                              )

def help(update, context):
    update.message.reply_text('Lista de comandos disponibles:\n\n🏁 /start\nBienvenida y redes sociales\n\n💬 /help\nComandos disponibles\n\n💰 /ayudas\nAlumnos con problemas economicos\n\n💻 /tryit\nEvento celebrado en la escuela\n\n👨‍🎓 /becas\nBecas ETSIINF, UPM y Comunidad de Madrid\n\n🧾 /reservas\nPuestos de biblioteca\n\n📄 /guias\nGuias de aprendizaje\n\n📚 /taquillas\nReserva y disponibilidad\n\n🧮 /prestamos\nMaterial de delegacion\n\n🎎 /mentor\nProyecto Mentor\n\n🆘 /incidencias\nSistema MANTIS\n\n📝 /evalua\nSistema EVALUA\n\n🦠 /covid19\nInformación y mapa')

def ayudas(update, context):
    update.message.reply_text('💰 ¿Tienes problemas económicos?\n\nDesde Delegación de Alumnos somos conscientes que muchos alumnos pueden tener determinados problemas económicos por distintas situacion, por ello, dedicamos una parte de nuestro presupuesto anual para ofrecer distintos tipos de ayudas.\n\n🧾 ¿Qué tipo de ayudas ofrecemos?\n\nHemos ofrecido Ayudas para Comedor y Ayudas para Transporte Público. Según la situación, intentaremos ofrecer ayudas para ayudaros todo lo que podamos, ya que esa es nuestra misión.\n\n🔓 ¿Qué ayudas hay actualmente abiertas?\n\nActualmente puedes solicitar la Ayuda para Transporte Público.\nLa fecha de apertura de solicitudes es el 19 de Junio de 2021 hasta el 25 de Junio de 2021 a las 23:59h.\nEjecute /basesTransportes para leer las normas y requisitos para solicitar esta ayuda.\n\nMás información en https://da.etsiinf.upm.es/ayudas\n\nRecuerda que estamos deseando ayudarte por cualquier de nuestros medios de comunicación.')

def tryit(update, context):
    update.message.reply_text(' ')

def becas(update, context):
    update.message.reply_text(' ')

def reservas(update, context):
    update.message.reply_text(' ')

def guias(update, context):
    update.message.reply_text(' ')

def taquillas(update, context):
    update.message.reply_text('Quedan 10 taquillas disponibles')

def prestamos(update, context):
    update.message.reply_text(' ')

def mentor(update, context):
    update.message.reply_text(' ')

def tryit(update, context):
    update.message.reply_text(' ')

def incidencias(update, context):
    update.message.reply_text(' ')

def evalua(update, context):
    update.message.reply_text(' ')

def covid19(update, context):
    update.message.reply_text(' ')


if __name__ == '__main__':
    updater = Updater(token='1743403372:AAHH6ed_toDBoPCWWabvmQOwbfMk2E2uI3Y', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('ayudas', ayudas))
    dp.add_handler(CommandHandler('tryit', tryit))
    dp.add_handler(CommandHandler('becas', becas))
    dp.add_handler(CommandHandler('reservas', reservas))
    dp.add_handler(CommandHandler('guias', guias))
    dp.add_handler(CommandHandler('taquillas', taquillas))
    dp.add_handler(CommandHandler('prestamos', prestamos))
    dp.add_handler(CommandHandler('mentor', mentor))
    dp.add_handler(CommandHandler('incidencias', incidencias))
    dp.add_handler(CommandHandler('evalua', evalua))
    dp.add_handler(CommandHandler('covid19', covid19))

    updater.start_polling()
    updater.idle()
