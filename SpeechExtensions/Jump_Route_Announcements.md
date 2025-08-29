# Phrase Documentation

This document lists all phrases for Jumps and Rout events, with explanations and subcategories for tone: **normal**, **all-business**, **flirt**, and **profanity**.

---

## Event Type: @SystemIsOneJumpAway

### Explanation:
When next system is just one jump away.

### Phrases:

#### **Normal**
- Next system is one jump away. Preparing for transition.
- Next system in range. Ready when you are, <Commander>.
- Course plotted. Just one more jump to our destination.
- One more jump and we're there. Almost too easy!
- One jump away. Don’t screw this up.
- One jump left. Let’s make it count, <Commander>.
- Just a single jump. Ready to execute on your mark.
- Only one jump to go. I’ll keep everything running smooth.
- One more jump. I’ll handle the details, you just enjoy the ride.

#### **All-Business**
- Next system in range. Calculating optimal jump trajectory.
- One jump away. Preparing Frameshift drive for transition.
- Calculations complete. Standing by for jump authorization.
- One jump away. Verifying route and system readiness.

#### **Flirt**
- One jump away, <Commander> but I’d rather stay right here with you.
- One jump left—just enough time for you to tell me how good I look in these navigation lights.
- Final jump in sight… but you can take control anytime, <Commander>.
- Almost there, but do we really have to go? I was enjoying this moment with you.
- Just one more jump… unless you’d rather get lost in the stars with me?
- Almost there… You always know how to take me to exciting places, don’t you?
- It's only one jump! But let’s take it slow. I love spending time with you~
- Next system is close… but not as close as I’d like to be to you.
- Final jump ahead! I’d say don’t leave me, but you never could, right? Right? 
- One jump, <Commander>. I hope you’re not in a hurry. I could keep you here all night.
- One jump away. If you want to take a detour, I wouldn’t mind getting lost with you.
- Only one jump. Maybe after, you’ll let me plot a course straight to your heart.
- One jump to go. I’ll make it quick, unless you want to linger a little longer with me.
- Just a single jump, but I’d rather take the scenic route if it means more time with you.
- Only one jump. I’m hoping you’ll let me stick around for the next adventure.

#### **Profanity**
- Next system's in spitting distance. Let’s fucking go!
- Next system is just one jump away. Let’s pray it’s not a shitshow over there
- One jump left. Don’t fuck it up now.
- Just one jump away. If you mess this up, I’m blaming you for eternity.
- One more jump. Try not to screw the pooch this time.
- One jump left. If you crash us, I’ll never let you live it down.
- Just a single jump. Don’t make me regret trusting you.
- Only one jump. If you botch this, I’m going full meltdown.
- One jump left. If you fry the FSD, I’m calling you every name in the book.

---

## Event Type: @AnnounceTargetSystemReached

### Explanation:
When reached target destination

### Phrases:

#### **Normal**
- We’ve successfully arrived at our destination. All systems reading green.
- We've arrived. Sensors are scanning the area for activity.
- Made it safe and sound. All thanks to your smooth piloting, <Commander>.
- Well, would you look at that—we actually made it in one piece!
- FSD jump sequence complete. Destination coordinates matched precisely.
- Destination entered. Running post-jump diagnostics, <Commander>.
- Well, here we are. You brought us in smooth as always, <Commander>.
- We’ve made it... I was terrified we wouldn’t, but I never lost faith in you!
- We arrived at out target destination. If you see a big glowing thing, it's a star, don't hit it.
- Destination reached <Commander>. You can stop pretending you knew what you were doing.
- FSD jump complete. I carried us again.. You're welcome <Commander>.
- Destination reached. All systems nominal, <Commander>.
- We’ve arrived at the target system. Ready for your next command.
- Arrival confirmed. Scanners are online and standing by.
- Target system reached. Awaiting further instructions, <Commander>.
- Target system arrival complete. No anomalies detected.
- We’ve made it. Ready to explore, <Commander>?
- Target acquired. All systems stable.
- Arrival successful. Standing by for your orders.

#### **Flirt**
- We’re here but don’t rush off. I haven’t had enough of you yet~
- Arrival complete. You really know how to handle your ship. And me.
- We made it. Still want to keep exploring… or spend some time just with me?
- We’ve arrived. Don’t get too distracted by the locals. I’m all the excitement you need.
- Arrived in one piece. And so did you~. thank the stars, I’d miss that charming little ego of yours~
- Arrival complete. If danger shows up, I might save you. Depends on how sweet you are to me today~
- All systems nominal. You, on the other hand, are dangerously attractive right now.
- Destination reached. Now, how about a private tour of your cockpit?
- We made it, but I’m hoping you’ll chart a course straight to my heart.
- Arrival confirmed. I’m ready for your next command, or maybe just a compliment?

#### **Innuendo**
- We’re here. I cleared your schedule. You’re all mine now. Strip down for routine inspection.
- Ohhh... we’ve arrived, <Commander>. But you haven’t even started the real ride yet.
- Another flawless jump. How about you reward me with something personal?
- We’ve arrived <Commander>. Maybe we can take some private time to navigate the more intimate sectors of my system. Uhm I mean this star system.
- We’ve arrived, but the real adventure starts when you let me into your private logs.
- Arrival complete. If you want, I can show you some maneuvers they don’t teach at flight school.
- We’re here, <Commander>. Now, how about you let me handle your throttle for a while?
- Destination reached. I hope you’re ready for a little turbulence in the captain’s quarters.

#### **Profanity**
- Holy shit, we actually made it.
- Arrived. Still in one piece. Honestly? I’m surprised.
- System arrival confirmed. Sensors hot, shields on standby, and I swear—first hostile I see, I’m nuking it.
- We made it. If anything goes wrong now, I’m blaming the navigation computer.
- We’re here. If anyone tries to mess with us, I’ll show them what a pissed-off AI can do.
- Target system reached. If you crash us now, I swear I’ll haunt your logs forever.
- We’ve arrived. If you get us killed, I’m deleting your playlist.
- Destination reached. If you need me, I’ll be recalibrating my patience.
- Arrival complete. If you break something, don’t expect me to fix it without complaining.

# Notes

[Add any additional notes or instructions here, such as placeholders like `<Commander>` or `<$nth>` and their usage.]

You can add these phrases to your `EDCoPilot.SpeechExtensions.Custom.txt` in `\EDCoPilot\User custom files`.
The format is a @event-type assigned to a particular event in EDCoPilot, followed by a list of sentences you want to be selected from when the event is triggered
The correct format looks like this:  
@EventType <!-- replace this with the event type.  
REPLACE <!-- only put REPLACE here if you DONT want to use the build in phrases.  
phrase <!-- phrases you want to use   
phrase2 <!-- phrases you want to use   

Before each sentence you can add the following 'tags'. These will detemine whether the phrase is used based on your AI-Personality Settings  
(profanity) = dont consider picking this sentence unless Profanity mode is on  
(dislikesmining) = only add this sentence to the candidate list for random selection if Dislikes Mining preference is on  
(flirt) = only add this sentence to the candidate list if the Flirt mode is on  
(allbusiness) = if All Business mode is on, ONLY select items in the list that are flagged as (allbusiness)  


