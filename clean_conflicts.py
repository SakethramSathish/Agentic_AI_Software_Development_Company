import os

def clean_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip files that don't have conflicts
        if '<<<<<<< HEAD' not in content:
            return

        lines = content.split('\n')
        cleaned_lines = []
        in_bottom_half = False
        
        for line in lines:
            if line.startswith('<<<<<<< HEAD'):
                # Start of conflict block, we keep lines after this until =======
                in_bottom_half = False
                continue
            elif line.startswith('======='):
                # Switch to bottom half (the duplicated code from Github) which we want to delete
                in_bottom_half = True
                continue
            elif line.startswith('>>>>>>>'):
                # End of conflict block
                in_bottom_half = False
                continue
                
            # If we are not currently ignoring the bottom duplicate half, keep the line
            if not in_bottom_half:
                cleaned_lines.append(line)
                
        # Write the cleaned content back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(cleaned_lines))
            
        print(f"Fixed: {filepath}")
    except Exception as e:
        print(f"Skipped {filepath} due to error: {e}")

# Walk through all directories
for root, _, files in os.walk('.'):
    # Ignore node_modules and virtual environments
    if 'node_modules' in root or '.venv' in root or 'dist' in root or '.git' in root:
        continue
        
    for file in files:
        if file.endswith('.py') or file.endswith('.txt') or file == 'app.py':
            clean_file(os.path.join(root, file))

print("\n✨ All conflict markers successfully removed! Code is restored.")
