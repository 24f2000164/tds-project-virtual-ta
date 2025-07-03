import json

# Load your JSON file
with open('processed_data/tds_combined.json', 'r') as file:
    data = json.load(file)

# # Define the string you want to search
# search_string = "You can visualize relationships between actors using IMDb data by following these steps:\n\n1. **Data Collection**: Scrape or obtain data from the IMDb database, focusing on actor appearances in movies. You can use libraries like Beautiful Soup or Scrapy for web scraping, or find datasets that are already available.\n\n2. **Network Construction**: Build a network where nodes represent actors and edges represent shared appearances in movies. Each time two actors appear in the same movie, an edge is created between them.\n\n3. **Use Network Analysis Libraries**: Utilize Python libraries such as NetworkX or Scikit-Network to create and analyze the actor network. These libraries allow you to construct the graph, compute properties, and find paths between actors.\n\n4. **Visualize the Network**: Use visualization tools like Matplotlib, Plotly, or Gephi to create visual representations of the network. You can depict actors as points and their relationships as lines connecting them.\n\n5. **Clustering and Community Detection**: Apply clustering algorithms to identify communities within the actor network. This can help you see which actors frequently work together.\n\n6. **Analysis and Interpretation**: Analyze the visualized data to find interesting patterns, such as the most connected actors or clusters of actors who frequently collaborate.\n\nBy following these steps, you can effectively visualize and analyze relationships between actors using IMDb data."

 

 
# # Define the string you want to search
# # Loop through the list to find matching page_content
# found = False
# for index, item in enumerate(data):
#     if search_string in item.get("page_content", ""):
#         print(f"✅ String found at index: {index}")
#         print("📄 Corresponding metadata:")
#         print(json.dumps(item.get("metadata", {}), indent=4))
#         found = True
#         break

# if not found:
#     print("❌ String NOT found in any page_content.")
    
def rename_key(obj, old_key, new_key):
    if isinstance(obj, dict):
        new_obj = {}
        for key, value in obj.items():
            new_key_name = new_key if key == old_key else key
            new_obj[new_key_name] = rename_key(value, old_key, new_key)
        return new_obj
    elif isinstance(obj, list):
        return [rename_key(item, old_key, new_key) for item in obj]
    else:
        return obj

# Rename "original_url" to "url"
updated_data = rename_key(data, "original_url", "url")

# Overwrite the same file
with open('processed_data/tds_combined.json', 'w') as file:
    json.dump(updated_data, file, indent=4)

print("Key 'original_url' renamed to 'url' in the same file.")
