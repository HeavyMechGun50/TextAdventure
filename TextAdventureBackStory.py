#Importing necessary modules
import time as tm
import random as rd
import sys
import os

def cs(notiftext):
    os.system('clear')
    print(notiftext)
    print("\n_____________________________________________________________________________________________________________\n\n",)


def print1by1(text, lineDelay=0.35, delay=0.025):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        tm.sleep(delay)
    tm.sleep(lineDelay)   







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