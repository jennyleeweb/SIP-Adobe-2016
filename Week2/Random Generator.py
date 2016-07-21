import random
food=["Chicken", "Beef", "Pork", "Eggs", "Shrimp", "Salmon", "Broccoli", "Tomato", "Tofu", "Taro"]
cooking_style=["Sauteed", "Fried", "Tempura", "Baked", "Steamed", "Roasted", "Grilled", "Toasted", "Boiled", "Szechuan"]
taste=["Spicy", "Creamy", "Sour", "Sweet", "Salty", "Crunchy", "Chewy", "Silken", "Delightful", "Minty"]
number=["1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10."]

def menu_item(number, taste, cooking_style, food):
    print("Menu")
    for i in range(10):
        random_food=random.randint(0,len(food)-1)
        random_cooking=random.randint(0,len(cooking_style)-1)
        random_taste=random.randint(0,len(taste)-1)
        print(number[i]+' '+taste[random_taste]+' '+cooking_style[random_cooking]+' '+ food[random_food])
menu_item(number, taste, cooking_style, food)

article=["The", "A", "One"]
adj=["Cool", "Basic", "Little", "Big", "Flashy", "Cheetah"]
noun=["Girls", "Boys", "Petal", "Trucks"]
def band_name(article, adj, noun):
    print("Band Names")
    for i in range(8):
        random_article=random.randint(0, len(article)-1)
        random_adj=random.randint(0, len(adj)-1)
        random_noun=random.randint(0, len(noun)-1)
        print(article[random_article]+' '+adj[random_adj]+' '+noun[random_noun])
band_name(article, adj, noun)

syllables5=["The many flowers", "Beautiful beaches", "Very sweet peaches", "Happy big hippos", "Staring at the stars", "Happy healthy horse", "Pretty peonies", "Soft fluffy puppy", "Cozy in winter", "Bright breezy summer"] 
syllables7=["Coffee is satisfying", "Sand slipping through the sandals", "Hammock swinging on palm trees", "Ocean waves slam into feet", "Smelling the strong scent in air", "Camels roaming the Sahara", "Snow falling on the bare trees", "Warm water is refreshing", "The volcano erupts now", "The sky turns blue and purple"]
def haiku(syllables5, syllables7, syllables5):
    user_title= input(Enter a title.)
    for i in range(3):
        line1=random_5=random.randint(0, len(syllables5)-1)
        line2=random_7=random.randint(0, len(syllables7)-1)
        5syllables.remove(line1);
        line3=random_5=random.randint(0, len(syllables5)-1)
        print(line1 \n line2 \n line3)
haiku(syllables5, syllables7, syllables5)

        
    
    
