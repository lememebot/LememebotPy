import discord, asyncio, re, logging
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

usage = '-- Usage --\nAccepts one of the following formats:\n!Remind(Me/All) <amount> <unit> <message>, i.e. !RemindMe 1 day 2 hours din gay\n!Remind(Me/All) <date> <time> <message> i.e. !RemindAll 26/05/17 20:35 din homo'
units = ['seconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'years']
remind_me = '!remindme'
remind_all = '!remindall'

'''
    check if the request is formatted as absolute time
    and return the formatted data as a dictionary
    of 'message' and 'seconds'
'''
def absolute_format(text):

    # TODO: change this whole shit to regex when you get the time

    args = text.split(' ')

    # validate
    if len(args) < 2:
        return None

    # initialize
    date = args[0].replace('\\', '/')
    time = args[1]
    isDate = False
    isTime = False
    message = args

    # calculations cba to explain just ask me or read it yourself
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

    # whew okie done with the calcs that was tuff xd jk im way past this and im just here to document but cba to reatd this shit lmao

    message = ' '.join(message).strip()
    seconds = (datetime.strptime(full, '%d/%m/%Y %H:%M:%S') - datetime.now()).total_seconds()

    if seconds <= 0:
        return None
    else:
        return {'seconds': seconds, 'message': message}

'''
    check if the request is formatted as relative time
    and return the formatted data as a dictionary
    of 'message' and 'seconds'
'''
def relative_format(text):

    # set regex to capture the time request
    pattern = r'^(\d+ (seconds?|minutes?|hours?|days?|weeks?|months?|years?) )+'
    m = re.match(pattern, text)
    if m:
        # extract time request
        time = str(m.group()).strip()
        if time == '':
            return None

        # extract message
        msg = (text[len(time):]).strip()

        # set regex to capture each group
        pattern = r'(\d+ \w+)'
        g = re.findall(pattern, time)

        if g:
            count = len(g)
            delta = relativedelta()

            # for each group, add the requested time to a relativedelta
            for i in range(count):
                req = g[i].split(' ')
                if not req[1].endswith('s'):
                    req[1] = req[1] + 's'
                delta += to_relative_delta(int(req[0]), req[1])

            # get total number of seconds to wait before reminding
            seconds = ((datetime.now() + delta) - (datetime.now())).total_seconds()

            # cancel if the reminder date passed
            if seconds <= 0:
                return None
            else:
                return {'seconds': seconds, 'message': msg}

'''
    convert a unit and an amount to relativedelta for time calculation
'''
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


'''
    set a reminder
'''
async def remind(client, channel, message, mention, seconds):
    if client:
        logging.info('Reminding ' + mention + ' in ' + str(seconds) + ' seconds: ' + message)
        message = 'Reminding ' + mention + ' ' + message
        await asyncio.sleep(seconds)
        await client.send_message(destination=channel, content=message)

'''
    manage incoming commands
'''
async def on_message(client, message):

    logging.info('remindMe on_message')
    print('[DEBUG: RemindMe] in on_message')

    # getting command arguments
    args = message.content.split(sep=' ')

    # checking command and mention
    if str.lower(args[0]) == remind_me:
        mention = message.author.mention
    elif str.lower(args[0]) == remind_all:
        mention = '@everyone'
    else:
        return

    # concat the message and remove the command
    content = ' '.join(args[1:])

    # formatting data
    data = absolute_format(content)
    if not data:
        data = relative_format(content)

    # debug
    print(data)

    if data:
        # settings reminder
        await remind(client, message.channel, data['message'], mention, data['seconds'])
    else:
        # wrong syntax, display bot usage
        await client.send_message(message.channel, usage)
