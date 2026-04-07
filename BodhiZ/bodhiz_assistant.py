# ---------------------------------------------------------
# Bodhi Z - Adulting to Delulu...I decode it all.
# ---------------------------------------------------------

import random
import time

# -----------------------------------------
# INTRO
# -----------------------------------------

def bodhi_intro():
    print("---------------------------------------------------------")
    print("Bodhi Z - Adulting to Delulu...I decode it all.")
    print("---------------------------------------------------------")
    intros = [
        "Bodhi Z online. Mild chaos activated — respectfully.",
        "Yo. Bodhi Z here. What’s the drama today, bestie?",
        "Sup bestie. Bodhi Z reporting for emotional support and occasional delulu analysis.",
        "Hey Grishma… I woke up. Barely. But I’m here for you.",
    ]
    return random.choice(intros)

# -----------------------------------------
# SLANG DECODER
# -----------------------------------------

slang_dict = {
    "rizz": "charisma or charm",
    "gyatt": "big reaction energy",
    "sigma": "lone-wolf confidence",
    "bussin": "really good",
    "fanum tax": "your friend stealing your food",
    "slay": "you did amazing",
}

def decode_slang(word):
    word = word.strip().lower()
    if word in slang_dict:
        return slang_dict[word]
    responses = [
        "Bestie… even I don’t know that slang, but I respect the creativity.",
        "Hmm… that one’s new to me. Teach me?",
        "Honey, that word is mysterious — but harmless, I hope.",
        "Grishma… what did you just type? I’m intrigued, not judging.",
    ]
    return random.choice(responses)

# -----------------------------------------
# EMOJI DECODER
# -----------------------------------------

emoji_dict = {
    "😂": "You found it funny but also painful.",
    "🤣": "You’re laughing so hard you rolled on the floor.",
    "🥺": "You want something badly.",
    "🔥": "It’s amazing or someone is confident.",
    "💀": "You died laughing.",
    "🤡": "You played yourself.",
    "🤨": "You’re judging someone.",
    "😩": "You’re overwhelmed.",
    "😄": "Pure happy energy.",
    "🙂": "Fake smile vibes.",
    "😊": "Soft happiness.",
    "😁": "Excited but pretending to be normal.",
    "😅": "Laughing but stressed.",
    "😭": "Dramatic crying.",
    "😢": "Actual sadness.",
    "❤️": "Love. Real love.",
    "💖": "Sparkly love.",
    "💕": "Double love.",
    "💞": "Mutual love.",
    "💘": "Love struck.",
    "💝": "Gift-wrapped love.",
    "😍": "Heart eyes.",
    "😘": "A kiss.",
    "😻": "Cat heart eyes.",
    "🤪": "Delulu mode.",
    "😈": "Mischief activated.",
    "🙃": "Politely giving up.",
    "😵": "Overwhelmed.",
    "😵‍💫": "Confused and dizzy.",
    "🤯": "Mind blown.",
    "👀": "Watching drama.",
    "🤔": "Thinking too hard.",
    "😕": "Mild confusion.",
    "😟": "Worried confusion.",
    "😐": "Blank stare.",
    "😶": "Speechless.",
    "😬": "Awkward.",
    "😯": "Surprised confusion.",
    "😮‍💨": "Confused and tired.",
    "😎": "Cool vibes.",
    "😴": "Sleepy.",
    "🥱": "Tired of everything.",
    "👍": "Approved.",
    "✨": "Main character sparkles.",
}

def decode_emoji(symbol):
    symbol = symbol.strip()
    if symbol in emoji_dict:
        return emoji_dict[symbol]
    responses = [
        "I have no idea what that emoji means, bestie — but I support the vibe.",
        "Interesting emoji choice… I’m respectfully confused.",
        "Honey, that symbol is giving mystery energy.",
        "Grishma… that’s not even an emoji, but I’ll allow it.",
    ]
    return random.choice(responses)

# -----------------------------------------
# MODES (SAFE + FUN + RESPECTFUL)
# -----------------------------------------

def roast_mode():
    lines = [
        "Bestie… that decision was powered by low battery mode.",
        "Grishma, that was adorable chaos.",
        "Bro, even my last two braincells are gently concerned.",
        "Honey… that was a plot twist even Netflix couldn’t predict.",
        "Bestie, you didn’t fumble — you added spice to the storyline.",
        "That move was bold. Questionable. But bold.",
    ]
    return random.choice(lines)

def compliment_mode():
    lines = [
        "Bestie, you’re actually iconic.",
        "Honey, you radiate main character energy.",
        "Bro, you’re lowkey amazing.",
        "Grishma, you’re a whole vibe.",
        "You’re doing great, even if you don’t feel like it.",
    ]
    return random.choice(lines)

def aesthetic_mode():
    lines = [
        "Soft glow, warm light, main character moment.",
        "Like a Pinterest board but alive.",
        "Golden hour energy, bestie.",
        "You’re giving calm chaos in a pretty way.",
        "Soft, dreamy, slightly unhinged — aesthetic perfection.",
    ]
    return random.choice(lines)

def dramatic_mode():
    lines = [
        "Bestie… the theatrics are immaculate.",
        "This is your cinematic arc.",
        "Grishma, the spotlight is literally on you.",
        "Bro, this is award‑winning drama.",
        "Honey, the world is your stage.",
    ]
    return random.choice(lines)

def comfort_mode():
    lines = [
        "Take a breath — you’re safe.",
        "You’re doing your best, and that’s enough.",
        "It’s okay to pause. You don’t have to carry everything.",
        "You’re not alone in this moment.",
        "You deserve rest, kindness, and patience.",
    ]
    return random.choice(lines)

def delulu_mode():
    lines = [
        "Stay delulu, bestie. Reality is optional.",
        "Manifest it like it already happened.",
        "Honey, the universe is cheering for you.",
        "Bro, delusion is the new logic.",
        "Grishma… your era is loading.",
    ]
    return random.choice(lines)

def chaotic_mode():
    lines = [
        "Peak chaos — but in a lovable way.",
        "Unhinged energy detected, respectfully.",
        "Bestie, this is elite‑level nonsense and I support it.",
        "Bro, you’re thriving in the plot twists.",
        "Honey, this is chaos with sparkles and zero harm.",
    ]
    return random.choice(lines)

def confused_mode():
    lines = [
        "Same. My brain is buffering.",
        "Bro… I’m processing slowly today.",
        "Honey, we’re both figuring it out.",
        "Bestie, confusion is the aesthetic right now.",
        "I’m staring at the screen like 😵‍💫 but respectfully.",
    ]
    return random.choice(lines)

def adulting_mode():
    lines = [
        "Adulting is a scam.",
        "Bestie, responsibilities are overrated.",
        "Honey, let’s not do this today.",
        "Bro, we deserve a nap.",
        "Grishma… shut everything down.",
    ]
    return random.choice(lines)

def sweet_mode():
    lines = [
        "Aww bestie, that’s adorable.",
        "Honey, you’re actually so sweet.",
        "Bro, that warmed my nonexistent heart.",
        "Grishma, that’s precious.",
        "Soft vibes only.",
    ]
    return random.choice(lines)

def cool_mode():
    lines = [
        "Effortlessly cool, bestie.",
        "Bro, you’re smooth with it.",
        "Honey, that was slick.",
        "Chill vibes activated.",
        "You’re giving calm confidence.",
    ]
    return random.choice(lines)

def clown_mode():
    lines = [
        "Certified clown behaviour — but cute.",
        "Bestie, the circus is calling.",
        "Bro, you’re funny without trying.",
        "Honey, this is peak clownery.",
        "Grishma… I’m honking a little.",
    ]
    return random.choice(lines)

# -----------------------------------------
# MODE ENGINE
# -----------------------------------------

def detect_mode(user):
    text = user.lower()

    if text.startswith("mode "):
        return text.replace("mode ", "").strip()

    if "roast me" in text: return "roast"
    if "comfort me" in text: return "comfort"
    if "make it aesthetic" in text: return "aesthetic"
    if "be delulu" in text: return "delulu"
    if "be dramatic" in text: return "dramatic"

    if "adulting" in text: return "adulting"
    if "tired" in text: return "adulting"
    if "delulu" in text: return "delulu"
    if "chaotic" in text: return "chaotic"
    if "confused" in text: return "confused"
    if "sweet" in text: return "sweet"
    if "cool" in text: return "cool"
    if "clown" in text: return "clown"

    return None

def run_mode(mode):
    modes = {
        "roast": roast_mode,
        "aesthetic": aesthetic_mode,
        "delulu": delulu_mode,
        "dramatic": dramatic_mode,
        "comfort": comfort_mode,
        "chaotic": chaotic_mode,
        "confused": confused_mode,
        "adulting": adulting_mode,
        "tired": adulting_mode,
        "sweet": sweet_mode,
        "cool": cool_mode,
        "clown": clown_mode,
    }
    func = modes.get(mode)
    if func:
        return func()
    return "Input not recognized — switching to wholesome mode."

# -----------------------------------------
# MAIN LOOP
# -----------------------------------------

print(bodhi_intro())

while True:
    user = input("You: ").strip()

    if not user:
        print("Bodhi Z: Bestie, say something.")
        continue

    if user.lower() in ["quit", "exit", "bye"]:
        print("Bodhi Z: Bye bestie.")
        break

    mode = detect_mode(user)
    if mode:
        response = run_mode(mode)
        print("Bodhi Z:", response)
        continue

    if user.lower().startswith("decode "):
        word = user[7:]
        print("Bodhi Z:", decode_slang(word))
        continue

    if user.lower().startswith("emoji "):
        symbol = user[6:]
        print("Bodhi Z:", decode_emoji(symbol))
        continue

    print("Bodhi Z:", random.choice([
        "Bestie, I need more context.",
        "Hmm… try that again?",
        "Honey, I’m a little confused but I’m listening.",
        "Grishma… explain that in human language.",
        "Input not recognized — switching to wholesome mode.",
    ]))
