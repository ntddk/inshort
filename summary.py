from summpy.lexrank import summarize
import sys

text = sys.stdin.read().decode('utf-8')

# ensure type(text) is unicode
sentences, debug_info = summarize(
    text, sent_limit=5, continuous=True, debug=True
)

for sent in sentences:
    print sent.strip().encode('utf-8')
