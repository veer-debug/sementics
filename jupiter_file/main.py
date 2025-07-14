import subprocess
import sys

steps = [
    ('Preprocessing', 'preprocess.py'),
    ('Tokenization', 'tokenize_data.py'),
    ('Splitting', 'split.py'),
    ('Training', 'train.py'),
    ('Evaluation', 'evaluate.py'),
    ('Inference (example)', 'infer.py'),
]

for step_name, script in steps:
    print(f'\n=== {step_name} ({script}) ===')
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f'Error: {script} failed. Stopping pipeline.')
        sys.exit(1)
print('\nPipeline completed successfully!') 