# Recipyzer

![PyPI](https://img.shields.io/pypi/v/recipyzer)
![License](https://img.shields.io/github/license/kmcconnell/recipyzer)

Welcome to **Recipyzer**, a meticulously organized and richly categorized repository of recipes. Explore, cook, and savor the flavors with ease!

## Getting Started

To get started, browse the [recipes](recipes/) folder and explore the categories and subcategories. You can find recipes for appetizers, main courses, desserts, drinks, and more. Each recipe includes detailed instructions, ingredients, and additional notes.

## Smart Index (Compiled by Recipyzer)

You can also browse the [index](index/) folder to explore recipes based on metadata. For example, you can find recipes based on [cuisines](index/Cuisines/), [holidays](index/Holidays/), [ingredients](index/Ingredients/), [seasons](index/Seasons/), and [tags](index/Tags/). This makes it easy to discover recipes based on your preferences.

## Recipyzer Python Package

The [index](index) folder is generated using the Recipyzer Python package, which provides a compiler for indexing and organizing recipes based on front matter metadata. You can install the package via PyPI and use it within your own recipe repository.

See [Recipyzer](https://pypi.org/project/recipyzer) on PyPI for more details.

## Front Matter Metadata

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

## Contributing

We welcome contributions for the improvement of the repository structure, metadata, and other aspects. However, please note that new recipes are only accepted from invited contributors. If you have any suggestions or improvements, feel free to submit a pull request.

For detailed contribution guidelines, please read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License for the repository structure and code. See the [LICENSE.md](LICENSE.md) file for details. Note that the recipes themselves are copyrighted by their respective authors as detailed in the [COPYRIGHT.md](COPYRIGHT.md) file.