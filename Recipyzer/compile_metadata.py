import os
import frontmatter
import urllib.parse
from collections import defaultdict

# Base directory for your recipe collection
BASE_DIR = 'recipes'

# Directories for metadata files
METADATA_DIR = 'index'
TAGS_DIR = os.path.join(METADATA_DIR, 'Tags')
CUISINE_DIR = os.path.join(METADATA_DIR, 'Cuisine')
INGREDIENTS_DIR = os.path.join(METADATA_DIR, 'Ingredients')
SEASONS_DIR = os.path.join(METADATA_DIR, 'Seasons')
HOLIDAYS_DIR = os.path.join(METADATA_DIR, 'Holidays')

# Function to ensure a directory exists
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to update metadata files with a table format
def update_metadata(metadata, base_dir, type_):
    for key, items in metadata.items():
        # Ensure the directory exists
        ensure_dir(base_dir)
        file_path = os.path.join(base_dir, f'{key}.md')
        with open(file_path, 'w') as f:
            key_display = key.replace('-', ' ').capitalize()
            f.write(f'# {key_display} Recipes\n\n')
            # f.write(f'## List of {type_.capitalize()} Recipes\n\n')
            f.write('| Recipe | Category | Cuisine | Tags |\n')
            f.write('|--------|----------|---------|------|\n')
            
            # Sort items alphabetically by title
            sorted_items = sorted(items, key=lambda x: x['title'])
            
            for item in sorted_items:
                item_path = f"../../{urllib.parse.quote(item['path'].replace('\\', '/'))}" # Fix for Windows paths
                category_link = f"[{item['category']}]({category_to_link(item['category'])})"
                cuisine_link = f"[{item['cuisine']}]({cuisine_to_link(item['cuisine'])})"
                tags_links = ', '.join([f"[{tag}]({tag_to_link(tag)})" for tag in item['tags']])
                f.write(f'| [{item["title"]}]({item_path}) | {category_link} | {cuisine_link} | {tags_links} |\n')

# Helper functions to create links
def category_to_link(category):
    return f"../../{urllib.parse.quote(category.replace(' ', '-'))}/"

def cuisine_to_link(cuisine):
    return f"../Cuisine/{urllib.parse.quote(cuisine.replace(' ', '-').lower())}.md"

def tag_to_link(tag):
    return f"../Tags/{urllib.parse.quote(tag.replace(' ', '-').lower())}.md"

def season_to_link(season):
    return f"../Seasons/{urllib.parse.quote(season.replace(' ', '-').lower())}.md"

def holiday_to_link(holiday):
    return f"../Holidays/{urllib.parse.quote(holiday.replace(' ', '-').lower())}.md"

# Function to extract metadata from a recipe file
def extract_metadata(recipe_path, base_dir):
    with open(recipe_path, 'r') as f:
        post = frontmatter.load(f)
    metadata = {
        'title': post.get('title', 'Untitled'),
        'category': post.get('category', 'Uncategorized'),
        'cuisine': post.get('cuisine', 'Uncategorized'),
        'tags': post.get('tags', []),
        'ingredients': post.get('ingredients', []),
        'season': post.get('season', 'All Seasons'),
        'holidays': post.get('holidays', []),
        'path': recipe_path.replace(base_dir + '/', '')
    }
    print(f"Extracted metadata for {recipe_path}: {metadata}")
    return metadata

# Function to scan recipe directories and compile metadata
def compile_metadata(base_dir):
    tags_metadata = defaultdict(list)
    cuisine_metadata = defaultdict(list)
    ingredients_metadata = defaultdict(list)
    seasons_metadata = defaultdict(list)
    holidays_metadata = defaultdict(list)
    
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                recipe_path = os.path.join(root, file)
                metadata = extract_metadata(recipe_path, base_dir)
                
                # Update tags metadata
                for tag in metadata['tags']:
                    tags_metadata[tag].append(metadata)
                
                # Update cuisine metadata
                cuisine_metadata[metadata['cuisine']].append(metadata)
                
                # Update ingredients metadata
                for ingredient in metadata['ingredients']:
                    ingredient_key = ingredient.replace(' ', '-').lower()
                    ingredients_metadata[ingredient_key].append(metadata)
                
                # Update seasons metadata
                seasons_metadata[metadata['season']].append(metadata)
                
                # Update holidays metadata
                for holiday in metadata['holidays']:
                    holidays_metadata[holiday].append(metadata)
    
    # Write tags metadata to files
    update_metadata(tags_metadata, TAGS_DIR, 'tag')
    
    # Write cuisine metadata to files
    update_metadata(cuisine_metadata, CUISINE_DIR, 'cuisine')
    
    # Write ingredients metadata to files
    update_metadata(ingredients_metadata, INGREDIENTS_DIR, 'ingredient')
    
    # Write seasons metadata to files
    update_metadata(seasons_metadata, SEASONS_DIR, 'season')
    
    # Write holidays metadata to files
    update_metadata(holidays_metadata, HOLIDAYS_DIR, 'holiday')

def main():
    print('Compiling metadata...')
    compile_metadata(BASE_DIR)
    print('Metadata compilation complete.')

# Run the metadata compilation
if __name__ == '__main__':
    main()