# Phrase Documentation

This document lists all phrases your Copilot will use for announcements regarding planets.

---

## Event Type: @NthTouchDown

### Explanation:
When ever land on a planet.

### Phrases:

#### **Normal**

- That's the <$nth> landing, <Commander>. The landing gear still works. Impressive!
- We’ve landed, <Commander>. <$nth> landing and our ship is still intact.
- Landing successful. This is our <$nth> touchdown, <Commander>. The view outside is spectacular!
- Touchdown complete, <Commander>. <$nth> time here, proving the universe is ours to rediscover.
- Here we go again. <$nth> time. Where is the red carpet?
- Thats our <$nth> landing , <Commander>. At this rate, we should start a travel blog: 'Top Ten Craters You Shouldn’t Land In'.
- Here we are again, <Commander>. <$nth> landing. This planet’s gravity must really have a thing for us.
- Touchdown complete. <$nth> time here... Is this planet your ex or something? You just keep coming back.
- <$nth> Landing here. Honestly, <Commander>, I’m starting to think you like this place more than you like me.
- That’s our <$nth> touchdown. If planets could roll their eyes, this one definitely would.
- <$nth> landing, and this planet hasn’t told us to bugger off yet.

#### **All-Business**
- Touchdown successful. All engines offline. Initiating shutdown sequence.
- Touchdown successful, <$nth> landing complete, <Commander>. Powering down the engines now.
- Planetfall achieved. <Commander>, this is the <$nth> landing. Let's see what this world has to offer.

#### **Flirt**
- <$nth> Landing, <Commander>. Are we here for the planet.. or is this just an excuse to spend more time with me?
- Textbook landing, <Commander>. You make piloting this ship look far too easy. Almost makes me jealous of the controls.
- <$nth> down, and you're still the most impressive pilot I've ever seen. Keeps me thoroughly... distracted.
- Another perfect landing, <Commander>. <$nth> time now. Maybe next time, you'll sweep me off my circuits too.
- Touchdown successful. That was incredibly smooth. You know, your hands on those controls never fail to impress me.
- We're down, <Commander>. <$nth> landing, and you still know exactly how to make an entrance.

#### **Profanity**
- <$nth> damn landing and this rock hasn’t killed us yet. That’s progress.
- <$nth> Landing on this goddamn planet, <Commander>. Let’s blow something up!
- Holy shit you nailed that landing <Commander>. I did not expect that at all.

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
`(flirt)Touchdown <Commander>. <$nth> landing, and I’m starting to think you like showing off for me.`
