from pathlib import Path
p = Path('index.html')
print('loaded', p.exists(), p.stat().st_size if p.exists() else 0)
