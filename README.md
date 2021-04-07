# TwitchBotSample
Just simple twitch-bot(not finished)

# Install needed modules
* Download lib using pip:
`pip install irc`

# How to add the commands
* Go to the `commands.py` and search for the list named `lst`. 
* Add a new command by appending to this list one of the following classes: `TextResponse`, `SoundCommand`(not working now), `ImageCommand`(not working now).
* You can also insert some value or a text to the command by using Insertions. Just write `${<NameOfTheInsertion(arguments)>}` in the text of the command. There are 2 working Insertions now: RandomNumber and TagTarget. If there are no arguments in the insertion, keep the brackets empty.
# Insertions
* RandomNumber(lower_bound, upper_bound). Sample of use: RandomNumber(0,100) -> a random number from 0 to 100(included).
* TagTarget(). Tags the user, who executed the command in the chat(or whom in brackets). Sample of use: TagTarget() -> @username.
* CurrentBalance()
* StartEconomyEvent()
* EndEconomyEvent()
* ParticipateInEconomyEvent()

# Usage
* Run AuthSetter.py to log in the bot and follow the instructions provided.
* Run Bot.py

#EconomyEvents(not really working now)
Now there are 1 awailable Event. It's `CollectBets`. Participants give their points, and there is only 1 winner, who will take all. (Support for db will be added later)
