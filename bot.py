import asyncio
import logging
import random
import datetime
import pytz
import time
from telegram import Bot
from telegram.ext import Application
from telegram.constants import ParseMode

# Configuração de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='tigrinho_bot.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

# Configurações do bot (substitua com valores reais!)
TOKEN = "7793194764:AAFK_H7H85Y6Lk6APOO80NzL5UyooolDBCo"  # Substitua pelo seu token real
CHANNEL_ID = "-1002267920920"  # Substitua pelo ID real do canal
SIGNAL_INTERVAL = 600  # 10 minutos entre sinais
LINK = "https://lobopg.vip?cid=381&inv_code=796305"
INVITE_CODE = "796305"

WIN_PHRASES = [
    "💰 <b>GANHOU?</b> Mostra pra gente nos comentários!",
    "🤑 <b>Quem tá lucrando?</b> Reage '💎' se ganhou!",
    "🏆 <b>Vitória confirmada?</b> Marca a gente no print!",
    "💬 <b>Deu green?</b> Conta pra gente como foi!"
]

EMOJIS = ["🐅", "🔥", "⚡", "💎", "🎯", "🚀", "💸", "🏦"]


def get_time_and_validity():
    tz = pytz.timezone("America/Sao_Paulo")
    now = datetime.datetime.now(tz)
    current_time = now.strftime("%H:%M")
    validity_time = (now + datetime.timedelta(minutes=6)).strftime("%H:%M")
    return current_time, validity_time

def generate_random_signal():
    normal_spins = random.randint(5, 10)
    turbo_spins = random.randint(3, 8)
    repeat_times = random.randint(1, 3)
    strategies = [
        "Intercalando", "Sequencial", "Turbo Total",
        "Normal Puro", "Padrão Ouro", "Método Tigre", "Estratégia 777"
    ]
    strategy = random.choice(strategies)
    emoji_combo = random.sample(EMOJIS, 3)
    return normal_spins, turbo_spins, repeat_times, strategy, emoji_combo

async def send_hack_signal(application: Application):
    try:
        current_time, validity_time = get_time_and_validity()

        # Fase 1: Processo de hack
        hack_phrases = [
            f"{random.choice(EMOJIS)} <b>Acesso aos servidores do Tigrinho iniciado...</b> {random.choice(EMOJIS)}",
            "🔐 <b>Decodificando algoritmos de vitória...</b>",
            "💻 <b>Conectando à rede de sinais quentes...</b>",
            "🖥️ <b>Injetando códigos de probabilidade...</b>"
        ]
        await application.bot.send_message(
            chat_id=CHANNEL_ID,
            text=random.choice(hack_phrases),
            parse_mode=ParseMode.HTML
        )
        await asyncio.sleep(2)

        # Fase 2: Progresso do hack
        progress_phrases = [
            f"📊 <b>Analisando padrões de vitória... {random.randint(30, 80)}% completo</b>",
            f"⚙️ <b>Ajustando parâmetros... {random.randint(40, 90)}% carregado</b>",
            f"🔍 <b>Localizando entrada ideal... {random.randint(50, 95)}% processado</b>"
        ]
        await application.bot.send_message(
            chat_id=CHANNEL_ID,
            text=random.choice(progress_phrases),
            parse_mode=ParseMode.HTML
        )
        await asyncio.sleep(3)

        # Fase 3: Sinal hackeado
        normal_spins, turbo_spins, repeat_times, strategy, emoji_combo = generate_random_signal()
        signal_message = f"""\
{emoji_combo[0]} <b>SINAL HACKEADO CONFIRMADO!</b> {emoji_combo[1]}
🐅 <b>FORTUNE TIGER - SINAL VIP</b> 🐅
⏰ <b>Horário:</b> {current_time}
⏳ <b>Validade:</b> {validity_time} (CORRE!)
🎯 <b>ESTRATÉGIA {strategy.upper()}</b>
🔹 {normal_spins}x Normal
🔸 {turbo_spins}x Turbo
🔁 <b>Repetir:</b> {repeat_times}x se necessário
💻 <b><a href='{LINK}'>JOGAR AGORA</a></b>
🎟️ <b>CÓDIGO VIP:</b> {INVITE_CODE}
{random.choice(WIN_PHRASES)}
{emoji_combo[2]} <b>Boa sorte, time de tigres!</b> {emoji_combo[0]}
"""
        await application.bot.send_message(
            chat_id=CHANNEL_ID,
            text=signal_message,
            parse_mode=ParseMode.HTML
        )
        logger.info(f"Sinal enviado - Estratégia: {strategy}")

    except Exception as e:
        logger.error(f"Erro ao enviar sinal: {str(e)}")
        await application.bot.send_message(
            chat_id=CHANNEL_ID,
            text="⚠️ <b>Sistema instável...</b> Novo hack em andamento!",
            parse_mode=ParseMode.HTML
        )

async def auto_signal_sender(application: Application):
    while True:
        try:
            await send_hack_signal(application)
            # Variação de 0 a 2 minutos para evitar intervalos fixos
            await asyncio.sleep(SIGNAL_INTERVAL + random.randint(0, 120))
        except Exception as e:
            logger.error(f"Erro no envio automático de sinais: {str(e)}")
            await asyncio.sleep(60)  # Pausa antes de tentar novamente

async def send_welcome_message(application: Application):
    welcome_message = f"""\
🌟 <b>NOVO SISTEMA DE HACK TIGRINHO ATIVADO!</b> 🌟
🐅 Bem-vindos ao <b>canal oficial</b> de sinais hackeados do Fortune Tiger!
🔓 <b>Como funciona:</b>
- Acesso direto aos servidores
- Sinais com alta taxa de acerto
- Atualizações a cada 10 minutos
💎 <b><a href='{LINK}'>LINK VIP</a></b>
🔑 <b>CÓDIGO EXCLUSIVO:</b> {INVITE_CODE}
⚠️ <b>Atenção:</b> Não compartilhe os sinais! Quanto menos gente usando, maior a eficácia!
"""
    await application.bot.send_message(
        chat_id=CHANNEL_ID,
        text=welcome_message,
        parse_mode=ParseMode.HTML
    )

async def send_motivational_messages(application: Application):
    motivational_msgs = [
        "💪 <b>Time de tigres unido nunca será vencido!</b> Bora pra cima!",
        "🚀 <b>Quem tá preparado para a próxima rodada?</b> O sinal vem aí!",
        "💰 <b>Lembrando:</b> Quem segue o método direito sempre lucra!",
        "🎯 <b>Foco nos sinais, disciplina nos ganhos!</b> O lucro é certo!"
    ]
    while True:
        try:
            await asyncio.sleep(random.uniform(1800, 3600))  # 30-60 minutos
            msg = random.choice(motivational_msgs)
            await application.bot.send_message(
                chat_id=CHANNEL_ID,
                text=msg,
                parse_mode=ParseMode.HTML
            )
            logger.info(f"Mensagem motivacional enviada: {msg}")
        except Exception as e:
            logger.error(f"Erro ao enviar mensagem motivacional: {str(e)}")
            await asyncio.sleep(60)  # Pausa antes de tentar novamente

async def main():
    application = Application.builder().token(TOKEN).build()
    await application.initialize()

    try:
        await send_welcome_message(application)
        asyncio.create_task(auto_signal_sender(application))
        asyncio.create_task(send_motivational_messages(application))

        # Mantém o bot rodando até ser interrompido
        while True:
            await asyncio.sleep(3600)  # Dorme por 1 hora para evitar CPU alto

    except asyncio.CancelledError:
        pass
    finally:
        await application.shutdown()

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()