import discord, asyncio, re
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

usage = '-- Usage --\nAccepts one of the following formats:\n!Remind(Me/All) <amount> <unit> <message>, i.e. !RemindMe 1 day 2 hours din gay\n!Remind(Me/All) <date> <time> <message> i.e. !RemindAll 26/05/17 20:35 din homo'
units = ['seconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'years']
remind_me = '!remindme'
remind_all = '!remindall'

def absolute_format(text):

    args = text.split(' ')

    if len(args) < 2:
        return None

    date = args[0].replace('\\', '/')
    time = args[1]
    isDate = False
    isTime = False
    message = args

    df = date.split('/')
    if len(df) == 1:
        time = date
    if len(df) == 2 and datetime.strptime(date, '%d/%m'):
        isDate = True
        date = date + '/' + str(datetime.today().year)
    elif len(df) == 3:
        if len(df[-1]) == 2:
            date = date[:-2] + str(int(date[-2:]) + 2000)
        if datetime.strptime(date, '%d/%m/%Y'):
            isDate = True

    tf = time.split(':')
    if len(tf) == 2:
        time = time + ':00'
        isTime = True
    elif len(tf) == 3 and datetime.strptime(time, '%H:%M:%S'):
        isTime = True

    if not isDate and not isTime:
        return None

    if isDate:
        full = date
        message = message[1:]
    else:
        today = datetime.today()
        full = str(today.day) + '/' + str(today.month) + '/' + str(today.year) # FIND WAY TO 2 DIGIT YEAR!!!!

    if isTime:
        full += ' ' + time
        message = message[1:]
    else:
        full += ' 00:00:00'

    message = ' '.join(message).strip()
    seconds = (datetime.strptime(full, '%d/%m/%Y %H:%M:%S') - datetime.now()).total_seconds()

    if seconds <= 0:
        return None
    else:
        return {'seconds': seconds, 'message': message}


def relative_format(text):

    pattern = r'^(\d+ (seconds?|minutes?|hours?|days?|weeks?|months?|years?) )+'
    m = re.match(pattern, text)
    if m:
        time = str(m.group()).strip()
        if time == '':
            return None

        msg = (text[len(time):]).strip()

        pattern = r'(\d+ \w+)'
        g = re.findall(pattern, time)

        if g:
            count = len(g)
            delta = relativedelta()

            for i in range(count):
                req = g[i].split(' ')
                if not req[1].endswith('s'):
                    req[1] = req[1] + 's'
                delta += to_relative_delta(int(req[0]), req[1])

            seconds = ((datetime.now() + delta) - (datetime.now())).total_seconds()

            if seconds <= 0:
                return None
            else:
                return {'seconds': seconds, 'message': msg}


def to_relative_delta(amount, unit):
    return {
        'seconds': relativedelta(seconds=+amount),
        'minutes': relativedelta(minutes=+amount),
        'hours': relativedelta(hours=+amount),
        'days': relativedelta(days=+amount),
        'weeks': relativedelta(weeks=+amount),
        'months': relativedelta(months=+amount),
        'years': relativedelta(years=+amount)
    }[unit]


async def remind(client, channel, message, mention, seconds):
    if client:
        message = 'Reminding ' + mention + ' ' + message
        await asyncio.sleep(seconds)
        await client.send_message(destination=channel, content=message)


async def on_message(client, message):

    # getting command arguments
    args = message.content.split(sep=' ')

    # checking command and mention
    if str.lower(args[0]) == remind_me:
        mention = message.author.mention
    elif str.lower(args[0]) == remind_all:
        mention = '@everyone'
    else:
        return

    content = ' '.join(args[1:])

    # formatting data
    data = absolute_format(content)
    if not data:
        data = relative_format(content)

    print(data)

    if data:
        # settings reminder
        await remind(client, message.channel, data['message'], mention, data['seconds'])
    else:
        await client.send_message(message.channel, usage)
