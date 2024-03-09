# Imports
import random
import discord
from discord.ui import Button, View
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("TOKEN")

#initializes discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# On ready
@client.event
async def on_ready():

    #verifies bot is on in terminal
    print("The bot is online as {0.user}".format(client))

# ROCK PAPER SCISSORS
# Rock paper scissor Buttons: 1 = rock, 2 = paper, 3 = scissors
def rpsSetup():

    #creates discord UI for game
    global rpsEmbed
    rpsEmbed = discord.Embed(title = "Rock Paper Scissors")
    rpsEmbed.add_field(name="Opponent", value="(unknown)", inline=True)
    rpsEmbed.add_field(name="Player (You)", value="(choose)", inline=True)

rpsSetup()

#button class for actions to take if rock button is hit
class RockButton(Button):
    global rpsEmbed
    def __init__(self, author):
        super().__init__(label="Rock" , style=discord.ButtonStyle.blurple)
        self.author = author
    async def callback(self, interaction):
        chance = random.randint(1,3)
        if chance == 1 and interaction.user == self.author:
            rpsEmbed = discord.Embed(title = "Rock Paper Scissors")
            rpsEmbed.add_field(name="Result", value = "You Tied!", inline=False)
            rpsEmbed.add_field(name="`Opponent`", value="Rock!", inline=True)
            rpsEmbed.add_field(name="Player (You)", value="Rock!", inline=True)
        elif chance == 2 and interaction.user == self.author:
            rpsEmbed = discord.Embed(title = "Rock Paper Scissors")
            rpsEmbed.add_field(name="Result", value = "You Lost!", inline=False)
            rpsEmbed.add_field(name="Opponent", value="Paper!", inline=True)
            rpsEmbed.add_field(name="Player (You)", value="Rock!", inline=True)
        elif chance == 3 and interaction.user == self.author:
            rpsEmbed = discord.Embed(title = "Rock Paper Scissors")
            rpsEmbed.add_field(name="Result", value = "You Won!", inline=False)
            rpsEmbed.add_field(name="Opponent", value="Scissors!", inline=True)
            rpsEmbed.add_field(name="Player (You)", value="Rock!", inline=True)
        try:
            await interaction.response.edit_message(embed=rpsEmbed, view=None)
        except:
            pass 


class PaperButton(Button):
    global rpsEmbed
    def __init__(self, author):
        super().__init__(label = "Paper" , style=discord.ButtonStyle.blurple)
        self.author = author
    async def callback(self, interaction):
        chance = random.randint(1,3)
        if chance == 1 and interaction.user == self.author:
            rpsEmbed = discord.Embed(title = "Rock Paper Scissors")
            rpsEmbed.add_field(name="Result", value = "You Won!", inline=False)
            rpsEmbed.add_field(name="Opponent", value="Rock!", inline=True)
            rpsEmbed.add_field(name="Player (You)", value="Paper!", inline=True)
        elif chance == 2 and interaction.user == self.author:
            rpsEmbed = discord.Embed(title = "Rock Paper Scissors")
            rpsEmbed.add_field(name="Result", value = "You Tied!", inline=False)
            rpsEmbed.add_field(name="Opponent", value="Paper!", inline=True)
            rpsEmbed.add_field(name="Player (You)", value="Paper!", inline=True)
        elif chance == 3 and interaction.user == self.author:
            rpsEmbed = discord.Embed(title = "Rock Paper Scissors")
            rpsEmbed.add_field(name="Result", value = "You Lost!", inline=False)
            rpsEmbed.add_field(name="Opponent", value="Scissors!", inline=True)
            rpsEmbed.add_field(name="Player (You)", value="Paper!", inline=True)
        try:
            await interaction.response.edit_message(embed=rpsEmbed, view=None)
        except:
            pass  


class ScissorsButton(Button):
    global rpsEmbed
    def __init__(self, author):
        super().__init__(label="Scissors" , style=discord.ButtonStyle.blurple)
        self.author = author
    async def callback(self, interaction):
        chance = random.randint(1,3)
        if chance == 1 and interaction.user == self.author:
            rpsEmbed = discord.Embed(title = "Rock Paper Scissors")
            rpsEmbed.add_field(name="Result", value = "You Lost!", inline=False)
            rpsEmbed.add_field(name="Opponent", value="Rock!", inline=True)
            rpsEmbed.add_field(name="Player (You)", value="Scissors!", inline=True)
        elif chance == 2 and interaction.user == self.author:
            rpsEmbed = discord.Embed(title = "Rock Paper Scissors")
            rpsEmbed.add_field(name="Result", value = "You Won!", inline=False)
            rpsEmbed.add_field(name="Opponent", value="Paper!", inline=True)
            rpsEmbed.add_field(name="Player (You)", value="Scissors!", inline=True)
        elif chance == 3 and interaction.user == self.author:
            rpsEmbed = discord.Embed(title = "Rock Paper Scissors")
            rpsEmbed.add_field(name="Result", value = "You Tied!", inline=False)
            rpsEmbed.add_field(name="Opponent", value="Scissors!", inline=True)
            rpsEmbed.add_field(name="Player (You)", value="Scissors!", inline=True)
        try:
            await interaction.response.edit_message(embed=rpsEmbed, view=None)
        except:
            pass 


# # BLACKJACK
def blackjackSetup(author, dealerCard1, playerCard1, playerCard2, dealerTotal, playerTotal):
    global bjEmbed
    global name
    global Author
    global DealerCard1
    global PlayerCard1
    global PlayerCard2
    global DealerTotal
    global PlayerTotal
    Author = author
    DealerCard1 = dealerCard1
    PlayerCard1 = playerCard1
    PlayerCard2 = playerCard2
    DealerTotal = dealerTotal
    PlayerTotal = playerTotal
    name = str(author).split('#')[0]
    bjEmbed = discord.Embed()
    bjEmbed = bjEmbed.set_author(name=f"{name}'s Blackjack Game", icon_url=author.avatar)
    bjEmbed.add_field(name=f"Casino (Dealer)", value=f"Cards: `{dealerCard1}` ` ? `\nTotal: `{dealerTotal}`", inline=False)
    bjEmbed.add_field(name=f"{name} (Player)", value=f"Cards: `{playerCard1}` `{playerCard2}`\nTotal: `{playerTotal}`", inline=False)

class HitButton(Button):
    global bjEmbed
    def __init__(self, author):
        super().__init__(label="Hit", style=discord.ButtonStyle.blurple)
        self.author = author
    global dealer_cards
    dealer_cards = []
    async def callback(self, interaction):
        def hitCard():
            global bjEmbed
            global card_sum
            global bjCount
            global bjView
            global bjOutcome
            # Third player card
            if card_sum <= 22 and bjCount == 0:
                # draw player card 3
                global PlayerCard3
                PlayerCard3 = card()
                # Edit embed
                bjEmbed = discord.Embed()
                bjEmbed = bjEmbed.set_author(name=f"{name}'s Blackjack Game", icon_url=Author.avatar)
                bjEmbed.add_field(name=f"Namron's Worst Nightmare (Dealer)", value=f"Cards: `{DealerCard1}` ` ? `\nTotal: `{dealer_card_sum}`", inline=False)
                bjEmbed.add_field(name=f"{name} (Player)", value=f"Cards: `{PlayerCard1}` `{PlayerCard2}` `{PlayerCard3}`\nTotal: `{card_sum}`", inline=False)
                bjCount += 1
                # make a new button
                bjView = View()
                hit1 = HitButton(self.author); stand1 = StandButton(self.author)
                bjView.add_item(hit1); bjView.add_item(stand1)
            #Fourth player card
            elif card_sum <= 22 and bjCount == 1:
                global PlayerCard4
                PlayerCard4 = card()
                bjEmbed = discord.Embed()
                bjEmbed = bjEmbed.set_author(name=f"{name}'s Blackjack Game", icon_url=Author.avatar)
                bjEmbed.add_field(name=f"Namron's Worst Nightmare (Dealer)", value=f"Cards: `{DealerCard1}` ` ? `\nTotal: `{dealer_card_sum}`", inline=False)
                bjEmbed.add_field(name=f"{name} (Player)", value=f"Cards: `{PlayerCard1}` `{PlayerCard2}` `{PlayerCard3}` `{PlayerCard4}`\nTotal: `{card_sum}`", inline=False)
                bjCount += 1
                bjView = View()
                hit2 = HitButton(self.author); stand2 = StandButton(self.author)
                bjView.add_item(hit2); bjView.add_item(stand2)
            # Fifth player card (win)
            elif card_sum <= 22 and bjCount == 2:
                global PlayerCard5
                PlayerCard5 = card()
                bjEmbed = discord.Embed()
                bjEmbed = bjEmbed.set_author(name=f"{name}'s Blackjack Game", icon_url=Author.avatar)
                bjEmbed.add_field(name=f"Namron's Worst Nightmare (Dealer)", value=f"Cards: `{DealerCard1}` ` ? `\nTotal: `{dealer_card_sum}`", inline=False)
                bjEmbed.add_field(name=f"{name} (Player)", value=f"Cards: `{PlayerCard1}` `{PlayerCard2}` `{PlayerCard3}` `{PlayerCard4}` `{PlayerCard5}`\nTotal: `{card_sum}`", inline=False)
                bjCount += 1
                if card_sum <= 22:
                    bjView = View()
                    bjOutcome = "Won, you had five cards and went under 21"
                    bjEmbed.remove_field(0)
                    bjEmbed.insert_field_at(0, name=f"Result", value=f'{bjOutcome}')
                    bjEmbed.insert_field_at(1, name=f"Namron's Worst Nightmare (Dealer)", value=f"Cards: `{DealerCard1}` `{dealer_card()}`\nTotal: `{dealer_card_sum}`", inline=False)
            if card_sum >= 22:
                bjOutcome = "Lost, you busted and went over 21."
                bjEmbed.remove_field(0)
                bjEmbed.insert_field_at(0, name=f"Result", value=f'{bjOutcome}')
                bjEmbed.insert_field_at(1, name=f"Namron's Worst Nightmare (Dealer)", value=f"Cards: `{DealerCard1}` `{dealer_card()}`\nTotal: `{dealer_card_sum}`", inline=False)
                bjView = View()

        if interaction.user == Author:
            hitCard()
            try:
                await interaction.response.edit_message(embed=bjEmbed, view=bjView)
            except:
                pass
    
class StandButton(Button):
    global bjEmbed
    def __init__(self, author):
        super().__init__(label="Stand" , style=discord.ButtonStyle.blurple)
        self.author = author
    global dealer_cards
    dealer_cards = []
    async def callback(self, interaction):
        def standCard():
            # Draws dealer's cards
            while dealer_card_sum <= 16:     
                dealer_cards.append(dealer_card())
            # Check win/loss/draw condition
            if dealer_card_sum >= 22 and card_sum < 22:
                bjOutcome = "Won, dealer bust and went over 21."
            elif dealer_card_sum > card_sum:
                bjOutcome = f"Lost, dealer stood with a higher score of `{str(dealer_card_sum)}`."
            elif dealer_card_sum == card_sum:
                bjOutcome = f"Drew, both you and the dealer stood with the same score of `{str(card_sum)}`."
            elif dealer_card_sum < card_sum:
                bjOutcome = f"Won, you stood with a higher score of `{str(card_sum)}`"
            # Edit embed
            if len(dealer_cards) == 1:
                bjEmbed.remove_field(0)
                bjEmbed.insert_field_at(0, name=f"Result", value=f'{bjOutcome}')
                bjEmbed.insert_field_at(1, name=f"Namron's Worst Nightmare (Dealer)", value=f"Cards: `{DealerCard1}` `{dealer_cards[0]}`\nTotal: `{dealer_card_sum}`", inline=False)
            elif len(dealer_cards) == 2:
                bjEmbed.remove_field(0)
                bjEmbed.insert_field_at(0, name=f"Result", value=f'{bjOutcome}')
                bjEmbed.insert_field_at(1, name=f"Namron's Worst Nightmare (Dealer)", value=f"Cards: `{DealerCard1}` `{dealer_cards[0]}` `{dealer_cards[1]}`\nTotal: `{dealer_card_sum}`", inline=False)
            elif len(dealer_cards) == 3:
                bjEmbed.remove_field(0)
                bjEmbed.insert_field_at(0, name=f"Result", value=f'{bjOutcome}')
                bjEmbed.insert_field_at(1, name=f"Namron's Worst Nightmare (Dealer)", value=f"Cards: `{DealerCard1}` `{dealer_cards[0]}` `{dealer_cards[1]}` `{dealer_cards[2]}`\nTotal: `{dealer_card_sum}`", inline=False)
            elif len(dealer_cards) == 4 and dealer_card_sum <= 21:
                bjOutcome = "Lost, dealer had five cards and went under 21"
                bjEmbed.remove_field(0)
                bjEmbed.insert_field_at(0, name=f"Result", value=f'{bjOutcome}')
                bjEmbed.insert_field_at(1, name=f"Namron's Worst Nightmare (Dealer)", value=f"Cards: `{DealerCard1}` `{dealer_cards[0]}` `{dealer_cards[1]}` `{dealer_cards[2]}` `{dealer_cards[3]}`\nTotal: `{dealer_card_sum}`", inline=False)
            elif len(dealer_cards) == 4:
                bjEmbed.remove_field(0)
                bjEmbed.insert_field_at(0, name=f"Result", value=f'{bjOutcome}')
                bjEmbed.insert_field_at(1, name=f"Namron's Worst Nightmare (Dealer)", value=f"Cards: `{DealerCard1}` `{dealer_cards[0]}` `{dealer_cards[1]}` `{dealer_cards[2]}` `{dealer_cards[3]}`\nTotal: `{dealer_card_sum}`", inline=False)
        if interaction.user == Author:
            standCard()
            try:
                await interaction.response.edit_message(embed=bjEmbed, view=None)
            except:
                pass 

# ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE
# ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE
# ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE - ON MESSAGE

@client.event
async def on_message(message):
    # Variables
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    # Prevents infinite loop
    if message.author == client.user:
        return

    # CLEAR COMMAND
    elif user_message.lower().split(' ')[0] == "$clear" and (str(message.author) == "rocket#7610" or str(message.author) == "LosPapasGrandes#7863"):
        try:
            await message.channel.purge(limit=int(user_message.lower().split(' ')[1]))
            await message.channel.send(f"{user_message.lower().split(' ')[1]} messages cleared.")
            return
        except:
            await message.channel.send("Please enter how many messages you want to clear.")
            return

    # RPS COMMAND
    elif "$rps" in user_message.lower():
        view = View()
        rock = RockButton(message.author); paper = PaperButton(message.author); scissors = ScissorsButton(message.author)
        view.add_item(rock); view.add_item(paper); view.add_item(scissors)
        await message.channel.send(embed = rpsEmbed, view = view)
        return

    # 8BALL COMMAND
    elif user_message.lower().split(' ')[0] == "$8ball":
        chance = random.randrange(0, 5)
        if chance == 0:
            await message.channel.send(f"Of course.")
            return
        elif chance == 1:
            await message.channel.send(f"No chance.")
            return
        elif chance == 2:
            await message.channel.send(f"Maybe.")
            return
        elif chance == 3:
            await message.channel.send(f"Of course not.")
            return
        elif chance == 4:
            await message.channel.send(f"Most definitely.")
            return
        elif chance == 5:
            await message.channel.send(f"No.")
            return
        elif chance == 6:
            await message.channel.send(f"Yes.")
            return
    
    # BLACKJACK COMMAND
    elif "$blackjack" in user_message.lower() or "$bj" in user_message.lower():
        global card_sum
        global ace_count
        global dealer_card_sum
        global dealer_ace_count
        global bjCount
        global bjOutcome
        global dealer_cards
        bjCount = 0
        card_sum = 0
        ace_count = 0
        dealer_card_sum = 0
        dealer_ace_count = 0
        bjOutcome = ""
        dealer_cards = []
        # GENERATES PLAYER CARD
        global card
        def card():
            global card_sum
            global ace_count
            global player_total
            card_suit = ["♥", "♣", "♦", "♠"]
            card_face = ["10", "J", "Q", "K"]
            card_num = random.randint(2,11)
            card_name = card_num
            if card_num == 10:
                card_name = random.choice(card_face)
            if card_num == 11:
                card_name = "A"
                ace_count += 1
            card_sum = card_sum + card_num
            if ace_count >= 1 and card_sum >= 22:
                card_sum = card_sum - 10
                ace_count -= 1
            return f"{random.choice(card_suit)} {card_name}"
        
        # GENERATES DEALER CARD
        global dealer_card
        def dealer_card():
            global dealer_card_sum
            global dealer_ace_count
            card_suit = ["♥", "♣", "♦", "♠"]
            card_face = ["10", "J", "Q", "K"]
            card_num = random.randint(2,11)
            card_name = card_num
            if card_num == 10:
                card_name = random.choice(card_face)
            if card_num == 11:
                card_name = "A"
                dealer_ace_count += 1
            dealer_card_sum = dealer_card_sum + card_num
            if dealer_ace_count >= 1 and dealer_card_sum >= 22:
                dealer_card_sum = dealer_card_sum - 10
                dealer_ace_count -= 1
            return f"{random.choice(card_suit)} {card_name}"
        
        blackjackSetup(message.author, dealer_card(), card(), card(), dealer_card_sum, card_sum)
        view = View()
        hit = HitButton(message.author); stand = StandButton(message.author)#; playagain = PlayAgainButton(message.author); quit = QuitButton(message.author)
        view.add_item(hit); view.add_item(stand)
        await message.channel.send(embed = bjEmbed, view = view)
        return



client.run(token)