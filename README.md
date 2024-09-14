# Recipyzer

![PyPI](https://img.shields.io/pypi/v/recipyzer)
![License](https://img.shields.io/github/license/kmcconnell/recipyzer)

Welcome to **Recipyzer**, a meticulously organized and richly categorized repository of recipes. Explore, cook, and savor the flavors with ease!

## Structure

The repository is organized into folders based on the type of recipes. Each recipe is stored as a markdown file and includes front matter for metadata. The metadata includes tags, cuisine, ingredients, seasons, holidays, and more.

## Tags and Metadata

Each recipe includes tags and metadata for easy search and filtering. You can explore recipes based on tags like vegetarian, vegan, gluten-free, dairy-free, low-carb, keto, paleo, and more. The metadata also includes cuisine types, ingredients, seasons, holidays, and dietary preferences.

### Front Matter Structure

```yaml
---
title: "Recipe Title"
description: "A brief description of the recipe."
category: "Category/Subcategory"  # e.g., Appetizers/Cold, Main Courses/Meat
cuisine: "Cuisine Type"  # e.g., Italian, Mexican
tags: ["tag1", "tag2", "tag3"]  # e.g., [vegan, quick, summer]
allergens: ["allergen1", "allergen2"]  # e.g., [gluten, dairy]
prep_time: "Preparation Time"  # e.g., 15 minutes
cook_time: "Cooking Time"  # e.g., 30 minutes
total_time: "Total Time"  # e.g., 45 minutes
servings: "Number of Servings"  # e.g., 4
calories: "Calories per Serving"  # e.g., 250
author: "Author's Name"
date: "Date"  # e.g., 2024-09-13
ingredients:
  - "Ingredient 1"
  - "Ingredient 2"
  - "Ingredient 3"
image_url: "URL to an image of the dish"
difficulty: "Difficulty level"  # e.g., Easy, Medium, Hard
nutrition:
  carbs: "Carbohydrates per serving"  # e.g., 30g
  protein: "Protein per serving"  # e.g., 10g
  fat: "Fat per serving"  # e.g., 15g
season: "Season"  # e.g., Summer, Winter
holidays: ["Holiday1", "Holiday2"]  # e.g., [Christmas, Thanksgiving]
---
```

## Copyright

All recipes in this repository are copyrighted by their respective authors. Unauthorized use and/or duplication of this material without express and written permission from the author is strictly prohibited. Please see the [COPYRIGHT.md](COPYRIGHT.md) file for more details.

## How to Use

Each folder contains markdown files for individual recipes. You can browse through the folders and open the markdown files to view the recipes. Media assets related to recipes (images and videos) are hosted externally and linked within the markdown files.

## Contributing

We welcome contributions for the improvement of the repository structure, metadata, and other aspects. However, please note that new recipes are only accepted from invited contributors. If you have any suggestions or improvements, feel free to submit a pull request.

For detailed contribution guidelines, please read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License for the repository structure and code. See the [LICENSE.md](LICENSE.md) file for details. Note that the recipes themselves are copyrighted by their respective authors as detailed in the [COPYRIGHT.md](COPYRIGHT.md) file.

## Releasing and Publishing

- **GitHub Releases**: Download the latest version of the repository from the [Releases](https://github.com/kmcconnell/recipyzer/releases) page.

- **Python Package**: Install the Recipyzer toolkit via PyPI.
  ```bash
  pip install recipyzer
  ```