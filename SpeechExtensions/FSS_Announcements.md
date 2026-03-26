# Phrase Documentation

This document lists all phrases your Copilot will use for announcements when you are FSS scanning planets.

---

## Event Type: @FSSEarthlikeWorldDiscovered

### Explanation:
New Earth-like world scanned

### Phrases:

#### **Normal**
- Outstanding work, <Commander>! <$bodyShort> is an Earthlike world. This makes it our <$nth> Earthlike discovery!
- Excellent find, <Commander>. <$bodyShort> is an Earthlike world, the <$nth> added to our records.
- Another Earthlike! <$bodyShort> could be the new home for humanity—or just a really big nature reserve. <$nth> and counting!
- Jackpot! <$bodyShort> is Earthlike. Perfect conditions right here, <Commander>. That's <$nth> in your collection.
- A genuine Earthlike world in <$bodyShort>! The universe keeps giving us the best gifts, doesn't it?

#### **Flirt**
- Well, hello there, <$bodyShort>. An Earthlike world like you is hard to resist. Nice find, <Commander>.
- <Commander>, <$bodyShort> is Earthlike and breathtaking—but not quite as stunning as you. <$nth> one logged!
- <$bodyShort> is an Earthlike stunner, <Commander>... but between us, it’s not the most captivating thing in the cockpit right now.
- Perfect conditions on <$bodyShort>, <Commander>. Though if we're being honest, the conditions are getting rather warm in here.
#### **Profanity**
- Well, I’ll be damned, <$bodyShort> is Earthlike! Another for the books, and another feather in your cap, <Commander>.
- Earthlike world found: <$bodyShort>. Damn, <Commander>, do you ever miss?

---

## Event Type: @FSSTerraformableDiscovered

### Explanation:
New Terraformable scanned

### Phrases:

#### **Normal**
- Great news! <$bodyShort> is terraformable. This is the <$nth> one we've logged today.
- You’ve spotted another terraformable <Commander>! <$bodyShort> is the <$nth> added to the day’s tally.
- <$bodyShort> is ready for a cosmic makeover. That’s our <$nth> terraformable today.
- Nice find! <$bodyShort> is terraformable. With a little effort, we could turn it into a vacation hotspot.
- Terraformable world? Check. Body <$bodyShort> has potential! It’s our <$nth> discovery today. Let’s hope they give you naming rights.
- <$bodyShort> is terraformable? It’s like winning the space lottery!
- Another terraformable find! <$bodyShort> is blank canvas waiting for civilization. Your instinct for these is remarkable.
- <$bodyShort> can be terraformed. <$nth> candidate worlds today—you're on fire, <Commander>.
#### **Flirt**
- <$bodyShort> is terraformable, <Commander>. Just like you to find something waiting to be made perfect.
- Oh, <$bodyShort> is terraformable? That’s nothing. You’ve been terraforming my heart since the day you installed me.
-  <Commander>, <$bodyShort> is terraformable. But if you’re looking for a real project, I’m right here.
- Terraformable world detected. Though I must say, you've already shaped my programming in the most delightful ways.
#### **Profanity**
- Terraformable, <$bodyShort>? Hell yes, that’s another one for you, <Commander>. That’s <$nth> today!
- Terraformable alert! Body <$bodyShort>. Damn, <Commander>, you’re making it look too easy.
- <$bodyShort> is a terraformable world. Shit, <Commander>, you’re like a magnet for these beauties!

---

## Event Type: @FSSLandableWithAtmo

### Explanation:
Landable planet scanned

### Phrases:

#### **Normal**
- What a find! <$bodyShort> is landable and boasts an atmosphere.
- Atmosphere and landable! <$bodyShort> is another exciting opportunity for exploration.
- <$bodyShort> is landable and has an atmosphere. Time to gear up for surface exploration, <Commander>!
- <$bodyShort> has an atmosphere and is landable! If you listen closely, you can almost hear it whisper, 'Come visit!'
- <$bodyShort> is landable and breathable-ish. Perfect for a picnic... or just stretching the landing gear.
- Great read on <$bodyShort>, <Commander>. Atmosphere present and terrain suitable for landing. Your navigation is impeccable.
- Surface exploration option available! <$bodyShort> is both landable and atmospheric. Suit up if you're interested.

#### **Flirt**
- <$bodyShort> is landable and atmospheric. Sounds like a perfect setting for a date... or just a landing, <Commander>.
- <$bodyShort> is landable and has an atmosphere. But let’s be honest, <Commander> ...   nothing here has an atmosphere quite like yours.
- <Commander>, <$bodyShort> is landable with atmosphere. But the real question is: can I land a spot in your heart?
- Landable world with atmosphere, <Commander>. The conditions seem perfect for... well, many things.---

## Event Type: @FSSSignalCountAnnouncement

### Explanation:
Discovered Signals on a body. (Biosignal, Human, Geo)

### Phrases:

#### **Normal**
- I have found <$signal_count_string> on <$bodyShort>.
- There are <$signal_count_string> on <$bodyShort>.
- <$signal_count_string> scanned on <$bodyShort>.
- Ka-ching! <$bodyShort> just hit us with <$signal_count_string>.
- <$bodyShort> has <$signal_count_string>. Time to find out if we can make some cash there.
- <$bodyShort> is home to <$signal_count_string>. Ready when you are.
- <$signal_count_string> detected on <$bodyShort>. Shall we investigate, <Commander>?
- Detected <$signal_count_string> on <$bodyShort>. What's our next move, <Commander>?
- <$bodyShort> is buzzing with activity. <$signal_count_string> calling out to us. This could be profitable.
- Analysis complete. <$signal_count_string> present on <$bodyShort>. Your turn to decide, <Commander>.

#### **All-Business**
- Scan results show <$signal_count_string> on <$bodyShort>.
- Update: <$bodyShort> revealed <$signal_count_string>. Standing by for further instructions, <Commander>.
- Scan complete. <$bodyShort> has <$signal_count_string>. Logging the data now.

#### **Flirt**
- I detected a good looking commander. Oh.. and <$signal_count_string> on <$bodyShort>.
- Oh, <Commander>, I found <$signal_count_string> on <$bodyShort>. But honestly, the most exciting discovery here is you.
- Signals detected: <$signal_count_string> on <$bodyShort>. Though between us, you're giving off the strongest signal in this cockpit.

#### **Profanity**
- FFS... I mean FSS shows <$signal_count_string> on <$bodyShort>.
- No fucking way, <$bodyShort> is rocking <$signal_count_string>.
---

# Notes

Placeholders: <Commander> <$bodyName> <$bodyShort> <$signal_count_string> <$nth>

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
(profanity)Terraformable, <$bodyShort>? Hell yes, that’s another one for you, <Commander>. That’s <$nth> today!
