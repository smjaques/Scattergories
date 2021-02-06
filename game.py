import random
import string

categoryString = "Organs,African Animals,Amphibians,Animals That are Blue,Arctic Animals,Birds,Dangerous Animals,Dog Breeds,Mammals,Pets,Slow Animals,Colors,Famous Paintings,Art Equipment,Medical Terms,Diseases,Medicine Names,Office Items,Clothing Worn by Cowboys,Men's Clothing,Women's Clothing,Ways to Entertain Oneself,Reality TV Show,Cartoon Characters,Products Sold on Comercials,Actors,Actresses,Fantasy Movies,Disney Movies,Horror Movies,Sports Teams,Sports Terms,Olympic Sports,Beverages,Beer Brands,Alcoholic Drinks,Breakfast Foods,Candy,Condiments,Types of Cheese,Desserts,Fast Food Restaurants,Ice Cream Flavors,Junk Food,Sandwiches,Spices,Flowers,Vegetables,Trees,Countries,Hot Places,Rivers or Seas,US Capitals,Politicians,Holiday Songs,Holiday Activities,Bathroom Accessories,Things You Sit On,Kitchen Appliances,Contractions,Nouns,Words With a Double Letter,Authors,Book or Movie Characters,Greek Gods,Units of Measure,Songs,Female Singers,Male Singers,Elements,Insects,IPhone Apps,Websites,Things That Are Cold,Things That Are Flat,Things That Are Round,Things That Are Made of Glass,Things That Are Yellow,Expensive Things,Things Found At a Circus,Things That Smell Bad,Mechanic's Tools,Board Games,Hobbies,Ways to Get From Here to There"
categoryString2 = "Things in a Mystery Novel,Computer Lingo,Loud Things,Math Terms,Underground Things,Found in New York City, Things in Fairy Tales,Healthy Foods,Party Things,Reasons to Skip School/Work,Things on a Hiking Trip,Things That Fly,Found at a Salad Bar,Words Ending in 'ly',Things With Motors,Things at a Zoo,Personality Traits,Things You Throw Away,Occupations,Words Associated With Money,Things You Shout,Things You Replace,Baby Foods,Notorious People,Fruits,Toys,Bodies of Water,Halloween Costumes,Words Associated With Exercise,Heroes,Terms of Endearment,Kinds of Dances,Things That are Black,Dairy Products,Items in Your Purse/Wallet,World Records,Street Names,Items in a Refrigerator,Farm Animals,Athletes,Things Found on a Map,Car Parts,Articles of Clothing,Famous Females, Famous Males,People in Uniform,Languages,School Supplies,Things Found in the Ocean,Furniture,Musical Instruments,Patterns (i.e. Chevron),School Subjects,Fish,Things in This Room,Historical Figures,Something You're Afraid Of,Book Titles,Things You're Allergic To,Nicknames,Things With Tails,Things That Are Sticky,Bad Habits,Things That Are Bright,Things on a Safari,Holiday Things,Things in Pairs or Sets,Things in Las Vegas,Harry Potter Characters,Menu Items,Kinds of Candy,Something You Keep Hidden,Worn Above the Waist,Things in Outer Space,Found in a College Dorm,Things at an Amusement Park,Things at a Picnic,Things That are Soft,Things at a Wedding,Colleges/Universities,Tech Companies,Pizza Toppings,Reasons to Divorce,Stores in the Mall,US States,TV Show,College Majors,Major Mistakes,Something You'd Put Vanilla In,Illegal Acts/Crimes,Gender-Neutral Names,Things That Are Pointy,Honeymoon Destinations,Titles People can Have,California Cities,Reasons to Call 911,Car Makes (i.e. Ford),Villains"
familyCategoryString = "Words Dad Made Up,Jaques Relative/Family Member,Things in the Laundry Room,Ways We (Jaques') Have Hurt Ourselves,Things Mom Has Yelled About,Mom's Famous Words or Sayings,Dad's Famous Words or Sayings,Jaques Family Jokes,Things Mom Hates,Things Dad Hates,Movies Cori Quotes Often,Places We (Jaques) Have Been,Embarassing Things Someone (Jaques) Has Done,Job Professions Kenzy Would Be Bad At,Incidents Where Sydney Couldn't Keep Her Mouth Shut,Items of Clothing That a Sister has Stolen From Another,Teachers Any Jaques Has Had,Reasons Jaques Sisters Have Fought,States a Jaques Has Been In Mass (i.e. drunk),Ways Taylore Has Hurt Herself,Times Cori Has Had Her 'Foot in Her Mouth',Things Cori is Good At,Things Taylore is Good At,Things Kenzy is Good At,Things Sydney is Good At"
print(str(len(categoryString) + len(categoryString2) + len(familyCategoryString)))
allLetters = string.ascii_letters
easyLetters = "A,B,C,D,F,G,H,J,K,L,M,N,P,R,S,T,W"
easyLetters = easyLetters.split(",")
roundColors = "#94dbe3,#f263b6,#6376f2,#43c234,#edae39,#cc3333,#4287f5,#82ed86"
roundColors = roundColors.split(",")

Gcategories = categoryString.split(",")
Gcategories = Gcategories + categoryString2.split(",")
famCategories = familyCategoryString.split(",")

def getGameList(fam):
    if fam == 'true':
        return Gcategories + famCategories
    return Gcategories


def getLetterGroup(allLet):
    if allLet:
        return list(allLetters)
    return easyLetters

def getRoundColor():
    return random.choice(roundColors)
