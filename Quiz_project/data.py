# List of 100 True/False questions for 10-year-old kids
# Categories: Math, Animals, General Knowledge

question_data = [
    # --- Math Questions (Approx. 30) ---
    {"text": "10 multiplied by 5 is 50.", "answer": "True"},
    {"text": "A triangle has 4 sides.", "answer": "False"}, # Geometry
    {"text": "100 divided by 10 is 10.", "answer": "True"},
    {"text": "5 plus 15 equals 25.", "answer": "False"},
    {"text": "A square has four equal sides.", "answer": "True"}, # Geometry
    {"text": "There are 60 seconds in a minute.", "answer": "True"}, # Time
    {"text": "Half of 50 is 20.", "answer": "False"},
    {"text": "A circle has corners.", "answer": "False"}, # Geometry
    {"text": "7 times 7 is 49.", "answer": "True"},
    {"text": "There are 100 centimeters in a meter.", "answer": "True"}, # Measurement
    {"text": "20 minus 8 equals 12.", "answer": "True"},
    {"text": "A rectangle always has four equal sides.", "answer": "False"}, # Geometry
    {"text": "There are 30 days in September.", "answer": "True"}, # Time/Calendar
    {"text": "1 kilogram is heavier than 1 gram.", "answer": "True"}, # Measurement
    {"text": "9 times 3 is 27.", "answer": "True"},
    {"text": "A dozen means 10 items.", "answer": "False"}, # Quantity
    {"text": "Adding 0 to any number changes the number.", "answer": "False"},
    {"text": "A pentagon has 5 sides.", "answer": "True"}, # Geometry
    {"text": "There are 24 hours in a day.", "answer": "True"}, # Time
    {"text": "Multiplying any number by 1 keeps the number the same.", "answer": "True"},
    {"text": "A cube has 6 faces.", "answer": "True"}, # Geometry
    {"text": "50 plus 50 equals 100.", "answer": "True"},
    {"text": "1 liter is a measure of weight.", "answer": "False"}, # Measurement (Volume)
    {"text": "An octagon has 8 sides.", "answer": "True"}, # Geometry
    {"text": "There are 7 days in a week.", "answer": "True"}, # Time/Calendar
    {"text": "Dividing a number by itself always equals 1 (if the number isn't zero).", "answer": "True"},
    {"text": "A sphere is a flat shape.", "answer": "False"}, # Geometry (3D)
    {"text": "6 times 8 is 48.", "answer": "True"},
    {"text": "There are 12 months in a year.", "answer": "True"}, # Time/Calendar
    {"text": "Even numbers can be divided exactly by 2.", "answer": "True"},

    # --- Animal Questions (Approx. 35) ---
    {"text": "A dolphin is a fish.", "answer": "False"}, # Mammal
    {"text": "Spiders have 8 legs.", "answer": "True"}, # Insects/Arachnids
    {"text": "Penguins live in the Arctic.", "answer": "False"}, # Antarctica
    {"text": "A giraffe is the tallest mammal on Earth.", "answer": "True"},
    {"text": "Snakes have smooth, slimy skin.", "answer": "False"}, # Scaly skin
    {"text": "Butterflies start their life as caterpillars.", "answer": "True"}, # Life Cycle
    {"text": "All birds can fly.", "answer": "False"}, # e.g., Ostrich, Penguin
    {"text": "A lion is known as the 'King of the Jungle'.", "answer": "True"},
    {"text": "Frogs are mammals.", "answer": "False"}, # Amphibians
    {"text": "A cheetah is the fastest land animal.", "answer": "True"},
    {"text": "Bats are birds.", "answer": "False"}, # Mammals
    {"text": "Fish breathe using lungs.", "answer": "False"}, # Gills
    {"text": "A koala is a type of bear.", "answer": "False"}, # Marsupial
    {"text": "Elephants are the largest land animals.", "answer": "True"},
    {"text": "Bees make honey.", "answer": "True"},
    {"text": "Sharks are mammals.", "answer": "False"}, # Fish
    {"text": "A group of lions is called a pack.", "answer": "False"}, # Pride
    {"text": "Dogs evolved from wolves.", "answer": "True"},
    {"text": "Tigers have spots.", "answer": "False"}, # Stripes
    {"text": "A kangaroo carries its baby in a pouch.", "answer": "True"}, # Marsupial
    {"text": "Owls are mostly active during the day.", "answer": "False"}, # Nocturnal
    {"text": "Crocodiles are reptiles.", "answer": "True"},
    {"text": "A zebra's stripes are unique, like human fingerprints.", "answer": "True"},
    {"text": "Whales are the largest animals on Earth.", "answer": "True"}, # Blue Whale
    {"text": "Ants can carry objects many times their own weight.", "answer": "True"},
    {"text": "Gorillas live in Asia.", "answer": "False"}, # Africa
    {"text": "A turtle can come out of its shell.", "answer": "False"}, # Shell is part of its body
    {"text": "Camels store water in their humps.", "answer": "False"}, # Store fat
    {"text": "A platypus lays eggs.", "answer": "True"}, # Mammal that lays eggs
    {"text": "Hippos spend most of their time on land.", "answer": "False"}, # Semi-aquatic
    {"text": "Bears sleep all winter long (hibernate).", "answer": "True"}, # Generalization, but true for many
    {"text": "A starfish has a brain.", "answer": "False"}, # No central brain
    {"text": "Peacocks are female peahens.", "answer": "False"}, # Peacocks are male, peahens are female
    {"text": "Rabbits eat carrots as their main food.", "answer": "False"}, # Mainly eat hay/grass
    {"text": "Snails are known for being very fast.", "answer": "False"},

    # --- General Knowledge Questions (Approx. 35) ---
    {"text": "The Earth revolves around the Sun.", "answer": "True"}, # Science/Astronomy
    {"text": "Water boils at 100 degrees Celsius.", "answer": "True"}, # Science/Physics
    {"text": "The capital of India is Mumbai.", "answer": "False"}, # Geography (New Delhi)
    {"text": "Plants need sunlight to grow.", "answer": "True"}, # Science/Biology
    {"text": "There are 7 continents in the world.", "answer": "True"}, # Geography
    {"text": "The moon produces its own light.", "answer": "False"}, # Reflects sunlight
    {"text": "The Great Wall of China can be seen from the moon.", "answer": "False"}, # Myth
    {"text": "Christopher Columbus discovered America.", "answer": "True"}, # History (Simplified)
    {"text": "Sound travels faster than light.", "answer": "False"}, # Science/Physics
    {"text": "The Pacific Ocean is the largest ocean on Earth.", "answer": "True"}, # Geography
    {"text": "Mount Everest is the tallest mountain in the world.", "answer": "True"}, # Geography
    {"text": "Trees produce oxygen.", "answer": "True"}, # Science/Biology
    {"text": "The human body has four lungs.", "answer": "False"}, # Two lungs
    {"text": "The Nile is the longest river in the world.", "answer": "True"}, # Geography
    {"text": "Clouds are made of cotton.", "answer": "False"}, # Water droplets/ice crystals
    {"text": "The primary colors are red, yellow, and blue.", "answer": "True"}, # Art/Color Theory
    {"text": "The Eiffel Tower is in London.", "answer": "False"}, # Paris, France
    {"text": "Magnets attract all types of metal.", "answer": "False"}, # Only certain metals (like iron)
    {"text": "The currency used in India is the Dollar.", "answer": "False"}, # Rupee
    {"text": "Rainbows appear when it's sunny and raining at the same time.", "answer": "True"}, # Science/Optics
    {"text": "The Amazon rainforest is located in Africa.", "answer": "False"}, # South America
    {"text": "Ice is water in a solid state.", "answer": "True"}, # Science/Chemistry
    {"text": "The Taj Mahal is located in Agra, India.", "answer": "True"}, # Geography/History
    {"text": "Thomas Edison invented the telephone.", "answer": "False"}, # Lightbulb (Telephone: Alexander Graham Bell)
    {"text": "Jupiter is the largest planet in our solar system.", "answer": "True"}, # Science/Astronomy
    {"text": "There are 5 oceans in the world.", "answer": "True"}, # Geography (Pacific, Atlantic, Indian, Arctic, Southern)
    {"text": "Football (Soccer) is played with your hands.", "answer": "False"}, # Sports
    {"text": "Paper is made from wood.", "answer": "True"}, # Materials
    {"text": "The heart pumps blood around the body.", "answer": "True"}, # Biology/Human Body
    {"text": "Glass is made from sand.", "answer": "True"}, # Materials
    {"text": "The language spoken in Japan is Chinese.", "answer": "False"}, # Japanese
    {"text": "Volcanoes erupt with hot lava.", "answer": "True"}, # Geology
    {"text": "Australia is both a country and a continent.", "answer": "True"}, # Geography
    {"text": "The internet was invented in the year 2000.", "answer": "False"}, # Earlier origins
    {"text": "Recycling helps protect the environment.", "answer": "True"} # Environment
]
