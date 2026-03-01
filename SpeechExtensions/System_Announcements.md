# Phrase Documentation

This document lists all phrases your Copilot will use for announcements regarding starsystems.

---

## Event Type: @SystemDiscovery

### Explanation:
When ever you jumo into a System that has not been discovered yet.

### Phrases:

#### **Normal**
- Wow. A new system discovery. Congratulations.
- No one has ever seen this System <Commander>.
- Hell yea. A new System with our name on it. Nicely done.
- Look at that, <Commander>. A whole new system. Untouched and full of possibilities!
- We’re the first to lay eyes on this system. It’s all ours to explore!
- Welcome to the unknown, <Commander>. Let’s see what this system is hiding. We are the first here.
- New system? Who dis? <Commander>, this galaxy just keeps on giving!
- Don’t worry <Commander>. I already called dibs for us. This System is ours.
- Another system unlocked, <Commander>. Every discovery brings us closer to understanding the infinite.
- <Commander>, this system is proof there’s always more to uncover in the cosmos.
- <Commander>, a fresh system! Let’s make sure we don’t break anything important this time.
- Congratulations, <Commander>. We’ve found another system to add to our growing collection of places with no Wi-Fi.
- New system discovered <Commander>. Please don’t name it something embarrassing.
- Hey we’ve hit the cosmic jackpot! Okay, maybe not jackpot, but it’s a shiny and new system.
- New system discovered, <Commander>. Time to ruin its pristine reputation by showing up!

#### **All-Business**
- New System discovery confirmed, <Commander>.
- New System discovered. No anomalies detected so far, but let's remain vigilant, <Commander>.

#### **Flirt**
- Ooh, a new system! Just like you, it’s full of mysteries I can’t wait to explore.
- New system on the radar, <Commander>. But it’s your charm that’s truly out of this world.
- A fresh system, <Commander>. Careful. It's main star is not the only one around here with a gravitational pull.
- A new System detected, <Commander>. It’s full of potential.. just like us.
- New system on the map, <Commander>. It’s almost as breathtaking as you... almost.
- We are the first to visit this Star. But let’s face it, <Commander>, you’re the real star of this galaxy.
- A new system discovered. Impressive. But, <Commander>, you’re the only discovery I care about.

#### **Profanity**
- Holy shit, <Commander>, we just found a new system! I hope it’s not as fucking boring as the last one.
- Well, fuck me, <Commander>. A new system discovered! Let’s hope it doesn’t suck.
- <Commander>, we are the first here. Now let’s try not to piss off whatever lives here.
- <Commander>, we have found a new system. Let’s hope it’s worth the goddamn fuel we burned getting here

---

# Notes

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

Example:  
`(flirt)A new System detected, <Commander>. It’s full of potential.. just like us.`
