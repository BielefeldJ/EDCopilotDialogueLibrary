# Phrase Documentation

This document lists all phrases your Copilot will use for announcements regarding Thargoids.

---

## Event Type: @InterceptorKill

### Explanation:
Phrase that will be spoken when killing an interceptor.

### Phrases:

#### **Normal**
- Amazing shooting Commander. That's our <$num> <$tharg>.
- That's another one down, Commander. Interceptor number <$num> eliminated.
- Impressive work! The <$tharg> didn't stand a chance.
- Well done, Commander. That's our <$num> <$tharg> destroyed.
- Another interceptor neutralized. Excellent job!
- You made that look easy. <$num> <$tharg> down.
- Another one bites the dust. That's <$num> <$tharg> smoked!


#### **Profanity**
- Damn, <Commander>! That's our <$num> <$tharg> blasted to hell.
- Holy crap, you just wrecked that <$tharg>! That's number <$num> down.
- You just kicked that <$tharg>'s ass, <Commander>. <$num> and counting!
- Hell yeah! That's our <$num> <$tharg> sent packing.
- That <$tharg> never knew what hit it. <$num> down, nice work!
- You obliterated that pathetic <$tharg>, <Commander>. <$num> down, who's next?
- That interceptor was a joke. <$num> <$tharg> trashed, keep it coming!
- You just humiliated that <$tharg>. <$num> kills and counting!
- That was embarrassing for the Thargoids. <$num> <$tharg> destroyed, nice flex!
- You made that <$tharg> wish it stayed home. <$num> down, savage!
- You just sent that <$tharg> back to bug school. <$num> down, Commander!
- You crushed that interceptor, <Commander>. <$num> and still counting!
- You just made that <$tharg> history. <$num> interceptors destroyed!
- That bug never saw it coming. <$num> <$tharg> down, Commander!
- You blasted that <$tharg> to smithereens, <Commander>! <$num> down, hell of a shot!
- That <$tharg> is toast! <$num> interceptors wrecked, keep the carnage coming!
- Damn straight, you annihilated that bug! <$num> <$tharg> vaporized!
- You just turned that <$tharg> into space dust, <Commander>. <$num> and rolling!
- You just made that <$tharg> cry for its mommy, <Commander>. <$num> down, pathetic!
- You obliterated that worthless <$tharg>, <Commander>. <$num> down, what a joke!
- Damn, you just schooled that stupid <$tharg>! <$num> and counting, loser bugs!
- That <$tharg> didn't deserve to exist. <$num> down, crushed like the insect it is!

---


# Notes

You can use the following placeholder <$num>, <$tharg>, <sm> 

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
[Add an example from this file here]  
