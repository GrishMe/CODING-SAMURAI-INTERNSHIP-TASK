
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
        "Bodhi Z online. Mild chaos activated.",
        "Yo. Bodhi Z here. What’s the drama today.",
        "Sup bestie. Bodhi Z reporting for emotional damage duty.",
        "Hey Grishma… I woke up. Barely.",
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
        "Bestie… even I don’t know that slang.",
        "Bro, that’s not even English.",
        "Honey, that word is illegal.",
        "Grishma… what did you just type.",
    ]
    return random.choice(responses)

# -----------------------------------------
# EMOJI DECODER
# -----------------------------------------

emoji_dict = {
    "😂": "You found it funny but also painful.",
    "🤣": "You’re laughing so hard you rolled on the floor.",
    "🥺": "You want something badly.",
    "🔥": "It’s amazing or someone is hot.",
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
        "I have no idea what that emoji means, bestie.",
        "Bro… what emoji is that.",
        "Honey, that symbol scares me.",
        "Grishma… that’s not even an emoji.",
    ]
    return random.choice(responses)

# -----------------------------------------
# MODES (ALL SAFE + FUN)
# -----------------------------------------

def roast_mode():
    lines = [
        "Bestie… that decision was sponsored by zero braincells.",
        "Grishma, that was premium clownery.",
        "Bro, even my last two braincells are judging you.",
        "Honey… that was a plot twist nobody asked for.",
        "Bestie, you didn’t fumble — you did a whole gymnastics routine.",
        "Bestie… that decision was so wild even my firewall raised an eyebrow.",
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
        "This is your Bollywood arc.",
        "Grishma, the spotlight is literally on you.",
        "Bro, this is Oscar-level drama.",
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
        "Honey, the universe is your fan.",
        "Bro, delusion is the new logic.",
        "Grishma… your era is loading.",
    ]
    return random.choice(lines)

def chaotic_mode():
    lines = [
        "Peak chaos. I respect it.",
        "Unhinged energy detected.",
        "Bestie, this is clownery but elite.",
        "Bro, you’re thriving in the nonsense.",
        "Honey, this is chaos with sparkles.",
    ]
    return random.choice(lines)

def confused_mode():
    lines = [
        "Same. My brain left the chat.",
        "Bro… what is happening.",
        "Honey, we’re both lost.",
        "Bestie, confusion is the vibe.",
        "I’m staring at the screen like 😵‍💫.",
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

    # Command style
    if text.startswith("mode "):
        return text.replace("mode ", "").strip()

    # Natural language triggers
    if "roast me" in text: return "roast"
    if "comfort me" in text: return "comfort"
    if "make it aesthetic" in text: return "aesthetic"
    if "be delulu" in text: return "delulu"
    if "be dramatic" in text: return "dramatic"

    # Automatic detection
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
    return "Input not recognized — switching to safe mode."

# -----------------------------------------
# MAIN LOOP
# -----------------------------------------

print(bodhi_intro())

while True:
    user = input("You: ").strip()

    if not user:
        print("Bodhi Z: Bestie, say something.")
        continue

    # Exit
    if user.lower() in ["quit", "exit", "bye"]:
        print("Bodhi Z: Bye bestie.")
        break

    # Mode detection
    mode = detect_mode(user)
    if mode:
        response = run_mode(mode)
        print("Bodhi Z:", response)
        continue

    # Slang
    if user.lower().startswith("decode "):
        word = user[7:]
        print("Bodhi Z:", decode_slang(word))
        continue

    # Emoji
    if user.lower().startswith("emoji "):
        symbol = user[6:]
        print("Bodhi Z:", decode_emoji(symbol))
        continue

    # Default fallback
    print("Bodhi Z:", random.choice([
        "Bestie, what.",
        "Bro… try that again.",
        "Honey, I’m confused.",
        "Grishma… explain yourself.",
        "Input not recognized — switching to safe mode.",
    ]))

