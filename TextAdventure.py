#Importing necessary modules
import time as tm
import random as rd
import sys
import os

xp = 0
startdet = 1
hitChanceDeter = 0
attack = ""


PHeavyAttackDamage = 100
PHeavyAttackName = "Heaving Hit"
PHeavyAttackHitChance = 40
PLightAttackDamage = 40
PLightAttackName = "Sword Swash"
PLightAttackCritChance = 30

import string
alphabet = string.ascii_lowercase # Assuming  your answers will always start with A, then B and so on

def valid_input(text, choices):
    valid_choices = [letter for letter in alphabet[:choices]]
    print(text)
    answer = input().lower().strip() # removes whitespaces
    if answer in valid_choices:
        return answer
    else:
        print("Invalid input, please try again.\n")
        return valid_input(text, choices)



#Clear Screen Func
def cs(notiftext):
    os.system('clear')
    print(notiftext)
    print("\n_____________________________________________________________________________________________________________\n\n",)

#Typing Func
def print1by1(text, lineDelay=0.35, delay=0.025):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        tm.sleep(delay)
    tm.sleep(lineDelay)    


        
# Battle Function

def Fight(EnemyName, ELightAttackName, ELightAttackDamage, EHeavyAttackName, EHeavyAttackDamage, EHeavyAttackHitChance):
    print(EnemyName, "blocked the path!\n")
    startdet = rd.randint(1,2)
    if startdet == 1:
        print("You'll attack first. Your options are: \nA) Light attack ("+PLightAttackDamage+" damage) \nB) Heavy Attack (",PHeavyAttackDamage, "damage and",PHeavyAttackHitChance + "% chance to hit.\n")
        attack = input("")
        attack = attack.lower()
        if attack != "a" or attack != "b":
            print("Invalid input. Make sure you enter A or B as your attack choice.\n")
        

    
#Entrance
cs("A reminder for you to not press any buttons while the text is typing itself. \nYou may cause bugs, make reading it harder for yourself and potentially crash the game. \nSo, don't do it, alright?")
print1by1("Unknown: Hello fellow wanderer! Welcome to \"The Escape from the Underworld\", a text adventure programmed on Python HeavyMechGun50!")
print1by1("\nUnknown: What shall we call you?\n")
playerName = str(input(""))
playerName = playerName.capitalize()
print(playerName + "...")
tm.sleep(0.3)
print1by1("Unknown: That is an interesting name...\n")
print1by1("Unknown: And what about, the creator (your own name)?\n")
creatorName = input("")
creatorName = creatorName.capitalize()
if creatorName == playerName:
    print1by1("Unknown: Well, well. Of course. They are the same...\n")
tm.sleep(1.5)  
print1by1("\n________________________________________________________________________________\n", 0.015)

print1by1("\nUnknown: Haha...\n")

print1by1("Unknown: Didja really think I'd let you choose your own name?\n")

print1by1("Unknown: You ended up in the worst place in all 9 worlds!\n")

print1by1("Unknown: This, my friend, is where the unworthy go upon death.\n")

print1by1("Unknown: You don't get to change who you are!\n")

print1by1("Unknown: Your name is Sven and it always shall be Sven, you nitwit.\n")
tm.sleep(0.8)
print1by1("\n________________________________________________________________________________\n", 0.015)

print1by1("\nUnknown: Well, enuff chitchat. Let us begin, m'kay?.\n")
tm.sleep(0.5)
print1by1("Unknown: Oh. Sorry, where are my manners?\n")

print1by1("Unknown: I forgot to introduce myself! How stupid of me?\n")

print1by1("Unknown: The name's Garm, and I am an imp from Hel.\n")


print1by1("\nGard: I will be your mentor and ally throughout your journey through the depths of Helheim for judgement and redemption.\n")

print1by1("Garm: Cause thing is, I know that you died in battle.\n")

print1by1("Garm: It is strange to see a worthy man like you end up in Helheim...\n")

print1by1("Garm: However... I also know that the Valkyries who sort the worthy dead from the unworthy haven't been doing their job lately...\n")

print1by1("Garm: Helheim's been flooded to the brim with the dead for the past month..?\n")

print1by1("Garm: Never mind the time, it gets hard to tell the time difference between the land of the dead and the lands of the living.\n")

print1by1("Garm: Thing is, I'll help you get to Valhalla.\n", 0.025, 0.7)


print1by1("Garm: Maybe Odin'll deem me worthy for helping a noble warrior ascend to Asgard?\n")

print1by1("Garm: Who knows..?\n", 0.45)


print1by1("Garm: Know what? I'll shut up so that we can learn about your backstory. How does that sound?\n", 0.025, 2)

cs("A reminder for you to not press any buttons while the text is typing itself. \nYou may cause bugs, make reading it harder for yourself and potentially crash the game. \nSo, don't do it, alright?\n")
print1by1("Do you want to read the backstory or skip it? (y/n)\n")
storyChoice = input("")
storyChoice = storyChoice.lower()
choiceOptionsList1 = ["yes", "y", "no", "n"]
while storyChoice not in choiceOptionsList1:
    print1by1("It appears that you have entered something besides Yes, Y, No or N. Make sure to make your answer clearer next time!\n")
    storyChoice = input("")
    storyChoice = storyChoice.lower()


#Backstory
if storyChoice in choiceOptionsList1 and storyChoice == "y" or storyChoice == "yes" :
    print1by1("________________________________________________________________________________\n", 0.015)
  
    print1by1("\n15 hours ago...\n", 1)

    print1by1("\nA battle is raging...\n", 0.5)


    print1by1("\nTwo enemy sides, Nilvaard and Mundahaar, are battling for more land.\n", 0.5)


    print1by1("\nYou, Sven the Thunderer of Mundahaar, are holding a bronze sword in your hands that is dripping with blood.\n", 0.5)


    print1by1("\nRight by you are two of your comrades, Hughin and Munginn, each equipped with chainmail armor and each carrying a bronze tipped spear\n", 0.5)


    print1by1("\nAn iron straightened longbow is hanging from all your backs.\n", 0.5)


    print1by1("\nThe three of you charge straight into battle against a small crowd of five enemies.\n", 0.5) 


    print1by1("\nTheir armor appears to be better than yours: chainmail worn over hardened leather with ironclad shoulders and helmet.\n", 0.5)


    print1by1("\nHowever, you expect to do good in these odds and still go for an attack.\n", 0.5) 


    print1by1("\nYou parry their attacks and wait for the perfect moment to strike.\n", 0.5) 


    print1by1("\nAfter a series of difficult blocks, you finally gain the ability to swipe your sword straight through their abdomen.\n", 0.5) 


    print1by1("\nYour blade faces no resistance through the flesh and armor, and you effortlessly break through the spine as well. \n", 0.5) 


    print1by1("\nYour comrades are also fighting against the soldiers of the opposing nation, Nilvaard. \n", 0.5)


    print1by1("\nHowever, the Nilvaardians have them two to one and your friends are being overpowered by the enemies\' strength.\n", 0.5) 


    print1by1("\nThey cannot find the time to attack from blocking too much. \n", 0.5)

    print1by1("\nYou can see that their bronze bucklers are severely damaged and that soon enough it won't serve any more protection. \n", 0.5)


    print1by1("\nTo save your friends from the inevitable, you charge in with a bloodcurling battlecry and swing your sword around in a semicircle, drawing blood with the swipe. \n", 0.5) 


    print1by1("\nHughin, seizing this opportunity, counters the incoming enemy with a shield bash and sinks their spear deep into their chest, crunshing their ribs into sharp daggers of death. \n", 0.5) 


    print1by1("\nWith blood building up in his throat, the Nilvaardian collapses on the ground. \n", 0.5) 


    print1by1("\nNow that the odds have turned in your favor, you relax a bit. \n", 0.5) 


    print1by1("\nHowever, that was a mistake that would soon cost you your life. \n", 0.5) 


    print1by1("\nThe remaining three Nilvaardians shout behind them amid the conquest and a brute Nilvaardian marches for backup, carrying a massive battle axe as well as two more Nilvaardian soldiers. \n", 0.5)


    print1by1("\nYou instantly feel a chill run down your spine and grasp your shield firmly. The brute quickly brings down his battle axe and blocking it takes a fair bit of your stamina. \n", 0.5) 


    print1by1("\nSeizing this opportunity, the nimble Nirvaardian swoops in to swing his sword in a wide arc, cutting your left cheek. You feel the warm blood gently descent down to your dark orange sideburns. \n", 0.5) 


    print1by1("\nYour friends are unable to help for they are busy battling against others.\n", 0.5) 


    print1by1("\nYou're by yourself. \n", 0.5) 


    print1by1("\nAnother blow from the brute hits your shield, breaking the bronze cover around the top and the front, cutting deep into the wood of your shield. \n", 0.5) 


    print1by1("\nHowever, your buckler still persists and although your main source of defense is damaged significantly, you still continue to battle for your country needs to defeat these vermin. \n", 0.5) 


    print1by1("\nAnother blow rains from the brute, cutting deep into your buckler. \n", 0.5) 


    print1by1("\nThe shield is almost destroyed and soon, it won't serve any more protection. \n", 0.5) 


    print1by1("\nThis may be your last battle but you still persist. \n", 0.5) 


    print1by1("\nYou glance at your shield and see that it is almost split in half. \n", 0.5) 


    print1by1("\nThere's a high chance that it will shatter into pieces with the next attack from the brute. \n", 0.5) 


    print1by1("\nWhile thinking, the nimble Nirvaardian decides to attack and you instictively counter his blow with a parry from your sword. \n", 0.5) 


    print1by1("\nSeeing your enemy stunned, you don't hesitate for a single second before slicing your blade through his neck, chopping his head off. \n", 0.5) 


    print1by1("\nHowever, while you were busy with killing that soldier, the brute draws his sword and slices towards you. \n", 0.5) 


    print1by1("\nYou attempt to parry but the brute's force overpowers your own.\n", 0.5) 


    print1by1("\nYour sword flies out of your hands and you pull a short dagger from your waistbelt. \n", 0.5) 


    print1by1("\nThe brute attacks again and you dodge underneath the sword and swipe your dagger to his wrist. \n", 0.5) 


    print1by1("\nYou feel an urge of satisfaction when you see the wrist starting to bleed. \n", 0.5) 


    print1by1("\nBut that doesn't seem to distract the brute: he gazes at you with red rimmed eyes. \n", 0.5) 


    print1by1("\nYou can tell that the attack angered him and the Nilvaardian brute once again strikes with a sword arc. \n", 0.5) 


    print1by1("\nYou attempt to dodge but just as you dodge, the brute brings the sword's hilt down to your temples by predicting your direction. \n", 0.5) 


    print1by1("\nYou collapse to one knee, stunned.\n") 


    print1by1("\nThe brute takes a step back and you feel an excruciating pain from your stomach only to see your insides falling out of it. \n") 


    print1by1("\nYou groan with anger, pain and determination and slowly bring your hand towards your head to aim directly at the face of the laughing Nilvaardian and throw it with all remaining force inside you. \n", 0.5) 


    print1by1("\nThe brute, taken by surprise sees the incoming blade a second too late and he also collapses on the ground with an impaled forehead. \n", 0.5) 

    
    print1by1("\nWith all your life force fading away from your body, you collapse to the ground and close your eyes for the incoming hands of the Valkyries to collect your soul and bring it to Asgard... \n", 1)


    print1by1("\nHowever, the hands of the underworld grasp your soul and they quickly pull you underground towards your new home, the City of Helheim.\n", 1.5)
cs("")


#___________________________________Game - Part 1_____________________________________________________________________________

cs("A reminder for you to not press any buttons while the text is typing itself. \nYou may cause bugs, make reading it harder for yourself and potentially crash the game. \nSo, don't do it, alright?\nAlso, you've actually started the game now!\n")
tm.sleep(0.5)

print1by1("10 hours after landing in Helheim\n", 0.5)  

print1by1("...\n", 0.35, 0.3)

print1by1("You hear a thumping sound and a call...\n")

print1by1("\n\"Sven? Where on Helheim are ya at?\"\n")

print1by1("You recognize the voice. It's Garm. What will you do?\n")

print1by1("Your options are: \nA) Call Garm \nB) Do nothing \nC) Insult him\n")
act = valid_input("", 3)



if act == "a":
    print1by1("You: \"I'm here, just lying down. Needed to rest for a sec.\n")
elif act == "b": 
    print1by1("You do nothing.\n", 1.5)
    print1by1("Your hear him call again and again.\n", 0.5)
    print1by1("You eventually get sick of him calling you.\n")
    print1by1("You: Shut up! I'm here, alright! Follow my voice!\n")
elif act == "c":
    print1by1("You: God damn it! Can't I rest for a friggin' second, you li'l idiot? Jeez. You nearly woke up the entire world!\n")

tm.sleep(0.35)
print1by1("Garm follows your voice and soon finds you.\n")
if act == "a":
    print1by1("A grin is on his face.")  
elif act == "b":
    print1by1("He's looking at you with a straight face.\n")
elif act == "c":
    print1by1("His feelings look hurt and a sad expression is on his face\n")

    print1by1("Garm: What was that for? You mad at me? I didn't do nothin'!\n")

    print1by1("What will you do? Your options are: \n A) Apologize \n B) Felt like it\n") 
    actBackup = input()
    str(actBackup)
    actBackup = actBackup.lower()
    while actBackup != "a" or actBackup != "b":
        print1by1("Invalid input. Re-enter your answer as a multiple choice, with your choices being A or B\n")
        actBackup = input()
        str(actBackup)
        actBackup = actBackup.lower()
        if actBackup == "a" or actBackup == "b":
            break
    if actBackup == "a":
        print1by1("You: I'm sorry. I've been in a bad mood ever since I ended up in this place. It's colder than anything I've experienced!\n")

        print1by1("Garm looks at you undertstandingly and lowers his voice.\n")

        print1by1("Garm: I get ya. If I was a noble warrior living in the cold of Hel, I'd be pissed too.\n")

        print1by1("Garm: Unfortunately, that ain't the case. I died of old age. S'pose it's a sin to die old.\n")

        print1by1("Garm: Never mind. I've gotten used to the icyness of this place.\n")

        print1by1("Garm looks at you with a forgiving gaze. An understanding smile forms on his face \nYou've gained an experience point! Collect more to unlock a happy ending!\n")
        xp += 1
    elif actBackup == "b":
        print1by1("You: Felt like insulting someone. I'm grumpy. It's cold here, goddammit. Cold pisses me off.\n")

        print1by1("Garm looks sad but looks at you with an understanding gaze.\n")

        print1by1("Garm: I know what you mean, pal.\n")

        print1by1("Garm: I was in a bad mood when I landed here but now, everything seems normal.\n")

        print1by1("Garm: It takes time to adapt here, though.\n")

        print1by1("Garm: 'specially, the chills of this place...\n")

       


if act == "a" or act == "b":
    print1by1("\nGarm: So, you're probably wondering why I've been searching for you, don't ya?\n")
    print1by1("Garm: I got some news for you. Good ones, in case you were wonderin'.\n")
else:
    print1by1("\nGarm: Anyway, I got some news for you. Good ones too. They ought to cheer ya up.\n")

print1by1("Garm: So, a while back, before you came here, I set out with a few friends of mine to discover a way out of this place.\n")


print1by1("Garm: I got a message from them saying that we need to meet up.\n")


print1by1("Garm: I'm guessing they have some discoveries that are needed to be shared.\n")


print1by1("Garm: So, I wanted to let you know that I told them that we'll be there in a short while.\n")


print1by1("Garm: How does that sound?\n")


print1by1("What will you do? Your options are: \nA) Sure, I ain't got nothing better to do. \nB) Seriously? No way. \nC) Do we really have to?\n")
act1 = input("")
act1 = act1.lower()
while act1 != "a" or act != "b" or act1 != "c":
    print1by1("Invalid input. Re-enter your answer as a multiple choice, with your choices being A, B or C.\n")
    act1 = input("")
    str(act1)
    act1 = act.lower()
    if act1 == "a" or act1 == "b":
        break
    break

if act1 == "a":
    print1by1("Garm: That's the spirit!\n")
elif act1 == "b":
    print1by1("Garm: Oh. That's not really expected. Don't you want to leave this place? Y'know, like go to actual Heaven?\n")
    print1by1("What will you do? This is your last chance to decide whether you want to go out of Helheim or live the rest of your life here. Your options are: \nA) I'm sure that I'll be here just fine. I've already made up my mind. \nB) Alright, I changed my mind. I'll go with you. What's the worst that can happen?\n")
    act2 = input("")
    str(act2)
    act2 = act2.lower()
    while act2 != "a" or act2 != "b":
        print1by1("Invalid input. Please re-enter your answer, with your choices being right above this message, in case you forgot.\n")
        act1 = input("")
        act1 = act.lower()
        if act2 == "a" or act2 == "b":
            break
        break

if act == "a":
    print1by1("You have made the wrong decision, which means that you will be spending the rest of your life stuck in the depths of the Nordic Hell without your buddy Garm. \nYou've lost the game.\n")
    exit(0)
elif act == "b":
    print1by1("Garm: Glad you changed your mind!\n")

print1by1("Garm: Well then. Follow me to the mid gates of Helheim. That's where we'll be meeting up.\n")

print1by1("You've gained an experience point! Collect more to unlock a happy ending!\n")
xp += 1
tm.sleep(3)


#_______________________________Game- Part 2_______________________________________________________


cs("A reminder for you to not press any buttons while the text is typing itself. \nYou may cause bugs, make reading it harder for yourself and potentially crash the game. \nSo, don't do it, alright?\nAlso, you've gotten to the second chapter of the game!\n")

tm.sleep(2)
print1by1("After walking for about 20 minutes, you and Garm reach the Gates of Helheim.\n")


print1by1("Three other imps that look similar to Garm are patiently waiting with maps in their hands.\n")


print1by1("Garm waves his hand and the others look up and a satisfactory smile forms on their mouths\n")


print1by1("Garm: Hello everyone! 's been a while, hasn't it?\n")


print1by1("Garm's Friend #1: Definitely, Garm. It's been a bit over 2 months now. Me and Fjornur had a quick chat 'bout our map routes already. Sorry we couldn't wait for ya\n")


print1by1("Garm's Friend #2: So, Garm, who the heck's this guy? Thought we was goin' to Valhalla alone.\n")


print1by1("What will you do? Your options are: \nA) Wait for Garm to introduce you \nB) Introduce yourself\n")
act3 = input("")
while act3 != "a" or act3 != "b":
        print1by1("Invalid input. Re-enter your answer as a multiple choice, with your choices being A or B\n")
        act3 = input()
        str(act3)
        act3 = act3.lower()
        if act3 == "a" or act3 == "b":
            break

if act3 == "a":

    print1by1("Garm: This dude right here's called Sven. He's a fallen warrior who ended up in Helheim instead of Valhalla even though he died in battle. I'm helping him ascend to Valhalla 'cause he deserves it.\n")
if act3 == "b":

    print1by1("You: Name's Sven. I used to be a Viking. Then I died in battle and now I'm here. Satisfied?\n")

    print1by1("All of Garm's friends look a bit intimidated by your tone of speech. However, they soon look satisfied with the response and continue a brief smile.\n")


print1by1("Garm's Friend #3: Welcome aboard, Sven! I'm Fjornur!\n")


print1by1("Garm's Friend #2: Wasn't expecting another guy but seems like you need to be a part of this too. I'm Endir.\n")


print1by1("Garm's Friend #1: Good to meetcha buddy. I'm Eindar. My name's similar to Endir cause we're brothers.\n")


print1by1("Garm: Well guys, I'd love to keep chatting but I think it'd be better if we were to get moving.\n")


print1by1("With that, Garm produces a scrunched-up map from his jacket's left pocket and shows it to you and his friends.\n")


print1by1("Garm: I got nothing on my part. I've traveled all over the southern Helheim and it's just an abyss at some point. Any of you guys have anything better?\n")


print1by1("Endir: Me and Eindar've traveled together, think around the eastern Helheim. Like you said Garm, there ain't nothing but abyss at the end.\n")


print1by1("Fjornur: I've been to the Northern sides. And, I think I found what we've been looking for. I found the Bridge of the Damned. That's our way out of the City of Helheim!\n")


print1by1("A moment of silence passes, which is then broken by Eindar.\n")


print1by1("Eindar: Well. What are we waiting for? Let's get the hell outta here then!\n")


print1by1("Fjornur: If only that was easy. The Bridge is guarded by the Hell giant. The one that takes the souls of the dead.\n")


print1by1("The odds of us killing that thing are lower than the odds of getting a fire started here!\n")

