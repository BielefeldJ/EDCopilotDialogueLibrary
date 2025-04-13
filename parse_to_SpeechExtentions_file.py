import os

def parse_markdown_folder(input_folder, output_file):
	# Initialize an output list to store the processed content
	output_lines = []

	# Iterate through all .md files in the input folder
	for filename in os.listdir(input_folder):
		if filename.endswith(".md"):
			file_path = os.path.join(input_folder, filename)
			print(f"Processing file: {file_path}")

			with open(file_path, 'r', encoding='utf-8') as infile:
				markdown_content = infile.readlines()
			
			event_type = None
			section = None
			tags = {
				"Normal": "",
				"All-Business": "(allbusiness)",
				"Flirt": "(flirt)",
				"Profanity": "(profanity)",
				"Dislike Mining": "(dislikesmining)",
				"Alcohol": "(alcohol)",
				"Innuendo": "(innuendo)",
			}

			for line in markdown_content:
				line = line.strip()
				
				# Extract Event Type
				if line.startswith("## Event Type:"):
					if event_type:  # Add a blank line between event types
						output_lines.append("")
					event_type = line.replace("## Event Type:", "").strip().replace("@", "").strip()
					output_lines.append("\n") # Add space between event types
					output_lines.append(f"@{event_type}")
				
				# Extract Section (Normal, All-Business, Flirt, Profanity)
				elif line.startswith("#### **"):
					section = line.replace("#### **", "").replace("**", "").strip()
				
				# Extract phrases and add appropriate tags
				elif line.startswith("- "):
					phrase = line[2:]  # Remove leading "- "
					tag = tags.get(section, "")
					if tag:
						output_lines.append(f"{tag}{phrase}")
					else:
						output_lines.append(phrase)
	
	# Write all processed content to the output file
	with open(output_file, 'w', encoding='utf-8') as outfile:
		del output_lines[0]  # Remove the first blank line
		outfile.write("\n".join(output_lines))
		print(f"Markdown parsed successfully. Output written to {output_file}")

# Usage
input_folder = "SpeechExtensions" 
output_path = "EDCoPilot.SpeechExtensions.Custom.txt"  
parse_markdown_folder(input_folder, output_path)
