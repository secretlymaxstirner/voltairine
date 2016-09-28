import discord
import asyncio
import random



client = discord.Client()

insult1 = ["a Lazy", "a Stupid", " an Insecure", "an Idiotic", "a Slimy", "a Jerky", "a Smelly", "a Pompous", "a Communist", "a Dicknose", "a Pie-eating", "a Racist", "an Elitist", "a White Trash", "a Drug-Loving", "a Butterface", "a Tone Deaf", "an Ugly", "a Creepy"]
insult2 = ["Douche", "Ass", "Turd", "Rectum", "Butt", "Cock", "Shit", "Crotch", "Fascist", "Prick", "Jerk", "Taint", "Fuck", "Dick", "Boner", "Shart", "Nut", "Sphincter" ]
insult3 = ["Pilot", "Canoe", "Captain", "Pirate", "Hammer", "Knob", "Box", "Jockey", "Nazi", "Waffle", "Goblin", "Blossum", "Biscuit", "Clown", "Socket", "Monster", "Hound", "Dragon", "Balloon"]
help_msg = ('''\
!help - Displays this message
!insult - Generates a random insult
!coin - Flips a coin
!encounter - Fight a random monster
!acab
!anarchism
!ancap
!ancom
!bestshit
!bookchin
!bordiga
!brd
!btfo
!bubbles
!coffee
!cyberpunk
!durruti
!ezln
!fresh
!goldman
!gulag
!hacktheplanet
!kitty
!kronstadt
!kropotkin
!lenin
!lenny
!liberals
!linux
!makhno
!marx
!motivation
!ohwell
!outside
!poblacht
!proudhon
!pusheen
!rainbowstalin
!reddit
!rules
!sexist
!sjw
!sparkles
!spook
!stirner
!tankie
!trotsky
!trump
!vaporwave
!vegan
!changelog
!gold - See how much gold you have

-Dice-
!d4
!d6
!d8
!d10
!d12
!d20
''')

changelog = ('''
v0.1.1
-changed !gold to !inventory
-Added shop
-Added whisper
-Added insult
-Added RPG Dice Roller
-Added encounters
-Added potions
-Added fresh and wtf
''')

user_gold = {}
user_potions={}


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

"""
@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith(''):
"""
 

@client.event
@asyncio.coroutine
def on_message(message):

    if message.author == client.user:
        return

    elif message.content.startswith('!help'):
        yield from client.send_message(message.channel, help_msg)

    elif message.content.startswith('!changelog'):
        yield from client.send_message(message.channel, changelog)

    elif message.content.startswith('Voltairine, introduce yourself'):
        yield from client.send_message(message.channel, '```Hi everyone! I\'m Voltairine. Nice to meet you all```')

    elif message.content.startswith('!acab'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmPftuPUGLzTScSYJssoXSfmj9gDg8qe7czP13UgXCH3gC\nhttps://ipfs.pics/QmdtTG428q3CcDqx4kcEZ4687Vyrk1LxhQYYLqsHpSngMK')

    elif message.content.startswith('!anarchism'):
        yield from client.send_message(message.channel, 'Anarchism is a social movement that seeks liberation from oppressive systems of control including but not limited to the state, capitalism, racism, sexism, speciesism, and religion. Anarchists advocate a self-managed, classless, stateless society without borders, bosses, or rulers where everyone takes collective responsibility for the health and prosperity of themselves and the environment.')

    elif message.content.startswith('!berkman'):
        yield from client.send_message(message.channel, ':books: **The Bolshevik Myth (Diary 1920–22)**: https://theanarchistlibrary.org/library/alexander-berkman-the-bolshevik-myth-diary-1920-22 \n**Bolsheviks Shooting Anarchists** with Emma Goldman: https://theanarchistlibrary.org/library/emma-goldman-alexander-berkman-bolsheviks-shooting-anarchists \n**The Russian Tragedy (A Review and An Outlook)**: https://theanarchistlibrary.org/library/alexander-berkman-the-russian-tragedy-a-review-and-an-outlook \n**What Is Communist Anarchism?**: https://theanarchistlibrary.org/library/alexander-berkman-what-is-communist-anarchism ')

    elif message.content.startswith('!ancap'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/ipfs/QmUq6F6NbYznU9y65Pc17gG8rSBx9w42224FneG3EspgXX \n https://ipfs.pics/QmY6jNpD4FGewhC6dJVKwQYrCgEPCxkBCLuyJWvu1bZXbF')

    elif message.content.startswith('!ancom'):
        yield from client.send_message(message.channel, ':ancom: A theory of anarchism which advocates the abolition of the state, capitalism, wage labour, and private property (while retaining respect for personal property), and in favour of common ownership of the means of production, direct democracy, and a horizontal network of voluntary associations and workers\' councils with production and consumption based on the guiding principle: "from each according to his ability, to each according to his need"\n:books: **Recommended Reading**:books: \n- **Anarchist communism - an introduction** https://libcom.org/thought/anarchist-communism-an-introduction\n- **A Short Introduction to Anarchist Communism**  https://afed.org.uk/short-intro/')

    elif message.content.startswith('!bestshit'):
        yield from client.send_message(message.channel, ':books: CONQUEST OF BREAD MOTHERFUCKER\nhttps://theanarchistlibrary.org/library/petr-kropotkin-the-conquest-of-bread \nABC OF ANARCHISM IF YOU LIKE IT IN SIMPLE ENGLISH! \nhttps://libcom.org/library/abc-anarchism-alexander-berkman \nCOMMUNIST MANIFESTO FOR THE CLASSIC SHIT :ok_hand: :ok_hand: :ok_hand:  \nhttps://www.marxists.org/archive/marx/works/1848/communist-manifesto/')

    elif message.content.startswith('!bookchin'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmWbWyHkq41Kk6BUzwHtBsu1vjahFLQe82kPakhyobE7DG')

    elif message.content.startswith('!books'):
        yield from client.send_message(message.channel, ':books: :books: \n* **Peter Marshall - Demanding the Impossible: A History of Anarchism**\n* **Clifford Harper - Anarchy: graphic guide** \n* **Peter Kropotkin - Conquest of Bread**\n* Peter Kropotkin - Mutual Aid\n* Alexander Berkman - The ABC of anarchism\n* Peter Gelderloos - Anarchy Works\n* Emma Goldman - Anarchism and Other Essays\n* Oscar Wilde - The Soul of Man Under Socialism\n* Marx/Engels - Manifesto of the Communist Party\n* **Ursula Le Guin - The Dispossessed**\n* Daniel Guérin - Anarchism: From Theory to Practice\n* Comité Invisible (The Invisible Committee) - The Coming Insurrection\n* Bob Black - The Abolition of Work\n* Karl Marx - Capital\n* Max Stirner - The Unique and His Property\n* Daniel Guerin - Anarchism: Theory and Practice\n* Colin Ward - Anarchism: A Short Introduction\n* Benjamin R. Tucker - Instead of a Book\n* Alexander Berkman - What is Anarchism?\n* Ken Knabb - The Joy of Revolution\n* **Crimethinc - Work**\n* Crimethinc - Days of War, Nights of Love\n* **Daniel Guerin - No Gods, No Masters**\n* The Organizational Platform of the General Union of Anarchists\n* Peter Arshinov - History of the Makhnovist Movement\n* **Prole.info - The Housing Monster**\n* **Prole.info - Abolish Restaurants**\n* Peter Gelderloos - How Nonviolence Protects the State\n* Mikhail Bakunin - God and the State\n* Mikhail Bakunin - Revolutionary Catechism\n* **David Graeber - Debt: The First 5000 Years**\n* Voltairine de Cleyre - Crime and Punishment')

    elif message.content.startswith('!bordiga'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmaiT3xNWqEN6ezhtrv8coPPrHSebTmrPLCK4eXdSEpSMK')

    elif message.content.startswith('!brd'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmbuSBhqaUkubCHvijAtfh4D9VPKUWci24cECJK19KzjXv')

    elif message.content.startswith('!btfo'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmSYFBYnwX4XVkaCyn1jFHZSGS3uYEhEdbaatfM6PoaiXS')

    elif message.content.startswith('!bubbles'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmQdekAPo4tSU99dSEHgRppTemBaBGFVc1ggbTcwaHADim')

    elif message.content.startswith('!coffee'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/Qmf55P9UNCQNQxPceYxQ3moAtHYiLbEHgoRD8X4VGt8Axz')

    elif message.content.startswith('!communism'):
        yield from client.send_message(message.channel, 'A spectre:ghost::ghost: is haunting:ghost: :earth_africa:Europe:earth_africa: — the spectre :ghost:of communism☭☭☭☭. All the :muscle::muscle:powers of old Europe:muscle: have entered into a :pray: holy alliance :pray:to exorcise this spectre:ghost::ghost::ghost:: Pope :poop::poop:and Tsar:poop::thumbsdown::thumbsdown:, Metternich:poop: and Guizot:poop::poop::poop:, French Radicals:flag_fr::flag_fr::thumbsdown::thumbsdown::thumbsdown: and German police-spies:put_litter_in_its_place::put_litter_in_its_place::put_litter_in_its_place::put_litter_in_its_place:. Where is the:tada: party:tada::tada: in opposition that has not been :crying_cat_face:decried:crying_cat_face::crying_cat_face: as communistic☭☭☭☭ by its :frowning::frowning:opponents in power:frowning:? Where is the opposition that has not hurled back the branding:fire::fire: reproach:fire::fire::fire::fire: of ☭☭☭☭communism☭☭, against the more advanced:confetti_ball: opposition parties:confetti_ball::confetti_ball::confetti_ball:, as well as against its :no_good::no_good::no_good::no_good:reactionary adversaries:no_good::no_good:? :clock2:Two things:clock2: result from this fact:closed_book::closed_book:: I. ☭☭☭☭Communism☭☭ is already acknowledged by all :muscle:European powers:muscle::muscle: to be itself a :muscle::muscle:☭power☭:muscle:. II. It is :clock12::bangbang:️:clock12:high time:clock12::clock12::clock12::exclamation: that ☭☭Communists☭☭☭ should openly, in the :stuck_out_tongue::stuck_out_tongue::stuck_out_tongue:face:stuck_out_tongue::stuck_out_tongue: of the :earth_africa:whole:earth_africa: world:earth_africa::earth_africa::earth_africa:, publish:closed_book::closed_book: their:closed_book: views:closed_book::closed_book::closed_book:, their :dart:aims:dart::dart:, their tendencies☭☭, and meet this :baby_bottle:nursery:baby_bottle::baby_bottle: tale:baby_bottle::closed_book::baby_bottle: of the :ghost:Spectre:ghost: of Communism:ghost::ghost: ☭ :ghost:☭ with a manifesto:closed_book::closed_book: of the party:closed_book::confetti_ball:☭ itself.')


    elif message.content.startswith('!cyberpunk'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmfP9iKkW9cNxr5jBbPKeNBsd6XKpZgHCSXPkpwAuRQEFR')

    elif message.content.startswith('!durruti'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmPVxR2uPoqemanm3u8WGhDX9sfsRdMuSuQPc5xWMhzHWk')

    elif message.content.startswith('!ezln'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmQHszGgh6dPWTTTVffwqPsJ8rwZYkfxPFRWa2TyLwpuua')

    elif message.content.startswith('!fresh'):
        yield from client.send_message(message.channel, '```Now, this is a story all about how \nMy life got flipped-turned upside down \nAnd I\'d like to take a minute \n Just sit right there \nI\'ll tell you how I became the prince of a town called Bel-Air```')

    elif message.content.startswith('!goldman'):
        yield from client.send_message(message.channel, ':books: **Anarchism and Other Essays**: https://theanarchistlibrary.org/library/emma-goldman-anarchism-and-other-essays\n**My Disillusionment in Russia** with Emma Goldman: https://theanarchistlibrary.org/library/emma-goldman-my-disillusionment-in-russia\n**My Further Disillusionment in Russia**: https://theanarchistlibrary.org/library/emma-goldman-my-further-disillusionment-in-russia\n**Voltairine De Cleyre**: https://theanarchistlibrary.org/library/emma-goldman-voltairine-de-cleyre')

    elif message.content.startswith('!gulag'):
        yield from client.send_message(message.channel, 'https://libcom.org/history/gay-gulag')

    elif message.content.startswith('!hitler'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmQLVPJCHZ7bD3tFi7PywvMLUnAAwqnDVPDM5JfTPRziG8')

    elif message.content.startswith('!hacktheplanet'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmcgcsvLj5n73wTPDtQUPtwF1TeyudSFqv5hinUxemyGU3')

    elif message.content.startswith('!hoxha'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmYR2kEYeLBwhYd7KqqsZMEFLGjuZQamKvMTVDMepFMshq')

    elif message.content.startswith('!ideology'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmUjKM9QesPUVFCoq5oPnyPwVRYd1JNf7zWtnvgkdj6FMP')

    elif message.content.startswith('!kitty'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmR6SGiRhvfs3riNMXUrvAf4N9qqcdn2aQ77fJ1UF2gf9j')

    elif message.content.startswith('!kronstadt'):
        yield from client.send_message(message.channel, 'http://www.veoh.com/watch/v18771330YDwTzP3g')

    elif message.content.startswith('!kropotkin'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmXMwSkQz97PSg6ivs6cAtjd39t73dXgR2CN1TacBYYgMZ')

    elif message.content.startswith('!lenin'):
        yield from client.send_message(message.channel, 'a counter-revolutionary class traitor, who is responsible for the creation of the state-capitalist dictatorship known as the USSR. Along with other state-capitalist dictators such as Stalin and Mao, Lenin has tarnished the reputation of communism better than any capitalist or fascist ever could. ')

    elif message.content.startswith('!lenny'):
        yield from client.send_message(message.channel, '( ͡° ͜ʖ ͡°)')

    elif message.content.startswith('!liberals'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmVjTr9rF1MTNk1DS7msUTVtfduzeeZtWptDxuwHYBRmNv')

    elif message.content.startswith('!linux'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmNay4iG5GKbyXb7o6oRjSm6o5W3aRJhWeMmsaK1xR9Rae')

    elif message.content.startswith('!makhno'):
        yield from client.send_message(message.channel, 'https://www.youtube.com/watch?v=WGqkyHd1cZk')

    elif message.content.startswith('!marx'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmYRwrEwnZccbZHBEzLXijs2a6swsvbUfoJcVrn3eP6H2S')

    elif message.content.startswith('!motivation'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmTf3mPZUH27ArzRwdjnAS7Auu5nTTbXAZ3MTc5YbYuJsH')

    elif message.content.startswith('!ohwell'):
        yield from client.send_message(message.channel, '¯\_(ツ)_/¯')

    elif message.content.startswith('!outside'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/Qma87xfLsp9MCBzu2eDTKModRsMsvhK6Q9dCPZCQiWeseq')

    elif message.content.startswith('!poblacht'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmdPabyTnRiCazy1scw7hK8Guwy93yDwZhov6gcy8tGhVS')

    elif message.content.startswith('!popcorn'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmW3FgNGeD46kHEryFUw1ftEUqRw254WkKxYeKaouz7DJA')

    elif message.content.startswith('!proudhon'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmWtrL1JG2apyiKaPmMUEuMnc6gdQxbQ1v2tpSn3ccEofX')

    elif message.content.startswith('!pusheen'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/Qmc3iqvGA3aSF82Fm8gtb2ZSdR17khZuoJjgstirvTNNfi\nhttps://ipfs.pics/Qma9hdzVy4Y5rBG5qFoNLyG9XY3nn3wJQaM3bTZXFTu2sS\nhttps://ipfs.pics/QmZX3zXUE5AUVvb7oarZ96JQj3PA9E7i7Ps8PgxhAyWLNc\nhttps://ipfs.pics/QmZ6BcrTwpV54PnuW6pkjDf4y5qeUphvM1rbTC87sRYgp6')

    elif message.content.startswith('!rainbowstalin'):
        yield from client.send_message(message.channel, 'http://rainbowstalin5.ytmnd.com/')

    elif message.content.startswith('!reddit'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/radical-reddit/')

    elif message.content.startswith('!revolution'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmeAyovfj8ToCEWtb5HGvgDXtdwAdeZGEkwG63XwwmXrEe')

    elif message.content.startswith('!rules'):
        yield from client.send_message(message.channel, 'http://pastebin.com/KpfbM3iC')

    elif message.content.startswith('!sexist'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmeWz6rHtAyhS2p71ZaahC5zwfUUbGVA1CFNUuha52oavo')

    elif message.content.startswith('!sjw'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmTVWTj9cXmxFecv2EfnCN6xQtYqX3wprkqL7vyo9wwqmM')

    elif message.content.startswith('!sparkles'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmVn2KNuXZLsvpsvCPwp9ssrJgzVjkL8m5MtxEPxCnphTB')

    elif message.content.startswith('!spook'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmYqcXLHuAxBha8nofihghbAWvQiSf2dSNa7oKiNAmNsoK')

    elif message.content.startswith('!stirner'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmbbBdDbhoZhYfxTwc8FH41AQmLZtFFMDC6y7YexXrJhqh')

    elif message.content.startswith('!tankie'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmQUfTTAQwUWq2peYL1EzyNiDsskdXvCteEn73uoZtXinF')

    elif message.content.startswith('!trotsky'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmcbRdEgYbpeYJ47mByVbta7vktsNRDwVAvcswGRHkTKmP')

    elif message.content.startswith('!trump'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmZQ2W3JuVpaZFY7q1vdMFLa6rHdgNJWjwKibqow3ur8vX\nhttps://ipfs.pics/QmdVbUVhoiJpHLhke1r8uDogSrPnbFfwSLe45vwXJ9DiSw')

    elif message.content.startswith('!vaporwave'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmWDodJS48z5JUGLTNVwMKCDQbRu6W5rytUbNv65JuxMug')

    elif message.content.startswith('!vegan'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmZVSvxDRRPswS4uPUYdMYKNxiWC6e2oJg16UuTipgyVBB')

    elif message.content.startswith('!whisper'):
        yield from client.send_message(message.author, 'pssst')
        
    elif message.content.startswith('!insult'):
        j = random.randint(0,18)
        k = random.randint(0,17)
        l = random.randint(0,18)
        yield from client.send_message(message.channel, '```You\'re ' + insult1[j] + ' ' + insult2[k] + ' ' + insult3[l] + '```')


    elif message.content.startswith('!coin'):
        j = random.randint(1,2)
        if j == 1:
            yield from client.send_message(message.channel, '```Heads!```')
        else:
            yield from client.send_message(message.channel, '```Tails!```')
            
    elif message.content.startswith('!d4'):
        j = random.randint(1,4)
        yield from client.send_message(message.channel, '```Rolling a d4\nRolled a ' + str(j) + '```')

    elif message.content.startswith('!d6'):
        j = random.randint(1,6)
        yield from client.send_message(message.channel, '```Rolling a d6\nRolled a ' + str(j) + '```')

    elif message.content.startswith('!d8'):
        j = random.randint(1,8)
        yield from client.send_message(message.channel, '```Rolling a d8\nRolled a ' + str(j) + '```')

    elif message.content.startswith('!d10'):
        j = random.randint(1,10)
        yield from client.send_message(message.channel, '```Rolling a d10\nRolled a ' + str(j) + '```')

    elif message.content.startswith('!d12'):
        j = random.randint(1,12)
        yield from client.send_message(message.channel, '```Rolling a d12\nRolled a ' + str(j) + '```')
    elif message.content.startswith('!d20'):
        j = random.randint(1,20)
        yield from client.send_message(message.channel, '```Rolling a d20\nRolled a ' + str(j) + '```')

    elif message.content.startswith('!swing'):
        j = random.randint(0,1)
        if j == 0:
            msg = 'They miss, burrying their sword into the ground'
        elif j == 1:
            msg = 'They hit. Cleaving the enemy in two'
        yield from client.send_message(message.channel,'```' +  message.author.name + ' swings their mighty sword\n' +msg+'```')

    elif message.content.startswith('!inventory'):
        if message.author not in user_gold:
           user_gold[message.author] = 0
        if message.author not in user_potions:
            user_potions[message.author] = 0

        yield from client.send_message(message.channel, '```'+message.author.name+' has '+str(user_gold[message.author])+' gold and '+str(user_potions[message.author])+' potions```')

    elif message.content.startswith('!encounter'):
        k = random.randint(0,3)
        enemy = ['ancap', 'tankie', 'fascist', 'liberal', 'trump', 'cop']
        enemy_pic = ['https://ipfs.pics/ipfs/QmUq6F6NbYznU9y65Pc17gG8rSBx9w42224FneG3EspgXX','https://ipfs.pics/QmRCh7AFfyL3ZSXCbF6ax6NjkrMwCCqgar8RoajCYp6Zot','https://ipfs.pics/QmSrPJqzc8dzni8EwvGMg3GJuNLrL4pwgfRNgeM68ZwF1s','https://ipfs.pics/QmTD8o6ZZ4Ppd4sbTMjY9Cf7SXmt7uTZdwuHwojyTLNtcs,https://ipfs.pics/QmdLNzYbiSfkEKp2mDotu1yCRabi43iopkFxdJBfaKJW93,https://ipfs.pics/QmcdWyBSp78n65VhxrFHgvLhjvfkA7FyKtTtwAnFx3Rszp']
        enemy_hp = [15,15, 17, 10, 15,20]
        enemy_hp_l = int(enemy_hp[k])
        player_hp = 20
        player_dmg = 0
        enemy_dmg = 0
        yield from client.send_message(message.channel, enemy_pic[k]+'\n```A '+enemy[k]+' appears!```')

        while enemy_hp_l > 0 and player_hp > 0:
            yield from client.send_message(message.channel, '```The '+enemy[k]+' has ' + str(enemy_hp_l) + ' hp \n'+message.author.name+' has ' + str(player_hp) + ' hp```')
            msg = yield from client.wait_for_message(author=message.author)
            if msg.content == 'attack' or msg.content == '!sttack':
                player_dmg = random.randint(1,12)
                enemy_hp_l = (enemy_hp_l - player_dmg)
                if enemy_hp_l < 0:
                    enemy_hp_l = 0
            elif msg.content == 'potion':
                if message.author not in user_potions:
                    user_potions[message.author] = 0
                if user_potions[message.author] > 0:
                    user_potions[message.author] -=1
                    player_hp +=5
                    yield from client.send_message(message.channel, '``` '+message.author.name+' used a potion. Their hp went up by 5```')
                    continue
                elif user_potions[message.author] == 0:
                    yield from client.send_message(message.channel, '```'+message.author.name+' fumbles around in their bag for a potion that isn\'t there')
            else:
                yield from client.send_message(message.channel, '```Accepted input, attack, potion```')

            if enemy_hp_l <= 0:
                gold = random.randint(1, 8)
                yield from client.send_message(message.channel, '```'+message.author.name+' defeats the '+enemy[k]+' and finds ' + str(gold) + ' gold!```')
                if message.author not in user_gold:
                    user_gold[message.author] = gold
                else:
                    user_gold[message.author] += gold
                break
                
            enemy_dmg = random.randint(1,12)
            player_hp = (player_hp - enemy_dmg)
            yield from client.send_message(message.channel, '```'+message.author.name+' swings, dealing ' + str(player_dmg) + ' damage.\nThe '+enemy[k]+' swings, dealing '+ str(enemy_dmg) +' damage.```')  
        
            if player_hp <= 0:
                yield from client.send_message(message.channel, '```The '+enemy[k]+' overpowers '+message.author.name+' and they black out```')

    elif message.content.startswith ('!shop'):
        if message.author not in user_gold:
            user_gold[message.author] = 0
        if message.author not in user_potions:
            user_potion[message.author] = 0
        yield from client.send_message(message.channel, '```Welcome to the shop!```\nPotion - 5g')
        msg = yield from client.wait_for_message(author=message.author)
        if msg.content == 'potion' or msg.content == 'Potion':
            if user_gold[message.author]<5:
                yield from client.send_message(message.channel, 'You don\'t have enough gold to buy this item')
            user_potions[message.author]+=1
            user_gold[message.author]-=5
            yield from client.send_message(message.channel, '```'+message.author.name+' bought a potion.\nThank you for visiting the shop!```')

    
#    elif message.content.startswith('!d100'):
#       yield from User.mention(message.author)
#        yield from client.send_message(message.channel, 'Rolled a ' + random.randint(1,100))

client.run('token')
