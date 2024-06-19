from modify_keys_attributes import insert_or_update_attribute
import mysql.connector
from run_sql import run_sql
 
# Database configuration for initial connection
initial_config = {
    'user': 'root',  # replace with your MySQL username
    'password': '2003',  # replace with your MySQL password
    'host': 'localhost'
}

# Connect to the MySQL server
conn = mysql.connector.connect(**initial_config)
cursor = conn.cursor()

# Create chameleon_db 
run_sql('create_db.sql' ,conn, cursor)


# Connect to the newly created database
conn.database = 'chameleon_db'

pizza_attributes = ['focaccia', 'pepperoni', 'mozzarella', 'pizzeria', 'hut', 'bagel', 'taco', 'parlor', 'pasta', 'takeaway','dough', 'subs', 'oven', 'sandwiches', 'tomato', 'crust', 'burgers', 'neapolitan', 'slice', 'baked','salad', 'cheese', 'sauce', 'papa', 'restaurant', 'fries', 'grill', 'sausage', 'delivery', 'burger','pie', 'topping', 'garlic', 'recipe']
burger_attributes = ['whopper', 'veggie', 'cheeseburger', 'burgers', 'franchisee', 'hamburger', 'fries', 'sandwiches', 'lettuce','bun', 'sandwich', 'taco', 'grilled', 'patty', 'steak', 'menu', 'hungry', 'pizza', 'chicken', 'grill','cheese', 'beef', 'fried', 'sauce', 'bacon', 'tomato', 'onion', 'onions', 'king', 'restaurant', 'angus','chef', 'chain', 'chili', 'hut', 'chains', 'meal', 'ingredients', 'franchise', 'cafe', 'fast', 'meat','subway', 'powell', 'advertising', 'breakfast', 'foods', 'xbox', 'trademark', 'outlets', 'toys', 'brands','fat', 'bypass', 'opinion', 'kitchen', 'food', 'egg', 'coffee', 'taste', 'bar', 'product', 'topped','parent', 'kids', 'holdings', 'beer', 'mac', 'warren', 'justice', 'stewart', 'stores', 'corporation','customers', 'marketing', 'tim', 'joint', 'logo']
salad_attributes = ['vinaigrette', 'coleslaw', 'mayonnaise', 'diced', 'lettuce', 'appetizer', 'anchovies', 'celery', 'dressing','carrots', 'cucumber', 'pickled', 'chopped', 'eggplant', 'macaroni', 'minced', 'parsley', 'avocado', 'grilled','grated', 'pita', 'dessert', 'condiment', 'yogurt', 'shredded', 'vinegar', 'onions', 'spinach', 'onion', 'papaya','pasta', 'sandwiches', 'boiled', 'desserts', 'mashed', 'tomato', 'sauce', 'cabbage', 'dish', 'gelatin', 'pickles','tuna', 'olives', 'fried', 'spicy', 'carrot', 'fingers', 'garlic', 'steak', 'roasted', 'buffet', 'seasoned','vegetables', 'fries', 'baked', 'potatoes', 'ingredient', 'flavored', 'cooked', 'whipped', 'mustard', 'sandwich','ingredients', 'dishes', 'potato', 'chicken', 'recipe', 'peanut', 'juice', 'lemon', 'vegetable', 'pudding','finely', 'cuisine', 'tomatoes', 'soup', 'canned', 'noodles', 'cheese', 'sausage', 'greens', 'smoked', 'peas','chili', 'lobster', 'beans', 'shrimp', 'recipes', 'herbs', 'sour', 'eaten', 'pork', 'olive', 'bread', 'seafood','sesame', 'pizza', 'pepper', 'meal', 'spices']
pasta_attributes = ['linguine', 'tagliatelle', 'tortellini', 'fettuccine', 'rigatoni', 'fusilli', 'lasagne', 'durum', 'ravioli','semolina', 'gnocchi', 'penne', 'pesto', 'grano', 'ricotta', 'lasagna', 'macaroni', 'couscous', 'polenta','parmesan', 'vermicelli', 'spaghetti', 'mozzarella', 'bolognese', 'sauce', 'duro', 'dough', 'alla', 'noodles','salad', 'tomato', 'dishes', 'extrusion', 'noodle', 'desserts', 'legumes', 'broth', 'dish', 'buckwheat', 'dessert','flour', 'pizza', 'rag', 'cooked', 'sandwiches', 'starch', 'cheese', 'garlic', 'baked', 'seafood', 'neapolitan','soup', 'pastry', 'grilled', 'sausage', 'canned', 'yogurt', 'cuisine', 'potatoes', 'beans', 'wheat', 'vegetables','recipe', 'dried', 'cookbook', 'vegetable', 'peas', 'cereals', 'sicilian', 'meat', 'chicken', 'ingredients','stuffed', 'beef', 'norma', 'pork', 'boiled', 'shapes', 'paste', 'mushrooms', 'recipes', 'butter', 'cooking','onion', 'fried', 'bread', 'onions', 'potato', 'grill', 'bravo', 'olive', 'meals', 'hut', 'drying', 'foods', 'spices', 'tuna', 'menu', 'fresh', 'ingredient']
chicken_attributes = ['fried', 'grilled', 'roast', 'wings', 'drumsticks', 'breast', 'nuggets', 'soup', 'sandwich', 'salad']
sushi_attributes = ['sashimi', 'tempura', 'wasabi', 'teriyaki', 'nobu', 'nori', 'conveyor', 'jiro', 'ginza', 'gari', 'bento', 'ramen', 'avocado', 'chef', 'seafood', 'tofu', 'tuna', 'buffet', 'pickled', 'restaurant', 'vinegar', 'soy', 'gnome', 'steak', 'sandwiches', 'salad', 'fermented', 'grill', 'menu', 'cuisine', 'rice', 'rolls', 'kanji', 'sauce', 'ono', 'sake', 'dishes', 'ingredients', 'octopus', 'pizza', 'edo', 'shrimp', 'ingredient', 'crab', 'bar', 'bars', 'burger', 'roll', 'cooked', 'dish', 'raw', 'cafe', 'ginger', 'mounds', 'fish', 'typhoon', 'fried', 'eaten', 'wrapped', 'belt', 'cheese', 'soup', 'osaka', 'loops', 'ninja', 'salmon', 'lounge', 'apprentice', 'japanese', 'pack', 'monica', 'tokyo', 'eating', 'kitchen', 'vegetables', 'chain', 'meals', 'meal', 'prepared', 'naked', 'consumed', 'domains', 'dining', 'cooking', 'machines', 'plates', 'sustainable', 'subway', 'foods', 'shop', 'chicken', 'eat', 'tea', 'cream', 'food', 'japan', 'mall', 'cat', 'tag', 'outlets']
steak_attributes = ['tartare', 'sirloin', 'beefsteak', 'porterhouse', 'filet', 'seared', 'lube', 'steakhouse', 'tenderloin', 'chateaubriand', 'fillet', 'loin', 'grilled', 'gravy', 'minced', 'fries', 'beef', 'burgers', 'sandwiches', 'roast', 'sauce', 'seasoning', 'chops', 'veal', 'hanger', 'pies', 'sandwich', 'pie', 'salad', 'rib', 'hamburger', 'pudding', 'ale', 'mashed', 'seafood', 'burger', 'fried', 'shake', 'onions', 'cooked', 'deli', 'dish', 'barbecue', 'onion', 'kidney', 'pasta', 'chopped', 'chicken', 'lobster', 'seasoned', 'thinly', 'pork', 'baked', 'potatoes', 'dessert', 'meat', 'cheese', 'smoked', 'rump', 'chop', 'dishes', 'tomato', 'grill', 'potato', 'sausage', 'restaurant', 'menu', 'toast', 'pastry', 'shrimp', 'skirt', 'knife', 'vegetarian', 'knives', 'garlic', 'mushrooms', 'ribs', 'melted', 'spice', 'dinner', 'chips', 'beans', 'pizza', 'oyster', 'patty', 'recipe', 'cuisine', 'stuffed', 'boiled', 'bacon', 'flavor', 'perpendicular', 'chili', 'meal', 'vegetables', 'recipes', 'bread', 'pepper', 'butter', 'ingredients']
tacos_attributes = ['carnitas', 'fajitas', 'nachos', 'guacamole', 'taco', 'cilantro', 'chorizo', 'canasta', 'tortilla', 'carne', 'shogi', 'avocado', 'rind', 'fries', 'salsa', 'burgers', 'chopped', 'sandwiches', 'pork', 'menu', 'onion', 'chili', 'fried', 'pasta', 'sausage', 'salad', 'sauce', 'grill', 'pizza', 'chow', 'stuffed', 'dishes', 'pico', 'sour', 'flour', 'onions', 'cabbage', 'maui', 'dish', 'chicken', 'dough', 'cheese', 'tomato', 'mole', 'shrimp', 'corn', 'seafood', 'beans', 'beverages', 'recipes', 'cuisine', 'beef', 'mexican', 'flavor', 'meat', 'potatoes', 'cooked', 'ingredients', 'cream', 'eaten', 'pastor', 'rolled', 'restaurant', 'vendors', 'twist', 'foods', 'chips', 'specialty', 'lime', 'bacon', 'drinks', 'fusion', 'rolls', 'item', 'breakfast', 'vegetables', 'dogs', 'wheat', 'hawaiian', 'truck', 'chocolate', 'food', 'chronic', 'lunch', 'cooking', 'mexico', 'filled', 'midnight', 'rice', 'bread', 'chain', 'items', 'fresh', 'topped', 'eating', 'don', 'milk', 'beer', 'eggs', 'soft']
soup_attributes = ['broth', 'dumplings', 'tripe', 'stew', 'noodles', 'noodle', 'porridge', 'cans', 'tofu', 'dish', 'carrots', 'salad', 'onions', 'melon', 'delicacy', 'cabbage', 'boiled', 'dessert', 'garlic', 'spicy', 'tomato', 'sour', 'chicken', 'pasta', 'pork', 'beef', 'chopped', 'kitchen', 'cuisine', 'fried', 'roasted', 'vegetables', 'spoon', 'ingredients', 'sauce', 'dishes', 'ingredient', 'cooked', 'yogurt', 'soy', 'eaten', 'onion', 'pea', 'potatoes', 'peas', 'seasoned', 'spices', 'beans', 'canned', 'vegetable', 'mushrooms', 'bread', 'potato', 'meat', 'seafood', 'recipe', 'meal', 'nuts', 'cakes', 'dried', 'steamed', 'recipes', 'barley', 'stuffed', 'bean', 'baked', 'chili', 'paste', 'pepper', 'boiling', 'herbs', 'shrimp', 'flour', 'meals', 'cheese', 'staple', 'pot', 'rice', 'crab', 'flavor', 'coconut', 'cream', 'turtle', 'curry', 'butter', 'bowls', 'corn', 'sandwich', 'cake', 'homeless', 'egg', 'juice', 'consumed', 'lamb', 'cooking', 'shark', 'prepared', 'menu', 'tomatoes', 'taste']
sandwich_attributes = ['whopper', 'mayonnaise', 'sandwiches', 'toasted', 'lettuce', 'tern', 'grilled', 'bun', 'burger', 'steak', 'montagu', 'roast', 'bread', 'hamburger', 'tomato', 'cheese', 'deli', 'salad', 'sausage', 'jelly', 'beef', 'loaf', 'onions', 'bacon', 'peanut', 'mustard', 'chicken', 'fried', 'patty', 'cookies', 'sauce', 'slice', 'pork', 'menu', 'butter', 'snack', 'ham', 'onion', 'recipe', 'cod', 'ingredients', 'islands', 'bean', 'filling', 'kent', 'shop', 'windsor', 'android', 'cooked', 'dover', 'admiralty', 'meat', 'breakfast', 'cream', 'dish', 'hawaiian', 'pizza', 'meal', 'egg', 'lunch', 'sub', 'antarctic', 'panels', 'subway', 'layers', 'chocolate', 'cuisine', 'specialty', 'restaurant', 'roll', 'composite', 'tomatoes', 'charted', 'topped', 'massachusetts', 'layer', 'hawaii', 'item', 'compounds', 'chain', 'hampshire', 'prepared', 'cook', 'plate', 'thin', 'eat', 'beam', 'eating', 'glass', 'varieties', 'invented', 'bars', 'cape', 'discovery', 'earl', 'fish', 'tea', 'consisting', 'coffee', 'food']
fries_attributes = ['epicrisis', 'frites', 'poutine', 'coleslaw', 'mozzarella', 'mayonnaise', 'ketchup', 'gravy', 'cheeseburger', 'burgers', 'cheddar', 'fried', 'grilled', 'mashed', 'sandwiches', 'mycologist', 'sauce', 'shakes', 'salad', 'steak', 'potatoes', 'potato', 'desserts', 'onion', 'burger', 'lemonade', 'lettuce', 'cheese', 'onions', 'toast', 'chips', 'baked', 'menu', 'calories', 'chili', 'chicken', 'barbecue', 'frisian', 'mushrooms', 'beef', 'hamburger', 'tomato', 'pizza', 'chopped', 'fry', 'dish', 'seasoned', 'dessert', 'nora', 'drinks', 'snack', 'peanut', 'epithet', 'cooked', 'melted', 'sandwich', 'freeze', 'dishes', 'bacon', 'cream', 'dressing', 'bread', 'vegetable', 'spices', 'flavor', 'elias', 'shake', 'fungi', 'pork', 'cuisine', 'foods', 'breakfast', 'butter', 'rings', 'genus', 'beans', 'sanctioned', 'sticks', 'botanist', 'frozen', 'pepper', 'meal', 'magnus', 'topped', 'fat', 'soft', 'eaten', 'restaurant', 'ingredients', 'meat', 'meals', 'vegetables', 'chocolate', 'fingers', 'chip', 'cooking', 'dogs', 'fresh', 'drink', 'corn']
hotdog_attributes = ['ketchup', 'sausage', 'hamburger', 'bun', 'vendor', 'rene', 'mustard', 'cart', 'eating', 'filipino', 'stand', 'dennis', 'contest', 'dog', 'universe', 'magazine', 'hot', 'band']
curry_attributes = ['laksa', 'roti', 'tamarind', 'turmeric', 'coriander', 'masala', 'chilli', 'mutton', 'ketchup', 'gravy', 'spicy', 'mallet', 'yosemite', 'paste', 'coconut', 'noodles', 'sauce', 'spices', 'garlic', 'dish', 'dishes', 'chili', 'powder', 'chicken', 'cuisine', 'cooked', 'mustard', 'fried', 'onions', 'ginger', 'sour', 'soup', 'pork', 'vegetable', 'eaten', 'vegetables', 'ingredients', 'rice', 'pepper', 'beef', 'recipes', 'potatoes', 'staple', 'thai', 'favor', 'meat', 'nba', 'favour', 'correspondence', 'milk', 'meal', 'warriors', 'somerset', 'bread', 'taste', 'cooking', 'thompson', 'fish', 'logic', 'sweet', 'howard', 'leaves', 'oregon', 'restaurant', 'seeds', 'prepared', 'gang']
rice_attributes = ['oryza', 'glutinous', 'cassava', 'bran', 'noodles', 'sugarcane', 'noodle', 'millet', 'maize', 'sorghum', 'pudding', 'beans', 'coconut', 'cooked', 'flour', 'cakes', 'peanuts', 'vegetables', 'bananas', 'potatoes', 'owls', 'fried', 'paddy', 'staple', 'tarzan', 'dish', 'dishes', 'onions', 'grains', 'cultivation', 'boiled', 'peas', 'spices', 'barley', 'corn', 'soy', 'steamed', 'wheat', 'garlic', 'tomato', 'banana', 'sesame', 'pork', 'paste', 'crops', 'crop', 'sauce', 'soup', 'rat', 'cake', 'vegetable', 'curry', 'chicken', 'eaten', 'potato', 'cultivated', 'ingredients', 'cuisine', 'beef', 'cane', 'bean', 'meal', 'pepper', 'varieties', 'fruits', 'sugar', 'dried', 'bamboo', 'harvest', 'meat', 'grain', 'milk', 'cotton', 'cooking', 'sweet', 'irrigation', 'grown', 'consumed', 'employment', 'farming', 'coffee', 'tobacco', 'bread', 'powder', 'fields', 'mills', 'houston', 'plantation', 'livestock', 'agricultural', 'tea', 'foods', 'wine', 'palm', 'tons', 'seeds', 'fish', 'salt', 'fruit', 'cattle']
fish_attributes = ['hatchery', 'largemouth', 'crappie', 'walleye', 'mackerel', 'sunfish', 'shellfish', 'carp', 'catfish', 'perch', 'trout', 'tuna', 'amphibians', 'aquaculture', 'fishes', 'squid', 'spawning', 'seafood', 'shrimp', 'aquarium', 'salmon', 'crabs', 'bait', 'wildlife', 'eel', 'cod', 'spawn', 'herring', 'reptiles', 'fins', 'fisheries', 'freshwater', 'sauce', 'fishery', 'aquatic', 'stocks', 'pike', 'fishing', 'algae', 'mammals', 'frogs', 'endemic', 'eaten', 'vegetables', 'chips', 'nets', 'prey', 'fried', 'swim', 'cooked', 'dishes', 'fin', 'coral', 'dried', 'chip', 'depths', 'shark', 'insects', 'soup', 'genus', 'predators', 'rainbow', 'catch', 'eggs', 'reef', 'caught', 'meat', 'dish', 'endangered', 'waters', 'species', 'dorsal', 'pond', 'eat', 'meal', 'feeding', 'diet', 'cuisine', 'habitat', 'birds', 'chicken', 'streams', 'feed', 'fresh', 'shallow', 'scales', 'larvae', 'bass', 'rivers', 'farming', 'brook', 'refuge', 'breeding', 'bones', 'foods', 'recreational', 'eating', 'lake', 'marine', 'processing']
cake_attributes = ['buttercream', 'frosting', 'fondant', 'marzipan', 'icing', 'cakes', 'pastry', 'baked', 'dessert', 'sponge', 'bake', 'baking', 'pastries', 'batter', 'pudding', 'chocolate', 'recipe', 'whipped', 'flour', 'dough', 'desserts', 'carrot', 'biscuit', 'soaked', 'butter', 'cookies', 'biscuits', 'bakery', 'cookie', 'ingredients', 'recipes', 'coconut', 'filtration', 'candles', 'cream', 'cinnamon', 'vanilla', 'ingredient', 'pie', 'oven', 'slice', 'paste', 'layered', 'steamed', 'eaten', 'fried', 'nuts', 'yeast', 'bread', 'strawberry', 'banana', 'cooked', 'sugar', 'filling', 'sauce', 'cuisine', 'birthday', 'bean', 'layers', 'texture', 'flavor', 'filter', 'dish', 'wedding', 'cheese', 'eat', 'prepared', 'sweet', 'topped', 'pound', 'dried', 'egg', 'layer', 'wrapped', 'jam', 'candy', 'rice', 'bride', 'honey', 'coffee', 'fruit', 'milk', 'meal', 'powder', 'eggs', 'dishes', 'tea', 'consumed', 'decorated', 'boss', 'pan', 'shop', 'chef', 'cooking', 'traditionally', 'fruits', 'taste', 'eating', 'filled', 'fat']

# Define the attributes_list with corresponding keywords
attributes_list = [
    (pizza_attributes, 'Pizza'),
    (burger_attributes, 'Burger'),
    (salad_attributes, 'Salad'),
    (pasta_attributes, 'Pasta'),
    (chicken_attributes, 'Chicken'),
    (sushi_attributes, 'Sushi'),
    (steak_attributes, 'Steak'),
    (tacos_attributes, 'Tacos'),
    (soup_attributes, 'Soup'),
    (sandwich_attributes, 'Sandwich'),
    (fries_attributes, 'Fries'),
    (hotdog_attributes, 'Hotdog'),
    (curry_attributes, 'Curry'),
    (rice_attributes, 'Rice'),
    (fish_attributes, 'Fish'),
    (cake_attributes, 'Cake')
]
# Insert or update each chicken attribute
for attributes, keyword in attributes_list:
    for attribute in attributes:
        insert_or_update_attribute(attribute, keyword, conn, cursor)