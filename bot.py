#!/usr/bin/env python3

import sys
import socket

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Botzentrum:
    server = ''
    channel = ''
    nick = 'yabbot'
    def __init__(self, server, channel):
        self.server = server
        self.channel = channel

    def connect(self):
        irc.connect((self.server, 6667))
        irc.send(bytes("USER " + self.nick + " " + self.nick + " " + self.nick + " " + self.nick + "\n", "UTF-8"))
        irc.send(bytes('NICK ' + self.nick + '\n', "UTF-8"))
        irc.send(bytes('JOIN ' + self.channel + '\n', "UTF-8"))
    def sendmsg(self, msg):
        irc.send(bytes("PRIVMSG "+ self.channel +" :"+ msg +"\n", "UTF-8"))
    def quit(self):
        self.sendmsg("Arrividerci")
        irc.send(bytes('DISCONNECT \n', "UTF-8"))
        exit(0)


def main():
    bot = Botzentrum('irc.freenode.net', '##francophonie')
    bot.connect()

    while True:
       text=irc.recv(2040).decode("UTF-8")  #receive the text
       text=text.strip('\n\r')
       print(text)
       if text.find("PRIVMSG") != -1:
           name = text.split('!',1)[0][1:]
           message = text.split('PRIVMSG',1)[1].split(':',1)[1]
           if message.find("Salut " + bot.nick) != -1:
               bot.sendmsg("Salut " + name + " !!")
           if message.find('tu ' + bot.nick) != -1:
               bot.sendmsg('Moi, quoi ?')
           if message.find('partir ' + bot.nick) != -1:
               bot.sendmsg('dac je pars')
               bot.quit()
           if message.find('Alors ' + bot.nick) != -1:
               bot.sendmsg('Tu veux que je raconte quoi ?')

           #bot.sendmsg('Hallo')

    #    command = input()
    #    if command == '.q':
    #        bot.quit()


if __name__ == '__main__':
    main()
